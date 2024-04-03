# 해리스 특징점 검출 구현하기
import cv2 as cv
import numpy as np

img = np.zeros([10, 10], np.float32)
for i in range(2,7):
    img[i,3:(i+2)] = 1

print(img)

ux = np.array([-1, 0, 1])
uy = ux.transpose()
k = cv.getGaussianKernel(3, 1)
g = np.outer(k, k.transpose()) # 3 x 3 Gaussian Filter

dy = cv.filter2D(img, cv.CV_32F, uy)
dx = cv.filter2D(img, cv.CV_32F, ux)
dyy = dy*dy
dxx = dx*dx
dyx = dy*dx
gdyy = cv.filter2D(dyy, cv.CV_32F, g)
gdxx = cv.filter2D(dxx, cv.CV_32F, g)
gdyx = cv.filter2D(dyx, cv.CV_32F, g)

C = (gdyy*gdxx - gdyx*gdyx) - 0.04*((gdyy+gdxx)**2)

for j in range(1, C.shape[0]-1):
    for i in range(1, C.shape[1]-1):
        if C[j,i] > 0.1 and sum(sum(C[j,i] > C[j-1:j+2, i-1:i+2])) == 8:
            img[j,i] = 9
            
np.set_printoptions(precision=2) # 소수점 2번째 자리수

print('dy:\n', dy)
print('dx:\n', dx)
print('dyy:\n', dyy)
print('dxx:\n', dxx)
print('gdyy:\n', gdyy)
print('gdxx:\n', gdxx)
print('gdyx:\n', gdyx)
print('C:\n', C)
print('img:\n', img)