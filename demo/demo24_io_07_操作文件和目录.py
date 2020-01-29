'''
os:
    - 可以与本地操作系统相关的一些功能
@author: xilh
@since: 20200128
'''
import os

# 创建文件夹
# os.mkdir("d:\\test01")
os.makedirs("d:\\test01\\a\\b\\c")

# 获取当前文件夹
print(os.getcwd())
#  切换当前文件夹
os.chdir("d:\\tmp")
print(os.getcwd())

# 删除文件夹
# os.rmdir("d:\\test01\\a\\b")
# 删除文件夹及其子目录
# shutil.rmtree("d:\\test01")


