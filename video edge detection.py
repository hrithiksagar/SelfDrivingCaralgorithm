#edge detection in videos(video analysis)
import cv2
cap=cv2.VideoCapture(0)
while True:
    ret, frame=cap.read()
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    canny=cv2.Canny(frame, 50,200)
    cv2.imshow('frame',canny)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()