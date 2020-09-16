import numpy as np
from math import *
import random
import matplotlib.pyplot as plt
import numpy.random as rnd
from PIL import Image
from matplotlib.patches import Ellipse
plt.rcParams['font.sans-serif'] = ['SimHei']

a = 30
b = 20
c1 = ("LJ1",a,b)
a2 = 25
b2 = 20
c2 = ("LJ2",a2,b2)
a3 = 39
b3 = 39
c3 = ("LJ3",a3,b3)
a4 = 29
b4 = 29
c4 = ("LJ4",a4,b4)
a5 = 27.5
b5 = 27.5
c5 = ("LJ5",a5,b5)
a6 = 26
b6 = 26
c6 = ("LJ6",a6,b6)
cs = [c1,c2,c3,c4,c5,c6]

def fun(c1,c2):
    infor = {}
    c_1,a,b = c1
    c_2,a2,b2 = c2
    if b<b2 or a<a2:
        return

    infor['c1'] = c_1
    infor['c2'] = c_2
    print(c_1,c_2,a,b,a2,b2)
    len = 6060#6060
    wi = 2160#2160

    def get_ellipse(e_x, e_y, a, b, e_angle):
        angles_circle = np.arange(0, 2 * np.pi, 0.01)
        x = []
        y = []
        for angles in angles_circle:
            or_x = a * cos(angles)
            or_y = b * sin(angles)
            length_or = sqrt(or_x * or_x + or_y * or_y)
            or_theta = atan2(or_y, or_x)
            new_theta = or_theta + e_angle/180*pi
            new_x = e_x + length_or * cos(new_theta)
            new_y = e_y + length_or * sin(new_theta)
            x.append(int(new_x))
            y.append(int(new_y))
        return np.array(x), np.array(y)


    def init():
        map = np.zeros((wi, len))
        for j in range(int(len/2/a)):
            xs, ys = get_ellipse(a+j*2*a, b, a, b, 0)
            for i, x in enumerate(xs):
                map[wi-ys[i]-1][x-1] = 255

        xs, ys = get_ellipse(2*a, 3*b, a2, b2, 0)
        while True:
            flag=0
            for i in range(xs.shape[0]):
                if map[wi-ys[i]][xs[i]]==255:
                    flag=1
                    break
            if flag==1:
                break
            ys = ys-1
        # print(min(ys))
        for i, x in enumerate(xs):
            map[wi - ys[i] - 1][x] = 255

        dleta = b*2-min(ys)
        return map, dleta

    map, detal=init()
    # print("detal:", detal)
    detal = detal+1
    # new_im = Image.fromarray(map)
    # new_im.show()
    j=0
    h = wi
    num1 = 0
    num2 = 0
    ells = []
    high = b
    flag = 0
    # while j != int(h/(2*b))+1:
    while high<=wi:
        for i in range(int(len/(2*a))):
            if j%2==0:
                num1 = num1 + 1
                flag=b2
                e = Ellipse(xy=[i*2*a+a,high], width=a*2, height=b*2, angle=0)
                e.set_facecolor([0.56880993, 0.66417204, 0.79058739])
            else:
                num2 = num2 + 1
                flag=b
                e = Ellipse(xy=[i*2*a+2*a,high], width=a2*2, height=b2*2, angle=0)
                e.set_facecolor([0.81830406, 0.84668072, 0.08017631])
            ells.append(e)
        high = high + b + b2 - detal
        if j % 2 == 1:
            num2=num2-1
        # print(j,int(h/(2*b)))
        j = j+1
        h = wi+detal*j

    print("个数：",c_1,num1*6,"；",c_2,num2*6)
    infor['num1'] = num1*6
    infor['num2'] = num2*6

    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111, aspect='equal')
    for e in ells:
        ax.add_artist(e)
        e.set_clip_box(ax.bbox)
        alf = rnd.rand()+0.2
        alf = 1 if alf>1 else alf
        e.set_alpha(alf)
        # e.set_facecolor(rnd.rand(3))

    ax.set_xlim(0, len)
    ax.set_ylim(0, wi)
    lylu = round(6*40*(num1*pi*a*b+num2*pi*a2*b2)/(len*wi*240),6)
    if c_1!=c_2:
        plt.title(c_1+"与"+c_2+"的切割方式，利用率:"+str(lylu*100)+"%")
    else:
        plt.title(c_1+"的切割方式，利用率:"+str(lylu*100)+"%")

    plt.show()
    print("利用率", lylu)
    infor['利用率'] = lylu
    return infor


infors = []
for aaa in cs:
    for bbb in cs:
        infor = fun(aaa,bbb)
        if infor!=None:
            infors.append(infor)


def bubble_sort(infor):
    count = len(infor)
    for i in range(count):
        for j in range(i + 1, count):
            if infor[i]['利用率'] > infor[j]['利用率']:
                infor[i], infor[j] = infor[j], infor[i]
    return infor

print(bubble_sort(infors))