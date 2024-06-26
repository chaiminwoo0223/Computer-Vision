# 비디오에서 얼굴 검출하기
import cv2 as cv
import mediapipe as mp

mp_face_detectioon = mp.solutions.face_detection
mp_drawimg = mp.solutions.drawing_utils
face_detection = mp_face_detectioon.FaceDetection(model_selection=0, min_detection_confidence=0.5)
cap = cv.VideoCapture(0, cv.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    if not ret:
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break

    res = face_detection.process(cv.cvtColor(frame, cv.COLOR_BGR2RGB))

    if res.detections:
        for detection in res.detections:
            mp_drawimg.draw_detection(frame, detection)
        
    cv.imshow('MediaPipe Face Detection from video', cv.flip(frame, 1))
    if cv.waitKey(5)==ord('q'):
        break

cap.release()
cv.destroyAllWindows()