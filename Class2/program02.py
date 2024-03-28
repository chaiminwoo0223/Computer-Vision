# 캐니 에지 실험하기
import cv2 as cv

img = cv.imread('./img/soccer.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

canny1 = cv.Canny(gray, 50, 150) # 낮은 임계값 50 / 높은 임계값 150
canny2 = cv.Canny(gray, 100, 200) # 낮은 임계값 100 / 높은 임계값 200

cv.imshow('Original', gray)
cv.imshow('Canny1', canny1)
cv.imshow('Canny2', canny2)

cv.waitKey()
cv.destroyAllWindows()