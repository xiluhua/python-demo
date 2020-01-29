'''
Created on 20200125
@author: xilh
'''
from _datetime import datetime, date

def toDict(obj):
    '''
    @note: convert obj to dict
    Created on 20200129
    @author: xilh
    '''
    dict1 = {}
    for attr in dir(obj):
        # ignore __init__ & __class__ etc...
        if (attr not in obj.columns()):
            continue
        
        # print(attr, ":", getattr(obj, attr), ":", type(getattr(obj, attr)))
        value = getattr(obj, attr)
        if isinstance(value, datetime):
            value = str(value)
        if isinstance(value, date):
            value = str(value)
        dict1[attr] = value
    return dict1

class Encoding:
    '''
    Created on 20200127
    @author: xilh
    '''
    UTF8    = "utf-8"
    GBK     = "gbk"
    
class Lev:
    '''
    Created on 20200127
    @author: xilh
    '''
    DEBUG   = 'DEBUG'
    INF     = 'INF'
    WARN    = 'WARN'
    ERR     = 'ERR'

level = {1:Lev.DEBUG, 2:Lev.INF, 3:Lev.WARN, 4:Lev.ERR}

def rm(v): 
    del v;
    v = None
    return v;

def pline():
    print("########################################")

def log(num, *args):
    tmp = level.get(num)
    print(tmp + ":", *args)

'''
Created on 20200127
@author: xilh
''' 
if __name__ == '__main__':
    print(555)
    pline()      
    
    tmp = isinstance(555, datetime)
    print(tmp)