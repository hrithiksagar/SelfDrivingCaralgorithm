import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canny=cv2.Canny(frame,50,300)
    cv2.imshow('frame1',canny)
    cv2.imshow('frame',gray)
    blurr=cv2.GaussianBlur(canny,(15,15),0)
    cv2.imshow('frame2',blurr)
    canny1=cv2.Canny(blurr,50,100)
    cv2.imshow('frame3',canny1)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
#now we know
# how to read video,real time ,normal video
#grey
#canny detection
#wait key(more detail)

