import cv2
import numpy as np

img = cv2.imread('image/fr.jpg',cv2.IMREAD_COLOR)
px  = img[55,55] # get the pixel location
print(px) # print out the color of the pixel
img[55,55] = [25,25,2]

# Take Region of the image:
roi  = img[100:150,100:150]
img[10:50,10:50] = [255,255,255] # to convert the pixel in this region into white

# copy a region and paste
copy_ver = img[50:200, 50:200]
img[200:350,200:350] = copy_ver

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()