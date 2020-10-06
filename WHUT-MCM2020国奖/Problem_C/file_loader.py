import matplotlib.pyplot as plt
import numpy as np

 # 生成画布
plt.figure(figsize=(20, 8), dpi=80)
 # 横坐标电影名字
movie_name = ['1','2','3','4', '5', '6', '7', '8']
 # 纵坐标票房
y=[41.278,57.273,28.927,-28.183,42.751,15.650,-41.487,37.468]
x=range(len(movie_name))

plt.bar(x,y,width=0.8)
plt.xticks(x, movie_name)
plt.ylabel("Gamma")
plt.xlabel("products")
plt.show()