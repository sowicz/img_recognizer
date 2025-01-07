from sys import monitoring
from time import sleep
from datetime import datetime
from pywinauto import Desktop
from datetime import datetime
from screeninfo import get_monitors
import mss
import mss.tools



class Screenshots:
  def __init__(self):
    """
    Set name of the application/window to open and take picture
    """
    self.region = None  # Initially, no region is set
  
  
  def _open_window(self, window_name):
      """
      Private method to open the specified window.
      """
      windows = Desktop(backend="uia").windows()
      for window in windows:
          if window_name in window.window_text():
              window.set_focus()
              sleep(1)  # Wait for the window to load
              return True
      print(f"Window '{window_name}' not found.")
      return False
   
  
  def set_roi(self, left, top, width, height):
    """
    Set the region o interest.

    :param left: Left edge of the region.
    :param top: Top edge of the region.
    :param width: Width of the region.
    :param height: Height of the region.
    """
    self.region = {
        "left": left,
        "top": top,
        "width": width,
        "height": height
    }
      
      
  def take_picture(self, check_window):
    """
    Take a screenshot of the defined region after focusing on the specified window.
    
    :param check_window: The name of the window/application to open.
    """
    
    # Check if region is provide and window is open
    if self.region is None:
      print("Region is not set.")
      return
    
    if not self._open_window(check_window):
      print("Failed to take screenshot: Target window not found.")
      return
    
    with mss.mss() as sct:
      screenshot = sct.grab(self.region)
      
      # Generate a timestamped filename
      timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Format: YYYY-MM-DD_HH-MM-SS
      output_path = f"screen_{timestamp}.png"

      # Save the screenshot
      mss.tools.to_png(screenshot.rgb, screenshot.size, output=output_path)
      # print(f"Screenshot saved to {output_path}")
    return output_path
  

  def take_full_screenshot(self, window_name):
    """
    Take full window screenshot to later take roi
    """    
    if not self._open_window(window_name):
        print("Failed to take screenshot: Target window not found.")
        return
      
    # Get primary monitor details
    monitor = get_monitors()[0] 
    screen_width = monitor.width
    screen_height = monitor.height
    
    full_region = {
        "left": 0,
        "top": 0,
        "width": screen_width,
        "height": screen_height
    }
    
    # Capture the full screenshot of the window
    with mss.mss() as sct:
        screenshot = sct.grab(full_region)

        # Generate a timestamped filename
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Format: YYYY-MM-DD_HH-MM-SS
        output_path = f"full_screen_{timestamp}.png"

        # Save the screenshot
        mss.tools.to_png(screenshot.rgb, screenshot.size, output=output_path)
        print(f"Full window screenshot saved to {output_path}")
    return output_path
  
      
      

if __name__ == "__main__":
  
    CHECK_WINDOW = "Excel"
    screenshot_tool = Screenshots()
    
    screenshot_tool.set_roi(238, 296, 340, 312)
    
    # screenshot_tool.take_picture(CHECK_WINDOW)
    screenshot_tool.take_full_screenshot(CHECK_WINDOW)
