import os
import cv2


#simple importer

#default models:

pytesseract.pytesseract.tesseract_cmd = (
    os.environ["HOMEDRIVE"]
    + os.environ["HOMEPATH"]
    + "\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
)

def Current_Directory_Import(filename):
    # sets current file direcory as a variable
    LIB_PATH = os.path.dirname(os.path.abspath(__file__))
    print(LIB_PATH)
    # we need to up a dir because we want to look int he main directory instead of the library directory
    ROOT_PATH = os.path.dirname(LIB_PATH)

    # appending file we want to process to the current dir
    image_path = ROOT_PATH + "\\" + filename
    #print(image_path)
    return image_path

#Current_Directory_Import("image.jpg")

def Select_Model(modelname):
    #input AI modelname
    match modelname:
        case "tesseract":
            return "TESSERACTPATH"
        case "test1":
            return 2
        case _:
            print("Invalid Model Provided")
            return 0



