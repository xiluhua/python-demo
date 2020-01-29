'''
os:
    - 可以与本地操作系统相关的一些功能
@author: xilh
@since: 20200128
'''
import os

# 创建文件夹
os.mkdir("d:\\test01")
os.makedirs("d:\\test01\\a\\b\\c")
print("OK")