import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class SubAcctWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def __init__(self, parent=None):
        super().__init__()
        self.setWindowModality(Qt.NonModal)     # to set non-modal dialog
        self.initUI()

    def initUI(self):
        self.setWindowTitle('자산취득등록')
        self.setGeometry(100, 100, 500, 300)

    def show(self):
        # to show non-modal dialog, show() and exec_() should be used together.
        super().show()
        # super().exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = SubAcctWindow()
    # w = MainWindow()
    w.show()
    sys.exit(app.exec_())