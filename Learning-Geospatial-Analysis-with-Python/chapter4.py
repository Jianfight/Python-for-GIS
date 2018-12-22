import math

# region 距离公式
# # 勾股定理(适用于平面地球模型)
# def gouGuDingLi(x1, y1, x2, y2):
#     x_dist = x2 - x1
#     y_dist = y2 - y1
#     distance = math.sqrt(x_dist**2 + y_dist**2) # python中使用**表示平方
#     return distance
#
# # 使用勾股定理进行十进制度距离量测
# def decimalDegreeCompute(x1, y1, x2, y2):
#     radius = 6371251.46 # 地球的平均半径
#
#     x_dist = math.radians(x1 - x2) # math库中的radians为将角度转换为弧度
#     y_dist = math.radians(y1 - y2)
#     dist_rad = math.sqrt(x_dist**2 + y_dist**2)
#     return dist_rad * radius
#
# # 使用半正矢量公式进行十进制度数距离量测（适用于球体地球模型）
# def banZhengShi(x1, y1, x2, y2):
#     radius = 6371 # 单位为千米，半径可以通过函数的参数引入
#     x_dist = math.radians(x1 - x2)
#     y_dist = math.radians(y1 - y2)
#     y1_rad = math.radians(y1)
#     y2_rad = math.radians(y2)
#     a = math.sin(y_dist/2)**2 + math.sin(x_dist/2)**2 * math.cos(y1_rad) * math.cos(y2_rad)
#     c = 2 * math.asin(math.sqrt(a))
#     return c * radius
#
# # Vincenty 公式（适用于椭球体地球模型）比如计算飞机在两地之间的飞行距离。
# def vincenty(x1, y1, x2, y2):
#     # 设置参考椭球体参数，以NAD83为例，可以将椭球参数通过函数的参数引入
#     a = 6378137 # 长半轴
#     f = 1/298.257222101 # 逆扁平率
#     b = abs((f*a) - a) # 短半轴
#
#     distance = None
#
#     # 进入Vincenty公式的编写
#     L = math.radians(x2 - x1)
#     U1 = math.atan((1-f) * math.tan(math.radians(y1)))
#     U2 = math.atan((1-f) * math.tan(math.radians(y2)))
#     sinU1 = math.sin(U1)
#     cosU1 = math.cos(U1)
#     sinU2 = math.sin(U2)
#     cosU2 = math.cos(U2)
#     lam = L
#
#     for i in range(100):
#         sinLam = math.sin(lam)
#         cosLam = math.cos(lam)
#         sinSigma = math.sqrt((cosU2*sinLam)**2 + (cosU1*sinU2-sinU1*cosU2*cosLam)**2)
#
#         # 判断两个点是否重合
#         if sinSigma == 0:
#             distance = 0
#             return
#
#         cosSigma = sinU1*sinU2 + cosU1*cosU2*cosLam
#         sigma = math.atan2(sinSigma, cosSigma)
#         sinAlpha = cosU1 * cosU2 * sinLam / sinSigma
#         cosSqAlpha = 1 - sinAlpha**2
#         cos2SinmaM = cosSigma - 2*sinU1*sinU2/cosSqAlpha
#
#         if math.isnan(cos2SinmaM):
#             cos2SinmaM = 0 # 表示赤道线
#         C = f/16*cosSqAlpha*(4+f*(4-3*cosSqAlpha))
#         LP = lam
#         lam = L + (1-C) * f * sinAlpha * (sigma + C*sinSigma*(cos2SinmaM+C*cosSigma * (-1+2*cos2SinmaM*cos2SinmaM)))
#         if not abs(lam - LP) > 1e-12:
#             break
#     uSq = cosSqAlpha * (a**2 - b**2) / b**2
#     A = 1 + uSq/16384*(4096+uSq*(-768+uSq*(320-175*uSq)))
#     B = uSq/1024 * (256+uSq*(-128+uSq*(74-47*uSq)))
#     deltaSigma = B*sinSigma*(cos2SinmaM+B/4 * (cosSigma*(-1+2*cos2SinmaM*cos2SinmaM) -
#                                                B/6*cos2SinmaM*(-3+4*sinSigma*sinSigma) * (-3+4*cos2SinmaM*cos2SinmaM)))
#     s = b*A*(sigma-deltaSigma)
#     distance = s
#     return distance
#
# # 测试数据
# list1 = [456456.23, 1279721.064, 576628.34, 1071740.33]
# distance = gouGuDingLi(*list1)
# print('将坐标投影后，使用勾股定理计算出的距离为：{}(m)'.format(distance))
#
# list2 = [-90.21, 32.31, -88.95, 30.43]
# dist_rad = decimalDegreeCompute(*list2)
# print('使用勾股定理量测出的十进制度的距离为（这种方法本身就是错的，只是做个对比）：{}(m)'.format(dist_rad))
#
# list3 = [-90.212452861859035, 32.316272202663704, -88.952170968942525, 30.438559624660321]
# dist_banZhengShi = banZhengShi(*list3)
# print('使用半正矢量公式计算十进制度的距离为：{}(km)'.format(dist_banZhengShi))
#
# list4 = [-90.212452861859035, 32.316272202663704, -88.952170968942525, 30.438559624660321]
# dist_vincenty = vincenty(*list4)
# print('使用Vincenty公式计算得到的十进制度的距离为：{}(m)'.format(dist_vincenty))
# endregion

# region 已知两个地点的经纬度计算其方位
# def azmuthCalculate(lon1, lat1, lon2, lat2):
#     lon1 = math.radians(lon1)
#     lat1 = math.radians(lat1)
#     lon2 = math.radians(lon2)
#     lat2 = math.radians(lat2)
#
#     angle = math.atan2(math.cos(lat1)*math.sin(lat2) - math.sin(lat1)*math.cos(lat2)*math.cos(lon2-lon1),
#                        math.sin(lon2-lon1)*math.cos(lat2))
#     # print(math.degrees(angle))
#     bearing = (math.degrees(angle) + 360) % 360      # 对应360取余数
#     return bearing
#
# # 测试数据
# list1 = [-90.21, 32.31, -88.95, 30.43]
# text = azmuthCalculate(*list1)
# print(text)
# endregion

# region shape点文件重投影
#
# from osgeo import ogr
# from osgeo import osr
# import os
# import shutil
#
# def reprojectionOfShape(srcName, tgtName, EPSGCode): # srcName代表原shape文件的名称，tgtName代表重投影后文件的名称，
#                                                      # EPSGCode代表重投影坐标系的EPSG码
#     tgt_spatRef = osr.SpatialReference()
#     tgt_spatRef.ImportFromEPSG(EPSGCode)
#     driver = ogr.GetDriverByName("ESRI Shapefile")
#     src = driver.Open(srcName, 0)
#     srcLyr = src.GetLayer()
#     src_spatRef = srcLyr.GetSpatialRef()
#
#     # 如果对应的转换为新文件已经存在，将其删除
#     if os.path.exists(tgtName):
#         driver.DeleteDataSource(tgtName)
#
#     tgt = driver.CreateDataSource(tgtName)
#     lyrName = os.path.splitext(tgtName)[0] # 使用这种方法提取文件的名称（不包含后缀名）
#
#     # 使用wkb格式声明几何图形
#     tgtlyr = tgt.CreateLayer(lyrName, geom_type=ogr.wkbPoint)
#     featDef = srcLyr.GetLayerDefn()
#     trans = osr.CoordinateTransformation(src_spatRef,tgt_spatRef)
#     # 开始转移要素
#     srcFeat = srcLyr.GetNextFeature()
#     while srcFeat:
#         geom = srcFeat.GetGeometryRef()
#         geom.Transform(trans)
#         feature = ogr.Feature(featDef) # 先将要素的几何和基本定义设置好，再在图层中创建要素
#         feature.SetGeometry(geom)
#         tgtlyr.CreateFeature(feature)
#         feature.Destroy()
#         srcFeat.Destroy()
#         srcFeat = srcLyr.GetNextFeature()
#     src.Destroy()
#     tgt.Destroy()
#     # 为了导出投影文件将几何图形转换为Esri的WKT格式
#     tgt_spatRef.MorphFromESRI()
#     prj = open(lyrName + ".prj", "w")
#     prj.write(tgt_spatRef.ExportToWkt())
#     prj.close()
#     srcDbf = os.path.splitext(srcName)[0] + ".dbf"
#     tgtDbf = lyrName + ".dbf"
#     shutil.copyfile(srcDbf, tgtDbf)
#
# # 测试
# srcName = "NYC_MUSEUMS_LAMBERT.shp"
# tgtName = "NYC_MUSEUMS_GEO.shp"
# EPSGCode = 4326                    # EPSG:4326代表WGS84椭球
# reprojectionOfShape(srcName, tgtName, EPSGCode)
# endregion


import shapefile

r = shapefile.Reader("MSCities_Geo_Pts") # 处理数据时，至少包括.shp和.dbf等多种文件，有时不包含文件扩展名的基础文件才能满足实际的需求
                                         # 如果基础文件名中包含句点，那么最好在调用时添加相应的文件拓展名。
# shape文件访问
print(r)
print(r.bbox) # bbox属性中存储着数据的边框信息，其包含最小值x,y和最大值x,y的list对象。
print(r.shapeType) # 几何类型通常是一个和Shapefile文件匹配的数字编号：1代表点，3代表线，5代表多边形。
print(r.numRecords) # 由numRecords属性可以知道该文件中包含了298条记录。

# shape属性读取
# print(r.fields) # 每个字段项都是包含四个元素：Field name、Field type、Field length、Decimal length。
# print('------------------------------------------------------------------------------')
# print([item[0] for item in r.fields[1:]])

print('使用索引来访问单个数据记录')
print(r.record(2)[:])# [:]不加这个切片设置，显示Record #2，不知道是为啥.......

print('使用字段名来访问数据记录')
fieldNames = [item[0] for item in r.fields[1:]] # 因为.fields返回的值的每一项都是一个列表，
                                                # 列表中的第一个元素才代表字段名称，故使用item[0],shapefile文件的第一个字段
                                                # 描述信息是隐藏的，因为它是作为dfb文件格式规范的一部分存在的。
print(fieldNames)
cityIndex = fieldNames.index('NAME10') # 返回字段名称在fieldNames中对应的索引
print(cityIndex)
print(r.record(2)[cityIndex])
print('----------------------------------------------------------------------------------')
# 使用python自带的zip函数将字段名和数据记录关联起来，该方法是通过两个或者多个list合并为一个元组List实现的。
rec = r.record(2)
zipRec = zip(fieldNames, rec)
# print(zipRec)
print(list(zipRec)) # list函数将zip函数组合成的形式以列表的形式展现出来，如果直接使用print函数，打印出来的是存储位置
# print(zipRec)
for z in zipRec:
    # print('0000000')
    if z[0] == 'NAME10':
        print(z[1])   # 问题：当不把print(list(zipRec))这行注释掉的时候，无法进入循环，这是为什么呢？
print('----------------------------------------------------------------------------------')

for record in enumerate(r.records()[:3]):       # 使用records方法可以遍历dbf文件中的所有记录<但是在此处仅仅取前三条记录>
                                                # 使用枚举函数<enumerate>创建记录列表，会自动为其创建一组编号，方便访问文件。
    print(record[0]+1, ':' , record[1][:]) #
print('----------------------------------------------------------------------------------')
counter = 0
for rec_1 in r.iterRecords(): # records方法会一次性将所有记录读入内存中，数据量很大时会使计算机难于管理，
                              # iterRecords方法不会一次性读取所有数据，而是根据需要读取一定量的数据
    counter += 1
print(counter)












