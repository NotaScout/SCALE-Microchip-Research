import cv2

import os 

## stuff we need

# sets current file direcory as a variable
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
print(ROOT_PATH)

# appending file we want to process to the current dir
image_path = ROOT_PATH + "\\" + "image.jpg"
print(image_path)

# sends image data to image variable
image = cv2.imread(image_path)


h,w = image.shape[:2]
print("Height = {}, Width = {}".format(h, w))

## delete // below this line //


