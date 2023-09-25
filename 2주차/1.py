import cv2 as cv
import sys
img=cv.imread('soccer.jpg')

if img is None:
    sys.exit('파일을 열 수 없습니다')
    
cv.imshow("Img",img)

cv.waitKey()
cv.destriyAllWindows()