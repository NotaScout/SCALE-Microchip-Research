import os
import cv2

#simple importer

def Current_Directory_Import(file):
    # sets current file direcory as a variable
    ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
    print(ROOT_PATH)

    # appending file we want to process to the current dir
    image_path = ROOT_PATH + "\\" + file
    print(image_path)

Current_Directory_Import("image.jpg")


