import cv2
import numpy as np

cap = cv2.VideoCapture(0) # to use the first camera
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('image/output.avi', fourcc,20.0, (640,480))

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray) # to show another window contain gray image

    # if user press q, break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# to release camera
cap.release()
out.release() # to release (export) video
cv2.destroyAllWindows()