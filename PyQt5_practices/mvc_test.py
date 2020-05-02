import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QAbstractTableModel, pyqtSlot

from interface import mysqlHandler


class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role:Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None

class UserTableModel(QAbstractTableModel):
    def __init__(self, parent, mylist, header, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.mylist = mylist
        self.header = header
    def rowCount(self, parent):
        return len(self.mylist)
    def columnCount(self, parent):
        #return len(self.mylist[0])
        return len(self.header)
    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.mylist[index.row()][index.column()]
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None
    def sort(self, col, order):
        """sort table by given column number col"""
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.mylist = sorted(self.mylist,
            key=operator.itemgetter(col))
        if order == Qt.DescendingOrder:
            self.mylist.reverse()
        self.emit(SIGNAL("layoutChanged()"))

class MVC_TestWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        # self.setTableWidgetData()

    def initUI(self):
        mainLayout = QVBoxLayout()
        btnRun = QPushButton('실행')
        btnRun.clicked.connect(self.__btnRunClicked)

        self._tableView = QTableView()

        self.loadUsers()
        self._tableWidget = QTableWidget()
        self._tableWidget.cellClicked.connect(self.__tableWidgetCellClicked)
        self._tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        mainLayout.addWidget(btnRun)
        mainLayout.addWidget(self._tableView)
        mainLayout.addWidget(self._tableWidget)
        self.setLayout(mainLayout)

        # col = self._userModel.columnCount(self)
        # print(col)

    def loadUsers(self):
        try:
            db_connection = mysqlHandler.dbConnect()
            cursor = mysqlHandler.dbCursor(db_connection)
            sql = 'select user_name, ' \
                         'job_type, ' \
                         'org, ' \
                         'regular_exchange, ' \
                         'region, ' \
                         'location, ' \
                         'extra_disk, ' \
                         'extra_disk_type, ' \
                         'extra_disk_capacity, ' \
                         'user_note ' \
                  ' from myasset.it_user order by user_name'
            cursor.execute(sql)
            data = cursor.fetchall()
            column_headers = ['user_name', 'job_type', 'org', 'regular_exchange', 'region', 'location', 'extra_disk', 'extra_disk_type', 'extra_disk_capacity', 'user_note']
            # self._userModel._data = result
            self._userModel = UserTableModel(self, data, column_headers)
            self._tableView.setModel(self._userModel)
        finally:
            db_connection.close()


    # Show selected query statement in the query input box
    @pyqtSlot(int, int)
    def __tableWidgetCellClicked(self, row, col):
        cell = self._tableWidget.item(row, 3)
        # if cell is not None:
        #     self._inputQuery.setText(cell.text())
        return

    # Run sql query
    def __btnRunClicked(self):
        pass
        # db_connection = mysqlHandler.dbConnect()
        # cursor = mysqlHandler.dbDictCursor(db_connection)
        # sql = self._inputQuery.toPlainText()
        # cursor.execute(sql)
        # result = cursor.fetchall()
        # self._dataframe = pd.DataFrame(result)
        # model = pandasModel(self._dataframe)
        # self._tableView.setModel(model)
        # db_connection.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MVC_TestWindow()
    w.show()
    sys.exit(app.exec_())