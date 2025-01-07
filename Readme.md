Python version 3.13.1

# About this application

This is simple gui application use library for converting image to text - Tesseract
As also it allows you to choose Window or app and then set Region of Interest of that screen.
Next after push "Take picture" Button app will focus that window/app (to make screenshot) and
then print founded text on image as string in logs in gui.


## How to use this application

### Install dependecies

```
pip install requirements.txt

```

### Run app

Type in console in app destination path

```
python main.py

```

### First Select ROI

Provide (just part for example "Excel") of the name of window/application that you want to take screenshot.
**It must be opened (but can be minimalized)**

### Second "Setup ROI"

1. Click Button "Setup ROI" - it will focus (open to take screenshot) that window or app name.
2. Next open our app second window (it should be screenshot to draw Region of interest ).
3. Draw by click and release Region of your interest  
4. Close that screenshot with drawed ROI

 - This region of interest will be convertet to text if Tesseract find any.

![Provide app or window name](/picture/pic1.png)
![Click setup ROI](/picture/pic2.png)
![Chose region of interest](/picture/pic3.png)


### Third "Take picture"

Push button "Take picture"
It will open again window/app to take screenshot and then use Tesseract to convert text from image to string and print in logs

![Take picture to convert image for text](/picture/pic4.png)


### To do

1. Select path to save screenshots
  - for now choosing path not work it will save all screenshots in app directory
2. Save results in file/db
  - Connect app to db or save results in file with time of conversion
3. Add automatic taking picture and saving results 
  - Automatic on triggered signal or timer to take picture save that picture and results


