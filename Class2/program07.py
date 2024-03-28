# GrabCut을 이용해 물체 분할하기
import cv2 as cv
import numpy as np

def painting(event, x, y, flags, param):
    if event==cv.EVENT_LBUTTONDOWN:
        cv.circle(img_show, (x,y), BrushSize, LColor, -1) # 왼쪽 버튼 클릭하면 파란색
        cv.circle(mask, (x,y), BrushSize, cv.GC_FGD, -1)
    elif event==cv.EVENT_RBUTTONDOWN:
        cv.circle(img_show, (x,y), BrushSize, RColor, -1) # 오른쪽 버튼 클릭하면 빨간색
        cv.circle(mask, (x,y), BrushSize, cv.GC_BGD, -1)
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_LBUTTON:
        cv.circle(img_show, (x,y), BrushSize, LColor, -1) # 왼쪽 버튼 클릭하고 이동하면 파란색
        cv.circle(mask, (x,y), BrushSize, cv.GC_FGD, -1)
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_RBUTTON:
        cv.circle(img_show, (x,y), BrushSize, RColor, -1) # 오른쪽 버튼 클릭하고 이동하면 빨간색
        cv.circle(mask, (x,y), BrushSize, cv.GC_BGD, -1)

img = cv.imread('./img/soccer.jpg') # 영상 읽기
img_show = np.copy(img) # 붓칠을 디스플레이할 목적의 영상
mask = np.zeros((img.shape[0], img.shape[1]), np.uint8) # 마스크
mask[:,:] = cv.GC_PR_BGD # 모든 화소를 배경일 것 같음으로 초기화
BrushSize = 9 # 붓의 크기
LColor, RColor = (255,0,0), (0,0,255) # 파란색(물체)과 빨간색(배경)

cv.imshow('Painting', img_show)
cv.namedWindow('Painting')
cv.setMouseCallback('Painting', painting)

# 붓칠을 끝내려면 'q' 키를 누름
while(True):
    if cv.waitKey(1)==ord('q'):
        break
    
# 여기부터 GrabCut 적용하는 코드
background = np.zeros((1,65), np.float64) # 배경 히스토그램 0으로 초기화
foreground = np.zeros((1,65), np.float64) # 물체 히스토그램 0으로 초기화

cv.grabCut(img, mask, None, background, foreground, 5, cv.GC_INIT_WITH_MASK)
mask2 = np.where((mask==cv.GC_BGD)|(mask==cv.GC_PR_BGD), 0, 1).astype('uint8')
grab = img * mask2[:,:,np.newaxis]
cv.imshow('Grab Cut Image', grab)

cv.waitKey()
cv.destroyAllWindows()