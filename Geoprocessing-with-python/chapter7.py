import ogr
from ospybook.vectorplotter import VectorPlotter

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










