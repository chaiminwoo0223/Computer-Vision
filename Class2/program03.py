# 에지 맵에서 경계선 찾기
import cv2 as cv

img = cv.imread('./img/soccer.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
canny = cv.Canny(gray, 100, 200) # 낮은 임계값 100 / 높은 임계값 200

contour, hierarchy = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

lcontour = [] # 경계선을 저장할 리스트
for i in range(len(contour)):
    if contour[i].shape[0] > 100:
        lcontour.append(contour[i])
        
cv.drawContours(img, lcontour, -1, (0,255,0), 3)

cv.imshow('Original', img)
cv.imshow('Canny', canny)

cv.waitKey()
cv.destroyAllWindows()