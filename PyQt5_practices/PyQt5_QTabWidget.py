import sys
from PyQt5.QtWidgets import *

class MyApp(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        tabs = QTabWidget()
        tabs.addTab(FirstTab(), 'First')
        tabs.addTab(QWidget(), 'Second')
        tabs.addTab(QWidget(), 'Third')

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)

        self.setLayout(vbox)

        self.setWindowTitle('Test')
        self.setGeometry(300, 300, 400, 300)
        self.show()

class FirstTab(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        name = QLabel('Name:')
        nameEdit = QLineEdit()
        age = QLabel('Age:')
        ageEdit = QLineEdit()

        okButton = QPushButton('OK',self)
        xButton = QPushButton('X', self)

        vbox = QVBoxLayout()
        vbox.addWidget(name)
        vbox.addWidget(nameEdit)
        vbox.addWidget(age)
        vbox.addWidget(ageEdit)
        vbox.addWidget(okButton)
        vbox.addWidget(xButton)
        vbox.addStretch()

        self.setLayout(vbox)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())