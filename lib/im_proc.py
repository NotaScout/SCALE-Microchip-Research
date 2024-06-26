
import cv2

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

def process_image(input_image,): # input image, and processing type




# def read_contours

# def 




def write_log(FILEPATH,saved_text):
    # write out the objects found to a text file and save it
    if FILEPATH == 0:
        FILEPATH = 

    
    file_write = open("FILEPATH","w+")
    file_write.write("") # clear file
    file_write.close()


def apply_model(input_image):
    threshold_img = threshold_image(input_image)

    
    
    




    



