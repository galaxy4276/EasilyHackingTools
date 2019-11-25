import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, qApp, QDesktopWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QFileDialog, QTextEdit, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import  QTime, Qt

class DCBA(QMainWindow, QWidget):

    # 프로그램 시작 시 가동되는 함수, 즉 초기화 담당 함수를 불러옴
    def __init__(self):
        super().__init__()

        self.time = QTime.currentTime()
        self.initUI()


    # 초기화 담당 함수
    def initUI(self):
        # 불러오는 파일의 내용이 들어가는 자료형
        file = []

        #GUI 시스템에 보여지는 부분들이 정리된 부분
        exitAction = QAction(QIcon('exit.png'), '종료하기', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('프로그램 종료')
        exitAction.triggered.connect(qApp.quit)
        FileOpenAction = QAction(QIcon('web.png'), '파일 열기', self)
        FileOpenAction.setShortcut('Ctrl+O')
        FileOpenAction.setStatusTip('파일을 엽니다.')
        FileOpenAction.triggered.connect(self.showDialog)
        self.statusBar().showMessage('develop by DDC_Semicolon_Network/Security Team')

        # 메뉴 GUI
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('파일')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(FileOpenAction)

        #Crack 동작 관련 동작 코드들
        self.result = QLineEdit(self)
        self.result.move(17,160)
        EventLabel = QLabel("result ^-_-^", self)
        EventLabel.move(19,125)
        EncBtn = QPushButton('Starting!', self)
        EncBtn.clicked.connect(self.crack)
        EncBtn.move(16,90)
        self.toolbar = self.addToolBar('종료')
        self.toolbar.addAction(exitAction)

        #프로그램 정보
        self.setWindowTitle('대덕뚫어')
        self.setWindowIcon(QIcon('DCBA_icon.png'))
        self.resize(300,500)
        self.show()


    # 화면 중앙배치 함수
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # 애플리케이션과 시스템이 상호작용할수있게끔 작성된 함수
    # 파일을 열수있게끔 대화창을 열어줌
    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self,'파일 열기', './')
        print(fname)
        print(fname[0])
        if fname[0]:
            file = open(fname[0], 'r')
            self.f = file.readline()
            print(self.f)
            file.close()

    def crack(self):
        crack=[]

        #crack 리스트변수안에 비밀번호가 될수있는 모든 문자를 저장
        for i in range(0, 123):
            crack.append(chr(i))
        Password = self.f
        print("crack test : %s"%Password)
        found_pw=[]
        cracked_pw=[]
        start_index = 0

        #패스워드 필드값 찾기 1
        for i in range(0, len(Password)):
            if(Password[i] == 'p' and Password[i+1] == "a" and Password[i+2] == 's' and Password[i+3] == 's' and Password[i+4] == 'w' and Password[i+5] == 'o' and Password[i+6] == 'r' and Password[i+7] == 'd' and Password[i+8] == ':'):
                start_index = i+9 # password 필드의 시작부터 긁게 된다.

        # 패스워드 필드값 찾기 2 ( 현재 버그 존재 ) # 11.23 13:54 버그 제거 완료 ( 테스트 필요 )
        for i in range(start_index, start_index+8): 
            found_pw.append(Password[i])

        #데이터 가공 처리 단계
        for i in range(0, len(found_pw)):
            for j in range(0, len(crack)):
                if(found_pw[i]==crack[j]):
                    cracked_pw.append(found_pw[i])

        # 최종 데이터 처리 구문
        hola = ""
        for i in found_pw:
            hola += i
        print(hola)

        # 프로그램 내에 LineEdit에 최종 데이터를 출력 ( 문자열 )
        self.result.setText(str(hola))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DCBA()
    sys.exit(app.exec_())