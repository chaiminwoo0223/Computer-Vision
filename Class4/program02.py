# OpenCV에 PyQt의 GUI 붙이기(비디오에서 프레임을 잡아 저장하기)
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
import sys
import cv2 as cv

class Video(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('비디오에서 프레임 수집')
        self.setGeometry(200,200,500,100)
        
        # 버튼 생성
        videoButton = QPushButton('비디오 켜기', self)
        openButton = QPushButton('비디오 불러오기', self)
        captureButton = QPushButton('프레임 잡기', self)
        saveButton = QPushButton('프레임 저장', self)
        quitButton = QPushButton('나가기', self)
                
        # 버튼 위치와 크기 지정
        videoButton.setGeometry(10, 10, 100, 30)
        openButton.setGeometry(110, 10, 120, 30)
        captureButton.setGeometry(230, 10, 100, 30)
        saveButton.setGeometry(330, 10, 100, 30)
        quitButton.setGeometry(430, 10, 60, 30)
                
        # 콜백 함수 지정
        videoButton.clicked.connect(self.videoFunction)
        openButton.clicked.connect(self.openFunction)
        captureButton.clicked.connect(self.captureFunction)
        saveButton.clicked.connect(self.saveFunction)
        quitButton.clicked.connect(self.quitFunction)
                
    def videoFunction(self):
        self.cap = cv.VideoCapture(0, cv.CAP_DSHOW)
        if not self.cap.isOpened(): self.close()
        while True:
            ret, self.frame = self.cap.read()
            if not ret: break
            cv.imshow('video display', self.frame)
            cv.waitKey(1)
            
    def openFunction(self):
        fname = QFileDialog.getSaveFileName(self, '파일열기', './')
        self.cap = cv.VideoCapture(fname[0])
        while True:
            ret, self.frame = self.cap.read()
            cv.imshow('video display', self.frame)
            cv.waitKey(25)
    
    def captureFunction(self):
        self.capturedFrame = self.frame
        cv.imshow('Captured Frame', self.capturedFrame)
        
    def saveFunction(self):
        fname = QFileDialog.getSaveFileName(self, '파일저장', './')
        cv.imwrite(fname[0], self.capturedFrame)
    
    def quitFunction(self):
        self.cap.release()
        cv.destroyAllWindows()
        self.close()
    
app = QApplication(sys.argv)
win = Video()
win.show()
app.exec_()