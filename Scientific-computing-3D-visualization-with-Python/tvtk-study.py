from tvtk.api import tvtk
from Tvtkfunc import ivtk_scene, event_loop
from tvtk.common import configure_input

# region 产看TVTK库中相应的类的功能。
#
# from tvtk.tools import tvtk_doc
# tvtk_doc.main()
# endregion

# region 立方体的创建与显示
# 创建立方体
# s = tvtk.CubeSource(x_length=1.0, y_length=2.0, z_length=3.0)
# yuanzhui = tvtk.ConeSource(height=6.0, radius=2.0, resolution=36) # resolution属性表示底面圆的分辨率：用36边形来近似圆
#
# # 显示立方体
# # 使用ploydatamapper将数据转换为图形数据<polydatamapper是一个映射器>
# m = tvtk.PolyDataMapper(input_connection=yuanzhui.output_port)
# # 创建一个Actor,actor是一个实体，将我们转换后的数据作为参数传递进去
# a = tvtk.Actor(mapper=m)
# # 创建一个Renderer<渲染器>,将Actor添加进去
# r = tvtk.Renderer(background=(1,0,0))
# r.add_actor(a)
# # 创建一个RenderWindow(窗口），将Render添加进去
# w = tvtk.RenderWindow(size=(300,300))
# w.add_renderer(r)
# # 创建一个RenderWindowInteractor(窗口的交互工具)
# i = tvtk.RenderWindowInteractor(render_window=w)
# # 开启交互
# i.initialize()
# i.start()
# endregion

# region 使用ivtk来观察管线的运行过程
# 使用ivtk来观察管线的运行过程
# s = tvtk.CubeSource(x_length=1.0, y_length=2.0, z_length=3.0)
# m = tvtk.PolyDataMapper(input_connection=s.output_port)
# a = tvtk.Actor(mapper=m)
#
# from Tvtkfunc import ivtk_scene, event_loop
#
# win = ivtk_scene(a)
# win.scene.isometric_view()
# event_loop()
# endregion

# region 数据集
# 数据集
# from tvtk.api import tvtk
#
# # imagedata数据集
# img = tvtk.ImageData(spacing=(1,1,1), origin=(1,2,3), dimensions=(3,4,5))
# for i in range(6):
#     print(img.get_point(i))
# print('---------------------------------------------------------------------------------------------------------------')
#
# #rectilinearGrid数据集
# import numpy as np
# x = np.array([0,3,9,15])
# y = np.array([0,1,5])
# z = np.array([0,2,3])
# r = tvtk.RectilinearGrid()
# r.x_coordinates = x
# r.y_coordinates = y
# r.z_coordinates = z
# r.dimensions = len(x),len(y),len(z)
# for i in range(6):
#     print(r.get_point(i))
# endregion

# region 数据加载
# 数据加载
# STL格式数据的读取
# s = tvtk.STLReader(file_name = "python.stl")
# m = tvtk.PolyDataMapper(input_connection = s.output_port)
# a = tvtk.Actor(mapper=m)
#
# win = ivtk_scene(a)
# win.scene.isometric_view()
# event_loop()

# obj格式数据的读取
# obj = tvtk.OBJReader(file_name="example.obj")
# obj_m = tvtk.PolyDataMapper(input_connection = obj.output_port)
# obj_actor = tvtk.Actor(mapper=obj_m)
# # 窗口绘制
# win = ivtk_scene(obj_actor)
# win.scene.isometric_view()
# event_loop()

# Plot3D格式数据的读取
# def read_data_plot3d(xyz_file_name, q_file_name): # 读入plot3D格式的数据
#     plot3d = tvtk.MultiBlockPLOT3DReader(
#         xyz_file_name=xyz_file_name,  # 网格数据
#         q_file_name=q_file_name,  # 空气动力学结果文件
#         scalar_function_number=100,  # 设置标量数据数量
#         vector_function_number=200  # 设置矢量数据数量
#     )
#     plot3d.update() # update方法，真正的从文件中读取数据
#     return plot3d
#
# plot3d = read_data_plot3d("combxyz.bin", "combq.bin")
# grid = plot3d.output.get_block(0) # 获取网格数据集
# print(grid.dimensions)
# print(grid.points.to_array())
# print(grid.cell_data.number_of_arrays)
# print(grid.point_data.number_of_arrays)
# print(grid.point_data.scalars.name) # 返回标量数组的名称
# print(grid.point_data.vectors.name) # 返回矢量数组的名称
# endregion

# region 数据读取
# def read_data_plot3d(xyz_file_name, q_file_name): # 读入plot3D格式的数据
#     plot3d = tvtk.MultiBlockPLOT3DReader(
#         xyz_file_name=xyz_file_name,  # 网格数据
#         q_file_name=q_file_name,  # 空气动力学结果文件
#         scalar_function_number=100,  # 设置标量数据数量
#         vector_function_number=200  # 设置矢量数据数量
#     )
#     plot3d.update() # update方法，真正的从文件中读取数据
#     return plot3d
#
# plot3d = read_data_plot3d("combxyz.bin", "combq.bin")
# grid = plot3d.output.get_block(0) # 获取网格数据集
# #
# # 标量数据可视化
# # 设定映射器的变量范围属性
# con = tvtk.ContourFilter() # 创建一个等值面过滤器
# con.set_input_data(grid) # 将网格于其进行绑定
# con.generate_values(10, grid.point_data.scalars.range) # 创建等值面,等值面的取值范围由标量数组决定,等值面的颜色也由标量数组决定，
#                                                     # 由于没有设置映射器的颜色表，系统将使用默认的映射表，既最小值为红色，最大值为蓝色
# # # 设置第一个等值面的值为原来的2倍
# # color_value = con.get_value(0)
# # con.set_value(0, 2*color_value)
#
# m = tvtk.PolyDataMapper(scalar_range=grid.point_data.scalars.range,
#                         input_connection=con.output_port
#                         )
# a2 = tvtk.Actor(mapper=m)
# a2.property.opacity = 0.5 # 由于等值面会产生嵌套，故调整等值面的透明度
# # # 窗口绘制
# # win = ivtk_scene(a2)
# # win.scene.isometric_view()
# # event_loop()
#
# # 矢量数据可视化
# # 对数据集中的数据进行随机选取，每50个点选择一个点
# mask = tvtk.MaskPoints(random_mode=True, on_ratio=50) # 降采样
# mask.set_input_data(grid) # 连接数据
# # 创建表示箭头的PolyData数据集
# glyph_source = tvtk.ArrowSource() # 生成箭头的类,ConeSource()是生成圆锥的类
# # 在Mask采样后的PolyData数据集每个点上放置一个箭头
# # 箭头的方向、长度和颜色由点对应的矢量和标量数据决定(本例中，箭头的方向表示速度的方向，大小和颜色表示密度，箭头越大表示该点的标量值越大，
# # 箭头的颜色表也表示标量的大小，红色小，蓝色大，)
# glyph = tvtk.Glyph3D(input_connection=mask.output_port,  # Glyph3D代表该库的符号化技术
#                      scale_factor=4 # 设置符号的共同放缩系数
#                      )
# glyph.set_source_connection(glyph_source.output_port)     # 在每一个数据上放置一个箭头
# m = tvtk.PolyDataMapper(scalar_range=grid.point_data.scalars.range,
#                         input_connection=glyph.output_port
#                         )
# a1 = tvtk.Actor(mapper=m)
# # # 窗口绘制
# # win = ivtk_scene(a1)
# # win.scene.isometric_view()
# # event_loop()
#
# # 轮廓数据可视化
# outline = tvtk.StructuredGridOutlineFilter() # 计算表示外边框的PolyData对象
# configure_input(outline, grid) # 将外框计算对象与数据集产生关联
# m = tvtk.PolyDataMapper(input_connection=outline.output_port)
# a = tvtk.Actor(mapper=m)
# a.property.color = 0.3, 0.3, 0.3
# # 窗口绘制
# # win = ivtk_scene(a)
# win = ivtk_scene(a, a1, a2) # 将三种实体加载到同一个屏幕中显示
# win.scene.isometric_view()
# event_loop()
# endregion





