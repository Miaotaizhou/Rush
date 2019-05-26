#! usr/bin/python3
# *-* coding=UTF-8 *-*
__author__ = "Rush"

import scipy
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

def get_random_data():
    x1 = np.random.normal(loc=0.2,scale=0.2,size=(1000,1000))
    x2 = np.random.normal(loc=0.9,scale=0.1,size=(1000,1000))
    x = np.r_[x1,x2]
    return x

x = get_random_data()

plt.cla()
plt.figure(1)
plt.title("Scan data")
plt.scatter(x[:, 0], x[:, 1])
plt.show()


def form_clusters(x,k):

    '''
    创建聚类
    '''

    no_clusters = k
    model = KMeans(n_clusters=no_clusters,init='random')
    model.fit(x)
    labels = model.labels_
    print(labels)
    # 计算轮廓系数
    sh_score = silhouette_score(x,labels)
    return sh_score


# 给定不同值来调用上述函数
sh_scores = []
for i in range(1, 5):
    sh_score = form_clusters(x, i + 1)
    sh_scores.append(sh_score)

no_clusters = [i+1 for i in range(1,5)]
plt.figure(2)
plt.plot(no_clusters,sh_scores)
plt.title("Cluster Quality")
plt.xlabel("No of cluster k")
plt.ylabel("Silhouette Coefficient")
plt.show()