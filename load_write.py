import cv2
import numpy as np
import matplotlib as plt

img = cv2.imread('image/fr.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('image', img)  # the name of the window is "image"
cv2.waitKey(0) # to wait for any key to be pressed
cv2.destroyAllWindows() # close all window after some key is pressed

plt.imshow(img, cmap = 'gray',interpolation = 'bicubic')
plt.plot([50,10],[80,50],'c', linewidth = 5)
plt.show()

cv2.imwrite('image/frgray.jpg',img)