import cv2
import numpy as np

img = cv2.imread('image/fr.jpg',cv2.IMREAD_COLOR)

# to draw a line on the image, with width = 15
cv2.line(img,(0,0),(150,150),(250,5,0), 15)
cv2.rectangle(img, (15,25),(200,150),(0,245,0),5)
cv2.circle(img,(100,63),55,(0,0,255),-1) # a negative line width will fill the color

pts = np.array([[10,3],[12,30],[30,23],[23,12]],np.int32)
# pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts], True,(0,255,255),3) # draw a polygon

font = cv2.FONT_HERSHEY_COMPLEX
# text start at position (0,120); spacing 5;
cv2.putText(img,'OpenCV text',(0,120),font, 1, (200,155,255),5, cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
