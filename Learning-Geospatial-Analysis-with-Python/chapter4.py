import math

# 勾股定理(适用于平面地球模型)
def gouGuDingLi(x1, y1, x2, y2):
    x_dist = x2 - x1
    y_dist = y2 - y1
    distance = math.sqrt(x_dist**2 + y_dist**2) # python中使用**表示平方
    return distance

# 使用勾股定理进行十进制度距离量测
def decimalDegreeCompute(x1, y1, x2, y2):
    radius = 6371251.46 # 地球的平均半径

    x_dist = math.radians(x1 - x2) # math库中的radians为将角度转换为弧度
    y_dist = math.radians(y1 - y2)
    dist_rad = math.sqrt(x_dist**2 + y_dist**2)
    return dist_rad * radius

# 使用半正矢量公式进行十进制度数距离量测（适用于球体地球模型）
def banZhengShi(x1, y1, x2, y2):
    radius = 6371 # 单位为千米，半径可以通过函数的参数引入
    x_dist = math.radians(x1 - x2)
    y_dist = math.radians(y1 - y2)
    y1_rad = math.radians(y1)
    y2_rad = math.radians(y2)
    a = math.sin(y_dist/2)**2 + math.sin(x_dist/2)**2 * math.cos(y1_rad) * math.cos(y2_rad)
    c = 2 * math.asin(math.sqrt(a))
    return c * radius

# Vincenty 公式（适用于椭球体地球模型）比如计算飞机在两地之间的飞行距离。
def vincenty(x1, y1, x2, y2):
    # 设置参考椭球体参数，以NAD83为例，可以将椭球参数通过函数的参数引入
    a = 6378137 # 长半轴
    f = 1/298.257222101 # 逆扁平率
    b = abs((f*a) - a) # 短半轴

    distance = None

    # 进入Vincenty公式的编写
    L = math.radians(x2 - x1)
    U1 = math.atan((1-f) * math.tan(math.radians(y1)))
    U2 = math.atan((1-f) * math.tan(math.radians(y2)))
    sinU1 = math.sin(U1)
    cosU1 = math.cos(U1)
    sinU2 = math.sin(U2)
    cosU2 = math.cos(U2)
    lam = L

    for i in range(100):
        sinLam = math.sin(lam)
        cosLam = math.cos(lam)
        sinSigma = math.sqrt((cosU2*sinLam)**2 + (cosU1*sinU2-sinU1*cosU2*cosLam)**2)

        # 判断两个点是否重合
        if sinSigma == 0:
            distance = 0
            return

        cosSigma = sinU1*sinU2 + cosU1*cosU2*cosLam
        sigma = math.atan2(sinSigma, cosSigma)
        sinAlpha = cosU1 * cosU2 * sinLam / sinSigma
        cosSqAlpha = 1 - sinAlpha**2
        cos2SinmaM = cosSigma - 2*sinU1*sinU2/cosSqAlpha

        if math.isnan(cos2SinmaM):
            cos2SinmaM = 0 # 表示赤道线
        C = f/16*cosSqAlpha*(4+f*(4-3*cosSqAlpha))
        LP = lam
        lam = L + (1-C) * f * sinAlpha * (sigma + C*sinSigma*(cos2SinmaM+C*cosSigma * (-1+2*cos2SinmaM*cos2SinmaM)))
        if not abs(lam - LP) > 1e-12:
            break
    uSq = cosSqAlpha * (a**2 - b**2) / b**2
    A = 1 + uSq/16384*(4096+uSq*(-768+uSq*(320-175*uSq)))
    B = uSq/1024 * (256+uSq*(-128+uSq*(74-47*uSq)))
    deltaSigma = B*sinSigma*(cos2SinmaM+B/4 * (cosSigma*(-1+2*cos2SinmaM*cos2SinmaM) -
                                               B/6*cos2SinmaM*(-3+4*sinSigma*sinSigma) * (-3+4*cos2SinmaM*cos2SinmaM)))
    s = b*A*(sigma-deltaSigma)
    distance = s
    return distance

# 测试数据
list1 = [456456.23, 1279721.064, 576628.34, 1071740.33]
distance = gouGuDingLi(*list1)
print('将坐标投影后，使用勾股定理计算出的距离为：{}(m)'.format(distance))

list2 = [-90.21, 32.31, -88.95, 30.43]
dist_rad = decimalDegreeCompute(*list2)
print('使用勾股定理量测出的十进制度的距离为（这种方法本身就是错的，只是做个对比）：{}(m)'.format(dist_rad))

list3 = [-90.212452861859035, 32.316272202663704, -88.952170968942525, 30.438559624660321]
dist_banZhengShi = banZhengShi(*list3)
print('使用半正矢量公式计算十进制度的距离为：{}(km)'.format(dist_banZhengShi))

list4 = [-90.212452861859035, 32.316272202663704, -88.952170968942525, 30.438559624660321]
dist_vincenty = vincenty(*list4)
print('使用Vincenty公式计算得到的十进制度的距离为：{}(m)'.format(dist_vincenty))