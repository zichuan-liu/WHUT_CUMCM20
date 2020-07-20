from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
# import matplotlib.pyplot as plt
import numpy
import matplotlib.colors as colors
import matplotlib.cm as cmx

dicts = {"1":[3,2], "2":[1,5], "3":[5,4],"4":[4,7], "5":[0,8],"6":[3,11],"7":[7,9],
        "8":[9,6],"9":[10,2], "10":[14,0],"11":[2,16], "12":[6,18],"13":[11,17],"14":[15,12],
        "15":[19,9],"16":[22,5], "17":[21,0],"18":[27,9], "19":[15,19],"0":[10,10],}
x_axis_data = []
y_axis_data = []

cars = [12	,11	,0	,15,	16,	0	,5	,2,	0,	14,	19,	13,	0,	4	,6,	0,	18,	0	,17,	10,0,	7,	0,	9,	1,0]

#0,	3,	8,
c_ = []
x = [0]
for j in range(len(cars)):
    x.append(cars[j])
    if cars[j]==0:
        c_.append(x)
        x = [0]

print(c_)
cmap = plt.cm.jet
cNorm = colors.Normalize(vmin=0, vmax=len(c_))
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cmap)
for fff in range(len(c_)):
    ###########
    x_axis_data = []
    y_axis_data = []
    road = c_[fff]
    x_tem = []
    y_tem = []
    for i in range(len(road)):
        x = str(road[i])
        x_axis_data.append(dicts[x][0])
        y_axis_data.append(dicts[x][1])

        try:
            x_tem.append(dicts[str(road[i + 1])][0])
            y_tem.append(dicts[str(road[i])][1])
        except:
            pass

    x_ = []
    y_ = []

    for i in range(len(x_tem)):
        x_.append(x_axis_data[i])
        y_.append(y_axis_data[i])
        x_.append(x_tem[i])
        y_.append(y_tem[i])


    colorVal = scalarMap.to_rgba(fff)
    x_.append(x_axis_data[i + 1])
    y_.append(y_axis_data[i + 1])
    plt.plot(x_, y_, 'ro-', alpha=0.8)
    for i in range(0,len(x_)-1):
        plt.arrow(x_[i], y_[i], x_[i+1] - x_[i], y_[i+1] - y_[i],
                  length_includes_head=True, head_width=0.3, lw=2,)

    for x, y in zip(x_axis_data, y_axis_data):
        plt.text(x, y + 0.3, '({},{})'.format(x, y),)

    plt.xlabel('X轴/km')
    plt.ylabel('Y轴/km')


cars = [3,	8,0]

#0,	3,	8,
c_ = []
x = [0]
for j in range(len(cars)):
    x.append(cars[j])
    if cars[j]==0:
        c_.append(x)
        x = [0]

print(c_)
cmap = plt.cm.jet
cNorm = colors.Normalize(vmin=0, vmax=len(c_))
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cmap)
for fff in range(len(c_)):
    ###########
    x_axis_data = []
    y_axis_data = []
    road = c_[fff]
    x_tem = []
    y_tem = []
    for i in range(len(road)):
        x = str(road[i])
        x_axis_data.append(dicts[x][0])
        y_axis_data.append(dicts[x][1])

        try:
            x_tem.append(dicts[str(road[i + 1])][0])
            y_tem.append(dicts[str(road[i])][1])
        except:
            pass

    x_ = []
    y_ = []

    for i in range(len(x_tem)):
        x_.append(x_axis_data[i])
        y_.append(y_axis_data[i])
        x_.append(x_tem[i])
        y_.append(y_tem[i])


    colorVal = scalarMap.to_rgba(fff)
    x_.append(x_axis_data[i + 1])
    y_.append(y_axis_data[i + 1])
    plt.plot(x_, y_, 'o-', alpha=0.8)
    # for i in range(0,len(x_)-1):
    #     plt.arrow(x_[i], y_[i], x_[i+1] - x_[i], y_[i+1] - y_[i],
    #               length_includes_head=True, head_width=0.3, lw=2,)

    for x, y in zip(x_axis_data, y_axis_data):
        plt.text(x, y + 0.3, '({},{})'.format(x, y),)

    plt.xlabel('X轴/km')
    plt.ylabel('Y轴/km')

plt.show()
# plt.savefig('demo.jpg')  # 保存该图片