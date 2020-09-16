import numpy as np
from math import *
import random
import matplotlib.pyplot as plt
import numpy.random as rnd
from scipy import optimize

a1 = 30
b1 = 20
c1 = ("LJ1",a1,b1)
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

def get_ellipse(e_x, e_y, a, b, e_angle):
    angles_circle = np.arange(0, 2 * np.pi, 0.01)
    x = []
    y = []
    for angles in angles_circle:
        or_x = a * cos(angles)
        or_y = b * sin(angles)
        length_or = sqrt(or_x * or_x + or_y * or_y)
        or_theta = atan2(or_y, or_x)
        new_theta = or_theta + e_angle / 180 * pi
        new_x = e_x + length_or * cos(new_theta)
        new_y = e_y + length_or * sin(new_theta)
        x.append(int(new_x))
        y.append(int(new_y))
    return np.array(x), np.array(y)

def init(a,b,a2,b2,len,wi):
    map = np.zeros((wi, len))

    for j in range(int(len / 2 / a)):
        xs, ys = get_ellipse(a + j * 2 * a, b, a, b, 0)
        for i, x in enumerate(xs):
            map[wi - ys[i] - 1][x - 1] = 255

    xs, ys = get_ellipse(2 * a, 3 * b, a2, b2, 0)
    while True:
        flag = 0
        for i in range(xs.shape[0]):
            if map[wi - ys[i]][xs[i]] == 255:
                flag = 1
                break
        if flag == 1:
            break
        ys = ys - 1
    for i, x in enumerate(xs):
        map[wi - ys[i] - 1][x] = 255
    dleta = b * 2 - min(ys)
    return map, dleta

dletas = {}
for i in cs:
    c_,a_, b_ = i
    _, dddd = init(a_, b_, a_, b_, 6060, 2400)
    dletas[c_]=dddd


def fun(c1,c2,len_,wi_):
    infor = {}
    c_1,a,b = c1
    c_2,a2,b2 = c2
    if c_1!=c_2:
        return
    if wi_<2*b or wi_==nan:
        return 0
    infor['c1'] = c_1
    infor['c2'] = c_2
    # print(c_1,c_2,a,b,a2,b2)
    len = len_#6060
    wi = int(wi_)+1#2160

    detal=dletas[c_2]
    detal = detal+1
    j=0
    num1 = 0
    num2 = 0
    high = b
    while high<=wi:
        if j%2==0:
            num1 = num1 + 1*int(len/(2*a))
        else:
            num2 = num2 + 1*int(len/(2*a))
        high = high + b + b2 - detal
        if j % 2 == 1:
            num2=num2-1
        j = j+1

    # lylu = round(6*40*(num1*pi*a*b+num2*pi*a2*b2)/(len*wi*240),6)

    return num1*6 + num2*6


class DE(object):
    def __init__(self, fangshi=4, xinghao=6, max_num=20, pop_size=100, c_rate=0.5, m_rate=0.6):
        self.fangshi = fangshi
        self.xinghao = xinghao
        self.max_num = max_num  # 迭代次数
        self.pop_size = pop_size  # 种群数目
        self.c_rate = c_rate  # 交换率
        self.m_rate = m_rate  # 突变率
        self.fitness = np.zeros(self.pop_size)
        pass

    def encode(self):  # 初始化编码, 问题的解
        gens = []

        for x in range(self.fangshi):  # 隔板的每一个基因
            gen = []
            for l in range(self.xinghao):
                gen.append(random.random())  # 初始化每一个隔板的位置
            gens.append(np.array(gen))
        # gens = np.sort(gens, axis=0)  # 按列排叙。列为单个订单的插板
        return np.array(gens)

    def creat_pop(self, size):
        pop = []
        for i in range(size):
            pop.append(self.encode())  # 加入种群
        return np.array(pop)

    def cross(self, parent1, parent2):
        """交叉p1,p2的部分基因片段"""
        if np.random.rand() > self.c_rate:
            return parent1
        newGene = np.zeros((parent1.shape[0], parent1.shape[1]))
        for i in range(parent1.shape[1]):        # 交叉，这里待优化
            for j in range(parent1.shape[0]):
                if np.random.rand() > self.c_rate:
                  newGene[j][i] = parent1[j][i]  # 取两个父代中间的随机数
                else:
                  newGene[j][i] = parent2[j][i]  # 取两个父代中间的随机数
        return newGene

    def mutate(self, gene):
        """突变"""
        if np.random.rand() > self.m_rate:
            return gene
        newGene = gene.copy()
        for i in range(gene.shape[1]):
            for j in range(gene.shape[0]):
                if np.random.rand()>0.8:
                  newGene[j][i] = random.random()
        return newGene

    def get_fitness(self, pop):
        d = []  # 适应度记录数组
        for i in range(pop.shape[0]):
            gens = pop[i]  # 取其中一条基因（编码解，个体）
            f1,_ = self.get_fun(gens)  # 计算此基因优劣（距离长短）
            d.append(f1)
        return d

    def get_fun(self, gens):
        def normalize(x):
            return x / sum(x)

        fangansss =  []
        gennns = []
        for i in range(self.fangshi):
            geban = normalize(gens[i])*2160      # 归一化
            fangan = []
            for idx,www in enumerate(geban):
                    num = fun(cs[idx],cs[idx],6060,www)
                    fangan.append(num)
            fangansss.append(fangan)
            gennns.append(geban)
        fanganssss = np.array(fangansss).T
        c = np.array([1, 1, 1, 1])
        a = fanganssss/10000
        b = np.array([1272000, 1521000, 1161000, 3229500, 2434500, 2421000])/10000
        res = optimize.linprog(c, -a, -b,
                               bounds=((0, None), (0, None), (0, None),
                                       (0, None)))
        return res.fun,fangansss

    def select_pop(self, pop):
        # 选择种群，优胜劣汰，策略1：低于平均的要替换改变
        best_f_index = np.argmin(self.fitness)
        av = np.median(self.fitness, axis=0)
        for i in range(self.pop_size):
            if i != best_f_index and self.fitness[i] > av:
                pi = self.cross(pop[best_f_index], pop[i])
                pi = self.mutate(pi)
                # print(pi)
                pop[i, :] = pi[:]
        return pop

    def evolution(self):
        distss = []
        self.pop = self.creat_pop(self.pop_size)
        self.fitness = self.get_fitness(self.pop)
        for num in range(self.max_num):
            # print(self.fitness)
            best_f_index = np.argmin(self.fitness)
            worst_f_index = np.argmax(self.fitness)
            local_best_gen = self.pop[best_f_index]
            # print(local_best_gen)
            local_best_dist, asasas = self.get_fun(local_best_gen)
            if num == 0:
                self.best_gen = local_best_gen
                self.best_dist = local_best_dist
            if local_best_dist < self.best_dist:
                self.best_dist = local_best_dist  # 记录最优值
                self.best_gen = local_best_gen  # 记录最个体基因
            else:
                self.pop[worst_f_index] = self.best_gen
            print('gen:%d evo, best num :%s ' % (num, self.best_dist))
            print(asasas)
            distss.append(self.best_dist)
            self.pop = self.select_pop(self.pop)  # 选择淘汰种群
            self.fitness = self.get_fitness(self.pop)  # 计算种群适应度
            for j in range(self.pop_size):
                r = np.random.randint(0, self.pop_size - 1)
                if j != r:
                    self.pop[j] = self.cross(self.pop[j], self.pop[r])  # 交叉种群中第j,r个体的基因
                    self.pop[j] = self.mutate(self.pop[j])  # 突变种群中第j个体的基因
            self.best_dist, _ = self.get_fun(self.best_gen)  # 记录最优值
        return distss

if __name__ == "__main__":
    model = DE()
    model.evolution()
    # gens = model.encode()

    # print(np.argmax([1300.1207729468597, 636.3349936760828, 603.7814658053018, 539.2888167234714, 528.5834981635094]))

