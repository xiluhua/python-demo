'''
os:
    - 可以与本地操作系统相关的一些功能
@author: xilh
@since: 20200128
'''
import os
import shutil

# 删除文件夹
path = "d:\\test01\\a\\b\\c"
if os.path.exists(path):
    os.rmdir(path)
# 删除文件夹及其子目录
shutil.rmtree("d:\\test01")


