#-*- coding=utf-8 -*-
# 关于pyQt5的学习记录，知识来源腾讯课堂的python图形界面编程

import sys
from PyQt4 import QtGui, QtCore

# region 简单的图形界面程序

# app = QtGui.QApplication(sys.argv) # sys.argv表示这个程序可以使用命令行的形式实现，app这个对象代表窗口程序，在进行图形化界面编程的时候必须生成一个该对象。
# widget = QtGui.QWidget() # QWidget是所有图形界面的一个父类，所以在编辑图形界面程序时，先生成一个该类的对象。
# widget.resize(350, 250) # 设置窗口的大小，单位为像素。
# widget.setWindowTitle(u'第一个窗口程序') # 为窗口设置一个标题。
# widget.show() # 显示窗口
# sys.exit(app.exec_()) # 该方法将程序的退出，交由我们编写的图形界面程序管理，该方法方便资源的回收。

# endregion

# region 为图形界面配置一个图标
# class Icon(QtGui.QWidget): # 定义一个类，其继承与QtGui.QWidget这个大类。
#     def __init__(self,parent=None): # 定义该类的构造函数，parent=None代表将QWidget设置为mainwindow，而不是QiGui(暂时不太理解)
#         QtGui.QWidget.__init__(self) # 初始化父类的构造函数
#         self.setGeometry(300,300,350,250) # 设置窗口的位置和大小，前两个表示窗口的位置，后两个表示窗口的大小
#         self.setWindowTitle(u'第一个窗口程序')
#         self.setWindowIcon(QtGui.QIcon('111.ico')) # 指定使用的图标的位置。
#
# app = QtGui.QApplication(sys.argv)
# icon = Icon()
# icon.show()
# sys.exit(app.exec_())
# endregion

# region 给鼠标在移动时增加一个小提示。
# class ToolTip(QtGui.QWidget): # 定义一个类，其继承与QtGui.QWidget这个大类。
#     def __init__(self,parent=None): # 定义该类的构造函数，parent=None代表将QWidget设置为mainwindow，而不是QiGui(暂时不太理解)
#         QtGui.QWidget.__init__(self) # 因为是继承与父类，所以在定义完该类的构造函数后紧接着初始化父类的构造函数。
#
#         self.setGeometry(300,300,350,250) # 设置窗口的位置和大小，前两个表示窗口的位置，后两个表示窗口的大小
#         self.setWindowTitle(u'小提示')
#         self.setWindowIcon(QtGui.QIcon('111.ico')) # 指定使用的图标的位置。
#         self.setToolTip('This is a <b>QWidget </b>weidget.') # 该行的作用是使字体加粗,<b>...</b>之间的内容是加粗的对象。
#
#         QtGui.QToolTip.setFont(QtGui.QFont('OldEnglis',10)) # 给提示设置一个字体和字体的大小。
#
# app = QtGui.QApplication(sys.argv)
# tooltip = ToolTip()
# tooltip.show()
# sys.exit(app.exec_())
# endregion

# region 添加一个关闭按钮
# from PyQt4 import QtCore # 因为下面的代码设计到程序的关闭，故在此引入该模块
# class Quitbutton(QtGui.QWidget): # 定义一个类，其继承与QtGui.QWidget这个大类。
#     def __init__(self,parent=None): # 定义该类的构造函数，parent=None代表将QWidget设置为mainwindow，而不是QiGui(暂时不太理解)
#         QtGui.QWidget.__init__(self) # 初始化父类的构造函数
#
#         self.setGeometry(300,300,350,250) # 设置窗口的位置和大小，前两个表示窗口的位置，后两个表示窗口的大小
#         self.setWindowTitle(u'关闭按钮')
#         self.setWindowIcon(QtGui.QIcon('111.ico')) # 指定使用的图标的位置。
#         # 创建一个按钮。
#         quit = QtGui.QPushButton(u'关闭', self)
#         quit.setGeometry(10,10,60,35) # 设置按钮的位置和大小。
#         self.connect(quit, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT('quit()'))
#         # 该句代码是将按钮的单击事件绑定给相应的图形界面程序并为事件触发后的处理设置关联函数。
#         #通过调用QObject对象的connect函数来将某个对象的信号和另外一个对象的槽函数相关联，当发射者发射信号时，接收者的槽函数将被调用。
#         # 信号处理：signal 和 slot 构建出一个信号和槽的关系（信号和槽机制是QT的核心机制。）但控件的事件触发后，对象就会将信号发射出去，
#         # 槽在接受到信号后调用相应的函数。
#
# app = QtGui.QApplication(sys.argv)
# quit = Quitbutton()
# quit.show()
# sys.exit(app.exec_())
# endregion

# region 为窗体添加一个关闭提示类型的消息窗口。
# class MessageBox(QtGui.QWidget):
#     def __init__(self, parent=None):
#         QtGui.QWidget.__init__(self)
#         self.setGeometry(300,300,350,350)
#         self.setWindowTitle(u'消息窗口')
#
#     # 对于定义这个函数后，程序是如何调用的，还不太了解，有待研究。
#     def closeEvent(self, event): # 定义一个消息提示函数,在pyqt中本身就有closeEvent关闭事件对应的函数，如果我们需要更改，就需要重新定义该函数。
#         # 使用question方法，将提示结果返回给变量reply，再通过reply的值进行判断。
#         reply = QtGui.QMessageBox.question(self, u'警告', u'确认退出？', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
#
#         if reply == QtGui.QMessageBox.Yes:
#             event.accept()
#         else:
#             event.ignore()
#
# app = QtGui.QApplication(sys.argv)
# ms = MessageBox()
# ms.show()
# sys.exit(app.exec_())
# endregion

# region 将显示的图形界面放置到屏幕的中央
# class MessageBoxAndCenter(QtGui.QWidget):
#     def __init__(self, parent=None):
#         QtGui.QWidget.__init__(self)
#         self.resize(550, 450)
#         self.setWindowTitle(u'居中')
#         self.center()
#
#     def center(self):
#             screen = QtGui.QDesktopWidget().screenGeometry()
#             size = self.geometry()
#             self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
#
#
#     # 重写QWidget类中的该方法，对于定义这个函数后，程序是如何调用的，还不太了解，有待研究。
#     def closeEvent(self, event): # 定义一个消息提示函数,在pyqt中本身就有closeEvent关闭事件对应的函数，如果我们需要更改，就需要重新定义该函数。
#         # 使用question方法，将提示结果返回给变量reply，再通过reply的值进行判断。
#         reply = QtGui.QMessageBox.question(self, u'警告', u'确认退出？', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
#
#         if reply == QtGui.QMessageBox.Yes:
#             event.accept()
#         else:
#             event.ignore()
#
# app = QtGui.QApplication(sys.argv)
# ms = MessageBoxAndCenter()
# ms.show()
# sys.exit(app.exec_())
# endregion

# region 在窗体中添加菜单栏和工具栏(在继承类的时候继承的是QMainWindow而非QWidget)
# class MainWindow(QtGui.QMainWindow):
#     def __init__ (self, parent=None):
#         QtGui.QMainWindow.__init__(self)
#
#         self.resize(550, 450)
#         self.setWindowTitle(u'我的主程序')
#         self.setWindowIcon(QtGui.QIcon('111.ico'))  # 指定使用的图标的位置。
#
#         exit = QtGui.QAction(QtGui.QIcon('exit.png'), u'退出', self) # 引入ACTION可以减轻界面构建的难度，一个action对象可以
#                                                                     # 拥有菜单、文本、图标、快捷方式、状态信息等。
#         exit.setShortcut('Ctrl+Q') # 创建一个快捷键
#         exit.setStatusTip(u'退出程序') # 当将鼠标放置在退出选项时，设置状态栏的提示信息
#
#         # 构建信号和槽机制
#         exit.connect(exit, QtCore.SIGNAL('triggered()'), QtGui.qApp, QtCore.SLOT('quit()'))
#
#         self.statusBar() # 调用该函数将状态栏的提示信息显示出来
#
#         # 设置一个菜单栏
#         menubar = self.menuBar()
#         file = menubar.addMenu(u'文件') # 在菜单栏中添加一个名称为文件的项
#         # file.addAction(exit) # 在文件这个项下方添加退出子项。
#
#         # 设置一个工具栏
#         toolbar = self.addToolBar(u'退出')
#         toolbar.addAction(exit)
#
#         # 添加一个文本编辑器
#         textEdit = QtGui.QTextEdit()
#         self.setCentralWidget(textEdit)
#
# app = QtGui.QApplication(sys.argv)
# main = MainWindow()
# main.show()
# sys.exit(app.exec_())
# endregion(在继承类的时候继承的是QMainWindow而非QWidget)

# region BOX布局
# class Boxlayout(QtGui.QWidget):
#
#     def __init__ (self, parent=None):
#         QtGui.QWidget.__init__(self)
#
#         self.setWindowTitle(u'Box布局')
#
#         # 定义两个按钮
#         ok = QtGui.QPushButton(u'确定')
#         cancel = QtGui.QPushButton(u'取消')
#
#         # 创建一个水平的布局
#         hbox = QtGui.QHBoxLayout()
#         hbox.addStretch(1) # 默认情况下addStretch(QSpacerItem=0),你有一个layer,里面有三个控件，一个放在最左边，一个放在最右边，
#                             # 最后一个放在layout的1/3处，这就可以通过addStretch去实现。addStretch()代表添加一个伸缩间隔元素。
#         hbox.addWidget(ok)   # 按钮属于小部件
#         hbox.addWidget(cancel) # 添加小部件使用的是addWidget()
#
#         # 创建一个竖直的布局
#         vbox = QtGui.QVBoxLayout()
#         vbox.addStretch(1)
#         vbox.addLayout(hbox) # 将创建的水平布局添加到竖直布局中，添加布局使用的是addLayout()
#
#         self.setLayout(vbox) # 为整个窗体设置一个垂直布局
#
#         self.resize(400,250)
#
# app = QtGui.QApplication(sys.argv)
# b = Boxlayout()
# b.show()
# sys.exit(app.exec_())
# endregion

# region 网格布局
# class Grildlayout(QtGui.QWidget):
#
#     def __init__(self,parent=None):
#         QtGui.QWidget.__init__(self)
#
#         self.setWindowTitle(u'网格布局')
#
#         names = [u'清除', u'后退', u'', u'关闭', '7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0','.', '=','+' ]
#
#         grid = QtGui.QGridLayout()
#         j = 0
#         pos = [(0,0), (0,1), (0,2), (0,3),
#                (1,0), (1,1), (1,2), (1,3),
#                (2,0), (2,1), (2,2), (2,3),
#                (3,0), (3,1), (3,2), (3,3),
#                (4,0), (4,1), (4,2), (4,3)]
#         for i in names:
#             button = QtGui.QPushButton(i)
#             if j ==2 :
#                 grid.addWidget(QtGui.QLabel(u''), pos[j][0], pos[j][1]) # 在格网布局中添加控件是时，参数第一个代表要添加的控件类型，
#                                                                         # 第二个代表X坐标,第三个代表Y坐标。
#             else:
#                 grid.addWidget(button,pos[j][0], pos[j][1])
#             j += 1
#
#         self.setLayout(grid)
#
# app = QtGui.QApplication(sys.argv)
# g = Grildlayout()
# g.show()
# sys.exit(app.exec_())
# endregion

# region 滑动块测试
# class SigSlot(QtGui.QWidget):
#     def __init__(self, parent=None):
#         QtGui.QWidget.__init__(self)
#
#         self.setWindowTitle(u'滑动块测试')
#         lcd = QtGui.QLCDNumber(self) # 该控件用来显示数字
#         slider = QtGui.QSlider(QtCore.Qt.Horizontal,self) # 添加一个滑动块
#
#         # 添加一个垂直布局
#         vbox = QtGui.QVBoxLayout()
#         vbox.addWidget(lcd)
#         vbox.addWidget(slider)
#
#         self.setLayout(vbox)
#         self.connect(slider, QtCore.SIGNAL('valueChanged(int)'), lcd, QtCore.SLOT('display(int)'))
#
#         self.resize(550, 450)
#
# app = QtGui.QApplication(sys.argv)
# s = SigSlot()
# s.show()
# sys.exit(app.exec_())
# endregion

# region 使用esc键来退出程序
# class Esc(QtGui.QWidget):
#     def __init__(self, parent=None):
#         QtGui.QWidget.__init__(self)
#
#         self.setWindowTitle(u'Esc键退出测试')
#         # self.connect(self,QtCore.SIGNAL('closeEmiApp()'), QtCore.SLOT('close()'))
#         self.resize(550, 450)
#
#     def keyPressEvent(self, event):
#         if event.key() == QtCore.Qt.Key_Escape:
#             self.close()
#
# app = QtGui.QApplication(sys.argv)
# s = Esc()
# s.show()
# sys.exit(app.exec_())
# endregion

# region 设置鼠标单击时发送一个信号(emit())同信号槽函数connect()完成信号与槽的匹配。
# class Rmit(QtGui.QWidget):
#     def __init__(self, parent=None):
#         QtGui.QWidget.__init__(self)
#
#         self.setWindowTitle(u'鼠标退出测试')
#         self.connect(self,QtCore.SIGNAL('closeEmiApp()'), QtCore.SLOT('close()'))
#         self.resize(550, 450)
#
#     def mousePressEvent(self, event):
#         self.emit(QtCore.SIGNAL('closeEmiApp()')) # emit()代表发出，我们设定鼠标单击时发送一个closeEmiApp信号，配合connect()函数完成
#                                                   # 信号与槽的匹配。
# app = QtGui.QApplication(sys.argv)
# s = Rmit()
# s.show()
# sys.exit(app.exec_())
# endregion

# region 对话框，进行简单交互
# class InputDialog(QtGui.QWidget):
#     def __init__(self, parent=None):
#         QtGui.QWidget.__init__(self)
#
#         self.setGeometry(300, 300, 350, 80) # 设置了窗体的位置和大小
#         self.setWindowTitle(u'输入对话框')
#         self.button = QtGui.QPushButton(u'对话', self) # 在窗体中添加一个按钮
#         self.button.setFocusPolicy(QtCore.Qt.NoFocus) # 取消按钮上的焦点
#         self.button.move(20,20)
#         self.connect(self.button, QtCore.SIGNAL('clicked()'), self.showDialog)
#         self.setFocus()
#         self.label = QtGui.QLineEdit(self)
#         self.label.move(130, 20)
#
#     def showDialog(self):
#         # text变量是返回输入的内容，button变量是返回我们在对话框中按下的是确定键还是取消键，该方法是打开输入框
#         text, button = QtGui.QInputDialog.getText(self, u'输入对话框', u'输入姓名')
#
#         if button:
#             self.label.setText(text)
#         else:
#             self.label.setText(u'对话框已被取消')
#
# app = QtGui.QApplication(sys.argv)
# i = InputDialog()
# i.show()
# sys.exit(app.exec_())
# endregion

# region 打开文件(在继承类的时候继承的是QMainWindow而非QWidget)
# class OpenFile(QtGui.QMainWindow):
#     def __init__(self, parent=None):
#         QtGui.QMainWindow.__init__(self)
#
#         self.setWindowTitle(u'打开文件')
#         self.setGeometry(300, 300, 350, 300)
#         self.setWindowIcon(QtGui.QIcon('111.ico'))  # 指定使用的图标的位置。
#         self.textEdit = QtGui.QTextEdit() # 添加一个文本编辑器
#         self.setCentralWidget(self.textEdit)
#         self.statusBar() # 添加一个状态栏
#         self.setFocus() # 设置焦点
#
#         open = QtGui.QAction(QtGui.QIcon('open.png'), u'打开', self)
#         open.setShortcut('Ctrl+o')
#         open.setStatusTip('打开文件')
#
#         self.connect(open, QtCore.SIGNAL('triggered()'), self.showFileDialog)
#
#         menubar = self.menuBar()
#         file = menubar.addMenu('文件')
#         file.addAction(open)
#
#     def showFileDialog(self):
#         filename = QtGui.QFileDialog.getOpenFileName(self, u'打开文件', './') # 打开文件框
#         file = open(filename)
#         data = file.read()
#         self.textEdit.setText(data)
#
# app = QtGui.QApplication(sys.argv)
# qb = OpenFile()
# qb.show()
# sys.exit(app.exec_())
# endregion

# region 复选框
# class CheckBox(QtGui.QWidget):
#     def __init__(self, parent=None):
#         QtGui.QWidget.__init__(self)
#
#         self.setGeometry(300, 300, 350, 250)
#         self.setWindowTitle(u'复选框')
#         self.cb = QtGui.QCheckBox(u'come baby!',self)
#         self.cb.setFocusPolicy(QtCore.Qt.NoFocus)
#         self.cb.move(10,10)
#
#         self.connect(self.cb, QtCore.SIGNAL('stateChanged(int)'), self.changeTitle)
#
#     def changeTitle(self):
#         if self.cb.isChecked():
#             self.setWindowTitle(u'Hellow World!')
#         else:
#             self.setWindowTitle(u'Come!!!!!')
#
# app = QtGui.QApplication(sys.argv)
# cb = CheckBox()
# cb.show()
# sys.exit(app.exec_())
# endregion

# region 更改颜色
# class ToggleButton(QtGui.QWidget):
#     def __init__(self,parent=None):
#         QtGui.QWidget.__init__(self)
#
#         self.setGeometry(300, 300, 280, 170)
#         self.setWindowTitle(u'改变颜色')
#
#         self.color = QtGui.QColor(0,0,0)
#
#         self.red = QtGui.QPushButton(u'红色', self)
#         self.red.setCheckable(True)  # 确保当按钮被按下时，按钮本身产生被按下的状态
#         self.red.move(10, 10)
#         self.connect(self.red, QtCore.SIGNAL('clicked()'), self.setRed)
#
#         self.green = QtGui.QPushButton(u'绿色', self)
#         self.green.setCheckable(True)
#         self.green.move(10, 60)
#         self.connect(self.green, QtCore.SIGNAL('clicked()'), self.setGreen)
#
#         self.blue = QtGui.QPushButton(u'蓝色', self)
#         self.blue.setCheckable(True)
#         self.blue.move(10, 110)
#         self.connect(self.blue, QtCore.SIGNAL('clicked()'), self.setBlue)
#
#         self.square = QtGui.QWidget(self)
#         self.square.setGeometry(150, 20, 100, 100)
#         self.square.setStyleSheet('QWidget {background-color:%s}' %self.color.name()) # self.color.name()返回的是颜色对应的
#                                                                                       # RGB值的十六进制数。
#
#         QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('cleanlooks'))
#
#     def setRed(self):
#         if self.red.isChecked():
#             self.color.setRed(255)
#         else:
#             self.color.setRed(0)
#
#         self.square.setStyleSheet('QWidget {background-color:%s}' % self.color.name())
#
#     def setGreen(self):
#         if self.green.isChecked():
#             self.color.setGreen(255)
#         else:
#             self.color.setGreen(0)
#
#         self.square.setStyleSheet('QWidget {background-color:%s}' % self.color.name())
#
#     def setBlue(self):
#         if self.blue.isChecked():
#             self.color.setBlue(255)
#         else:
#             self.color.setBlue(0)
#
#         self.square.setStyleSheet('QWidget {background-color:%s}' % self.color.name())
#
# app = QtGui.QApplication(sys.argv)
# tb = ToggleButton()
# tb.show()
# sys.exit(app.exec_())
# endregion

# region 根据滑动块来更改显示的图片
# class Car(QtGui.QWidget):
#     def __init__(self, parent=None):
#         QtGui.QWidget.__init__(self)
#
#         self.setGeometry(200, 200, 1000, 400)
#         self.setWindowTitle(u'GO! GO! GO!')
#         self.slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
#         self.slider.setFocusPolicy(QtCore.Qt.NoFocus)
#         self.slider.setGeometry(30, 40, 100, 60)
#         self.connect(self.slider, QtCore.SIGNAL('valueChanged(int)'), self.changeValue)
#         self.label = QtGui.QLabel(self)
#         self.label.setPixmap(QtGui.QPixmap('car01.png'))
#         self.label.setGeometry(160, 40, 800, 400)
#
#     def changeValue(self):
#         pos = self.slider.value()
#         if pos ==0:
#             self.label.setPixmap(QtGui.QPixmap('car01.png'))
#         elif 0< pos <= 30:
#             self.label.setPixmap(QtGui.QPixmap('car02.png'))
#         elif 30 < pos <= 80:
#             self.label.setPixmap(QtGui.QPixmap('car03.png'))
#         elif pos > 80:
#             self.label.setPixmap(QtGui.QPixmap('car04.png'))
#
# app = QtGui.QApplication(sys.argv)
# c = Car()
# c.show()
# sys.exit(app.exec_())
# endregion

# region 调色盘
# class color(QtGui.QWidget):
#     def __init__(self, parent=None):
#         QtGui.QWidget.__init__(self)
#
#         color = QtGui.QColor(255,255,255)
#         self.setGeometry(300,300,255,255)
#         self.setWindowTitle(u'调色盘')
#
#         self.button = QtGui.QPushButton(u'选择颜色',self)
#         self.button.setFocusPolicy(QtCore.Qt.NoFocus)
#         self.button.move(20,20)
#
#         self.connect(self.button, QtCore.SIGNAL('clicked()'), self.showDialog)
#         self.setFocus()
#
#         self.widget = QtGui.QWidget(self)
#         self.widget.setStyleSheet('QWidget{background-color:%s}'%color.name())
#         self.widget.setGeometry(130,22,100,100)
#
#     def showDialog(self):
#         col = QtGui.QColorDialog.getColor() # 打开调色盘对话框
#         if col.isValid():
#             self.widget.setStyleSheet('QWidget{background-color:%s}'%col.name()) # col.name()返回的是所选中颜色的十六位RGB码
#
# app = QtGui.QApplication(sys.argv)
# color = color()
# color.show()
# sys.exit(app.exec_())
# endregion

# region 字体选择
# class Font(QtGui.QWidget):
#     def __init__(self, parent=None):
#         QtGui.QWidget.__init__(self)
#
#         self.setGeometry(300,300,250,110)
#         self.setWindowTitle(u'字体对话框')
#         self.button = QtGui.QPushButton(u'选择字体', self)
#         self.button.setFocusPolicy(QtCore.Qt.NoFocus)
#         self.button.move(20,20)
#
#         hbox = QtGui.QHBoxLayout() # 水平布局
#         hbox.addWidget(self.button)
#
#         self.connect(self.button, QtCore.SIGNAL('clicked()'), self.showFontDialog)
#         self.label = QtGui.QLabel(u'问君能有几多愁，恰似一江春水向东流！', self)
#         self.label.move(130, 20)
#         hbox.addWidget(self.label, 1) # 参数1表示标签的大小是可以进行变化的
#         self.setLayout(hbox)
#
#     def showFontDialog(self):
#         font, button = QtGui.QFontDialog.getFont() # 打开选择字体对话框
#         if button:
#             self.label.setFont(font) # 根据选择字体对话框中的选择设定标签的字体
#
# app = QtGui.QApplication(sys.argv)
# font = Font()
# font.show()
# sys.exit(app.exec_())
# endregion

# region 进度条
# class ProgressBar(QtGui.QWidget):
#     def __init__(self, parent=None):
#         QtGui.QWidget.__init__(self)
#
#         self.setGeometry(300,300,250,150)
#         self.setWindowTitle(u'进度条')
#
#         self.pbar = QtGui.QProgressBar(self) # 创建一个进度条
#         self.pbar.setGeometry(30,40,200,25)
#
#         self.button = QtGui.QPushButton(u'开始', self)
#         self.button.setFocusPolicy(QtCore.Qt.NoFocus)
#         self.button.move(40,80)
#
#         self.connect(self.button, QtCore.SIGNAL('clicked()'), self.onStart)
#
#         self.timer = QtCore.QBasicTimer() # 创建一个定时器
#
#         self.step = 0
#
#     def onStart(self):
#         if self.timer.isActive():
#             self.timer.stop()
#             self.button.setText(u'开始')
#         else:
#             self.timer.start(100, self) # 参数100表示是最大值，当计时器超过最大值时将会产生一个事件，参数self表示这个事件将会被self本体接收
#             self.button.setText(u'停止')
#
#     def timerEvent(self, event): # 该函数为定时器超时后会激发的事件，我们重新将其进行定义。
#         if self.step >= 100:
#             self.timer.stop()
#             self.button.setText(u'重新开始')
#             self.step = 0
#             return
#         self.step += 1
#         self.pbar.setValue(self.step)
#
# app = QtGui.QApplication(sys.argv)
# text = ProgressBar()
# text.show()
# sys.exit(app.exec_())
# endregion

# region 添加日期选择框
# class Calendar(QtGui.QWidget):
#     def __init__(self, parent=None):
#         QtGui.QWidget.__init__(self)
#
#         self.setGeometry(300, 300, 350, 300)
#         self.setWindowTitle(u'日期选择')
#         self.cal = QtGui.QCalendarWidget(self)
#         self.cal.setGridVisible(True)  # 将日期设置为表格装显示
#
#         self.connect(self.cal, QtCore.SIGNAL('selectionChanged()'), self.showDate)
#
#         self.label = QtGui.QLabel()
#         date = self.cal.selectedDate() # 建立一个日期的对象，方便显示
#         self.label.setText(str(date.toPyDate())) # 将pyqt4中的日期转换为常见的日期格式，toPyDate()会将数据转换为datetime.date形式
#                                                     # 并非是文本的格式，所以需要再使用str()对其进行强制转换。
#
#         vbox = QtGui.QVBoxLayout()
#         vbox.addWidget(self.label)
#         vbox.addWidget(self.cal)
#         self.setLayout(vbox)
#
#     def showDate(self):
#         date = self.cal.selectedDate()
#         self.label.setText(str(date)) # 并不对日期格式进行转换，与初始界面的日期格式产生对比
#
# app = QtGui.QApplication(sys.argv)
# text = Calendar()
# text.show()
# sys.exit(app.exec_())
# endregion





