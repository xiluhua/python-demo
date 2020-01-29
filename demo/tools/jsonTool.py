'''
Created on 20200129
@author: xilh
'''
import json
from demo.tools.tool import toDict

def toJsonString(obj):
    '''
    @note: convert obj to json str
    Created on 20200129
    @author: xilh
    '''
    jsonString = json.dumps(obj, default=toDict, ensure_ascii=False)
    return jsonString

def toObject(obj, jsonStr):
    '''
    @note: convert json str to obj
    Created on 20200129
    @author: xilh
    '''
    # for debug, don't rm, by xilh 20200129
    dict1 = json.loads(jsonStr)
    obj.__dict__ = dict1;
    # <== over
    return obj