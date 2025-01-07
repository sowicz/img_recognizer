import cv2


class imageRoiSelector():
    def __init__(self, image_path, window_width=1200, window_height=800):
        self.image_path = cv2.imread(image_path)
        self.window_width = window_width
        self.window_height = window_height
        self.original_image = self.image_path.copy()  # Store the original image
        self.scaled_image = None
        self.roi = {}
        self.start_point = None
        self.drawing = False
        self.scale_factor = 1
        
    
    def scale_image(self, image):
        """
        Scale image to fit window.
        """
        original_height, original_width = image.shape[:2]
        self.scale_factor = min(self.window_width / original_width, self.window_height / original_height)
        
        # Calculate new dimensions
        new_width = int(original_width * self.scale_factor)
        new_height = int(original_height * self.scale_factor)
        
        # Resize image
        resized_image = cv2.resize(image, (new_width, new_height))
        return resized_image
    
    def mouse_callback(self, event, x, y, flags, param):
        """
        Callback function for mouse events.
        """
        scaled_x = int(x / self.scale_factor)
        scaled_y = int(y / self.scale_factor)
        
        # Start drawing rectangle when mouse button clicked
        if event == cv2.EVENT_LBUTTONDOWN:
            self.start_point = (scaled_x, scaled_y)
            self.drawing = True
            # Reset roi when starting a new selection
            self.roi = {}
            param["image"][:] = self.original_image.copy()  # Reset the image to the original
            
        # Update rectangle while dragging
        elif event == cv2.EVENT_MOUSEMOVE:
            if self.drawing:
                img_copy = param["image"].copy()
                # Draw rectangle
                cv2.rectangle(img_copy, (self.start_point[0], self.start_point[1]), (scaled_x, scaled_y), (0, 255, 0), 2)
                self.scaled_image = self.scale_image(img_copy)
                cv2.imshow("Select ROI rectangle", self.scaled_image)
                
        # End drawing on mouse button released
        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing = False
            end_point = (scaled_x, scaled_y)
            left = min(self.start_point[0], end_point[0])
            top = min(self.start_point[1], end_point[1])
            width = abs(self.start_point[0] - end_point[0])
            height = abs(self.start_point[1] - end_point[1])
            
            # Save ROI dimensions
            self.roi = {
                "left": left,
                "top": top,
                "width": width,
                "height": height,
            }
            
            # Update image to stay drawn rectangle
            cv2.rectangle(param["image"], (left, top), (left + width, top + height), (0, 255, 0), 2)
            self.scaled_image = self.scale_image(param["image"])
            cv2.imshow("Select ROI rectangle", self.scaled_image)
            print(f"Region: {self.roi}")
            param["roi"] = self.roi
        
        # Reset selected region on right button click
        elif event == cv2.EVENT_RBUTTONDOWN:
            print("Reset selected region")
            param["image"][:] = self.original_image.copy()
            self.scaled_image = self.scale_image(param["image"])
            cv2.imshow("Select ROI rectangle", self.scaled_image)
            
    def run(self):
        """
        Main program loop to display image and handle drawing ROI.
        """
        cv2.namedWindow("Select ROI rectangle")
        
        # To store Region dictionary and return it to the rest of the application
        roi_data = {"roi": None}
        cv2.setMouseCallback("Select ROI rectangle", self.mouse_callback, {"image": self.image_path, "roi": roi_data})
        
        while True:
            self.scaled_image = self.scale_image(self.image_path)
            cv2.imshow("Select ROI rectangle", self.scaled_image)
            
            # Close app after "q" keyboard button clicked
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            # Close app after closing the window "Select ROI rectangle"
            if cv2.getWindowProperty("Select ROI rectangle", cv2.WND_PROP_VISIBLE) < 1:
                break
            # If region selected, break main loop
            if roi_data["roi"] is not None:
                print(f"Returning region data: {roi_data['roi']}")
                break
        
        cv2.destroyAllWindows()
        # return roi_data["roi"]
        return self.roi
    

if __name__ == "__main__":
    selector = imageRoiSelector("full_screen_2025-01-06_14-29-00.png")
    region = selector.run()
    
    if region:
        print(f"Final selected region: {region}")
