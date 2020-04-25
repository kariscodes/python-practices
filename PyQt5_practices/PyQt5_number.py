# number delimiter

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtCore import QLocale

import locale

# import locale
# locale.setlocale(locale.LC_ALL, '')
# n = -1234567890.123
# s = locale.format_string('%.3f', n, 1)
# print(s)



class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        locale.setlocale(locale.LC_ALL, '')
        self.numberEdit = QLineEdit()
        # theValidator = QIntValidator(0, 1999999999)   # 최대 숫자 제한
        # 최소수(0),최대수(99억),소수점 뒤 갯수(0)
        theValidator = QDoubleValidator(0,9999999999,0)
        theValidator.setNotation(QDoubleValidator.StandardNotation)
        self.numberEdit.setValidator(theValidator)
        self.numberEdit.setMaxLength(10)
        # theLocale = QLocale()
        # theLocale.toString
        # # theLocale.setNumberOptions(QLocale.DefaultNumberOptions)
        # # theLocale.currencySymbol(QLocale.CurrencyIsoCode)
        # theLocale.setNumberOptions(QLocale.OmitGroupSeparator)
        # self.numberEdit.setLocale(theLocale)
        # self.numberEdit.setInputMask('#,###,###,###')
        # self.numberEdit.setInputMask('0,000,000,000')
        # self.numberEdit.setInputMask('+99_9999_999999')     # 국제 전화번호
        self.numberEdit.textChanged.connect(self.__textChanged)
        self.numberEdit.returnPressed.connect(self.__textReturned)

        vbox = QVBoxLayout()
        vbox.addWidget(self.numberEdit)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('TEST')
        self.setGeometry(300, 300, 300, 200)

    def __textChanged(self):
        pass

    def __textReturned(self):
        number = int(self.numberEdit.text())
        formattedNumber = locale.format_string('%d', number, 1)
        # self.numberEdit.setText(formattedNumber)
        print(formattedNumber)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())

