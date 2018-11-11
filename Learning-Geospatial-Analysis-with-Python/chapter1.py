import turtle

# 将常用的数字放在方便记忆的变量中是普遍的做法，这个变量通常称为常量。
name = 0
points = 1
pop = 2

# 建立州列表
state = ["COLORADO", [[-109, 37], [-109, 41], [-102, 41], [-102, 37]], 5187582]

# 城市信息将已嵌套列表的形式存储
cities = []
cities.append(["DENVER", [-104.98, 39.74], 634265])
cities.append(["BOULDER", [-105.27, 40.02], 98889])
cities.append(["DURANGO", [-107.88, 37.28], 17069])

# 定义地图的尺寸
map_width = 400
map_height = 300

# 为保证地图和绘图板尺寸匹配，首先确定最大层的范围，在该示例中最大范围是州的尺寸
minx = 180
maxx = -180
miny = 90
maxy = -90
for x,y in state[points]:
    if x < minx : minx = x
    elif x > maxx : maxx = x
    if y < miny : miny = y
    elif y > maxy : maxy = y
# 计算州和绘图板之间的缩放比例
dist_x = maxx - minx
dist_y = maxy - miny
x_redio = map_width / dist_x
y_redio = map_height / dist_y

# 定义转换函数，将经纬度坐标转换为屏幕坐标
def convert(point):
    lon = point[0]
    lat = point[1]
    x = map_width - ((maxx - lon) * x_redio)
    y = map_height - ((maxy - lat) * y_redio)
    # turtle是以屏幕中心为起点的，因此需要把坐标点的位置进行适当的偏移
    x = x - (map_width/2)
    y = y - (map_height/2)
    return [x, y]

# 渲染
# 绘制州的范围
turtle.ht()
turtle.up()
first_pixel = None
for point in state[points]:
    pixel = convert(point)
    if not first_pixel:
        first_pixel = pixel
    turtle.goto(pixel)
    turtle.down()
turtle.goto(first_pixel)
turtle.up()
turtle.goto([0,0])
turtle.write(state[name], align='center', font=("Arial", 16, "bold"))
# 绘制城市
for city in cities:
    pixel = convert(city[points])
    turtle.up()
    turtle.goto(pixel)
    turtle.dot(10, 'blue')
    turtle.write(city[name] + ", Pop : " + str(city[pop]), align="left")
    turtle.up()

# 进行属性查询功能
# 人口最多的城市
biggest_city = max(cities, key=lambda city:city[pop])
# print(biggest_city)
turtle.goto(0, -200)
turtle.write("The biggest city is: " + biggest_city[name])
# 最西边的城市
western_city = min (cities, key=lambda city:city[points])
# print(western_city)
turtle.goto(0, -220)
turtle.write("The western-most city is: " + western_city[name])

# print(cities)
turtle.done()




