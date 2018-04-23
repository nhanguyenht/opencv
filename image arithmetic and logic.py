# https://pythonprogramming.net/image-arithmetics-logic-python-opencv-tutorial/
import cv2
import numpy as np

img1 = cv2.imread('image/p1.png')
img2 = cv2.imread('image/p2.png')

#add = img1 + img2
weigted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
# cv2.imshow('add',add)
cv2.imshow("weigted", weigted)
cv2.waitKey(0)
cv2.destroyAllWindows()