'''
@author: xilh
@since: 20200128
'''
from demo.tools.tool import Encoding

file = None
try:
    # 读取文件, 获取文件流对象
    file = open(file="D:\\tmp\\test.txt", mode="rb")
    # 读取所有内容
    content = file.read()
    print("content:")
    print(content.decode(Encoding.GBK))
except Exception as es:
    print(es)
finally:
    # 关闭文件
    if file != None:
        file.close()