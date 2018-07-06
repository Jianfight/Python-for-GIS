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

# 创建线
# region

# sidewalk = ogr.Geometry(ogr.wkbLineString)
# sidewalk.AddPoint(54, 37)
# sidewalk.AddPoint(62, 35.5)
# sidewalk.AddPoint(70.5, 38)
# sidewalk.AddPoint(74.5, 41.5)
# print(sidewalk)
# vp = VectorPlotter(False)
# vp.plot(sidewalk, 'b-')
#
# # # 使用SetPoint函数，可以更改线对象中的某个点的坐标
# # sidewalk.SetPoint(2, 76, 41.5)
# # vp.plot(sidewalk, 'r-')
# # # 同样可以使用循环，将先要素整体偏移一定的距离
# # for i in range(sidewalk.GetPointCount()):
# #     sidewalk.SetPoint(i, sidewalk.GetX(i), sidewalk.GetY(i) + 3)
# # vp.plot(sidewalk, 'g--')
#
# # # 在一个线要素中的某个位置插入一个顶点
# # vertices = sidewalk.GetPoints() # 返回线要素各个顶点的坐标列表，列表中每个顶点的坐标使用列表的形式创建<元组列表>
# # vertices[2:2] = [(66.5, 35, 0.0)] # 在列表中插入一个顶点，插入的形式要符合顶点坐标的形式
# # # 使用更新过的列表创建新的线要素
# # new_sidewalk = ogr.Geometry(ogr.wkbLineString)
# # for vertex in vertices:
# #     new_sidewalk.AddPoint(*vertex) # *符号是python的运算符，将元组展开成独立参数，并依次传递给AddPoint函数。
# # vp.plot(new_sidewalk, 'g:')
# # vp.draw()
#
# # 从线创建点
# def line_to_point_layer(ds, line_name, pt_name):
#     """Creates a point layer from vertices in a line layer."""
#     if ds.GetLayer(pt_name):
#         ds.DeleteLayer(pt_name)
#     line_lyr = ds.GetLayer(line_name)
#     sr = line_lyr.GetSpatialRef() # 获取图层的空间参考
#     pt_lyr = ds.CreateLayer(pt_name, sr, ogr.wkbPoint) # 通过空间参考创建新的点图层
#     pt_lyr.CreateFields(line_lyr.schema) # 设置点图层的属性字段
#     pt_feat = ogr.Feature(pt_lyr.GetLayerDefn()) # 使用图层的定义创建一个要素
#     pt_geom = ogr.Geometry(ogr.wkbPoint) # 创建几何对象
#     for line_feat in line_lyr:
#         atts = line_feat.items() # 返回的是一个字典，包含要素的属性名称和属性值
#         for fld_name in atts.keys(): # 遍历属性表将原图层中的属性值添加到新要素中
#             pt_feat.SetField(fld_name, atts[fld_name])
#         for coords in line_feat.geometry().GetPoints(): # 将每个要素的几何类型提取出来
#             pt_geom.AddPoint(*coords)
#             pt_feat.SetGeometry(pt_geom) # 将几何类型和属性合并到一起
#             pt_lyr.CreateFeature(pt_feat) # 将合并好的新要素添加到创建的图层中
#     return pt_lyr

# endregion

# 创建和编辑多线（类似与发射状的河流，像树叶的脉络一样）
# region

# path1 = ogr.Geometry(ogr.wkbLineString)
# path1.AddPoint(61.5, 29)
# path1.AddPoint(63, 20)
# path1.AddPoint(62.5, 16)
# path1.AddPoint(60, 13)
#
# path2 = ogr.Geometry(ogr.wkbLineString)
# path2.AddPoint(60.5, 12)
# path2.AddPoint(68.5, 13.5)
#
# path3 = ogr.Geometry(ogr.wkbLineString)
# path3.AddPoint(69.5, 33)
# path3.AddPoint(80, 33)
# path3.AddPoint(86.5, 22.5)
#
# paths = ogr.Geometry(ogr.wkbMultiLineString)
# paths.AddGeometry(path1)
# paths.AddGeometry(path2)
# paths.AddGeometry(path3)
# print(paths)
# vp = VectorPlotter(False)
# vp.plot(paths, 'b--')
#
# # 一旦顶点被添加到多线，想要编辑它，首先需要获取想要编辑的单线，然后像多点那样编辑它。
# paths.GetGeometryRef(0).SetPoint(1, 63, 22) # 编辑多线中第一条线要素中第二个点的坐标
# # 可以使用循环将多线整体平移一个距离
# for i in range(paths.GetGeometryCount()):
#     path = paths.GetGeometryRef(i)
#     for j in range(path.GetPointCount()):
#         path.SetPoint(j, path.GetX(j) + 3, path.GetY(j) + 3)
# vp.plot(paths, 'r--')
#
# vp.draw()

# endregion


# 创建多边形
# ring = ogr.Geometry(ogr.wkbLinearRing)
# ring.AddPoint(58, 38.5)
# ring.AddPoint(53, 6)
# ring.AddPoint(99.5, 19)
# ring.AddPoint(73, 42)
# yard = ogr.Geometry(ogr.wkbPolygon)
# yard.AddGeometry(ring)
# yard.CloseRings()
#
# vp = VectorPlotter(False)
# vp.plot(yard, fill=False, edgecolor='green') # edgecolor参数代表边框的颜色
#
# # 整体平移多边形
# # ring = yard.GetGeometryRef(0) # 从多边形中获取第一个环
# # for i in range(ring.GetPointCount()):
# #     ring.SetPoint(i, ring.GetX(i) - 5, ring.GetY(i))
# # vp.plot(yard, fill=False, ec='red', linestyle='dashed') # dashed表示虚线
#
# # 可以使用顶点插入线的方法将顶点插入到多边形环中
# ring = yard.GetGeometryRef(0)
# vertices = ring.GetPoints()
# # print(vertices)
# vertices[2:3] = ((90,16), (90,27))
# # vertices = tuple(vertices)
# # print(vertices)
# for i in range(len(vertices)):
#     ring.SetPoint(i, *vertices[i])
# vp.plot(yard, fill=False, ec='black', ls='dotted', linewidth=3)
#
# vp.draw()

# # 从多边形中创建线
# def poly_to_line_layer(ds, poly_name, line_name):
#     """Creates a line layer from a polygon layer."""
#     if ds.GetLayer(line_name):
#         ds.DeleteLayer(line_name)
#     poly_lyr = ds.GetLayer(poly_name)
#     sr = poly_lyr.GetSpatialRef()
#     line_lyr = ds.CreateLayer(line_name, sr, ogr.wkbLineString)
#     line_lyr.CreateFields(poly_lyr.schema)
#     line_feat = ogr.Feature(line_lyr.GetLayerDefn())
#     for poly_feat in poly_lyr:
#         atts = poly_feat.items()
#         poly_geom = poly_feat.geometry()
#         for fld_name in atts.keys():
#             line_feat.SetField(fld_name, atts[fld_name])
#         for i in range(poly_geom.GetGeometryCount()):
#             ring = poly_geom.GetGeometryRef(i)
#             line_geom = ogr.Geometry(ogr.wkbLineString)
#             for coords in ring.GetPoints():
#                 line_geom.AddPoint(*coords)
#             line_feat.SetGeometry(line_geom)
#             line_lyr.CreateFeature(line_feat)
#     return line_lyr

# 创建和编辑复合多边形（multipolygons）
box1 = ogr.Geometry(ogr.wkbLinearRing)
box1.AddPoint(87.5, 25.5)
box1.AddPoint(89, 25.5)
box1.AddPoint(89, 24)
box1.AddPoint(87.5, 24)
garden1 = ogr.Geometry(ogr.wkbPolygon)
garden1.AddGeometry(box1)

box2 = ogr.Geometry(ogr.wkbLinearRing)
box2.AddPoint(89, 23)
box2.AddPoint(92, 23)
box2.AddPoint(92, 22)
box2.AddPoint(89, 22)
garden2 = ogr.Geometry(ogr.wkbPolygon)
garden2.AddGeometry(box2)

# 因为复合多边形是由一个人或多个多边形构成的，所以创建复合多边形向其中添加的是多边形。
gardens = ogr.Geometry(ogr.wkbMultiPolygon)
gardens.AddGeometry(garden1)
gardens.AddGeometry(garden2)
gardens.CloseRings() # 一次性关闭所有的环
print(gardens)

vp = VectorPlotter(False)
vp.plot(gardens)

# 整体移动复合多边形
for i in range(gardens.GetGeometryCount()):
    ring = gardens.GetGeometryRef(i).GetGeometryRef(0)
    for j in range(ring.GetPointCount()):
        ring.SetPoint(j, ring.GetX(j) + 1,ring.GetY(j) + 0.5)
vp.plot(gardens, fill=False, ec='red', ls='dashed')

# 创建带有岛的多边形
lot = ogr.Geometry(ogr.wkbLinearRing)
lot.AddPoint(58, 38.5)
lot.AddPoint(53, 6)
lot.AddPoint(99.5, 19)
lot.AddPoint(73, 42)

house = ogr.Geometry(ogr.wkbLinearRing)
house.AddPoint(67.5, 29)
house.AddPoint(69, 25.5)
house.AddPoint(64, 23)
house.AddPoint(69, 15)
house.AddPoint(82.5, 22)
house.AddPoint(76, 31.5)

yard = ogr.Geometry(ogr.wkbPolygon)
yard.AddGeometry(lot)
yard.AddGeometry(house)
yard.CloseRings()
vp.plot(yard, fill=False)

# 移动带有岛的多边形
for i in range(yard.GetGeometryCount()):
    ring = yard.GetGeometryRef(i)
    for j in range(ring.GetPointCount()):
        ring.SetPoint(j, ring.GetX(j) + 1, ring.GetY(j) + 0.5)
vp.plot(yard, fill=False, hatch='x', color='blue')

vp.draw()










