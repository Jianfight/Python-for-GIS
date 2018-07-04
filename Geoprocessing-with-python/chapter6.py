import ogr
from ospybook.vectorplotter import VectorPlotter

# 创建点和多点对象
# region

# faucets = ogr.Geometry(ogr.wkbMultiPoint) # 创建多点对象
# faucet = ogr.Geometry(ogr.wkbPoint) # 创建点对象
# faucet.AddPoint(67.5, 16) # 设定点的坐标
# faucets.AddGeometry(faucet) # 将点对象添加到多点对象中
# faucet.AddPoint(73, 31)
# faucets.AddGeometry(faucet)
# faucet.AddPoint(91, 24.5)
# faucets.AddGeometry(faucet)
# print(faucets)
#
# # 通过传递目标点的索引给GetGeometryRef()从多点几何类型中得到特定的点。
# faucets.GetGeometryRef(1).AddPoint(75, 32) # 修改多点集中点的坐标
# print(faucets)
#
# # 通过循环可以对点集中的多个点进行整体的偏移
# faucets_shift = ogr.Geometry(ogr.wkbMultiPoint)
# for i in range(faucets.GetGeometryCount()):
#     coordinate = faucets.GetGeometryRef(i).Clone() # 如果不使用克隆函数，会将faucets中的数据更改,
#                                                    # 这就证明GetGeometryRef函数只是将新的变量名指向faucets中数据的存储地址
#     coordinate.AddPoint(coordinate.GetX() + 10, coordinate.GetY())
#     faucets_shift.AddGeometry(coordinate)
# print(faucets)
# print(faucets_shift)
#
# vp = VectorPlotter(False)
# vp.plot(faucets, 'b.')
# vp.plot(faucets_shift, 'r^')
# # vp.zoom(-5) # 缩小范围让点可见
# vp.draw()

# endregion

# 创建线要素
sidewalk = ogr.Geometry(ogr.wkbLineString)
sidewalk.AddPoint(54, 37)
sidewalk.AddPoint(62, 35.5)
sidewalk.AddPoint(70.5, 38)
sidewalk.AddPoint(74.5, 41.5)
print(sidewalk)
vp = VectorPlotter(False)
vp.plot(sidewalk, 'b-')

# # 使用SetPoint函数，可以更改线对象中的某个点的坐标
# sidewalk.SetPoint(2, 76, 41.5)
# vp.plot(sidewalk, 'r-')
# # 同样可以使用循环，将先要素整体偏移一定的距离
# for i in range(sidewalk.GetPointCount()):
#     sidewalk.SetPoint(i, sidewalk.GetX(i), sidewalk.GetY(i) + 3)
# vp.plot(sidewalk, 'g--')

# # 在一个线要素中的某个位置插入一个顶点
# vertices = sidewalk.GetPoints() # 返回线要素各个顶点的坐标列表，列表中每个顶点的坐标使用列表的形式创建<元组列表>
# vertices[2:2] = [(66.5, 35, 0.0)] # 在列表中插入一个顶点，插入的形式要符合顶点坐标的形式
# # 使用更新过的列表创建新的线要素
# new_sidewalk = ogr.Geometry(ogr.wkbLineString)
# for vertex in vertices:
#     new_sidewalk.AddPoint(*vertex) # *符号是python的运算符，将元组展开成独立参数，并依次传递给AddPoint函数。
# vp.plot(new_sidewalk, 'g:')

vp.draw()




















