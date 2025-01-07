# main.py
import tkinter as tk
from gui import UserInterface


if __name__ == "__main__":
    tesseract_path = r'D:\programy\TesseractOCR\tesseract'
    root = tk.Tk()
    app = UserInterface(root, tesseract_path)
    root.mainloop()