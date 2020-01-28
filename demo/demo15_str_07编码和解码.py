'''
编码
        字符 --> 字节
解码
        字节 --> 字符
@author: xilh
@since: 20200126
'''
from demo.tools.tool import Encoding

print("== str 编码 & 解码 ==")
str1  = "我是钢铁侠";
ret1  = str1.encode(Encoding.UTF8)
print("ret1:", type(ret1))
print("ret1:", ret1)

ret2  = str1.encode(Encoding.GBK)
print("ret2:", type(ret2))
print("ret2:", ret2)

str3  = ret1.decode(Encoding.UTF8)
print("str3:", str3)
str4  = ret2.decode(Encoding.GBK)
print("str4:", str4)