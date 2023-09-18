import cv2 as cv
import sys

img = cv.imread('car.jpg')
if img is None:
    sys.exit("파일을 찾을 수 없습니다")

drawing = False  # 마우스 왼쪽 버튼이 눌러진 상태 여부를 나타내는 변수
ix, iy = -1, -1  # 사각형의 시작점 좌표
final_rectangle = None  # 최종으로 그린 사각형을 저장하는 변수

def draw(event, x, y, flags, param):
    global ix, iy, drawing, final_rectangle

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            img_copy = img.copy()
            cv.rectangle(img_copy, (ix, iy), (x, y), (255, 0, 0), 2)
            cv.imshow('Drawing', img_copy)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        final_rectangle = (ix, iy, x, y)
        cv.rectangle(img, (ix, iy), (x, y), (255, 0, 0), 2)
        cv.imshow('Drawing', img)

cv.namedWindow('Drawing')
cv.setMouseCallback('Drawing', draw)

while True:
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

# 최종으로 그린 사각형을 출력
if final_rectangle is not None:
    ix, iy, x, y = final_rectangle
    final_img = img.copy()
    cv.rectangle(final_img, (ix, iy), (x, y), (0, 255, 0), 2)
    cv.imshow('Final Rectangle', final_img)
    cv.waitKey(0)
