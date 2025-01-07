import os
import tkinter as tk
from time import sleep
from tkinter import messagebox, font
from PIL import Image, ImageTk

from screenshots import Screenshots
from roi import imageRoiSelector
from image_recognition import ImageRead

class UserInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to text ")
        self.root.geometry("800x600")
        self.root.rowconfigure(3, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.custom_font = font.Font(size=12)
        self.roi_params = None

        # Ramka dla sekcji input
        self.input_frame = tk.Frame(root, borderwidth=2, relief="groove", padx=10, pady=10)
        self.input_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Etykieta i pole tekstowe
        self.label_app_name = tk.Label(self.input_frame, text="Set app or window name:")
        self.label_app_name.grid(row=0, column=0, pady=5, sticky="w")

        self.entry_app_name = tk.Entry(self.input_frame, width=20, font=self.custom_font)
        self.entry_app_name.grid(row=1, column=0, pady=2, padx=5)

        # Przycisk "Setup ROI"
        self.setup_roi_button = tk.Button(self.input_frame, text="Setup ROI", command=self.setup_roi)
        self.setup_roi_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Przycisk "Take picture"
        self.take_picture_button = tk.Button(self.input_frame, text="Take picture", command=self.take_picture)
        self.take_picture_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Przycisk "Reset ROI"
        self.reset_roi_button = tk.Button(self.input_frame, text="Reset ROI", command=self.reset_roi)
        self.reset_roi_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Przycisk "Clear logs"
        self.clear_logs_button = tk.Button(self.input_frame, text="Clear logs", command=self.clear_logs)
        self.clear_logs_button.grid(row=6, column=0, columnspan=2, pady=10)

        # Ramka dla sekcji obrazu
        self.pic_frame = tk.Frame(root, borderwidth=2, relief="groove")
        self.pic_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.root.columnconfigure(1, weight=3)  # Ustawienie szerokości 3/5 dla ramki obrazu
        self.root.rowconfigure(0, weight=1)

        # Canvas do wyświetlania obrazka
        self.canvas = tk.Canvas(self.pic_frame, bg="gray")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Paski przewijania
        self.scroll_x = tk.Scrollbar(self.pic_frame, orient="horizontal", command=self.canvas.xview)
        self.scroll_y = tk.Scrollbar(self.pic_frame, orient="vertical", command=self.canvas.yview)
        
        self.scroll_x.pack(side="bottom", fill="x")
        self.scroll_y.pack(side="right", fill="y")
        
        # Przypięcie pasków do prawej strony i dolnej krawędzi
        self.scroll_x.place(relx=0, rely=1, relwidth=1, anchor="sw")  # Przypięcie paska poziomego do dołu
        self.scroll_y.place(relx=1, rely=0, relheight=1, anchor="ne")  # Przypięcie paska pionowego do prawej strony

        self.canvas.configure(xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)

        # Etykieta i pole tekstowe dla ścieżki zapisu
        self.save_path_label = tk.Label(root, text="Path to save file - default is application root path:")
        self.save_path_label.grid(row=1, column=0, columnspan=2, sticky="w", padx=10, pady=5)

        self.save_path_entry = tk.Entry(root, font=self.custom_font)
        self.save_path_entry.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
        self.save_path_entry.insert(0, "./")  # Domyślna wartość

        # Sekcja logów
        self.logs_frame = tk.Frame(root, borderwidth=2, relief="groove")
        self.logs_frame.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
        self.logs_frame.rowconfigure(0, weight=1)
        self.logs_frame.columnconfigure(0, weight=1)

        # Label nad logami
        self.logs_label = tk.Label(self.logs_frame, text="Logs:")
        self.logs_label.pack(anchor="nw", padx=5, pady=5)

        # Pole tekstowe na logi
        self.logs_text = tk.Text(self.logs_frame, height=5, )
        self.logs_text.pack(fill="both", expand=True)

    def setup_roi(self):
        app_name = self.entry_app_name.get()
        
        if app_name:
            try:
                screenshot = Screenshots() 
                screen_name = screenshot.take_full_screenshot(app_name)

                if os.path.exists(screen_name):
                    setup_roi = imageRoiSelector(screen_name)
                    self.roi_params = setup_roi.run() 

                    if self.roi_params:
                        self.add_log(f"ROI selected: {self.roi_params}")
                    else:
                        self.add_log("ROI setup failed.")
                else:
                    messagebox.showerror("Error", f"Screenshot not found at: {screen_name}")

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showwarning("Warning", "Please enter a valid app or window name!")

    def take_picture(self):
        app_name = self.entry_app_name.get()
        save_path = self.save_path_entry.get()

        if app_name and self.roi_params:
            try:
                screenshot = Screenshots()
                screenshot.set_roi(self.roi_params["left"], self.roi_params["top"], self.roi_params["width"], self.roi_params["height"])
                saved_image_path = screenshot.take_picture(app_name)

                image = Image.open(saved_image_path)

                photo = ImageTk.PhotoImage(image)

                self.canvas.create_image(0, 0, anchor="nw", image=photo)
                self.canvas.image = photo 
                self.canvas.config(scrollregion=self.canvas.bbox("all"))
                
                # Image to text with tesseract
                tesseract_path = r'D:\programy\TesseractOCR\tesseract'
                img_to_text = ImageRead(tesseract_path)
                text = img_to_text.img_to_string(saved_image_path)
                self.add_log(f"Text from image: {text}")

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showwarning("Warning", "Please enter a valid app or window name and select ROI!")

    def reset_roi(self):
        """Zresetuj ustawienia ROI."""
        self.roi_params = None
        self.add_log("ROI reseted.")

    def clear_logs(self):
        """Wyczyść logi."""
        self.logs_text.delete(1.0, tk.END)

    def add_log(self, message):
        """Dodaje wpis do logów."""
        self.logs_text.insert("end", f"{message}\n")
        self.logs_text.see("end") 


if __name__ == "__main__":
    root = tk.Tk()
    app = UserInterface(root)
    root.mainloop()
