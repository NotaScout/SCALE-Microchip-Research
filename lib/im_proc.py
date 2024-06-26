import os
import cv2
import lib.autoimport as cv2import

font                   = cv2.FONT_HERSHEY_DUPLEX
#bottomLeftCornerOfText = (x,y)
fontScale              = 1
fontColor              = (0,255,0)
thickness              = 1
lineType               = 2



# we can have each individual part of the processing separate, then bring them together in 1 function.

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


FILENAME = "Detected Items.txt"

# helper sub-routines

def find_centroid(x_start,y_start,width,height):
    x_centroid = x_start+width/2
    y_centroid = y_start+height/2
    return x_centroid,y_centroid

def crop_image(input_image,x_start,y_start,width,height):
    cropped_image = input_image[y_start:y_start+height, x_start:x_start+width]
    return cropped_image



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
    return contours, hierarchy

def quick_process_image(input_image,draw_boxes): # input image, and processing type
    image_stage1 = threshold_image(input_image)
    contours = find_contours(image_stage1)
    if draw_boxes:
        for count in range(len(contours)):  # {
            contour_count = contours[count]  # just takes the first contour
        # then we need to extract the x,y coords as well as the width and height of the bounding box on our contour
            x, y, w, h = cv2.boundingRect(contour_count)
            print(cv2.boundingRect(contour_count))
            cropped_image = input_image[y : y + h, x : x + w]
            cv2.imshow('Cropped',cropped_image)
            cx = x+(w/2)
            cy = y+(h/2)
    
    #centroid_image_test = cv2.circle(image,(int(cx),int(cy)),1,(0,240,0),4) << just draws a centroid on our text

        # X Centroid:
    # cx = int(M['m10']/M['m00']) --> (xcoord+(width/2))
    # Y Centroid:
    # cy = int(M['m01']/M['m00']) --> (ycoord+(height/2))


    # now we can feed each individual cropped image into OCR to be processed
            detected_word = pytesseract.image_to_string(cropped_image)
            bounding_box_test = cv2.rectangle(
            input_image, (x, y), (x + w, y + h), (31, 255, 31), 3
            )
            cv2.putText(bounding_box_test,'{}:{}'.format(str(count),detected_word),(int(cx+w+5),int(cy)),font, 
            fontScale,
            fontColor,
            thickness,
            lineType)


            cv2.imshow(
            "Bounding Box", bounding_box_test
            )  # cv2.imshow('Original',input_image)




# def read_contours

# def 



'''

def write_log(FILEPATH,saved_text):
    # write out the objects found to a text file and save it
    if FILEPATH == 0:
        FILEPATH = 

    
    file_write = open("FILEPATH","w+")
    file_write.write("") # clear file
    file_write.close()


def apply_model(input_image,MODEL_EXEC):
    threshold_img = threshold_image(input_image)



'''

    
    
    




    



