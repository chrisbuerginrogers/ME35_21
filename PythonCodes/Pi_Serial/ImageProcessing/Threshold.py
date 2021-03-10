import cv2
import numpy as np

cap = cv2.VideoCapture(0)
if not (cap.isOpened()):
    print('Could not open video device')

while(True):
    ret, frame = cap.read()
    cv2.imshow('Image',frame)
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(grey,127,255,cv2.THRESH_BINARY)
    cv2.imshow('Grey',thresh)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()

cv2.destroyAllWindows()