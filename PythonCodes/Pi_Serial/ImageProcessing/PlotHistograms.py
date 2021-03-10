# from https://docs.opencv2.org/3.4/d7/d4d/tutorial_py_thresholding.html

import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

cap = cv2.VideoCapture(0)
if not (cap.isOpened()):
    print('Could not open video device')

figure,(image,histo) = plt.subplots(1,2)
figure.suptitle("live view")
image.set_title('image')

histo.set_title('Histogram')
plt.ion()
plt.show()
    
while(True):
    image.clear()
    image.axis('off')
    histo.clear()
    ret, frame = cap.read()
    ret1,th1 = cv2.threshold(frame,127,255,cv2.THRESH_BINARY)
    image.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    for i, col in enumerate(['b', 'g', 'r']):
        hist = cv2.calcHist([frame], [i], None, [256], [0, 256])
        histo.plot(hist, color = col)
        #hist.xlim([0, 256])
    plt.draw()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()