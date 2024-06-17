import os 

import lib.autoimport as cv2import

#ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
#print(ROOT_PATH)

# should be able to access it as a library now, so this can be written a bt cleaner
image_path = cv2import.Current_Directory_Import("demoIMG.png")

print("Image Path {}".format(image_path))

print("Model {}".format(cv2import.Select_Model("")))


