# 감마 보정 실험하기
import cv2 as cv
import numpy as np

def gamma(f, gamma=1.0):
    f1 = f / 255.0
    return np.uint8(255*(f1**gamma))

img = cv.imread('./img/soccer.jpg')
img = cv.resize(img, dsize=(0,0), fx=0.25, fy=0.25)

gc = np.hstack((gamma(img, 0.5), gamma(img, 0.75), gamma(img, 1.0), gamma(img, 2.0), gamma(img, 3.0)))
cv.imshow('gamma', gc)

cv.waitKey()
cv.destroyAllWindows()