import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, Qt

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.resize(290, 290)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.cellClicked.connect(self._clickedTableWidget)
        self.tableWidget.setSortingEnabled(True)            # 컬럼 헤더를 클릭하면 정렬이 되게 한다.
        self.tableWidget.setAlternatingRowColors(True)      # 행 색상이 번갈아 구분 표시되게 한다.

        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)      # Edit 금지
        # EditTriggers : AllEditTriggers(default), NoEditTriggers

        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)     # Row 단위로 선택이 표되게 한다.
        # SelectionBehavior : SelectRows, SelectColumns, SelectItems

        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)    # 하나의 Row만 선택하게 함. (다중 선택하지 못하게 함.)
        # SelectionMode : NoSelection, SingleSelection, MultiSelection, ContiguousSelection, ExtendedSelection
        # (ExtendedSelection ~ drag, Ctrl, Shift 키로 다중 선택 가능)

        self.setTableWidgetData()

    def setTableWidgetData(self):
        self.tableWidget.setItem(0, 0, QTableWidgetItem("(0,0)"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("(0,1)"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("(1,0)"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("(1,1)"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("(2,0)"))
        a = QTableWidgetItem("(2,1)")
        a.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)   # item alignment
        self.tableWidget.setItem(2, 1, a)

    @pyqtSlot()  # prevents executing following function twice
    def _clickedTableWidget(self):
        row = self.tableWidget.currentRow()
        # print(row)
        # self.tableWidget.selectRow(row)     # 클릭한 쎌의 행 전체가 색상으로 표시되게 한다.

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()