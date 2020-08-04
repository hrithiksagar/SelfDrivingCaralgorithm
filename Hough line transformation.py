import cv2
import numpy as np
video = cv2.VideoCapture(0)

while True:
    ret, orig_frame = video.read()
    if not ret:
        video = cv2.VideoCapture(0)
        continue

    frame = cv2.GaussianBlur(orig_frame, (5, 5), 1)
    edges = cv2.Canny(frame, 75, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, maxLineGap=50)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)
    cv2.imshow("frame", frame)
    #cv2.imshow("edges", edges)

    key = cv2.waitKey(27)
    if key == 27:
        break

cv2.waitKey(27)
video.release()
cv2.destroyAllWindows()

