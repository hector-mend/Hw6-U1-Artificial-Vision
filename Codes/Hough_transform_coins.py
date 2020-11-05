import sys
import cv2 as cv
import numpy as np

default_file = 'img1.jpg'

src = cv.imread(default_file, cv.IMREAD_COLOR)

dsize = (440, 400)
src0 = cv.imread(default_file, cv.IMREAD_COLOR)
src = cv.resize(src0, dsize, interpolation = cv.INTER_AREA)
src2 = cv.resize(src0, dsize, interpolation = cv.INTER_AREA)

#Eliminate background
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray, 5)
rows = gray.shape[0]
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8, param1=100, param2=30, minRadius=1, maxRadius=100)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        center = (i[0], i[1])
        cv.circle(src, center, 1, (0, 100, 100), 3)
        radius = i[2]
        cv.circle(src, center, radius, (255, 0, 255), 3)

cv.imshow("Circles Detected", src)
cv.imwrite('img3.png',src)
cv.waitKey(0)
