#! usr/bin/python3
# *-* coding=UTF-8 *-*
__author__ = "Rush"

import numpy as np


def euclidean_dist(x,y):# 欧式距离
    if len(x) == len(y):
        return np.sqrt(np.sum(np.power((x-y),2)))
    else:
        print("请输入相同尺寸的值")
    return None


def lrNorm_dist(x,y,power):# 切比雪夫距离
    if len(x) == len(y):
        return np.power(np.sum(np.power(np.abs(x-y),power)),(1/(1*power)))
    else:
        print("请输入相同尺寸的值")
    return None


def cosine_dist(x,y):# 余弦距离
    if len(x) == len(y):
        return np.dot(x,y)/np.sqrt(np.dot(x,x)*np.dot(y,y))
    else:
        print("请输入相同尺寸的值")
    return None


def jaccard_dist(x,y):# 杰卡德距离
    set_x = set(x)
    set_y = set(y)
    return 1-len(set_x.intersection(set_y))/len(set_x.union(set_y))


def hamming_dist(x,y):# 汉明距离
    diff = 0
    if len(x) == len(y):
        for char1,char2 in zip(x,y):
            if char1 != char2:
                diff+=1
        return diff
    else:
        print("请输入相同尺寸的值")
    return None
