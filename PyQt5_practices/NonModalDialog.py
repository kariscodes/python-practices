import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class NonModalDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def __init__(self, parent):
        super().__init__()
        self.setWindowModality(Qt.NonModal)     # to set non-modal dialog
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Dialog')
        self.setGeometry(100, 100, 200, 100)

    def show(self):
        # to show non-modal dialog, show() and exec_() should be used together.
        super().show()
        super().exec_()

