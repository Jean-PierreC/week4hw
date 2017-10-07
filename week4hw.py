import cv2
import numpy as np
count = -1
img = cv2.imread("320px-Flag_of_Japan.svg.png")
#cv2.namedWindow("Original", CV.WINDOW_AUTOSIZE)
cv2.imshow("Original", img)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#cv2.imshow("HSV", img_hsv)
#cv2.waitKey(0)
THRESHOLD_MIN = np.array([0, 0, 0],np.uint8)
THRESHOLD_MAX = np.array([50, 255, 255],np.uint8)

frame_threshed = cv2.inRange(img_hsv, THRESHOLD_MIN,THRESHOLD_MAX)
edges = image, contours, count, = cv2.findContours(frame_threshed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image,contours,count,(0,20,3),10)
cv2.imshow("320px-Flag_of_Japan.svg.png", edges)
cv2.waitKey(0)



