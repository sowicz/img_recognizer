# 📷 Image to Text Converter GUI Application

### 🐍 Python Version: 3.13.1

---

## 🌟 About This Application

This is a simple GUI application that uses the Tesseract OCR library to convert images to text. It allows users to:

- **Select a specific window or application** to take a screenshot from.
- **Define a Region of Interest (ROI)** on the screenshot.
- Extract text from the selected region and display it in the app logs.

With this tool, you can quickly extract text from any visible window or application on your screen.

---

## 🚀 How to Use This Application

### 🛠️ Install Dependencies

Run the following command in your terminal to install the required libraries:

```bash
pip install -r requirements.txt
```

### Install TesseractOCR

install Tesseract ORC engine from 
[Github link to Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)

**tesseract-ocr-w64-setup-5.5.0.20241111.exe (64 bit)**

After installation ends, type location path to installed Tesseract OCR in main.py file:

> tesseract_path = r'C:\your_path_to_tesseractOCR\tesseract'


### ▶️ Run the Application

Navigate to the application's directory and run:
```bash
python main.py
```

### 📝 Steps to Use the Application

1️⃣ **Provide the Window/Application Name**
Enter a part of the name of the window or application you want to take a screenshot of.
💡 Note: The window or application must be open (it can be minimized).


2️⃣ **Set Up the ROI**
1. Click the "Setup ROI" button.
    - This will bring the selected window or application to the foreground for a screenshot.
2. A new window will open displaying the screenshot.
    - Use your mouse to click and drag to define the Region of Interest (ROI).
3. Close the ROI selection window after defining the region.


### 📸 Screenshots of the process:

![Provide app or window name](/picture/pic1.png)
![Click setup ROI](/picture/pic2.png)
![Chose region of interest](/picture/pic3.png)


3️⃣ **Take a Picture**
1. Click the "Take Picture" button.
    - The app will refocus on the selected window or application to take a screenshot.
    - The captured image's text will be extracted using Tesseract and displayed in the logs.

🖼️ Example of the process:

![Example of converting img to text](/picture/pic4.png)


### 🔧 Features in Progress

🔜 **Planned Updates:**
1. Select Path to Save Screenshots:
    - Currently, all screenshots are saved in the app directory. Adding functionality to specify a custom save path.
2. Save Results in File/Database:
    - Enable saving extracted text results along with timestamps to a file or database.
3. Automate Screenshot and Text Extraction:
    - Implement an automatic mode that triggers screenshot capture and text extraction based on signals or timers.


**Thank you for using the Image to Text Converter!**
Feel free to contribute or report issues to improve the app. 🤝

