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


'''
THRESHOLDING
ret, thresholded_image = cv.threshold(image, lower_threshold, upper_threshold,threshold_algorithm)
I dont know what ret means exactly (return?)

'''

'''
How to Contour trace (edge detect):
Step 1
read image <<< done
Step 2
Convert to greyscale
Step 3
Apply Binary Thresholding (WHat is that)
Step 4
findcontours () funciton
Step 5
Draw Contours on original input IMG
'''
## delete // below this line //


