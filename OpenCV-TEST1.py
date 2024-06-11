'''
TODO:

Make tesseract also install-able for all users (in addition to keeping the one user thing)

rects around contour

image stretching to get better results

text display on image

save recognized text to file


'''


import cv2

import os 

import time

import numpy

import pytesseract

## stuff we need

#pip install opencv-python
#pip install pytesseract

# to print a list of all environment varables:
#print(os.environ)


'''
TEST BOX
'''

rectangle_kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(9,9))
rectangle_kernel

# X Centroid: 
# cx = int(M['m10']/M['m00'])
# Y Centroid:
# cy = int(M['m01']/M['m00'])



'''
</>

'''


'''
Defines
'''
#tesseract path
#'C:\Users\scho3988\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
#so
#os.environ["HOMEPATH"] + "\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

# install for 1 user
pytesseract.pytesseract.tesseract_cmd = os.environ["HOMEDRIVE"]+os.environ["HOMEPATH"] + "\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"




# input image here
input_image = "demoIMG.png"

lower_threshold = 100

upper_threshold = 255


# sets current file direcory as a variable
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

print(ROOT_PATH)

# appending file we want to process to the current dir
image_path = ROOT_PATH + "\\" + input_image

print(image_path)

# sends image data to image variable
original_image = cv2.imread(image_path)
image = original_image.copy()

# converts the image to greyscale
grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# shows us a greyscale version of our orignal image
#cv2.imshow('ImageWindow', grey_image)
'''


'''
# waits for keypress input to continue
cv2.waitKey(0)

h,w = image.shape[:2]
print("Height = {}, Width = {}".format(h, w))
# return image, 

'''
THRESHOLDING
ret, thresholded_image = cv.threshold(image, lower_threshold, upper_threshold,threshold_algorithm)
I dont know what ret means exactly (return?)

'''

# thresholding the image
ret, thresholded_image = cv2.threshold(grey_image, lower_threshold, upper_threshold, cv2.THRESH_BINARY)

#cv2.imshow('Binary Threshold Applied', thresholded_image)
cv2.waitKey(0)
# Locate Contours
# input. contours, hierarchy = cv.findContours(thresholded_img, contour retrival mode, contour approximation mode)
exact_contours, hierarchy = cv2.findContours(thresholded_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# is hierarcy 

#cv2.imshow('Output',contours)
#print("Contours = {}", format(contours))
#contour_data = numpy.array(contours)

#print("Raw Image Data = {}", format(contour_data))
 
 # third input arg is id, basically it specifies which contours to draw. -1 draws all
print(pytesseract.image_to_string(image))
exact_image_contour = cv2.drawContours(image,exact_contours,-1,(31,255,31)) 


#cv2.imshow("Exact Contour", exact_image_contour)

cv2.waitKey(0)

'''
OCR
'''

recognized_text_file = open("recognized_text.txt","w+")
recognized_text_file.write("") # clear file
recognized_text_file.close()
# <> net recognized text (control group)

cv2.destroyAllWindows()

# replace with increment in future
# also another note: if we just do the 0th one, it appears to just capture the entire image. ie. (0,0,[image size])
contour_count = exact_contours[2] # just takes the first contour

# then we need to extract the x,y coords as well as the width and height of the bounding box on our contour
x,y,w,h = cv2.boundingRect(contour_count)
print(cv2.boundingRect(contour_count))

bounding_box_test = cv2.rectangle(original_image,(x,y),(x+w,y+h),(31,255,31),3)
cv2.imshow('Bounding Box',bounding_box_test)
cv2.imshow('Original',original_image)
cv2.waitKey(0)


# what we need:

# contours from the source image

# apply OCR



'''
How to Contour trace (edge detect):
Step 1
read image <<< done
Step 2
Convert to greyscale <<< done
Step 3
Apply Binary Thresholding <<< done
>>> basically we need the processed image to be black and white
Step 4
findcontours () funciton << done
Step 5
Draw Contours on original input IMG <<< done
'''


'''
To apply OCR (text detect)
Step 1
get nth contour 
Step 2
draw rect
Step 3

'''



## delete // below this line //


