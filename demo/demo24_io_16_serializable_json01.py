'''
@author: xilh
@since: 20200128
'''
import json

from demo.tools.tool import pline


infos = {
    'sid': 10,
    'sname': '张三',
    'sage': 30
}
# serialize
ret1 = json.dumps(infos)
print(ret1)

# deserialize
ret2 = json.loads(ret1)
print(ret2)
pline()
