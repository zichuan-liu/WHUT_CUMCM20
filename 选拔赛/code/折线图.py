from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']

dict = {"1":[3,2], "2":[1,5], "3":[5,4],"4":[4,7], "5":[0,8],"6":[3,11],"7":[7,9],
        "8":[9,6],"9":[10,2], "10":[14,0],"11":[2,16], "12":[6,18],"13":[11,17],"14":[15,12],
        "15":[19,9],"16":[22,5], "17":[21,0],"18":[27,9], "19":[15,19],"20":[10,10],}
x_axis_data = []
y_axis_data = []
road = [20,8,3,4,5,2,1,9,10,17,16,18,15,14,19,13,12,11,6,7,20]
x_tem = []
y_tem = []
for i in range(len(road)):
    x = str(road[i])
    print(dict[x])
    x_axis_data.append(dict[x][0])
    y_axis_data.append(dict[x][1])

    try:
        x_tem.append(dict[str(road[i+1])][0])
        y_tem.append(dict[str(road[i])][1])
    except:
        pass

x_ = []
y_ = []

for i in range(len(x_tem)):
    x_.append(x_axis_data[i])
    y_.append(y_axis_data[i])
    x_.append(x_tem[i])
    y_.append(y_tem[i])

x_.append(x_axis_data[i+1])
y_.append(y_axis_data[i+1])

plt.plot(x_, y_, 'ro-', color='#4169E1', alpha=0.8, label='路径')

for x, y in zip(x_axis_data, y_axis_data):
    plt.text(x, y+0.3, '({},{})'.format(x,y), ha='center', va='bottom', fontsize=10.5)

# plt.legend(loc="road")
plt.xlabel('X轴/km')
plt.ylabel('Y轴/km')

# plt.show()
plt.savefig('demo.jpg')  # 保存该图片
