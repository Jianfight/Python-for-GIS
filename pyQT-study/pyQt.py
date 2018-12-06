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

# region 在窗体中添加菜单栏和工具栏
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
# endregion

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














