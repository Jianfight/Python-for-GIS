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

# 使用mayavi对numpy数组进行可视化
# points3D的形式
# 建立数组
# t = np.linspace(0,4*np.pi,20) # numpy中的linspace将创建一个等差数列的一维数组，建立的数组元素的数据格式是浮点型，常见的三个参数分别代表起始值
#                               # 终止值（默认包含自身）、数列个数
# x = np.sin(2*t)
# y = np.cos(t)
# z = np.cos(2*t)
# s = 2 + np.sin(t)
# # 对数据进行可视化
# points = mlab.points3d(x, y, z, s, colormap='Blues', scale_factor=0.25)
# mlab.show() # 该函数表示与图形进行交互，在默认情况下该函数建立了简单的GUI并开始事件循环，该函数中有一个默认参数stop=False用来定义事件循环是否结束

# plot3D的形式
# 建立数据
n_mer, n_long = 6, 11
dphi = np.pi /1000.0
phi = np.arange(0.0, 2*np.pi + 0.5*dphi, dphi) # 用与创建等差数组：start<起始值，可忽略不写，默认从0开始>，stop<结束值，生成的元素不包括结束值>
                                               # step<步长，可忽略不写，默认步长为1>，dtype<默认为None，设置显示元素的数据类型>
mu = phi * n_mer
x = np.cos(mu) * (1 + np.cos(n_long * mu / n_mer) *0.5)
y = np.sin(mu) * (1 + np.cos(n_long * mu / n_mer) *0.5)
z = np.sin(n_long * mu / n_mer) * 0.5

# 对数据进行可视化
l = mlab.plot3d(x, y, z, np.sin(mu), tube_radius=0.025, colormap='Spectral')
mlab.show()







