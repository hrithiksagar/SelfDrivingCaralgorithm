import cv2
import numpy as np
vid=cv2.VideoCapture('lane1.mp4')
while True:
    ret, frame = vid.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([10,0,0])#not yellow
    upper_yellow = np.array([145,60,255])
    mask_img = cv2.inRange(hsv, lower_yellow, upper_yellow)
    lines = cv2.HoughLinesP(mask_img, 1, np.pi / 180, 50, maxLineGap=50)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
    contours, _ = cv2.findContours(mask_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(frame, contours, -1, (0, 0, 0), 1)
    cv2.imshow('mask', frame)
    if cv2.waitKey(10) & 0xff == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()