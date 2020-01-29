'''
文件读取后自动关闭, 使用: with open() as
@author: xilh
@since: 20200128
'''
from demo.tools.tool import Encoding

# 读取文件, 获取文件流对象
with open(file="D:\\tmp\\test.txt", mode="rb") as file:
    print("file.closed:", file.closed)
    # 读取所有内容
    content = file.read()
    
print("content    :", content.decode(Encoding.GBK))
print("file.closed:", file.closed)
