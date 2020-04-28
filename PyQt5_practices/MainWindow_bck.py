import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from reference.SubWindow import SubWindow
from reference.SubDialog import SubDialog
from PyQt5_practices.NonModalDialog import NonModalDialog

# create menu, tool bar, status bar
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Main Window')
        # self.setGeometry(100, 100, 500, 400)
        self.fontsize = 11


        layout = QVBoxLayout()
        layout.addStretch(1)
        label = QLabel("미지정")
        label.setAlignment(Qt.AlignCenter)
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        self.label = label

        btn = QPushButton("값 얻어오기")
        btn.clicked.connect(self.onButtonClicked3)
        layout.addWidget(label)
        layout.addWidget(btn)

        layout.addStretch(1)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
        # Main Window Layout

        # layout1 = QVBoxLayout()
        # layout1.addStretch(1)
        # layout1.addWidget(btnAcq)
        # layout1.addWidget(btnResource)
        # layout1.addWidget(btnSW)
        # layout1.addWidget(btnUser)
        # layout1.addWidget(btnCode)
        # layout1.addStretch(1)
        #
        # layout2 = QVBoxLayout()
        # layout2.addStretch(1)
        # layout2.addWidget(btnReport1)
        # layout2.addWidget(btnReport2)
        # layout2.addStretch(1)
        #
        # layout = QHBoxLayout()
        # layout.addStretch(1)
        # layout.addLayout(layout1)
        # layout.addLayout(layout2)
        # layout.addStretch(1)

        # self.createGridLayout()
        # centralWidget = QWidget()
        # centralWidget.setLayout(self.layout)
        # self.setCentralWidget(centralWidget)

        # self.setLayout(layout)
        # self.center()
        # self.show()

    def createGridLayout(self):
        btnAcq =QPushButton("자산취득")
        btnAcq.setStyleSheet('color:black; background:white')
        btnResource = QPushButton("전산자원관리")
        btnResource.setStyleSheet('color:black; background:white')
        btnSW =QPushButton("소프트웨어")
        btnSW.setStyleSheet('color:black; background:grey')
        btnSW.setDisabled(True)
        btnUser = QPushButton("사용자")
        btnUser.setStyleSheet('color:blue; background:white')
        btnReport = QPushButton("보고서")
        btnReport.setStyleSheet('color:blue; background:white')
        btnSetting = QPushButton("설정")
        btnSetting.setStyleSheet('color:blue; background:white')
        self.layout = QGridLayout()
        # layout.setColumnStretch(1, 4)
        # layout.setColumnStretch(2, 4)
        self.layout.addWidget(btnAcq, 0, 0)
        self.layout.addWidget(btnResource, 0, 1)
        self.layout.addWidget(btnSW, 0, 2)
        self.layout.addWidget(btnUser, 1, 0)
        self.layout.addWidget(btnReport, 1, 1)
        self.layout.addWidget(btnSetting, 1, 2)

    def onButtonClicked3(self):
        win = NonModalDialog(self)
        win.show()

    def onButtonClicked2(self):
        win = SubWindow(self)

        r = win.show()

        if r:
            text = win.edit.text()
            self.label.setText(text)

    def onButtonClicked(self):
        win = SubDialog(self)
        # win.setWindowModality(Qt.NonModal)
        # win.setModal(False)
        # r = win.showModal()
        # r = win.show()
        win.show()
        win.exec_()
        #
        # if r:
        #     text = win.edit.text()
        #     self.label.setText(text)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def show(self):
        super().show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())