# 时隔两个月，我又回来学习敲代码了，好开心

import os
from osgeo import gdal

# 将3个单独的Landsat波段合成一个堆栈图像。

file_path = input('please input file path: ')
os.chdir(file_path) # 将当前目录更改到数据存放的目录
# os.chdir('{0}'.format(file_path))
# print('{0}'.format(file_path))

# 输入三个波段文件的名称，方便读写。
band1_fn = 'p047r027_7t20000730_z10_nn10.tif'
band2_fn = 'p047r027_7t20000730_z10_nn20.tif'
band3_fn = 'p047r027_7t20000730_z10_nn30.tif'

# 利用和波段1相同的属性创建三波段GeoTIFF。
in_ds = gdal.Open(band1_fn)
in_band = in_ds.GetRasterBand(1) # 波段索引从1开始，而不是0
gtiff_driver = gdal.GetDriverByName('GTiff')
out_ds = gtiff_driver.Create('nat_color.tif', in_band.XSize, in_band.YSize, 3, in_band.DataType)

# 定义输出数据集的空间位置
out_ds.SetProjection(in_ds.GetProjection())
out_ds.SetGeoTransform(in_ds.GetGeoTransform()) # geotransform，它提供原始坐标和像素大小，并伴随着旋转值，其可以使影像朝北。

# 从输入波段复制像素到输出波段3
in_data = in_band.ReadAsArray()
out_band = out_ds.GetRasterBand(3)
out_band.WriteArray(in_data)

# 从数据集而不是波段复制数据
in_ds = gdal.Open(band2_fn)
out_band = out_ds.GetRasterBand(2)
out_band.WriteArray(in_ds.ReadAsArray())

# 最简单的读取方式
out_ds.GetRasterBand(1).WriteArray(gdal.Open(band3_fn).ReadAsArray())

# 在计算统计数据之前，必须确保数据已写入磁盘，而不是只缓存在内存中。
out_ds.FlushCache()
# 为每个波段计算统计值
for i in range(1, 4):
    out_ds.GetRasterBand(i).ComputeStatistics(False) # 传递False给这个函数，告诉它需要计算的是实际统计数据，而不是估计值

# 创建概视金字塔图层
out_ds.BuildOverviews('average', [2, 4, 8, 16, 32])

del out_ds









