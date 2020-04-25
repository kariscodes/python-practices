## Ex 5-9. QSplitter.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QFrame, QSplitter, QStyleFactory
from PyQt5.QtCore import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()

        # top frame design --- good for me
        top = QFrame()
        top.setFrameShape(QFrame.Box)
        top.setFrameShadow(QFrame.Raised)
        top.setLineWidth(2)
        top.setMidLineWidth(0)

        midleft = QFrame()
        midleft.setFrameShape(QFrame.StyledPanel)
        midleft.setFrameShadow(QFrame.Raised)
        midleft.setLineWidth(3)
        midleft.setMidLineWidth(3)

        midright = QFrame()
        midright.setFrameShape(QFrame.Panel)
        midright.setFrameShadow(QFrame.Raised)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.WinPanel)   # Frame style
        bottom.setFrameShadow(QFrame.Sunken)    # Frame shadow style
        bottom.setLineWidth(3)
        bottom.setMidLineWidth(3)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(midleft)
        splitter1.addWidget(midright)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(top)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        # QApplication.setStyle(QStyleFactory.create('Cleanlooks'))
        # QApplication.setStyle(QStyleFactory.create('Fusion'))
        # QApplication.setStyle(QStyleFactory.create('GTK+'))
        # QApplication.setStyle(QStyleFactory.create('Plastique'))
        # styles = ["Plastique", "Cleanlooks", "CDE", "Motif", "GTK+"]
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyle('Fusion')
    app.setStyle('Windows')
    ex = MyApp()
    sys.exit(app.exec_())