'''
@author: xilh
@since: 20200128
'''
import os

# 分隔
path = 'd:\\test02\\test2.txt'
print(os.path.splitext(path))
print(os.path.split(path))

# 判断
print("exists:", os.path.exists(path))
print("isfile:", os.path.isfile(path))
print("isdir :", os.path.isdir(path))