'''
处理异常:
    1. 代码异常
        - 异常模式    try...except... else... finally...
    2. 逻辑异常
        - 在设计上考虑更周全, 代码逻辑清晰明确
@author: xilh
@since: 20200127
'''
from demo.tools.tool import pline

print('begin...')
try:
    num = 1/0
    print('end  ...')
except:
    print('不能除0')   
print('over')
pline()

print('begin...')
try:
    num = 1/0
    print('end  ...')
except (NameError, ZeroDivisionError) as ex:
    print('ERR:', ex)   
print('over')
pline()

print('begin...')
try:
    num = 1/0
    print('end  ...')
except NameError as ex:
    print('ERR1:', ex)   
except ZeroDivisionError as ex:
    print('ERR2:', ex)   
print('over')
pline()

print('begin...')
try:
    num = 1/1
    print('end  ...')
except ZeroDivisionError as ex:
    print('ERR2:', ex)
else:    
    print('else')
print('over')
pline()

print('begin...')
try:
    num = 1/0
    print('end  ...')
except ZeroDivisionError as ex:
    print('ERR2:', ex)
else:    
    print('else')
finally:
    print('finally')    
print('over')
