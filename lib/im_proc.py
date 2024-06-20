
import cv2

# we can have each individual part of the processing separate, then bring them together in 1 function.



def threshold_image(input_image,upper_threshold = 255, lower_threshold = 127):

    image = input_image.copy()
    # threshold the image in this function
    # possibly want to threshold values that we take in
    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # thresholding the image
    ret, thresholded_image = cv2.threshold(
    grey_image, lower_threshold, upper_threshold, cv2.THRESH_BINARY_INV)
    return thresholded_image



def find_contours(thresholded_image,kernelsize = 15):
    

    rectangle_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernelsize, kernelsize))

    dilation_image = cv2.dilate(thresholded_image, rectangle_kernel, iterations=2)
    
    contours, hierarchy = cv2.findContours(
    dilation_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE
    )
    return contours

# def read_contours

# def 




    
    




    



