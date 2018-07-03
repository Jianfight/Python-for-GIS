import ogr
import ospybook
from ospybook.vectorplotter import VectorPlotter

# 使用属性过滤条件来过滤数据
# region

# file_path = r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\global"
# ds = ogr.Open(file_path)
# lyr = ds.GetLayer('ne_50m_admin_0_countries')
# print('feature count for layer:{0}'.format(lyr.GetFeatureCount()))
# vp = VectorPlotter(False)
# vp.plot(lyr, fill=False)
#
# # 筛选亚洲的国家
# lyr.SetAttributeFilter("continent = 'Asia'") # 使用“号括住查询语句，使用‘号括住字符串。
# print('feature count for layer of Asia: {0}'.format(lyr.GetFeatureCount()))
# vp.plot(lyr, 'b')
#
# # 筛选南美洲的国家(如果设置了另一个属性过滤条件，它并不是创建当前图层要素的一个子集，而是将新的过滤条件应用于整个图层)
# lyr.SetAttributeFilter("continent = 'South America'")
# print('feature count for layer of South America: {0}'.format(lyr.GetFeatureCount()))
# vp.plot(lyr, 'y')

# vp.draw()

# endregion


# 使用空间过滤条件来过滤数据
# region

# file_path = r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\global"
# ds = ogr.Open(file_path)
# country_lyr = ds.GetLayer('ne_50m_admin_0_countries')
#
# # 将世界地图添加为底图
# vp = VectorPlotter(False)
# vp.plot(country_lyr, fill=False)
#
# # 将中国的几何数据通过属性过滤提取出来
# country_lyr.SetAttributeFilter("name = 'China'")
# feature_china = country_lyr.GetNextFeature() # 属性过滤条件有且只会返回一个要素，因此使用GetNextFeature函数会获得过滤结果中的唯一一个要素。
# china_geometry = feature_china.geometry().Clone()
#
# # 将其他国家的人口数据使用黄色的点标识
# city_lyr = ds.GetLayer('ne_50m_populated_places')
# vp.plot(city_lyr, 'y.')
#
# # 通过空间过滤将中国的人口数据提取出来，用蓝色的圆表示
# city_lyr.SetSpatialFilter(china_geometry)
# vp.plot(city_lyr, 'r.')
# # 将中国人口超过100万的城市筛选出来使用红色正方形表示
# city_lyr.SetAttributeFilter("pop_min > 1000000")
# vp.plot(city_lyr, 'rs')
# # 将世界上人口大于100万的城市筛选出来用紫色三角形表示
# city_lyr.SetSpatialFilter(None)
# vp.plot(city_lyr, 'm^', markersize=8)
# vp.draw()
#
# # 使用坐标的最大和最小值来确定空间筛选的范围SetSpatialFilterRect(minx, miny, maxx, maxy)
# vp.clear()
# country_lyr.SetAttributeFilter(None)
# vp.plot(country_lyr, fill=False)
# country_lyr.SetSpatialFilterRect(100, -50, 160, 10)
# vp.plot(country_lyr, 'y')
# vp.draw()

# endregion


# 使用ExecuteSQL()函数作用于数据源，过滤数据。
# region

# # 当数据源中并不包含自身的SQL引擎时，默认使用OGR SQL标准
# file_path = r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\global"
# ds = ogr.Open(file_path)
# # 在写SQL语句时一定要将文件名称用双引号括起来
# sql = '''SELECT ogr_geom_area as area, name, pop_est
#          FROM "ne_50m_admin_0_countries" ORDER BY "POP_EST" DESC'''
# lyr = ds.ExecuteSQL(sql)
# ospybook.print_attributes(lyr, 3)
#
# # 当数据源中包含自身的SQL引擎时,会使用原生的SQL版本。
# file_path_1 = r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\global\natural_earth_50m.sqlite"
# ds = ogr.Open(file_path_1)
# sql = '''SELECT geometry, area(geometry) AS area, name, pop_est
#          FROM countries ORDER BY pop_est DESC LIMIT 3'''
# lyr = ds.ExecuteSQL(sql)
# ospybook.print_attributes(lyr)

# endregion


# 使用ExecuteSQL()函数连接多个图层的属性。
# region

# ds = ogr.Open(file_path)
# sql = '''SELECT pp.name AS city, pp.pop_min AS city_pop,
#                 c.name AS country, c.pop_est AS country_pop
#         FROM ne_50m_populated_places pp
#         LEFT JOIN ne_50m_admin_0_countries c
#         ON pp.adm0_a3 = c.adm0_a3
#         WHERE pp.adm0cap = 1'''
# lyr = ds.ExecuteSQL(sql)
# ospybook.print_attributes(lyr, 3, geom=False) # 由于OGR SQL标准会自动返回几何类型，在这里应该是返回主表（城市图层）中的几何类型
#
# # 使用SQLite标准,进行两个表的连接
# ds = ogr.Open(file_path)
# sql = '''SELECT pp.name AS city, pp.pop_min AS city_pop,
#                 c.name AS country, c.pop_est AS country_pop
#         FROM ne_50m_populated_places pp
#         LEFT JOIN ne_50m_admin_0_countries c
#         ON pp.adm0_a3 = c.adm0_a3
#         WHERE pp.adm0cap = 1 AND c.continent = "South America"''' # OGR标准中的where语句不支持使用连接表的字段
# lyr = ds.ExecuteSQL(sql, dialect='SQLite') # dialect参数更改SQL的标准
# ospybook.print_attributes(lyr, 3)

# endregion


# 在3.3中使用循环和判断筛选要素，再学习完新的方法后可以使用新的办法来过滤数据
# 使用属性过滤
def attribute_filter(data_source, layer, condition, new_name_of_layer):
    layer.SetAttributeFilter(condition)
    out_layer = data_source.CopyLayer(layer, new_name_of_layer)
    return out_layer
# 使用ExecuteSQL函数进行过滤
def executeSQL(data_source, new_name_of_layer):
    sql = '''SELECT NAME, ADMONAME FROM ne_50m_populated_places
             WHERE FEATURECLA = "Admin-0 capital"'''
    in_lyr = data_source.ExecuteSQL(sql)
    out_lyr = data_source.CopyLayer(in_lyr, new_name_of_layer)
    return out_lyr


