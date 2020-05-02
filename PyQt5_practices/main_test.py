#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QAction, QGroupBox, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # self.setGeometry(300, 300, 400, 300)  # x, y, w, h
        self.setWindowTitle('ITRM')
        self.statusBar().showMessage('Message in status bar')

        mainMenu = self.menuBar()
        # fileMenu = mainMenu.addMenu('File')
        # editMenu = mainMenu.addMenu('Edit')
        # viewMenu = mainMenu.addMenu('View')
        # searchMenu = mainMenu.addMenu('Search')
        # toolsMenu = mainMenu.addMenu('Tools')
        # helpMenu = mainMenu.addMenu('Help')
        fileMenu = mainMenu.addMenu('파일')
        editMenu = mainMenu.addMenu('등록')
        # viewMenu = mainMenu.addMenu('View')
        searchMenu = mainMenu.addMenu('조회')
        toolsMenu = mainMenu.addMenu('설정')
        helpMenu = mainMenu.addMenu('도움말')

        # exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton = QAction('종료', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)
        # exitMenu = fileMenu.addMenu('종료')
        # exitMenu.addAction(exitButton)

        menuBarcode = QAction('바코드 등록', self)
        menuBarcode.triggered.connect(self.setBarcode)
        # menuBarcode.triggered.connect(self.close)
        editMenu.addAction(menuBarcode)

        self.show()

    def setBarcode(self):
        self.createHorizontalLayout()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

        self.show()

    def createHorizontalLayout(self):
        self.horizontalGroupBox = QGroupBox("What is your favorite color?")
        layout = QHBoxLayout()

        buttonBlue = QPushButton('Blue', self)
        buttonBlue.clicked.connect(self.on_click)
        layout.addWidget(buttonBlue)

        buttonRed = QPushButton('Red', self)
        buttonRed.clicked.connect(self.on_click)
        layout.addWidget(buttonRed)

        buttonGreen = QPushButton('Green', self)
        buttonGreen.clicked.connect(self.on_click)
        layout.addWidget(buttonGreen)

        self.horizontalGroupBox.setLayout(layout)

    def on_click(self):
        print('PyQt5 button click')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.showMaximized()
    # palette = QPalette()
    # palette.setColor(QPalette.Background, Qt.white)
    # mainWindow.setPalette(palette)
    mainWindow.show()
    sys.exit(app.exec_())