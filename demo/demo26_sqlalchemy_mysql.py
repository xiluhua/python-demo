'''
@see: https://www.jianshu.com/p/0ad18fdd7eed
@author: xilh
@since: 20200128
'''
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime

from demo.tools import jsonTool, dateTool
from demo.tools.tool import pline


# 生成orm基类
base = declarative_base()

class Student(base):
    __tablename__ = 'student'  # 表名
    __table_args__ = {
        #'schema': 'Code'    #数据库架构名
        'mysql_charset':'utf8'
    }
    sid = Column(Integer, primary_key=True, name="SID")
    sname = Column(String(20), name="SNAME")
    createTime = Column(DateTime, name="CREATE_TIME")

    def set(self, sid, sname, createTime):
        self.sid = sid
        self.sname = sname
        self.createTime = createTime
        
    @classmethod
    def columns(cls):
        # print(cls.__name__)
        return set('sid sname createTime'.split())    

# 1. 创建连接
# demo: mysql+pymysql：//username+password@host:prot/databas
url = 'mysql+pymysql://root:1111@localhost:3308/python01?charset=utf8'
# engine = create_engine(url, echo=False)
engine = create_engine(
        url,
        max_overflow = 0,  # 超过连接池大小外最多创建的连接
        pool_size    = 10,  # 连接池大小
        pool_timeout = 30  # 池中没有线程最多等待的时间，否则报错
    )
# 创建表结构,已存在表则无需执行
# base.metadata.create_all(engine)  

# 2. 创建与数据库的会话, class, 不是实例
print("== 实现方式(一) ==")
# 使用thread local storage技术, 使 session 线程隔离
SessionFactory = sessionmaker(bind=engine)
# 生成session实例, 单例模式, 与线程绑定
session = scoped_session(SessionFactory)
# over

'''
# print("== 实现方式(二) ==")
Session = sessionmaker(bind=engine)
# 生成session实例, 每次生成一个新的
session = Session() 
# over
'''

# 3. add
stu = Student()
Student.set(stu, sid=8, sname='新增8', createTime='2014-07-15 10:25:03')
# 把要创建的数据对象添加到这个session里 
session.add(stu)  
# 提交，使前面修改的数据生效
session.commit() 
print("add OK")
 
# 4.1. query all
stu = session.query(Student).all()    
for row in stu:  #打印全部内容
    print('type(row):', type(row))
    print('type(row):', type(row.createTime))
    print(row.sid, row.sname, row.createTime)
    ret1 = jsonTool.toJsonString(row)
    print('ret1      :', ret1)
    print('type(ret1):', type(ret1))
         
    stu = jsonTool.toObject(Student(), ret1)
    print('type(stu)     :', type(stu))
    print('type(stu)     :', type(stu.createTime))
    print('stu.createTime:', stu.createTime)
    pline()

# 4.2. query one    
row = session.query(Student).filter(Student.sid == 6).first()
print("query one:", jsonTool.toJsonString(row))
pline()
     
# 4.3. update
row.sname = '王五'
row.createTime = dateTool.curDatetime()
session.commit()
print("update OK")
pline()
   
# 4.4. delete
session.query(Student).filter(Student.sid == 6).delete()
session.commit()
print("delete OK")

# 将连接交还给连接池
try:
    session.remove()
    print("== 实现方式(一) ==")
except:
    print("== 实现方式(二) ==")
    session.close()
