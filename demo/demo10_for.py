'''
@author: xilh
@since: 20200125
'''
from demo.tools.tool import pline

for letter in 'Python':     # 第一个实例
    print('当前字母 :', letter)

pline()

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
    print('当前水果 :', fruit)
 
pline()
print("通过序列索引迭代")
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
    print('当前水果 :', fruits[index])
 
pline()
print("循环使用 else 语句")
for num in range(10,20):    # 迭代 10 到 20 之间的数字
    for i in range(2,num):  # 根据因子迭代
        if num%i == 0:      # 确定第一个因子
            j=num/i         # 计算第二个因子
            print('%d 等于  %d * %d' % (num,i,j))
            break           # 跳出当前循环
        else:
            print(num, '是一个质数')
            break
      
