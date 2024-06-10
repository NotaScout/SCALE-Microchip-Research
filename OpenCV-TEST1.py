import cv2

import os 

import time

import numpy

## stuff we need

'''
Defines
'''

lower_threshold = 127

upper_threshold = 255


# sets current file direcory as a variable
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
print(ROOT_PATH)

# appending file we want to process to the current dir
image_path = ROOT_PATH + "\\" + "image.jpg"
print(image_path)

# sends image data to image variable
image = cv2.imread(image_path)
# converts the image to greyscale
grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# shows us a greyscale version of our orignal image
cv2.imshow('ImageWindow', grey_image)
'''


'''
# waits for keypress input to continue
cv2.waitKey(0)

h,w = image.shape[:2]
print("Height = {}, Width = {}".format(h, w))
# return image, 

# thresholding the image
ret, thresholded_image = cv2.threshold(grey_image, lower_threshold, upper_threshold, cv2.THRESH_BINARY)

cv2.imshow('Binary Threshold Applied', thresholded_image)
cv2.waitKey(0)
# Locate Contours
# input. contours, hierarchy = cv.findContours(thresholded_img, contour retrival mode, contour approximation mode)
contours, hierarchy = cv2.findContours(thresholded_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# is hierarcy 

#cv2.imshow('Output',contours)
#print("Contours = {}", format(contours))
#contour_data = numpy.array(contours)

#print("Raw Image Data = {}", format(contour_data))
 
 # third input arg is id, basically it specifies which contours to draw. -1 draws all
image_contour = cv2.drawContours(image,contours,-1,127) 
cv2.imshow("Contour", image_contour)
cv2.waitKey(0)



'''
How to Contour trace (edge detect):
Step 1
read image <<< done
Step 2
Convert to greyscale <<< done
Step 3
Apply Binary Thresholding
>>> basically we need the processed image to be black and white
Step 4
findcontours () funciton
Step 5
Draw Contours on original input IMG
'''
## delete // below this line //


