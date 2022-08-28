import cv2
import numpy as np

camera = cv2.VideoCapture(0)

dusuk = np.array([25, 50, 50])
yuksek = np.array([32, 255, 255])

while True:

  ret, goruntu = camera.read()

  hsv = cv2.cvtColor(goruntu, cv2.COLOR_BGR2HSV)

  cv2.imshow("hsv", hsv)

  mask = cv2.inRange(hsv, dusuk, yuksek)

  son_grnt = cv2.bitwise_and(goruntu, goruntu, mask = mask)

  cv2.imshow("renk algılama", son_grnt)

  kernel = np.ones((15, 15), dtype = np.float32) / 225

  smoothed = cv2.filter2D(son_grnt, -1, kernel)



  blur = cv2.GaussianBlur(son_grnt, (15, 15), 0)


  cv2.imshow("bgrlı ana goruntu", goruntu)

  cv2.imshow("blur", blur)


  median = cv2.medianBlur(son_grnt, 15)

  bilateral = cv2.bilateralFilter(son_grnt, 15, 75, 75)

  cv2.imshow("median", median)

  cv2.imshow("bilateral", bilateral)



  if cv2.waitKey(1) & 0xFF == ord('q'):
   break

   camera.release()
   cv2.destroyAllWindows()




