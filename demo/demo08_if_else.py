'''
@author: xilh
@since: 20200125
'''

def test08():
    num = None
    if num is None:
        print ('1. is None')    
    
    num = 'python'
    if num == 'python':         # 判断变量是否为 python
        print ('2. num is python')    
    
    num = input("please enter a num: ") 
    
    print('type: '+str(type(num)))
    print('num1: '+num+'')
    # num = num.strip().replace('\n\r', '').replace('\n', '').replace('\r', '');
    print('num2: '+num+'')
    if len(num) == 0:            # 判断字符串num为空
        print('3. str isspace')        
        return
    
    num = int(num)
    if num == 3:            # 判断num的值
        print('3. boss')        
    elif num == 2:
        print('3. user')
    elif num == 1:
        print('3. worker')
    elif num < 0:           # 值小于零时输出
        print('3. error')
    else:
        print('3. roadman')    # 条件均不成立时输出


if __name__ == '__main__':
    test08()        