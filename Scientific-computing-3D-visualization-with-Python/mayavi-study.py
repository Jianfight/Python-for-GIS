from mayavi import mlab
import numpy as np

# region 简单尝试
# 简单尝试
# x = [[-1,1,1,-1,-1], [-1,1,1,-1,-1]]
# y = [[-1,-1,-1,-1,-1], [1,1,1,1,1]]
# z = [[1,1,-1,-1,1], [1,1,-1,-1,1]]
# mesh = mlab.mesh(x,y,z,representation='wireframe')
# mlab.show()

# 建立数据
# dphi, dtheta = np.pi/250.0, np.pi/250.0
# [phi, theta] = np.mgrid[0:np.pi+dphi*1.5:dphi, 0:2*np.pi+dphi*1.5:dtheta]
# m0 = 4; m1 = 3; m2 = 2; m3 = 3; m4 = 6; m5 = 2; m6 = 6; m7 = 4;
# r = np.sin(m0*phi)**m1 + np.cos(m2*phi)**m3 + np.sin(m4*theta)**m5 + np.cos(m6*theta)**m7
# x = r*np.sin(phi)*np.cos(theta)
# y = r*np.cos(phi)
# z = r*np.sin(phi)*np.sin(theta)
# # 对该数据进行三维可视化
# s = mlab.mesh(x,y,z,representation='points') # representation参数可以设置模型的表现形式:表面（surface）
#                                                                 # 线框（wireframe）、点云（points）
# mlab.show()
# endregion

# region 使用mayavi对numpy数组进行可视化
# 使用mayavi对numpy数组进行可视化
# points3D绘图函数
# 建立数组
# t = np.linspace(0,4*np.pi,20) # numpy中的linspace将创建一个等差数列的一维数组，建立的数组元素的数据格式是浮点型，常见的三个参数分别代表起始值
#                               # 终止值（默认包含自身）、数列中元素的个数
# x = np.sin(2*t)
# y = np.cos(t)
# z = np.cos(2*t)
# s = 2 + np.sin(t)
# # 对数据进行可视化
# points = mlab.points3d(x, y, z, s, colormap='Blues', scale_factor=0.25)
# mlab.show() # 该函数表示与图形进行交互，在默认情况下该函数建立了简单的GUI并开始事件循环，该函数中有一个默认参数stop=False用来定义事件循环是否结束

# plot3D绘图函数
# 建立数据
# n_mer, n_long = 6, 11
# dphi = np.pi /1000.0
# phi = np.arange(0.0, 2*np.pi + 0.5*dphi, dphi) # 用与创建等差数组：start<起始值，可忽略不写，默认从0开始>，stop<结束值，生成的元素不包括结束值>
#                                                # step<步长，可忽略不写，默认步长为1>，dtype<默认为None，设置显示元素的数据类型>
# mu = phi * n_mer
# x = np.cos(mu) * (1 + np.cos(n_long * mu / n_mer) *0.5)
# y = np.sin(mu) * (1 + np.cos(n_long * mu / n_mer) *0.5)
# z = np.sin(n_long * mu / n_mer) * 0.5
#
# # 对数据进行可视化
# l = mlab.plot3d(x, y, z, np.sin(mu), tube_radius=0.025, colormap='Spectral')
# mlab.show()

# imshow绘图函数
# 建立数据
# s = np.random.random((10,10))
#
# # 对数据进行可视化
# img = mlab.imshow(s,colormap='gist_earth') # gist_earth将显示一个地球表面色彩为颜色的颜色映射关系
# mlab.show()

# surf绘图函数
# def f(x,y):
#     return np.sin(x-y)+np.cos(x+y)
#
# x, y = np.mgrid[-7.:7.05:0.1,-5.:5.05:0.05] # numpy中的mgrid[a:b:c]如果c为实数表示间隔，表示从a开始以c为间隔等间距划分到b
#                                     # 的一维行数组，如果等分时不管能不能取到b，最后一项都取在a-b以内最接近b的，而且对于a,b来说左闭右开。
#                                     # 如果c为虚数<nj>，则n表示个数，将a-b等间距分为相应个数的一维行数组。对于a,b来说左闭右闭。
#
#                                     # 当mgrid[a:b:c,d:e:f]表示生成两个二维矩阵，其中c,f的用法与一维时一样，两个矩阵的行数与c定义
#                                     # 的在a,b中分割出的个数相同，列数与f定义的在d,e中分割出的个数相同，
#                                     # 第一个矩阵是依照a-b向下等分排列，形式如下：
#                                     #[a,a,......,a,a]
#                                     #[..............]
#                                     #[b,b,......,b,b]
#                                     # 第二个矩阵是依照d-e向右等分排列，形式如下：
#                                     #[d,..........,e]
#                                     #[..............]
#                                     #[d,..........,e]
# print(x)
# print('---------------------------')
# print(y)
# s = mlab.surf(x, y, f)
# mlab.show()

# contour3d绘图函数
# x, y, z = np.ogrid[-5:5:64j, -5:5:64j, -5:5:64j]
# scalars = x*x + y*y + z*z
# print(x)
# print('---------------------------')
# print(y)
# print('---------------------------')
# print(z)
# print('---------------------------')
# print(scalars)
# obj = mlab.contour3d(scalars, contours=8, transparent=True) # contours=8等值面的数量设置为8，transparent=True表示该对象可以透明表示
# mlab.show()

# quiver3d绘图函数
# x,y,z = np.mgrid[-2:3, -2:3, -2:3]
# r = np.sqrt(x**2 + y**2 + z**4)
# u = y * np.sin(r)/(r + 0.001)
# v = -x * np.sin(r)/(r + 0.001)
# w = np.zeros_like(z)
#
# obj = mlab.quiver3d(x,y,z,u,v,w,line_width=3,scale_factor=1)
# mlab.show()
# endregion

# region 改变颜色
# 改变颜色

# 建立数据
# x, y = np.mgrid[-10:10:200j, -10:10:200j]
# z = 100 * np.sin(x * y)/(x * y)
# # 对数据进行可视化
# mlab.figure(bgcolor=(1,1,1)) # figure图表的意思，将改图表背景色设置为白色
# surf = mlab.surf(z, colormap='cool') # coolb表示使用冷色系
#
# lut = surf.module_manager.scalar_lut_manager.lut.table.to_array() # 通过更改lut的颜色映射模式，来修改显示情况，lut是一个255x4的数组
#                                                                 # 其中列向量分别表示R,G,B,A(A是alpha表示透明度)
# lut[:, -1] = np.linspace(0, 256, 256) # 修改lut的最后一列，既alpha通道
# surf.module_manager.scalar_lut_manager.lut.table = lut # 将变化后的lut重新赋值给设置
#
# # 更新视图并显示
# mlab.show()
# endregion

# region 鼠标选取交互操作
# # 鼠标选取交互操作
# # 选取红色小球问题分析
#
# ######场景初始化######
# figure = mlab.gcf()
# # 添加该语句是为了增加小球的绘制速度，在构建小球时，不允许绘制器绘制小球
# figure.scene.disable_render = True
#
# # 用mlab.points3d建立红色和白色小球的集合
# x1, y1, z1 = np.random.random((3, 10))
# red_glyphs = mlab.points3d(x1, y1, z1, color=(1,0,0), resolution=10) # resolution可以理解为小球的分辨率
#
# x2, y2, z2 = np.random.random((3, 10))
# white_glyphs = mlab.points3d(x2, y2, z2, color=(0.9,0.9,0.9), resolution=10)
#
# # 当所有小球构建完成后，再统一绘制,这是一种在有多个模型时，为了加快显示速度而使用的方法。
# figure.scene.disable_render = False
#
#
# # 绘制选取框，并放在第一个小球上
# outline = mlab.outline(line_width=3)
# outline.outline_mode = 'cornered'
# outline.bounds = (x1[0] - 0.1, x1[0] + 0.1,
#                   y1[0] - 0.1, y1[0] + 0.1,
#                   z1[0] - 0.1, z1[0] + 0.1,
#                   )
# # 获取小球的顶点坐标列表
# glyph_points = red_glyphs.glyph.glyph_source.glyph_source.output.points.to_array()
# # 当选取事件发生时，调用此函数
# def picker_callback(picker):
#     if picker.actor in red_glyphs.actor.actors:
#         # print('11111')
#         # 计算那个小球被选取
#         # 计算被选取的小球的ID号
#         point_id = int(picker.point_id / glyph_points.shape[0]) # shape[0]会返回该小球有多少个顶点,int函数会向下取整
#         # 如果没有小球被选取，则point_id = -1
#         if point_id != -1:
#             # 计算与此红色小球相关的坐标
#             x , y, z = x1[point_id], y1[point_id], z1[point_id]
#             # 将外框移到小球上
#             outline.bounds = (
#                 x - 0.1, x + 0.1,
#                 y - 0.1, y + 0.1,
#                 z - 0.1, z + 0.1,
#             )
#
# picker = figure.on_mouse_pick(picker_callback)
# # 为了提高选取小球时的精度，设置tolerance参数，提高选取精度
# picker.tolerance = 0.01
#
# mlab.title('Click on red balls.')
# mlab.show()
# endregion

# region 标量数据的可视化
# # 标量数据的可视化
# # 生成标量数据
# x, y, z = np.ogrid[-10:10:20j, -10:10:20j, -10:10:20j]
# s = np.sin(x*y*z)/(x*y*z)
# print(s)
#
# # # 等值面的绘制
# # # mlab.contour3d(s)
# #
# # # 切平面的绘制
# # # 绘制x轴的切平面
# # mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(s),
# #                                  plane_orientation='x_axes',
# #                                  slice_index=10,
# #                                  )
# # # 绘制y轴的切平面
# # mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(s),
# #                                  plane_orientation='y_axes',
# #                                  slice_index=10,
# #                                  )
# # # 绘制模型的外轮廓线
# # mlab.outline()
#
# # 复合观测方法
# # 将数据转换为标量场数据
# src = mlab.pipeline.scalar_field(s)
#
# mlab.pipeline.iso_surface(src, contours=[s.min()+0.1*s.ptp(), ], opacity=0.3)
# # mlab.pipeline.iso_surface(src, contours=[s.min()+0.1*s.ptp(), ])
# mlab.pipeline.image_plane_widget(src,
#                                  plane_orientation='z_axes',
#                                  slice_index=10,
#                                  )
# mlab.show()
# endregion

# region 矢量数据的可视化
# # 矢量数据的可视化
# # 创建数据
# x, y, z = np.mgrid[0:1:20j, 0:1:20j, 0:1:20j]
# u = np.sin(np.pi*x) * np.cos(np.pi*z)
# v = -2*np.sin(np.pi*y) * np.cos(2*np.pi*z)
# w = np.cos(np.pi*x)*np.sin(np.pi*z) + np.cos(np.pi*y)*np.sin(2*np.pi*z)
#
# # 绘制图形
# # mlab.quiver3d(u,v,w)
#
# # 使用masking进行数据的抽稀后可视化
# # src = mlab.pipeline.vector_field(u, v, w)
# # mlab.pipeline.vectors(src, mask_points=10, scale_factor=2.0)
#
# # Cut Plane切面可视化
# # src = mlab.pipeline.vector_field(u, v, w)
# # mlab.pipeline.vector_cut_plane(src, mask_points=10, scale_factor=2.0)
#
# # 级数的等值面可视化
# # src = mlab.pipeline.vector_field(u,v,w)
# # magnitude = mlab.pipeline.extract_vector_norm(src)
# # mlab.pipeline.iso_surface(magnitude, contours=[2.0, 0.5])
#
# # 流线（Flow）的可视化,在某些时候他可以表示流体力学的轨迹或者电磁场线。
# # flow = mlab.flow(u,v,w, seed_scale=1,
# #                  seed_resolution=5,
# #                  integration_direction='both'
# #                  )
#
# # 复合观测
# src = mlab.pipeline.vector_field(u,v,w)
# magnitude = mlab.pipeline.extract_vector_norm(src)
# iso = mlab.pipeline.iso_surface(magnitude, contours=[2.0,], opacity=0.3)
# vec = mlab.pipeline.vectors(magnitude, mask_points=40,
#                             line_width=1,
#                             color=(0.8,0.8,0.8),
#                             scale_factor=4.0
#                             )
# flow = mlab.pipeline.streamline(magnitude, seedtype='plane',
#                                 seed_visible=False,
#                                 seed_scale=0.5,
#                                 seed_resolution=1,
#                                 linetype='ribbon',
#                                 )
# vcp = mlab.pipeline.vector_cut_plane(magnitude, mask_points=2,
#                                      scale_factor=4,
#                                      colormap='jet',
#                                      plane_orientation='x_axes'
#                                      )
#
# mlab.outline()
# mlab.show()
# endregion





