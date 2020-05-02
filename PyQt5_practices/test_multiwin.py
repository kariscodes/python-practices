from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

# from ui_Main import Ui_Main
# from ui_Window1 import Ui_Window1
# from ui_Window2 import Ui_Window2

class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        #Initialisation functions

        self.PushButton1.clicked.connect(self.OpenWindow1)
        self.PushButton2.clicked.connect(self.OpenWindow2)

    def OpenWindow1(self):
        showWindow1.show()

    def OpenWindow2(self):
        showWindow2.show()

class Window1(QMainWindow, Ui_Window1):
    def __init__(self, parent=None):
        super(Window1, self).__init__(parent)
        self.setupUi(self)

class Window2(QMainWindow, Ui_Window2):
    def __init__(self, parent=None):
        super(Window2, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    showMain = Main()
    showWindow1 = Window1()
    showWindow2 = Window2()
    showMain.show()

    app.exec_()