# 产看TVTK库中相应的类的功能。
# from tvtk.tools import tvtk_doc
# tvtk_doc.main()

from tvtk.api import tvtk
# # 创建立方体
# s = tvtk.CubeSource(x_length=1.0, y_length=2.0, z_length=3.0)
# yuanzhui = tvtk.ConeSource(height=3.0, radius=1.0, resolution=36) # resolution属性表示底面圆的分辨率：用36边形来近似圆
#
# # 显示立方体
# # 使用ploydatamapper将数据转换为图形数据<polydatamapper是一个映射器>
# m = tvtk.PolyDataMapper(input_connection=s.output_port)
# # 创建一个Actor,actor是一个实体，将我们转换后的数据作为参数传递进去
# a = tvtk.Actor(mapper=m)
# # 创建一个Renderer<渲染器>,将Actor添加进去
# r = tvtk.Renderer(background=(0,0,0))
# r.add_actor(a)
# # 创建一个RenderWindow(窗口），将Render添加进去
# w = tvtk.RenderWindow(size=(300,300))
# w.add_renderer(r)
# # 创建一个RenderWindowInteractor(窗口的交互工具)
# i = tvtk.RenderWindowInteractor(render_window=w)
# # 开启交互
# i.initialize()
# i.start()

# # 使用ivtk来观察管线的运行过程
# s = tvtk.CubeSource(x_length=1.0, y_length=2.0, z_length=3.0)
# m = tvtk.PolyDataMapper(input_connection=s.output_port)
# a = tvtk.Actor(mapper=m)
#
# from Tvtkfunc import ivtk_scene, event_loop
#
# win = ivtk_scene(a)
# win.scene.isometric_view()
# event_loop()

# 数据集
from tvtk.api import tvtk

# imagedata数据集
img = tvtk.ImageData(spacing=(1,1,1), origin=(1,2,3), dimensions=(3,4,5))
for i in range(6):
    print(img.get_point(i))
print('---------------------------------------------------------------------------------------------------------------')

#rectilinearGrid数据集
import numpy as np
x = np.array([0,3,9,15])
y = np.array([0,1,5])
z = np.array([0,2,3])
r = tvtk.RectilinearGrid()
r.x_coordinates = x
r.y_coordinates = y
r.z_coordinates = z
r.dimensions = len(x),len(y),len(z)
for i in range(6):
    print(r.get_point(i))






