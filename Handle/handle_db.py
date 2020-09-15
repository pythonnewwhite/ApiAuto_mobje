#coding=utf-8
import pymysql
# 关闭数据库连接
from Handle.handle_init import Handle_init
import json
class HandleDb:
    '''数据库操作流程
    1、初始化连接对象db_name，pymysql.connect()
    2、使用cursor()方法获取操作游标，dbname.cursor()
    3、使用execute方法执行SQL语句，dbname.execute()
    4、使用 fetchone() 方法获取一条数据 或  使用 fetchall() 方法获取多条数据
    5、使用close 关闭数据库连接，dbname.close()
    '''
    HI=Handle_init()
    def __init__(self,option,section):
        '''option 参数为ini文件中的选项名，section为ini文件中test名'''
        db_config=json.loads(self.HI.read_ini(option,section))
        db=pymysql.connect(host=db_config["host"],port=db_config["port"],user=db_config["user"],password=db_config["password"],database=db_config["database"],charset='utf8')
        self.cursor=db.cursor()
    def get_one(self,sql):
        '''根据传入的sql语句，读取数据为单字段、单条数据'''
        self.cursor.execute(sql)
        return self.cursor.fetchone()
    def get_all(self,sql):
        '''根据传入的sql语句，读取数据为单字段、单条数据'''
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    def db_close(self):
        self.db.close()


if __name__ == '__main__':
    h_db=HandleDb("db_test","test1")
    sql="select * from people where sex='女'"
    print(h_db.get_one(sql))
    sql="select * from people"
    print(h_db.get_all(sql))

    # HI=Handle_init()
    # db_config = json.loads(HI.read_ini("db_test","test1"))
    # db=pymysql.connect(host=db_config["host"],port=db_config["port"],user=db_config["user"],password=db_config["password"],database=db_config["database"],charset='utf8')
    # cursor=db.cursor()
    # cursor.execute(sql)
    # print(cursor.fetchone())
    # print(cursor.fetchall())
    # db.close()