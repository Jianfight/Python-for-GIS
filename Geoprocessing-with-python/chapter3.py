from osgeo import ogr
import ospybook as pb
from ospybook.vectorplotter import VectorPlotter
import sys
import os

# 测试有没有相应矢量数据格式的驱动
# region

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
# region

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
# region

# 使用ospybook中的print_attributes()函数直接查看属性值，这个函数对于查看小数据的属性信息运行正常，但如果使用他来输出一个大数据的所有属性，
# 你会后悔的。
# fn = r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\global\ne_50m_populated_places.shp"
# pb.print_attributes(fn, 50, ['NAME', 'POP_MAX'])

# endregion

# 绘制空间数据
# region

# # 更改工作目录，直接键入文件命就可以读取数据，不需要输入整个文件路径
# os.chdir(r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\global")
#
# vp = VectorPlotter(False) # 新建一个VectorPlotter类（矢量绘图）向构造函数中传递一个布尔变量，进入交互模式。
# vp.plot('ne_50m_admin_0_countries.shp', fill=False) # 不填充图形的内部
# vp.plot('ne_50m_populated_places.shp', 'bo') # bo表示蓝色的圆圈，b代表蓝色，o代表符号是圆圈。
# vp.draw()

# endregion


# 输出图层的边界坐标
# region

# ds = ogr.Open(r'C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\Washington\large_cities.geojson')
# lyr = ds.GetLayer(0)
# extent = lyr.GetExtent() # 该函数返回一个元组，为图层对象的边界坐标（min_x, max_x, min_y, max_y）
# print(extent)
#
# # 查看图层中要素的类型
# print(lyr.GetGeomType()) # 查看图层中要素的类型，但是返回的是一个整数。
# # 查看要素的类型
# feature = lyr.GetFeature(0)
# print(feature.geometry().GetGeometryName()) # 查看要素的类型，返回的是字符串（类型描述）
# # 查看图层的空间参考系统
# print(lyr.GetSpatialRef()) # 查看图层的空间参考系统。
#
# # 通过图层对象的schema属性来获得FieldDefn列表，其中每个对象包含属性列名称及数据类型等信息。
# for field in lyr.schema:
#     print(field.name, field.GetTypeName())

# endregion


# 矢量数据的写入
# region

# 打开要写入的数据源
# ds = ogr.Open(r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\global",1)
# if ds is None:
#     sys.exit('Could not open folder.')
#
# in_lyr = ds.GetLayer('ne_50m_populated_places') # 获取shape文件
#
# if ds.GetLayer('capital_cities'):
#     ds.DeleteLayer('capital_cities') # 如果要创建的图层已经存在将其删除
#
# out_lyr = ds.CreateLayer('capital_cities',
#                          in_lyr.GetSpatialRef(),
#                          ogr.wkbPoint) # 创建新的图层，几何类型点，空间参考于输入的图层相同
# out_lyr.CreateFields(in_lyr.schema) # 属性字段与输入坐标相同
#
# out_defn = out_lyr.GetLayerDefn() # 获取输入图层的定义信息
# out_feat = ogr.Feature(out_defn) # 创建一个空的要素
#
# for in_feat in in_lyr:
#     if in_feat.GetField('FEATURECLA') == 'Admin-0 capital':
#         geom = in_feat.geometry()
#         out_feat.SetGeometry(geom)
#         for i in range(in_feat.GetFieldCount()):
#             value = in_feat.GetField(i)
#             out_feat.SetField(i,value)
#         out_lyr.CreateFeature(out_feat)
# del ds

# endregion


# 创建数据源，写入新的数据，添加属性字段，更新属性值
# region

# # 创建数据源前，应该考虑好使用什么样的驱动程序，每种驱动程序只知道如何处理操作一种矢量数据类型
# shape_driver = ogr.GetDriverByName('esri shapefile') # 通过GetDriverByName()函数来获得驱动程序。
# shape_fn = r"C:\Users\think\Desktop\python\python-for-GIS-DATA" \
#           r"\osgeopy-data\osgeopy-data\CreateDataSource" # 定义一个数据源的路径
#
# if os.path.exists(shape_fn): # 检测一下我们要创建的数据源是否已经存在
#     shape_driver.DeleteDataSource(shape_fn) # 如果存在，必须使用驱动程序删除相应的数据源，而不是python的内置函数，
#                                           # 因为驱动程序可以确保所有必须的文件都被删除。
# shape_ds = shape_driver.CreateDataSource(shape_fn) # 使用驱动程序创建数据源。
# if shape_ds is None: # 检测一下创建的数据源是否为空。
#     sys.exit('Could not create {0}.'.format(shape_fn))
# shape_ds.SyncToDisk()
#
# # 打开需要读取的数据源
# input_fn = r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\global"
# ds_input = ogr.Open(input_fn,False)
# if ds_input == None:
#     sys.exit('Could not open {0}.'.format(input_fn))
# in_lyr = ds_input.GetLayer('ne_50m_populated_places') # 获取需要进行筛选复制的shp文件
#
# # 在创建的数据源中写入数据
# if shape_ds.GetLayer('capital_cities'):
#     shape_ds.DeleteLayer('capital_cities') # 如果要创建的图层已经存在将其删除
#
# out_lyr = shape_ds.CreateLayer('capital_cities',
#                          in_lyr.GetSpatialRef(),
#                          ogr.wkbPoint) # 创建新的图层，几何类型点，空间参考于输入的图层相同
# out_lyr.CreateFields(in_lyr.schema) # 属性字段与输入坐标相同
#
# out_defn = out_lyr.GetLayerDefn() # 获取输入图层的定义信息
# out_feat = ogr.Feature(out_defn) # 创建一个空的要素
#
# for in_feat in in_lyr:
#     if in_feat.GetField('FEATURECLA') == 'Admin-0 capital':
#         geom = in_feat.geometry()
#         out_feat.SetGeometry(geom)
#         for i in range(in_feat.GetFieldCount()):
#             value = in_feat.GetField(i)
#             out_feat.SetField(i,value)
#         out_lyr.CreateFeature(out_feat)
#
# # 在输出的图层中创建新的属性字段
# coord_fld = ogr.FieldDefn('X', ogr.OFTReal) # 创建新的字段,设置字段名称和字段类型（浮点型）
# coord_fld.SetWidth(8)      # 设置字段宽度，在shape文件中如果需要设置字段精度，必须先设置字段宽度
# #coord_fld.SetPrecision(6)  # 设置字段的精度，在本例中因为精度无法判断，故将该行注释
# out_lyr.CreateField(coord_fld)  # 将设置好的字段添加到图层中
# coord_fld.SetName('Y')     # 通过更改已创建字段的定义来重用定义新的另一个字段
# out_lyr.CreateField(coord_fld)
#
# # 为新的属性字段添加属性值
# for feature in out_lyr:
#     geo = feature.geometry()
#     x_value = geo.GetX()
#     # print(x_value,type(x_value))
#     feature.SetField('X', x_value)
#     y_value = geo.GetY()
#     # print(y_value,type(y_value))
#     feature.SetField('Y', y_value)
#     out_lyr.SetFeature(feature) # 对每个要素的属性字段添加完属性值后，需要传递更改信息给Layer.SetFeature函数,以更新已有要素的属性值
#                                 # 在上一个循环（添加要素中并没有使用SetFeature函数），是因为两个循环目的不同，一个是添加，一个是更新，
#                                 # 所以代码看起来有些不同
#
# del ds_input
# del shape_ds

# endregion


# 更改属性字段
# region

# # 更改已有的属性字段
# layer_defn = layer.GetLayerDefn()
# i = layer_defn.GetFieldIndex('X') # 通过属性字段的名称获得，字段值的索引
# width = layer_defn.GetFieldDefn(i).GetWidth()
# fld_defn = ogr.FieldDefn('X_coord', ogr.OFTReal) # 设定新的字段
# fld_defn.SetWidth(width)
# fld_defn.SetPrecision(4)
# flag = ogr.ALTER_NAME_FLAG + ogr.ALTER_WIDTH_PRECISION_FLAG # 添加字段需要更改的标识
# layer.AlterFieldDefn(i, fld_defn, flag) # 使用AlterFieldDefn()函数更改已有的属性字段，将字段的定义更改为新设定的字段的定义。

# endregion


# 删除要素
# region

# layer.DeleteFeature(feature.GetFID()) # 如果删除要素，需要获得要素的FID（要素编号，也成为偏移值）

# 如果删除了很多要素，在文件中可能存在大量不必要的已用空间，就类似Access数据库中删除数据后需要进行压缩或者修复。
# data_source.ExecuteSQL('REPACK' + layer.GetName()) # 将删除要素后的空间进行释放，对于shape类型的数据可以使用。

# endregion

