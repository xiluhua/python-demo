'''
@author: xilh
@since: 20200125
'''
from demo.tools.tool import pline

count = 0
while (count < 10):
    print('The count is:', count)
    count = count + 1
    
pline()

# continue 和 break 用法
i = 1
while i < 10:   
    i += 1
    if i%2 > 0:     # 非双数时跳过输出
        continue
    print(i)         # 输出双数2、4、6、8、10

pline() 
i = 1
while 1:            # 循环条件为1必定成立
    print(i)         # 输出1~10
    i += 1
    if i > 10:     # 当i大于10时跳出循环
        break

pline()

print("循环使用 else 语句")
count = 0
while count < 5:
    print("count", count, "is less than 5")
    count = count + 1
else:
    print("count", count, "is not less than 5")