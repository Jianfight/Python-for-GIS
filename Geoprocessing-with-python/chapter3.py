from osgeo import ogr
import ospybook as pb
from ospybook.vectorplotter import VectorPlotter
import sys
import os

# 测试有没有相应矢量数据格式的驱动
# region Description
# deiver = ogr.GetDriverByName('geojson')
# print(deiver)
# # 在检测shape文件的驱动时，名称应为：esri shapefile
# deiver1 = ogr.GetDriverByName('esri shapefile')
# print(deiver1)
#
# # 使用ospybook库检测有没有相应矢量数据格式的驱动
# pb.print_drivers()
# endregion


# 输出一个shape file中的前10条记录
# region Description
# # 将文件路径存储到变量中
# fn = r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\global\ne_50m_populated_places.shp"
#
# # 打开数据源
# ds = ogr.Open(fn, 0) # ds取自数据源（data source）
# if ds == None:
#     # 如果打开的文件为空，提示路径错误
#     sys.exit('Could not open {0}.'.format(fn))
# # 将图层信息存储到变量中
# lyr = ds.GetLayer(0) # 从数据源中取回第一个图层
#
# i = 0
# for feat in lyr:
#     pt = feat.geometry()  # 提取要素的几何信息
#     x = pt.GetX()
#     y = pt.GetY()
#
#     name = feat.GetField('NAME') # 根据字段名称提取属性
#     pop = feat.GetField('POP_MAX')
#
#     print(name, pop, x, y)
#
#     i += 1
#     if i == 10:
#         break
#
# # 使用GetFeature()来获得指定的要素
# num_features = lyr.GetFeatureCount()
# last_feature = lyr.GetFeature(num_features - 1)
# print(last_feature.NAME)
#
# del ds # 在最后删除ds变量，强制关闭文件。
# endregion


# 查看数据
# 使用ospybook中的print_attributes()函数直接查看属性值，这个函数对于查看小数据的属性信息运行正常，但如果使用他来输出一个大数据的所有属性，
# 你会后悔的。
# fn = r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\global\ne_50m_populated_places.shp"
# pb.print_attributes(fn, 50, ['NAME', 'POP_MAX'])

# 绘制空间数据
# 更改工作目录，直接键入文件命就可以读取数据，不需要输入整个文件路径
# os.chdir(r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\global")
#
# vp = VectorPlotter(False) # 新建一个VectorPlotter类（矢量绘图）向构造函数中传递一个布尔变量，进入交互模式。
# vp.plot('ne_50m_admin_0_countries.shp', fill=False) # 不填充图形的内部
# vp.plot('ne_50m_populated_places.shp', 'bo') # bo表示蓝色的圆圈。
# vp.draw()


# 输出图层的边界坐标
ds = ogr.Open(r'C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\Washington\large_cities.geojson')
lyr = ds.GetLayer(0)
extent = lyr.GetExtent() # 该函数返回一个元组，为图层对象的边界坐标（min_x, max_x, min_y, max_y）
print(extent)

# 查看图层中要素的类型
print(lyr.GetGeomType()) # 查看图层中要素的类型，但是返回的是一个整数。
# 查看要素的类型
feature = lyr.GetFeature(0)
print(feature.geometry().GetGeometryName()) # 查看要素的类型，返回的是字符串（类型描述）
# 查看图层的空间参考系统
print(lyr.GetSpatialRef()) # 查看图层的空间参考系统。

# 通过图层对象的schema属性来获得FieldDefn列表，其中每个对象包含属性列名称及数据类型等信息。
for field in lyr.schema:
    print(field.name, field.GetTypeName())











