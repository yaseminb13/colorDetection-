

# line-follower.py

# A line following robot for Robotics Systems final project
# Coded using Python 2.7.13 and OpenCV 3.3 for a Raspberry Pi 3B running Raspbian
# Uses Raspberry Pi camera module v2

import numpy as np
import time
import cv2
import matplotlib



cap = cv2.VideoCapture(0)





	cv2.imshow('cap', cap)

	# Create key to break for loop
	key = cv2.waitKey(1) & 0xFF  # 1 e basılınca duruyor

	# convert to grayscale, gaussian blur, and threshold
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray, (5, 5), 0)
	ret, thresh1 = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY_INV)

	# Erode to eliminate noise, Dilate to restore eroded parts of image
	mask = cv2.erode(thresh1, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)

	# Find all contours in frame
	something, contours, hierarchy = cv2.findContours(mask.copy(), 1, cv2.CHAIN_APPROX_NONE)

	# Find x-axis centroid of largest contour and cut power to appropriate motor
	# to recenter camera on centroid.
	# This control algorithm was written referencing guide:
	# Author: Einsteinium Studios
	# Availability: http://einsteiniumstudios.com/beaglebone-opencv-line-following-robot.html
	if len(contours) > 0:
		# Find largest contour area and image moments
		c = max(contours, key=cv2.contourArea)
		M = cv2.moments(c)

		# Find x-axis centroid using image moments
		cx = int(M['m10'] / M['m00'])

		if cx >= 150:
			cap.output(12, cap.LOW)
			cap.output(21, cap.HIGH)

		if cx < 150 and cx > 40:
			cap.output(12, cap.HIGH)
			cap.output(21, cap.HIGH)

		if cx <= 40:
			cap.output(12, cap.HIGH)
			cap.output(21, cap.LOW)

if key == ord("q"):
	pass
else:
	pass