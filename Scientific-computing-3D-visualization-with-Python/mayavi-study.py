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

# 鼠标选取交互操作
# 选取红色小球问题分析

# 用mlab.points3d建立红色和白色小球的集合
x1, y1, z1 = np.random.random((3, 10))
red_glyphs = mlab.points3d(x1, y1, z1, color=(1,0,0), resolution=10) # resolution可以理解为小球的分辨率

x2, y2, z2 = np.random.random((3, 10))
white_glyphs = mlab.points3d(x2, y2, z2, color=(0.9,0.9,0.9), resolution=10)

# 绘制选取框，并放在第一个小球上
outline = mlab.outline(line_width=3)
outline.outline_mode = 'cornered'
outline.bounds = (x1[0] - 0.1, x1[0] + 0.1,
                  y1[0] - 0.1, y1[0] + 0.1,
                  z1[0] - 0.1, z1[0] + 0.1,
                  )






