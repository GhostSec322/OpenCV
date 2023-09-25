import cv2 as cv
import sys

# 이미지를 읽어옵니다.
img = cv.imread('car.jpg')

# 'Drawing'이라는 이름의 창을 생성하고 초기 이미지를 표시합니다.
cv.imshow('Drawing', img)

# 이미지가 없을 경우 프로그램을 종료합니다.
if img is None:
    sys.exit("파일을 찾을 수 없습니다")

drawing = False
ix, iy = -1, -1
final_rectangle = None

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

# 'Drawing' 창에 마우스 이벤트 핸들러를 연결합니다.
cv.setMouseCallback('Drawing', draw)

while True:
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

if final_rectangle is not None:
    ix, iy, x, y = final_rectangle
    final_img = img.copy()
    cv.rectangle(final_img, (ix, iy), (x, y), (0, 255, 0), 2)

# 'Final Rectangle' 창에 최종 이미지를 표시합니다.

cv.waitKey(0)
