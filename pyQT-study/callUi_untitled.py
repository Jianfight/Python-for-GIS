import sys
import Ui_untitled
from PyQt4 import QtGui, QtCore

class MyMainWindow(QtGui.QDialog, Ui_untitled.Ui_Dialog):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

app = QtGui.QApplication(sys.argv)
mywindow = MyMainWindow()
mywindow.show()
sys.exit(app.exec_())