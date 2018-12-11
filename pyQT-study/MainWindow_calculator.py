import sys
from PyQt4 import QtGui, QtCore
#import Ui_calculator
from Ui_calculator import Ui_MainWindow

class mainWindowCalculator(QtGui.QMainWindow, Ui_MainWindow):

    lcdstring = '' # 定义一个公共的变量，用于显示lcd控件中显示文本
    operation = '' # 定义一个存储操作符的变量
    currentNum = 0 # 用来存储参与运算的变量
    prevlousNum = 0 # 用来存储参与运算的变量
    result = 0 # 用来存储运算结果

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.action() # 将信号和槽的函数都放在当中

    def action(self):
        # 按下数字时执行的方法
        self.connect(self.b0, QtCore.SIGNAL('clicked()'), self.buttonClicked)
        self.connect(self.b1, QtCore.SIGNAL('clicked()'), self.buttonClicked)
        self.connect(self.b2, QtCore.SIGNAL('clicked()'), self.buttonClicked)
        self.connect(self.b3, QtCore.SIGNAL('clicked()'), self.buttonClicked)
        self.connect(self.b4, QtCore.SIGNAL('clicked()'), self.buttonClicked)
        self.connect(self.b5, QtCore.SIGNAL('clicked()'), self.buttonClicked)
        self.connect(self.b6, QtCore.SIGNAL('clicked()'), self.buttonClicked)
        self.connect(self.b7, QtCore.SIGNAL('clicked()'), self.buttonClicked)
        self.connect(self.b8, QtCore.SIGNAL('clicked()'), self.buttonClicked)
        self.connect(self.b9, QtCore.SIGNAL('clicked()'), self.buttonClicked)
        self.connect(self.b_point, QtCore.SIGNAL('clicked()'), self.buttonClicked)

        # 按下操作符时执行的方法
        self.connect(self.b_plus, QtCore.SIGNAL('clicked()'), self.opClicked)
        self.connect(self.b_sub, QtCore.SIGNAL('clicked()'), self.opClicked)
        self.connect(self.b_mul, QtCore.SIGNAL('clicked()'), self.opClicked)
        self.connect(self.b_div, QtCore.SIGNAL('clicked()'), self.opClicked)

        # 按下清除键时执行的方法
        self.connect(self.b_reset, QtCore.SIGNAL('clicked()'), self.resetClicked)

        # 按下等于键时执行的方法
        self.connect(self.b_eq, QtCore.SIGNAL('clicked()'), self.eqClicked)

    def buttonClicked(self):
        # 防止输入过多，数字无法显示
        if len(mainWindowCalculator.lcdstring) <= 7: # 这里判断条件为7是因为，我们是先判断后执行lcdstring的更新，所以数量会少1
            mainWindowCalculator.lcdstring = mainWindowCalculator.lcdstring + self.sender().text()  # 将按键值和变量中原有的值相连接
            # 防止用户只输入.和多输入.的时候报错
            if mainWindowCalculator.lcdstring == '.':
                mainWindowCalculator.lcdstring = '0.'
            elif str(mainWindowCalculator.lcdstring).count('.') > 1:  # 使用str()是因为在此时为QString，其并不具备count()方法
                mainWindowCalculator.lcdstring = str(mainWindowCalculator.lcdstring)[:-1]  # 使用切片的方式将新点击的.删除掉
            else:
                self.lcd.display(mainWindowCalculator.lcdstring)
                mainWindowCalculator.currentNum = float(mainWindowCalculator.lcdstring)
        else:
            pass

    def opClicked(self):
        mainWindowCalculator.prevlousNum = mainWindowCalculator.currentNum
        mainWindowCalculator.currentNum = 0
        mainWindowCalculator.lcdstring = ''
        mainWindowCalculator.operation = self.sender().objectName() # 将按钮的名称传给操作变量

    def resetClicked(self):
        mainWindowCalculator.prevlousNum = 0
        mainWindowCalculator.currentNum = 0
        mainWindowCalculator.result = 0
        mainWindowCalculator.lcdstring = ''
        mainWindowCalculator.operation = ''
        self.lcd.display(0)

    def eqClicked(self):
        if mainWindowCalculator.operation == 'b_plus':
            mainWindowCalculator.result = mainWindowCalculator.prevlousNum + mainWindowCalculator.currentNum
            self.lcd.display(str(mainWindowCalculator.result))
        elif mainWindowCalculator.operation == 'b_sub':
            mainWindowCalculator.result = mainWindowCalculator.prevlousNum - mainWindowCalculator.currentNum
            self.lcd.display(str(mainWindowCalculator.result))
        elif mainWindowCalculator.operation == 'b_mul':
            mainWindowCalculator.result = mainWindowCalculator.prevlousNum * mainWindowCalculator.currentNum
            self.lcd.display(str(mainWindowCalculator.result))
        elif mainWindowCalculator.operation == 'b_div':
            # 对被除数为0这种情况做一个，一种错误提示
            if mainWindowCalculator.currentNum == 0:
                self.lcd.display('Error')
                mainWindowCalculator.result = 0
                mainWindowCalculator.prevlousNum = 0
            else:
                mainWindowCalculator.result = mainWindowCalculator.prevlousNum / mainWindowCalculator.currentNum
                self.lcd.display(str(mainWindowCalculator.result)[0:8]) # 使用切片是因为当lcd只显示数字最后的8位，小数点后过多时
                                                                        # 显示的数据无意义，故只取前八位。

        mainWindowCalculator.currentNum = mainWindowCalculator.result
        mainWindowCalculator.lcdstring = ''

    def closeEvent(self, event): # 将closeEvent这个事件进行重写，已符合我们的要求
        reply = QtGui.QMessageBox.question(self, u'警告', u'确认退出', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

app = QtGui.QApplication(sys.argv)
calculator = mainWindowCalculator()
calculator.show()
sys.exit(app.exec_())
