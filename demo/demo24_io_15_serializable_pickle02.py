'''
@author: xilh
@since: 20200128
'''
import pickle

infos = {
    'sid': 10,
    'sname': '张三',
    'sage': 30
}

# serialize 并持久化到文件
with open(file="D:\\tmp\\test1.txt", mode="wb") as file:
    pickle.dump(infos, file)

# 读取文件并 deserialize
with open(file="D:\\tmp\\test1.txt", mode="rb") as file:
    ret1 = pickle.load(file);

print(ret1)
    