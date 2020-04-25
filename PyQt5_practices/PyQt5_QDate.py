import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDateEdit, QVBoxLayout
from PyQt5.QtCore import QDate


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbl = QLabel('QDateEdit')

        self.dateEditWidget = QDateEdit()
        # theDate = QDate()
        # self.dateEditWidget.setDate(theDate.currentDate())    # 현재 날짜
        # theDate.setDate()
        # self.dateEditWidget.setDate(QDate.currentDate())    # 현재 날짜
        self.dateEditWidget.setMinimumDate(QDate(2000, 1, 1))
        self.dateEditWidget.setMaximumDate(QDate(2100, 12, 31))
        self.dateEditWidget.setDisplayFormat('yyyy.MM.dd')
        self.dateEditWidget.setCalendarPopup(True)
        self.dateEditWidget.setDate(QDate(2020, 5, 1))    # 지정한 날짜

        # self.dateEditWidget.setDate(QDate.currentDate())

        self.dateEditWidget.dateChanged.connect(self.__dateChanged)

        vbox = QVBoxLayout()
        vbox.addWidget(lbl)
        vbox.addWidget(self.dateEditWidget)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('QDateEdit')
        self.setGeometry(300, 300, 300, 200)

    def __dateChanged(self):
        varQDate = self.dateEditWidget.date()   # QDate
        print(varQDate)
        print(varQDate.toString('yyyy-MM-dd'))
        print(f'Year:{varQDate.year()} Month:{varQDate.month()} Day:{varQDate.day()}')
        print('5 Years later:\t', varQDate.addYears(5).toString('yyyy-MM-dd'))
        print('5 Months later:\t', varQDate.addMonths(5).toString('yyyy-MM-dd'))
        print('5 Days later:\t', varQDate.addDays(5).toString('yyyy-MM-dd'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())