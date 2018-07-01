import os
import urllib
import folium
import  ogr
import ospybook
import gdal
from ospybook.vectorplotter import VectorPlotter

# # 定义一个查看数据源中图层的函数
# region

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

# endregion


# # 查看SpatiaLite数据库
# region

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

# endregion


# 查看eari文件地理数据库
# region

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

# endregion

# 复制要素到文件地理数据库(前提是FileGDB类型的数据驱动可以使用)
# region

# def layers_to_feature_dataset(ds_name, gdb_fn, dataset_name):
#     """复制地理要素到文件地理数据库中的资料组"""
#     in_ds = ogr.Open(ds_name)
#     if in_ds is None:
#         raise RuntimeError('Could not open datasource')
#
#     gdb_driver = ogr.GetDriverByName('FileGDB')
#     if os.path.exists(gdb_fn):
#         gdb_ds = gdb_driver.Open(gdb_fn, 1)
#     else:
#         gdb_ds = gdb_driver.CreateDataSource(gdb_fn)
#     if gdb_ds is None:
#         raise RuntimeError('Could not open file geodatabase')
#
#     if dataset_name : # 如果分类集存在就创建分类参数
#         options = ['FEATURE DATASET=' + dataset_name]
#
#     for i in range(in_ds.GetLayerCount()):
#         lyr = in_ds.GetLayer(i)
#         lyr_name = lyr.GetName()
#         print('Copying' + lyr_name + '...')
#         if options :
#             gdb_ds.CopyLayer(lyr, lyr_name, options)
#         else:
#             gdb_ds.CopyLayer(lyr, lyr_name)
#
# layers_to_feature_dataset(r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\global",
#                           r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\CreateDataSource\osgeopy-data.gdb",
#                           'global')

# endregion


# 网络要素服务（WFS）
def get_bbox(geom):
    """Return the bbox based on a geomtry envelope."""
    return '{0}，{2}，{1}，{3}'.format(*geom.GetEnvelope())

def get_center(geom):
    """返回几何图形的中心点"""
    centroid = geom.Centroid()
    return [centroid.GetY(), centroid.GetX()]

def get_state_geom(state_name, file_path):
    """返回一个州的几何图形"""
    ds = ogr.Open(file_path)
    if ds is None:
        raise RuntimeError('Could not open the states dataset. Is the path corrent?')
    lyr = ds.GetLayer()
    lyr.SetAttributeFilter('state = "{0}"'.format(state_name))
    feature = next(lyr)
    return feature.geometry().Clone()

def save_state_gauges(out_fn, wfs_data_url, bbox=None):
    """保存wfs数据到geojson文件"""
    parms = {
        'version': '1.1.0',
        'typeNames': 'ahps_gauges:Observed_River_Stages',
        'srsName': 'urn:ogc:def:crs:EPSG:6.9:4326',
    }
    if bbox:
        parms['bbox'] = bbox
    try:
        request = 'WFS:{0}？{1}'.format(wfs_data_url, urllib.urlencode(parms))
    except:
        request = 'WFS:{0}?{1}'.format(wfs_data_url, urllib.parse.urlencode(parms))
    wfs_ds = ogr.Open(request)
    if wfs_ds is None:
        raise RuntimeError('Could not open WFS.')
    wfs_lyr = wfs_ds.GetLayer(0)

    driver = ogr.GetDriverByName('GeoJson')
    if os.path.exists(out_fn):
        driver.DeleteDataSource(out_fn)
    json_ds = driver.CreateDataSource(out_fn)
    json_ds.CopyLayer(wfs_lyr,'')

def make_map(state_name, json_fn, html_fn, file_path, wfs_data_url, **kwargs):
    """使用folium库制作地图"""
    geom = get_state_geom(state_name, file_path)
    save_state_gauges(json_fn, wfs_data_url, get_bbox(geom))
    fmap = folium.Map(location=get_center(geom), **kwargs)
    fmap.geo_json(geo_path=json_fn)
    fmap.create_map(path=html_fn)

base_map_file_path = r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\US\states.geojson"
wfs_url = "http://gis.srh.noaa.gov/arcgis/services/ahps_gauges/MapServer/WFSServer"
make_map('Oklahoma', 'ok.json', 'ok.html', base_map_file_path, wfs_url, zoom_start=7)





