# 소벨 에지 검출(Sobel 함수 사용)하기
import cv2 as cv

img = cv.imread('./img/soccer.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 소벨 연산자 적용
grad_x = cv.Sobel(gray, cv.CV_32F, 1, 0, ksize=3)
grad_y = cv.Sobel(gray, cv.CV_32F, 0, 1, ksize=3)

# 절댓값을 취해 양수 영상으로 변환
sobel_x = cv.convertScaleAbs(grad_x)
sobel_y = cv.convertScaleAbs(grad_y)

# 에지 강도 계산
edge_strength = cv.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

cv.imshow('Original', gray)
cv.imshow('Sobel x', sobel_x)
cv.imshow('Sobel y', sobel_y)
cv.imshow('Edge Strength', edge_strength)

cv.waitKey()
cv.destroyAllWindows()