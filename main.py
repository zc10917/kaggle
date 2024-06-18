# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import shapiro

from scipy import  stats
import sys;


def ks_test(data):
    u = data.mean()  # 计算均值
    std = data.std()
    d, p = stats.kstest(data, 'norm', (u, std))
    print('data的 ks 结果为{}'.format(stats.kstest(data, 'norm', (u, std))))
    print('data的   为{}'.format(stats.normaltest(data)))
    print('data的 shapiro结果为{}'.format(stats.shapiro(data)))

    return p > 0.05




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    reviews = pd.read_csv('arpu.csv')
    cols = ['uid1', 'uid2']
    norm_reviews = reviews[cols]
    data = norm_reviews['uid1']
    ks_r = ks_test(data)
    print(ks_r)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
