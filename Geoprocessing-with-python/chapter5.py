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
file_path = r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\global"
ds = ogr.Open(file_path)
country_lyr = ds.GetLayer('ne_50m_admin_0_countries')

# 将世界地图添加为底图
vp = VectorPlotter(False)
vp.plot(country_lyr, fill=False)

# 将德国的几何数据通过属性过滤提取出来
country_lyr.SetAttributeFilter("name = 'China'")
feature_china = country_lyr.GetNextFeature()
china_geometry = feature_china.geometry().Clone()

# 将其他国家的人口数据使用黄色的点标识
city_lyr = ds.GetLayer('ne_50m_populated_places')
vp.plot(city_lyr, 'y.')

# 通过空间过滤将中国的人口数据提取出来，用蓝色的圆表示
city_lyr.SetSpatialFilter(china_geometry)
vp.plot(city_lyr, 'ro')
vp.draw()







