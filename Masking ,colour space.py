import cv2
import numpy as np
cap= cv2.VideoCapture('car race.mp4')
while True:
    ret, frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_blue=np.array([101,50,38])
    upper_blue=np.array([110,255,255])
    mask_img=cv2.inRange(hsv,lower_blue,upper_blue)
    contour,_ = cv2.findContours(mask_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(frame, contour, 3,(0,255,0),3)
    cv2.imshow('frame',frame)
    cv2.imshow('frame_mask', mask_img)
    if cv2.waitKey(10) & 0xff==27:
        break

cap.release()
cv2.destroyAllWindows()
