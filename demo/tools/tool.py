'''
Created on 2020年1月25日

@author: Administrator
'''
class Encoding:
    UTF8    = "utf-8"
    GBK     = "gbk"
    
class Lev:
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

    
# def isDefined(v): 
#     try : 
#         type (eval(v)) 
#     except : 
#         return False
#     else : 
#         return True
 
if __name__ == '__main__':
    print(555)
    pline()      
    
