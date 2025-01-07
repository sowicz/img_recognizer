# main.py
import tkinter as tk
from gui import UserInterface


if __name__ == "__main__":
    root = tk.Tk()
    app = UserInterface(root)
    root.mainloop()