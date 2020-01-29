'''
os:
    - 可以与本地操作系统相关的一些功能
@author: xilh
@since: 20200128
'''
import os

# 获取当前文件夹
print(os.getcwd())
#  切换当前文件夹
os.chdir("d:\\tmp")
print(os.getcwd())
