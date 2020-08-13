import numpy as np
import matplotlib.pyplot as plt
import imageio
import scipy, scipy.misc, scipy.signal
import cv2
import sys
import PIL
from PIL import Image

windowName = ''
threshold = 11
size = 5

# path to input image is specified and   
# image is loaded with imread command  
image1 = cv2.imread('0136ns.png')
# image1 = cv2.imread('02.jpg')
   
# cv2.cvtColor is applied over the 
# image input with applied parameters 
# to convert the image in grayscale  
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY) 
   
# applying different thresholding  
# techniques on the input image 
thresh1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                          cv2.THRESH_BINARY, 199, 5) 
  
thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                          cv2.THRESH_BINARY, 11, 5) 
  
# the window showing output images 
# with the corresponding thresholding  
# techniques applied to the input image

cv2.namedWindow( windowName )

def update():
    thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                          cv2.THRESH_BINARY, threshold, size)
    cv2.imshow(windowName, thresh2)

def onTrackbarChange1(x):
    global threshold
    threshold = x*2+3
    update()

def onTrackbarChange2(x):
    global size
    size = x + 1
    update()

cv2.createTrackbar(
    'threshold',
    windowName,
    4,
    99,
    onTrackbarChange1,
)
cv2.createTrackbar(
    'size',
    windowName,
    4,
    99,
    onTrackbarChange2,
)
# cv2.setTrackbarMin( 'min2', windowName, 0 )
# cv2.imshow('Adaptive Mean', thresh1) 
# cv2.imshow('Adaptive Gaussian', thresh2)
cv2.imshow(windowName, thresh2)


while True:
    print("Press [q] or [esc] to close the window.")
    k = cv2.waitKey() & 0xFF
    if k in (ord("s"), ord("S")):
        # print("SAVE IMAGE")
        # print( thresh2.ndim )
        # cv2.cvtColor(thresh2, cv2.COLOR_RGB2GRAY)
        cv2.imwrite( "output.bmp", thresh2 )
    if k in (ord("q"), ord("\x1b")):
        cv2.destroyWindow(self.name)
        break
     
# # De-allocate any associated memory usage   
# if cv2.waitKey(0) & 0xff == 27:
#     cv2.destroyAllWindows()  
