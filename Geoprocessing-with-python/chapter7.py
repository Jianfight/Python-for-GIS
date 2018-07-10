import os
import ogr
from osgeo import osr
from ospybook.vectorplotter import VectorPlotter
import time

# 叠加数据分析
# region

# 一些练习计算新奥尔良市有多少湿地面积
# 提取沼泽的数据
# file_path = r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\US\wtrbdyp010.shp"
# water_ds = ogr.Open(file_path)
# water_lyr = water_ds.GetLayer(0)
# water_lyr.SetAttributeFilter('WaterbdyID = 1011327')
# marsh_feat = water_lyr.GetNextFeature()
# marsh_geom = marsh_feat.geometry().Clone()
#
# vp = VectorPlotter(False)
# vp.plot(marsh_geom, 'b')
#
# # 提取新奥尔良边界数据，来提供背景
# file_path_city = r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\Louisiana\NOLA.shp"
# nola_ds = ogr.Open(file_path_city)
# nola_lyr = nola_ds.GetLayer(0)
# nola_feat = nola_lyr.GetNextFeature()
# nola_geom = nola_feat.geometry().Clone()
# vp.plot(nola_geom, fill=False, ec='red', ls='dashed', lw=3)
#
# # 提取两数据相交的部分
# # intersection = marsh_geom.Intersection(nola_geom)
# # vp.plot(intersection, 'yellow', hatch='x')
# vp.draw()
#
# # 提取新奥尔良市的湿地面积
# water_lyr.SetAttributeFilter("Feature != 'Lake'")
# water_lyr.SetSpatialFilter(nola_geom)
# wetlands_area = 0
# for feat in water_lyr:
#     intersect = feat.geometry().Intersection(nola_geom)
#     wetlands_area += intersect.GetArea()
# pcnt = wetlands_area / nola_geom.GetArea()
# print('{:.1%} of New Orleans is wetland.'.format(pcnt)) # 因为坐标是用经纬度的形式表示的，所以计算面积的值不准确，已百分比的形式显示更贴切
# # print("Orleans area of wetland is {0}".format(wetlands_area))
#
# # 提取新奥尔良市的湿地面积的另一种方法
# water_lyr.SetAttributeFilter("Feature != 'Lake'")
# # 在内存中创建一个临时图层
# memory_driver = ogr.GetDriverByName('Memory')
# temp_ds = memory_driver.CreateDataSource('temp')
# temp_lyr = temp_ds.CreateLayer('temp')
# # 将图层相交的结果储存在临时图层内
# nola_lyr.Intersection(water_lyr, temp_lyr)
# sql = "SELECT SUM(OGR_GEOM_AREA) AS area FROM temp"
# lyr = temp_ds.ExecuteSQL(sql)
# pcnt = lyr.GetFeature(0).GetField('area') / nola_geom.GetArea()
# print('{:.1%} of New Orleans is wetland.'.format(pcnt))

# endregion


# 邻近分析
# region

# 获取美国有多少座城市位于火山10英里（1英里=1609.3米）范围之内的。
# 提取原始数据图层
# file_path = r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\US"
# shp_ds = ogr.Open(file_path)
# volcano_lyr = shp_ds.GetLayer('us_volcanos_albers')
# cities_lyr = shp_ds.GetLayer('cities_albers')
# # 创建临时图层，用于存放火山缓冲区
# memory_driver = ogr.GetDriverByName('memory')
# memory_ds = memory_driver.CreateDataSource('temp')
# buff_lyr = memory_ds.CreateLayer('buffer')
# buff_feat = ogr.Feature(buff_lyr.GetLayerDefn())
# # 提取火山缓冲区
# for volcano_feat in volcano_lyr:
#     buff_geom = volcano_feat.geometry().Buffer(16000)
#     buff_feat.SetGeometry(buff_geom)
#     buff_lyr.CreateFeature(buff_feat)
# vp = VectorPlotter(False)
# vp.plot(buff_lyr,)
# # 将城市数据与火山缓冲区数据进行叠加
# result_lyr = memory_ds.CreateLayer('result')
# buff_lyr.Intersection(cities_lyr, result_lyr) # 使用这种方法存在一个问题如果一个城市与多个火山缓冲区相交，那么他将被计入多次。
# print('The number of cities within the range of 16000 meters of the volcano is:{0}'.format(result_lyr.GetFeatureCount()))
# vp.plot(result_lyr, 'r.')
# vp.draw()

# 该例子的另一种方法
# file_path = r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\US"
# shp_ds = ogr.Open(file_path)
# volcano_lyr = shp_ds.GetLayer('us_volcanos_albers')
# cities_lyr = shp_ds.GetLayer('cities_albers')
# # 将火山的缓冲区添加到复合多边形中
# multipoly = ogr.Geometry(ogr.wkbMultiPolygon)
# for volcano_feat in volcano_lyr:
#     buff_geom = volcano_feat.geometry().Buffer(16000)
#     multipoly.AddGeometry(buff_geom)
# # 使用空间过滤获取在火山缓冲区中的城市数量
# cities_lyr.SetSpatialFilter(multipoly.UnionCascaded()) # unionCascaded()函数可以将多个几何要素合并在一起。
# print('The number of cities within the '
#       'range of 16000 meters of the volcano is:{0}'.format(cities_lyr.GetFeatureCount()))
# country_lyr = shp_ds.GetLayer('countyp010')

# 计算两个点要素之间的距离
# file_path = r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\US"
# shp_ds = ogr.Open(file_path)
# volcano_lyr = shp_ds.GetLayer('us_volcanos_albers')
# cities_lyr = shp_ds.GetLayer('cities_albers')
# # 获取一个Rainier火山的位置
# volcano_lyr.SetAttributeFilter("NAME = 'Rainier'")
# feat = volcano_lyr.GetNextFeature()
# rainier = feat.geometry().Clone()
# # 获取Seattle西雅图的位置
# cities_lyr.SetAttributeFilter("NAME = 'Seattle'")
# feat = cities_lyr.GetNextFeature()
# seattle = feat.geometry().Clone()
# # 计算两个要素之间的距离
# meters = round(rainier.Distance(seattle)) # 计算单位为米
# miles = meters / 1600 # 转换为英里
# print('{0} meters, {1}miles'.format(meters, miles))

# endregion


# 实例：风力发电厂选址
# region

# vp = VectorPlotter(False) # 用于显示数据
# # 首先添加人口密度字段，并为每个要素添加相应的数据
# census_fn = r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\California\ca_census_albers.shp"
# census_ds = ogr.Open(census_fn, True)
# # print(census_ds)
# census_lyr = census_ds.GetLayer()
# # 如果属性字段已经存在先将其删除
# if census_lyr.FindFieldIndex('popsqkm', 0):
#     census_lyr.DeleteField(census_lyr.FindFieldIndex('popsqkm', 0))
# density_field = ogr.FieldDefn('popsqkm', ogr.OFTReal)
# census_lyr.CreateField(density_field)
# for row in census_lyr:
#     pop = row.GetField('HD01_S001') # 获取人口数量
#     sqkm = row.geometry().GetArea() / 1000000 # 除以1000000是为了将数据计算到每平方千米
#     row.SetField('popsqkm', pop / sqkm) # 计算每平方千米的人口数，并将其添加到新设定的字段中
#     census_lyr.SetFeature(row)
#
# # 提取因皮里尔县的空间尺度范围
# county_fn = r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\US\countyp010.shp"
# county_ds = ogr.Open(county_fn)
# county_lyr = county_ds.GetLayer()
# county_lyr.SetAttributeFilter("COUNTY = 'Imperial County'")
# county_row = next(county_lyr)
# county_geom = county_row.geometry().Clone()
# del county_ds # 因为已经将几何边框克隆了出来，所以将城市的数据源删除并不影响该程序
#
# # 转换城市边界的坐标系统
# county_geom.TransformTo(census_lyr.GetSpatialRef())
# vp.plot(county_geom, fill=False, ec='red') # 添加底图数据
# census_lyr.SetSpatialFilter(county_geom) # 根据因皮里尔县的边界信息筛选数据
# census_lyr.SetAttributeFilter('popsqkm < 0.5') # 根据每平方千米人口小于0.5的属性条件筛选数据
#
# # 打开风力数据，筛选评级为3以上的区域
# wind_fn = r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\California\california_50m_wind_albers.shp"
# wind_ds = ogr.Open(wind_fn)
# wind_lyr = wind_ds.GetLayer()
# wind_lyr.SetAttributeFilter('WPC >= 3') # 将评选等级为3级以上的数据筛选出来
#
# # 创建一个储存分析结果的数据源
# out_fn = r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\California\wind_farm.shp"
# out_ds = ogr.GetDriverByName('ESRI shapefile').CreateDataSource(out_fn)
# out_lyr = out_ds.CreateLayer('wind_farm', wind_lyr.GetSpatialRef(), ogr.wkbPolygon)
# out_lyr.CreateField(ogr.FieldDefn('wind', ogr.OFTInteger))
# out_lyr.CreateField(ogr.FieldDefn('popsqkm', ogr.OFTReal))
# out_row = ogr.Feature(out_lyr.GetLayerDefn())
#
# # 将因皮里尔县内的人口数据与风力数据进行相交
# for census_row in census_lyr:
#     census_geom = census_row.geometry()
#     censue_geom = census_geom.Intersection(county_geom) # 将人口密度小于0.5的人口普查数据与县界相交
#     wind_lyr.SetSpatialFilter(census_geom)
# print('Intersecting census tract with {0} wind polygons'.format(wind_lyr.GetFeatureCount()))
#
# # 检查是否存在风力多边形
# if wind_lyr.GetFeatureCount() > 0:
#     out_row.SetField('popsqkm', census_row.GetField('popsqkm'))
#     for wind_row in wind_lyr:
#         wind_geom = wind_row.geometry()
#         if census_geom.Intersection(wind_geom):
#             new_geom = census_geom.Intersection(wind_geom)
#             out_row.SetField('wind', wind_row.GetField('WPC'))
#             out_row.SetGeometry(new_geom)
#             out_lyr.CreateFeature(out_row)
#
# # 将结果中小的多边形合成一个大的多边形
# folder = r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\California"
# output_ds = ogr.Open(folder, True)
# output = output_ds.CreateLayer('wind_farm2', wind_lyr.GetSpatialRef(), ogr.wkbMultiPolygon)
# print(output)
# output_feat = ogr.Feature(output.GetLayerDefn())
# multipoly = ogr.Geometry(ogr.wkbMultiPolygon)
# for out_row in out_lyr:
#     out_geom = out_row.geometry().Clone()
#     out_geom_type = out_geom.GetGeometryType()
#     if out_geom_type == ogr.wkbPolygon:
#         multipoly.AddGeometry(out_geom)
#     elif out_geom_type == ogr.wkbMultiPolygon: # 打散符合多边形
#         for i in range(out_geom.GetGeometryCount()):
#             multipoly.AddGeometry(out_geom.GetGeometryRef(i))
# # 将多边形合并
# multipoly = multipoly.UnionCascaded()
# # 只保留面积大的多边形
# for i in range(multipoly.GetGeometryCount()):
#     poly = multipoly.GetGeometryRef(i)
#     if poly.GetArea() > 1000000:
#         output_feat.SetGeometry(poly)
#         output.CreateFeature(output_feat)
#
# vp.plot(output) # 将合并后的结果绘出
# vp.draw()

# endregion


# 实例：动物跟踪数据
# 研究对象：加拉帕戈斯 信天翁的GPS定位数据
# 从CSV格式的信天翁GPS定位数据提取数据，创建shapefile文件
csv_fn = r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\Galapagos\Galapagos Albatrosses.csv"
shp_fn = r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\Galapagos\albatross_dd.shp"
sr = osr.SpatialReference(osr.SRS_WKT_WGS84) # 设定空间参考为WGS84

# 创建空的图层，规定好图层的属性
shp_ds = ogr.GetDriverByName('ESRI shapefile').CreateDataSource(shp_fn)
shp_lyr = shp_ds.CreateLayer('albatross_dd', sr, ogr.wkbPoint)
shp_lyr.CreateField(ogr.FieldDefn('tag_id', ogr.OFTString))
shp_lyr.CreateField(ogr.FieldDefn('timestamp', ogr.OFTString))
shp_row = ogr.Feature(shp_lyr.GetLayerDefn())

# 打开CSV文件，从中提取数据
csv_ds = ogr.Open(csv_fn)
csv_lyr = csv_ds.GetLayer()
for csv_row in csv_lyr:
    x = csv_row.GetFieldAsDouble('location-long')
    y = csv_row.GetFieldAsDouble('location-lat')
    shp_pt = ogr.Geometry(ogr.wkbPoint)
    shp_pt.AddPoint(x, y)
    tag_id = csv_row.GetField('individual-local-identifier')
    timestamp = csv_row.GetField('timestamp')
    shp_row.SetGeometry(shp_pt)
    shp_row.SetField('tag_id', tag_id)
    shp_row.SetField('timestamp', timestamp)
    shp_lyr.CreateFeature(shp_row)

del csv_ds # 再使用完CSV数据后将其删除

# 剔除图层中GPS定位错误的点
shp_lyr.SetSpatialFilterRect(-1, -1, 1, 1)
for shp_row in shp_lyr:
    shp_lyr.DeleteFeature(shp_row.GetFID())
shp_lyr.SetSpatialFilter(None)
shp_ds.ExecuteSQL("REPACK " + shp_lyr.GetName()) # 使用REPACK永久的删除错误点
shp_ds.ExecuteSQL("RECOMPUTE EXTENT ON " + shp_lyr.GetName()) # 重新计算shapefile的空间范围

# 会直结果
# vp = VectorPlotter(False)
# vp.plot(shp_lyr, 'r.')

# 定义一个从属性列表中获得唯一值的方法
def get_unique(datasource, layer_name, field_name):
    sql = "SELECT DISTINCT {0} FROM {1}".format(field_name, layer_name)
    lyr = datasource.ExecuteSQL(sql)
    values = []
    for row in lyr:
        values.append(row.GetField(field_name))
    datasource.ReleaseResultSet(lyr)
    return values

# 已经使用ogr2oogr将数据转换为兰伯特等角圆锥投影下的数据
# 计算相邻点之间的距离
file_path = r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\Galapagos"
ds = ogr.Open(file_path, True)
lyr = ds.GetLayerByName('albatross_lambert')

if lyr.FindFieldIndex('distance', 0): # 如果距离字段已经存在，将其删除
    lyr.DeleteField(lyr.FindFieldIndex('distance', 0))
lyr.CreateField(ogr.FieldDefn('distance', ogr.OFTReal)) # 添加一个距离字段

tag_ids = get_unique(ds, 'albatross_lambert', 'tag_id') # 遍历单独的id
for tag_id in tag_ids:
    print('Processing ' + tag_id)
    lyr.SetAttributeFilter("tag_id = '{}'".format(tag_id)) # 千万别忘了{}的两侧有单引号，否则SQL语句将不成立
    row = next(lyr)
    # 保存第一次结果和点
    precious_pt = row.geometry().Clone()
    # precious_name = row.GetField('tag_id') # 因为动物GPS数据是记录了多只信天瓮的飞行数据，当载入下一只信天瓮的时间戳时必然比上一只信天瓮的初始时间小
    precious_time = time.mktime(time.strptime(row.GetField('timestamp'), '%Y-%m-%d %H:%M:%S.%f')) # 将时间的形式转换为时间戳，
                                                                     # 先将数据中的时间转换为格式化元组，再将时间元组转换为时间戳
    # print(precious_time) # 检查错误时添加的代码
    for row in lyr:
        # 确保点是按照时间顺序排列的
        current_time = time.mktime(time.strptime(row.GetField('timestamp'), '%Y-%m-%d %H:%M:%S.%f'))
        # current_name = row.GetField('tag_id')
        # print(current_time) # 检出错误时使用的代码
        if current_time < precious_time : # 只用当是同一个代号出现时间排列错误时才报错and current_name == precious_name
            raise Exception('Timestamp out of order') # 如果不是按照时间顺序排列，报错
        current_pt = row.geometry().Clone()
        distance = current_pt.Distance(precious_pt)
        row.SetField('distance', distance) # 将当前时间收集的位置与前一次时间收集的位置间的距离存储在属性表中
        lyr.SetFeature(row)
        # 保存本次结果
        precious_pt = current_pt
        # precious_name = current_name
        precious_time = current_time
del ds # 在计算完相邻点距离后可以讲数据源删除

# 在计算完相邻点的距离后可以通过SQL语句筛选出GPS定位点之间飞行的最大距离
ds = ogr.Open(file_path)
for tag_id in get_unique(ds, 'albatross_lambert', 'tag_id'):
    sql = """SELECT MAX(distance) FROM albatross_lambert
             WHERE tag_id = '{0}'""".format(tag_id)
    lyr = ds.ExecuteSQL(sql)
    for row in lyr:
        print('{0}: {1}'.format(tag_id, row.GetField(0)))
del ds

# 计算GPS采样间隔中的最大飞行速度和所耗时间，但是该最大速度不一定准确，因为鸟在GPS采样间隔期间不一定一直在飞行
date_format = '%Y-%m-%d %H:%M:%S.%f'
ds = ogr.Open(file_path)
lyr = ds.GetLayerByName('albatross_lambert')
for tag_id in get_unique(ds, 'albatross_lambert', 'tag_id'):
    max_speed = 0
    lyr.SetAttributeFilter("tag_id = '{}'".format(tag_id))  # 千万别忘了{}的两侧有单引号，否则SQL语句将不成立
    row = next(lyr)
    ts = row.GetField('timestamp')
    previous_time = time.mktime(time.strptime(ts, date_format))
    for row in lyr:
        ts = row.GetField('timestamp')
        current_time = time.mktime(time.strptime(ts, date_format))
        elapsed_time = current_time - previous_time
        hours = elapsed_time / 3600
        distance = row.GetField('distance')
        speed = distance / hours
        max_speed = max(max_speed, speed)
    print('Max speed for {0}: {1} m/h'.format(tag_id, max_speed))

# 添加底图数据
# background_shp_fn = r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\global\ne_50m_admin_0_countries.shp"
# background_shp_ds = ogr.Open(background_shp_fn)
# background_shp_layer = background_shp_ds.GetLayer()
# background_shp_layer.SetAttributeFilter("continent = 'South America'") # 将背景设定在南美洲
# vp.plot(background_shp_layer, fill=False)
# vp.draw()





