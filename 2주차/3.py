import cv2 as cv
import sys
img =cv.imread('Car.jpg')
if img is None:
    sys.exit("파일을 찾을 수 없습니다")

cv.rectangle(img,(204,50),(700,700),(0,0,255),2)
cv.putText(img,'Car',(204,34),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)

cv.imshow('Draw',img)
cv.waitKey()
cv.destroyAllWindows()