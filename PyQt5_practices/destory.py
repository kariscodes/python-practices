from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

def Log_Closed():
    print("Bye bye")

class My_dlg(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__( self, parent )

        #self.conn = open_connection()
        print("Connection Opened")

        close_btn  = QPushButton("Actually Close")
        QVBoxLayout(self).addWidget(close_btn)

        close_btn.clicked.connect(self.Actually_Close)
        self.destroyed.connect(Log_Closed)

    def Actually_Close(self):
        print("Actually Close")
        self.parent().close()

    def closeEvent(self, event):
        if event.type() == QEvent.Close:
            event.ignore()
            self.hide()
            print("hidden")

    # And I guess I need something like
    def destroyEvent(self, event):
        #self.conn.close()
        print("Connection Closed")
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main= QMainWindow()
    tsd = My_dlg(main)
    tsd.show()
    sys.exit(app.exec_())