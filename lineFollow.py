import cv2
import numpy as np


cap = cv2.VideoCapture(0)


while 1:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    cv2.imshow("show ", frame)
    blur = cv2.GaussianBlur(frame, (9, 9), 5)
    cv2.imshow("blur", blur)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray", gray)
    (thresh, gray) = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)
    dataHsv: object = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    lower_color = np.array([0, 0, 0])
    upper_color = np.array([255, 255, 255])
    cv2.imshow("datahsv", dataHsv)
    mask = cv2.inRange(dataHsv, lower_color, upper_color)
    mask = cv2.dilate(mask, (3, 3), iterations=3)


    edges: object = cv2.Canny(mask, 90, 200)
    cv2.imshow("canny", edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

        cap.release()
        cv2.destroyAllWindows()





