import cv2
import numpy as np

cap = cv2.VideoCapture(0)
if not (cap.isOpened()):
    print('Could not open video device')

while(True):
    ret, frame = cap.read()
    red = frame[:,:,2]
    blue = frame[:,:,0]
    green = frame[:,:,1]
    red_img = np.zeros(frame.shape)
    red_img[:,:,2] = red -(blue+green)
    
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(grey,127,255,cv2.THRESH_BINARY)
    kernel = np.ones((5,5),np.uint8)
    erosion = cv2.erode(thresh,kernel,iterations = 1)

    cv2.imshow('Greyscale',grey)
    cv2.imshow('Binary',thresh)
    cv2.imshow('Morphed',erosion)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()

cv2.destroyAllWindows()