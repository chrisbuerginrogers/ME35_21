# from https://docs.opencv2.org/3.4/d7/d4d/tutorial_py_thresholding.html

import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)
if not (cap.isOpened()):
    print('Could not open video device')

plt.title('Histogram')
plt.ion()
plt.show()
    
while(True):
    plt.clf()
    ret, frame = cap.read()
    cv2.imshow('Image',frame)
    for i, col in enumerate(['b', 'g', 'r']):
        hist = cv2.calcHist([frame], [i], None, [256], [0, 256])
        plt.plot(hist, color = col)
        #hist.xlim([0, 256])
    plt.draw()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()