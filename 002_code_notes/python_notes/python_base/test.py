import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

from collections import Counter
import math
from math import log

import pprint

def create_data():
    datasets = [
        ['晴','29','85','否','0'],
        ['晴','26','88','是','0'],
        ['多云','28','78','否','1'],
        ['雨','21','96','否','1'],
        ['雨','20','80','否','1'],
        ['雨','18','70','是','0'],
        ['多云','18','65','是','1'],
        ['晴','22','90','否','0'],
        ['晴','21','68','否','1'],
        ['雨','24','80','否','1'],
        ['晴','24','63','是','1'],
        ['多云','22','90','是','1'],
        ['多云','27','75','否','1'],
        ['雨','21','80','是','0']
    ]
    labels = [u'天气',u'温度',u'湿度',u'是否有风',u'是否前往游乐场']

    return datasets,labels

# 熵
def calc_ent(datasets):
    data_length = len(datasets)
    label_count = {}
    for i in range(data_length):
        label = datasets[i][-1]
        if label not in label_count:
            label_count[label] = 0
        label_count[label] += 1
    ent = -sum([(p/data_length)*log(p/data_length, 2) for p in label_count.values()])
    return ent

# 经验条件熵
def cond_ent(datasets, axis=0):
    data_length = len(datasets)
    feature_sets = {}
    for i in range(data_length):
        feature = datasets[i][axis]
        if feature not in feature_sets:
            feature_sets[feature] = []
        feature_sets[feature].append(datasets[i])
    cond_ent = sum([(len(p)/data_length)*calc_ent(p) for p in feature_sets.values()])
    return cond_ent

# 信息增益
def info_gain(ent, cond_ent):
    return ent - cond_ent

# def info_gain_train(datasets):
# # #     count = len(datasets[0]) - 1
# # #     ent = calc_ent(datasets)
# # #     best_feature = []
# # #     for c in range(count):
# # #         c_info_gain = info_gain(ent, cond_ent(datasets, axis=c))
# # #         best_feature.append((c, c_info_gain))
# # #         print('特征({}) - info_gain - {:.3f}'.format(labels[c], c_info_gain))
# # #     # 比较大小
# # #     best_ = max(best_feature, key=lambda x: x[-1])
# # #     return '特征({})的信息增益最大，选择为根节点特征'.format(labels[best_[0]])

res1 = -(4/9*math.log(4/9,2)+5/9*math.log(5/9,2))
res2 = -(4/5*math.log(4/5,2)+1/5*math.log(1/5,2))
res = 0.940-(9/14*res1+5/14*res2)

print(res)