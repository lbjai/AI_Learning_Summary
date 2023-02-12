#!/user/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import numpy as np
import pandas as pd

print("numpy的版本号：", np.__version__)
print("pandas的版本号：", pd.__version__)

# 当前的工作路径，就是你在什么地方执行的python命令
# print(os.getcwd())
# 使用os.path.abspath(),在主函数中调用该函数，并传入sys.argv[0] 就可以达到这个效果
# print(os.path.abspath(sys.argv[0]))
# 脚本所在的目录可以使用
# print(os.path.dirname(os.path.realpath(__file__)))

currut_path = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
data_dir = os.path.join(currut_path, 'joyful_pandas', 'data')


def get_data_path(data_name):
    data_path = os.path.join(data_dir, data_name)
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"{data_path}路径不存在")
    return data_path


print(data_dir)
