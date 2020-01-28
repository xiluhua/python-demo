'''
@author: xilh
@since: 20200126
'''
import functools

list2 = [1, 2, 3]
ret1 = functools.reduce(lambda x,y:x+y, list2)
print(ret1)

ret1 = functools.reduce(lambda x,y:x+y, list2, 10)
print(ret1)