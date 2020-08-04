import cv2
cap=cv2.VideoCapture(0)
while True:
    ret, frame= cap.read()
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',grey)
    cv2.imshow('color_frame',frame)
    if cv2.waitKey(30) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

