'''
@author: xilh
@since: 20200128
'''
import logging

# 创建一个logging对象
logger = logging.getLogger()
# 创建一个文件对象  创建一个文件对象,以UTF-8 的形式写入 标配版.log 文件中
fh = logging.FileHandler('d:\\test555.log',encoding='utf-8')
# 创建一个屏幕对象
sh = logging.StreamHandler()
# 配置显示格式  可以设置两个配置格式  分别绑定到文件和屏幕上
formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
# 将格式绑定到两个对象上
fh.setFormatter(formatter)
sh.setFormatter(formatter)
# 将两个句柄绑定到logger
logger.addHandler(fh)  
logger.addHandler(sh)
# 总开关
logger.setLevel(logging.DEBUG)
# 写入文件的从10开始
fh.setLevel(logging.DEBUG)
# 在屏幕显示的从10开始
sh.setLevel(logging.DEBUG)

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')