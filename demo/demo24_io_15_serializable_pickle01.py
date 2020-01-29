'''
@author: xilh
@since: 20200128
'''
import pickle

from demo.tools.tool import pline


infos = {
    'sid': 10,
    'sname': '张三',
    'sage': 30
}
# serialize
ret1 = pickle.dumps(infos)
print(ret1)
# deserialize
ret2 = pickle.loads(ret1)
print(ret2)
pline()

# 持久化到文件
with open(file="D:\\tmp\\test1.txt", mode="wb") as file:
    file.write(ret1)


with open(file="D:\\tmp\\test1.txt", mode="rb") as file:
    ret1 = file.read();
    print(ret1)

# deserialize
ret2 = pickle.loads(ret1)
print(ret2)
    