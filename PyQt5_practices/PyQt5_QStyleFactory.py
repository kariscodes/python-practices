import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)
        self.styleLabel = QLabel('Application Style')
        self.styleComboBox = QComboBox()
        factory = QStyleFactory.keys()
        self.styleComboBox.addItems(factory)
        self.styleComboBox.currentIndexChanged.connect(self._selectStyle)

        winLayout = QHBoxLayout()
        winLayout.addWidget(self.styleLabel)
        winLayout.addWidget(self.styleComboBox)

        theBox = QFrame()
        theBox.setLayout(winLayout)
        self.setCentralWidget(theBox)

    @pyqtSlot()  # prevents executing following function twice
    def _selectStyle(self):
        styleName = self.styleComboBox.currentText()
        QApplication.setStyle(styleName)        # Application Style을 변경한다.

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()