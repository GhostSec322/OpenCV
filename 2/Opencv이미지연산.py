
#이미지 읽어서 살펴보기
## flag : 이미지 읽는 방법 설정
##cv2.imread(filename,flag):이미지를 읽어서 Numpy객체로 만드는 함수
##IMREAD_COLOR:이미지 Color로 읽고 투명 부분 무시
##IMREAD_GRAYSCALE: 이미지를 Grayscale로 읽기(흑백사진)
##IMREAD_UNCHANGED: 이미지를 clolor로 읽고 투명한 부분도 읽기
##Opencv는 BGR로 처리한다 ex Numpy 객체(행,열, 색상:기본 BGR)



## 이미지 읽어서 살펴보기 cv2.imshow(title,image):특정한 이미지를 화면에 출력 title=윈도우 창 제목,image=출력할 이미지



##cv2.imwrite(filename,image):특정한 이미지를 파일로 저장하는 함수
# filename 저장할 이미지 파일 이름
# image 저장할 이미지 객체

## cv2.waitKey(time):기보드 입력을 처리하는 함수
# cv2.destoryAllWindows():화면의 모든 윈도우를 닫는 함수 

## 실습
##이미지 읽어서 Numpy객체로 표시 
import cv2

img = cv2.imread('home.png', cv2.IMREAD_COLOR)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.imwrite("result.png", img)

# 이미지를 흑백으로 변환
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 여기에서 이미지 객체를 넣어야 합니다.
cv2.imshow('img_gray', img_gray)
cv2.waitKey(0)
cv2.imwrite("result_gray.png", img_gray)

cv2.destroyAllWindows()
