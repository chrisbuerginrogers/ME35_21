# from https://learnopencv.com/blob-detection-using-opencv-python-c/

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
if not (cap.isOpened()):
    print('Could not open video device')
    
params = cv2.SimpleBlobDetector_Params()
params.minThreshold = 10;
#params.thresholdStep = 10;
params.maxThreshold = 255;

# Filter by Area.
params.filterByArea = True
params.minArea = 100
params.maxArea = 800
# Filter by Circularity
params.filterByCircularity = False
params.minCircularity = 0.5

# Filter by Convexity
params.filterByConvexity = False
params.minConvexity = 0.8

# Filter by Inertia
params.filterByInertia = False
params.minInertiaRatio = 0.01

# Create a detector with the parameters
detector = cv2.SimpleBlobDetector_create(params)

while(True):
    ret, frame = cap.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(grey,127,255,cv2.THRESH_BINARY)

    cv2.imshow('Color',frame)
    cv2.imshow('Grey',grey)

    # Detect blobs.
    keypoints = detector.detect(grey)

    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
    blobs = cv2.drawKeypoints(grey, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Show keypoints
    cv2.imshow("Keypoints", blobs)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()

cv2.destroyAllWindows()