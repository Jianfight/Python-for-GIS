from osgeo import ogr, osr, gdal
import ospybook
from ospybook.vectorplotter import VectorPlotter
import pyproj
vp = VectorPlotter(False) # 用于显示几何成果

# 创建控件参考对象
# sr = osr.SpatialReference() # 创建一个空的空间参考对象
# sr.ImportFromEPSG(26912) # 使用EPSG码来定义空间参考系统，26912代表NAD83 UTM 12N
# # 使用proj4来定义空间参考系统
# #sr.ImportFromProj4('''+proj=utm +zone=12 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ''')
# print(sr.GetAttrValue('PROJCS'))

# 自定义空间坐标系
# sr = osr.SpatialReference()
# sr.SetProjCS('USER Albers') # 定义投影的名称
# sr.SetWellKnownGeogCS('NAD83') # 设定基准
# sr.SetACEA(29.5, 45.5, 23, -96, 0, 0) # 设定参数：标准平行线1， 标准平行线2， 中央纬线， 中央经线， 东移假定值， 北移假定值
# sr.Fixup() # 该函数用于为缺少的参数添加默认值，并重新排序项目，以使它们与标准匹配
# print(sr.Validate()) # 该函数用于确保没有缺少任何东西，返回一个0表示一切正常

# 几何对象重投影
# file_path = r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\global\ne_110m_land_1p.shp"
# world = ospybook.get_shp_geom(file_path) # 该方法可以从shape file中获得第一个几何对象
# tower = ogr.Geometry(wkt='POINT (2.294694 48.858093)') # 获取艾弗尔铁塔的位置
# # 使用AssignSpatialReference函数为几何对象分配SRS，但是它并不会将数据转换到该坐标系下，仅仅是提供空间信息
# tower.AssignSpatialReference(osr.SpatialReference(osr.SRS_WKT_WGS84)) # 因为WGS84坐标系很常用，所以在OSR模块中有一个常量，
#                                                                       # 用于表示该地理坐标系统的WKT。
# gdal.SetConfigOption('OGR_ENABLE_PARTIAL_REPROJECTION', 'TRUE') # 该方式可以修复，在进行web墨卡托投影时，南北极投影出错的问题
# web_mercator_sr = osr.SpatialReference() # 第一步还是创建空的空间参考对象
# web_mercator_sr.ImportFromEPSG(3857)
# world.TransformTo(web_mercator_sr) # 将几何对象重投影到web墨卡托
# tower.TransformTo(web_mercator_sr) # 将艾弗尔铁塔的位置重投影到web墨卡托
# print(tower)
# vp.plot(world)
# vp.draw()
#
# # 使用源和目标空间参考来创建CoordinateTransformation对象，从而进行投影转换
# peters_sr = osr.SpatialReference()
# peters_sr.ImportFromProj4("""+proj=cea +lon_0=0 +x_0=0 +y_0=0
#                              +lat_ts=45 +ellps=WGS84 +datum=WGS84
#                              +units=m +no_defs""") # 添加高尔-彼得斯（Gall-Peters）投影的proj4信息
# ct = osr.CoordinateTransformation(web_mercator_sr, peters_sr) # 使用源和目标空间参考来创建转换参数
# world.Transform(ct)
# vp.plot(world)
# vp.draw()

# 重投影整个图层
# 创建输出图层的空间参考
# sr = osr.SpatialReference()
# sr.ImportFromProj4("""+proj=aea +lat_1=29.5 +lat_2=45.5 +lat_0=23
#                        +lon_0=-96 +x_0=0 +y_0=0 +ellps=GRS80
#                        +datum=NAD83 +units=m +no_defs""")
# # print(sr.GetAttrValue('PROJCS'))
#
# file_path = r"C:\Users\think\Desktop\python\python-for-GIS-DATA\osgeopy-data\osgeopy-data\US"
# ds = ogr.Open(file_path, True)
# in_lyr = ds.GetLayer('us_volcanos')
#
# if ds.GetLayer('us_volcanos_aea'): # 如果输出图层已经存在，先将其删除
#     ds.DeleteLayer('us_volcanos_aea')
# out_lyr = ds.CreateLayer('us_volcanos_aea', sr, ogr.wkbPoint)
# out_lyr.CreateFields(in_lyr.schema) # 将输入图层的字段复制到输出图层中
# out_feat = ogr.Feature(out_lyr.GetLayerDefn())
#
# for in_feat in in_lyr:
#     geom = in_feat.geometry().Clone()
#     geom.TransformTo(sr)
#     out_feat.SetGeometry(geom)
#     for i in range(in_feat.GetFieldCount()):
#         out_feat.SetField(i, in_feat.GetField(i))
#     out_lyr.CreateFeature(out_feat)


# 使用pyproj库进行空间转换
# 投影到UTM坐标系下
utm_proj = pyproj.Proj(init='epsg:32631')
x, y = utm_proj(2.294694, 48.858093)
print(x, y)
# 将UTM坐标系下的坐标转换为地理坐标,将inverse参数设置为True
x1, y1 = utm_proj(x, y, inverse=True)
print(x1, y1)

# 在两个基准之间进行转换
wgs84 = pyproj.Proj('+proj=utm +zone=18 +datum=WGS84')
nad27 = pyproj.Proj('+proj=utm +zone=18 +datum=NAD27')
x, y = pyproj.transform(wgs84, nad27, 580744.32, 4504695.26) # 坐标数据为在WGS84下的数据
print(x, y) # 从出输出中可以看出相同的投影方式但是使用不同的基准，坐标值差值很大

# 计算大圆距离（大地线）
la_lat, la_lon = 34.0500, -118.2500
berlin_lat, berlin_lon = 52.5167, 13.3833
geod = pyproj.Geod(ellps='WGS84')
forward, back, dist = geod.inv(la_lon, la_lat, berlin_lon, berlin_lat) # 该函数可以计算出前后方位角和大地线
print("forward: {}\nback: {}\ndist: {}".format(forward, back, dist))
# 通过一个位置的经纬度、方位角和距离计算目标点的经纬度
x, y, bearing = geod.fwd(berlin_lon, berlin_lat, back, dist)
print('{}, {}\n{}'.format(x, y, bearing))

# 可以通过传递起始坐标、结束坐标和所需点的数量，来获得沿着大圆线的等间距坐标列表
coords = geod.npts(la_lon, la_lat, berlin_lon, berlin_lat, 100)
for i in range(3):
    print(coords[i])








