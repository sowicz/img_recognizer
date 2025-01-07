import cv2
import pytesseract



class ImageRead:
  def __init__(self, tesseract_path):
    """
    Initialize tesseract OCR.
    """
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
    
  
  def show_image(self, path):
    """
    Show picture by opencv
    """
    try:
      img_cv = cv2.imread(path)
      if img_cv is None:
        raise FileNotFoundError(f"Picture not found: {path}")
      cv2.imshow("Display",img_cv)
      cv2.waitKey(0)
      cv2.destroyAllWindows()
    except Exception as e:
      print(f"Error during loading image by openCV: ${e}")
  
  
  def img_to_string(self, path):
    """
    Convert image to string, first change from BGR to Grayscale to better read by Tesseract OCR
    """
    try:
      img_cv = cv2.imread(path)
      if img_cv is None:
        raise FileNotFoundError(f"Picture not found: {path}")
      img_rgb2gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)    
      text_from_img = pytesseract.image_to_string(img_rgb2gray)
      trimmed_output = " ".join(text_from_img.split())
      return trimmed_output
    except Exception as e:
      print(f"Error during converting image to text: ${e}")
      return None
