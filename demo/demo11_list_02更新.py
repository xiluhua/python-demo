'''
@author: xilh
@since: 20200125
'''
print("== 更新列表 ==")
slist = []                  # 空列表
print(slist)
slist.append('Google')      # 使用 append() 添加元素
print(slist)
slist.append('FaceBook')
print(slist)

iterable = ['baidu', '360']
slist.extend(iterable);
print(slist)

iterable = ('ali', 'taobao')
slist.extend(iterable);
print(slist)

iterable = {'QQ': 0, 'weixin': 0}
slist.extend(iterable);
print(slist)
