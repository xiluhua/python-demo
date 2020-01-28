'''
@author: xilh
@since: 20200125
'''
# Python的元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号，列表使用方括号。
# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可, 注意：必须加上逗号','以免不必要的麻烦
print("创建元祖")
tup1 = ()       # 创建空元组
print("tup1: ", tup1)
tup1 = (50,)    # 元组中只包含一个元素时，需要在元素后面添加逗号
print("tup1: ", tup1)
tup1 = ('physics', 'chemistry', 1997, 2000)
print("tup1: ", tup1)
tup2 = (1, 2, 3, 4, 5 )
print("tup2: ", tup2)
tup3 = "a", "b", "c", "d"
print("tup3: ", tup3)

# 注意点
tup2 = (20)
print("反例-(20)  :",type(tup2))
# 申明时必须加上逗号','
tup2 = (20, )
print("正例-(20, ):", type(tup2))