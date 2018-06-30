import  ogr
import ospybook
from ospybook.vectorplotter import VectorPlotter

# # 定义一个查看数据源中图层的函数
# def print_layers(fn):
#     ds = ogr.Open(fn, False)
#     if ds == None:
#         raise OSError('Could not open {}'.format(fn))
#     for i in range(ds.GetLayerCount()):
#         lyr = ds.GetLayer(i)
#         print('{0}:{1}'.format(i, lyr.GetName()))
#
# # 测试函数
# fn = r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\global"
# print_layers(fn)


# # 查看SpatiaLite数据库
# fn = r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\global\natural_earth_50m.sqlite"
# ospybook.print_layers(fn)
# # 绘制数据库中的图层
# ds = ogr.Open(fn)
# lyr = ds.GetLayer('populated_places')
# lyr_1 = ds.GetLayer('countries')
# vp = VectorPlotter(False)
# vp.plot(lyr, 'go')
# vp.plot(lyr_1, fill=False)
# vp.draw()


# 查看eari文件地理数据库
# fn = r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\global\natural_earth.gdb"
# ospybook.print_layers(fn)
# ds = ogr.Open(fn)
# lyr = ds.GetLayer('countries_10m')
# # vp = VectorPlotter(False)
# # vp.plot(lyr)
# # vp.draw()
# # 复制文件地理数据库中的图层为新的shape文件
# fn_out = r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\CreateDataSource"
# shape_ds = ogr.Open(fn_out, 1)
# shape_ds.CopyLayer(lyr, 'countries_110m')
# del ds, shape_ds
# def copy_layer_of_gdb_to_shape(in_gdb_fn, out_fn, layer_name):
#     """将GDB中的图层以shape的格式复制到到新的数据源中"""
#     gdb_ds = ogr.Open(in_gdb_fn)
#     layer = gdb_ds.GetLayer(layer_name)
#     shape_ds = ogr.Open(out_fn, 1)
#     if shape_ds.GetLayer(layer_name):
#         shape_ds.DeleteLayer(layer_name)
#     shape_ds.CopyLayer(layer, layer_name)
#     del gdb_ds, shape_ds
#copy_layer_of_gdb_to_shape(fn, fn_out, 'countries_10m')


# 复制要素到文件地理数据库
gdb_driver = ogr.GetDriverByName('FileGDB')
print(gdb_driver)










