import numpy as np
import cv2
from tensorflow.keras.applications.vgg16 import preprocess_input

def resize_img(img,
                out_height = 128,    # default, can alter
                out_width = 128):     # default, can alter
    """
    Reshapes an image to desired dimensions
    """

    img = np.array(img)
    dims = np.shape(img)

    if dims[0]*dims[1] > out_height*out_width:
        img = cv2.resize(img, dsize=(out_height, out_width), interpolation=cv2.INTER_AREA)
    elif dims[0]*dims[1] < out_height*out_width:
        img = cv2.resize(img, dsize=(out_height, out_width), interpolation=cv2.INTER_LINEAR)
    else:
        pass

    return img

def vgg16_preproc(img):
    '''
    Implements VGG16 processing function
    '''
    img = preprocess_input(img)

    return img
