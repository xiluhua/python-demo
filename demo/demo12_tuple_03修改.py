'''
@author: xilh
@since: 20200125
'''
print("== 修改元组 ==")
tup1 = (12, 34.56)
print("tup1: ", tup1)

# 以下修改元组元素操作是非法的。
try:
    tup1[0] = 100
    print("tup1: ", tup1, "NOT PRINT AT ALL")
except Exception as ex:
    print('ERROR: ', ex)

tup2 = ('abc', 'xyz')
print("tup2: ", tup2)
# 创建一个新的元组
tup3 = tup1 + tup2
print("tup3", tup3)
