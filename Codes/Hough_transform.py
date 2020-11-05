import sys
import math
import cv2 as cv
import numpy as np

#Read image.
default_file = 'circuito.jpg'
source_img = cv.imread(default_file, cv.IMREAD_GRAYSCALE)

#Canny operator.
dst = cv.Canny(source_img, 50, 200, None, 3)
    
# Copy edges to the images that will display the results in BGR
hough = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
hough_prob = np.copy(hough)
    
lines = cv.HoughLines(dst, 1, np.pi / 180, 150, None, 0, 0)
    
if lines is not None:
    for i in range(0, len(lines)):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = math.cos(theta)
        b = math.sin(theta)
        x0 = a * rho
        y0 = b * rho
        pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
        pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
        cv.line(hough, pt1, pt2, (0,0,255), 3, cv.LINE_AA)
        
linesP = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)
    
if linesP is not None:
    for i in range(0, len(linesP)):
        l = linesP[i][0]
        cv.line(hough_prob, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv.LINE_AA)
    
cv.imshow("Original Image", source_img)
cv.imshow("Standard Hough Line Transform", hough)
cv.imwrite('img4.png', hough)
#cv.imshow("Probabilistic Line Transform", hough_prob)
    
cv.waitKey()
