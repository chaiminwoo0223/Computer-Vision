# PyQt로 간단한 GUI만들기(버튼을 클릭하면 삑 소리 들려주기)
from PyQt5.QtWidgets import *
import sys

class BeepSound(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('삑 소리 내기')
        self.setGeometry(200, 200, 500, 100)
        
        # 버튼 생성
        shortBeepButton = QPushButton('짧게 삑', self)
        longBeepButton = QPushButton('길게 삑', self)
        quitButton = QPushButton('나가기', self)
        self.label = QLabel('환영합니다.', self)
        
        # 버튼 위치와 크기 지정
        shortBeepButton.setGeometry(10, 10, 100, 30)
        longBeepButton.setGeometry(110, 10, 100, 30)
        quitButton.setGeometry(210, 10, 100, 30)
        self.label.setGeometry(10, 40, 500, 70)
        
        # 콜백 함수 지정
        shortBeepButton.clicked.connect(self.shortBeepFunction)
        longBeepButton.clicked.connect(self.longBeepFunction)
        quitButton.clicked.connect(self.quitFunction)
        
    def shortBeepFunction(self):
        self.label.setText('짧게 삑 소리를 내는 척 합니다.')
        
    def longBeepFunction(self):
        self.label.setText('길게 삑 소리를 내는 척 합니다.')
        
    def quitFunction(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = BeepSound()
    win.show()
    sys.exit(app.exec_())