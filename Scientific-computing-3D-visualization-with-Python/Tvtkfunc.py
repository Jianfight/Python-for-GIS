

def ivtk_scene(actors, *actors2): # 方便使用ivtk来检查我们进行管线的过程
    from tvtk.tools import ivtk
    # 创建一个带Crust(python shell)的窗口
    win = ivtk.IVTKWithCrustAndBrowser()
    win.open()
    if actors2 != None:
        win.scene.add_actor(actors)
        for i in range(len(actors2)):
            win.scene.add_actor(actors2[i])
    else :
        win.scene.add_actor(actors)

    # 修正错误,显示出来的图形子窗口不在主窗口内
    dialog = win.control.centralWidget().widget(0).widget(0)
    from pyface.qt import QtCore
    dialog.setWindowFlags(QtCore.Qt.WindowFlags(0x00000000))
    dialog.show()
    return win

def event_loop(): # 开始界面消息循环
    from pyface.api import GUI
    gui = GUI()
    gui.start_event_loop()