
import pymysql

class connect_mysql:


    def __init__(self,usname,pwd,port,host,db_s):   #连接数据库，连接对象

        self.connect=pymysql.connect(user=usname,
                            password=pwd,
                            port=port,
                            host=host,
                            db=db_s)
        self.sqls = self.connect.cursor()   #直接在init里，定义属性，下面直接用   获取游标

    # def sql_y(self):
    #
    #     self.sqls=self.connect.cursor()   #通过实例方法，定义实例属性，要return 通过调用
    #
    #     return self.sqls

    def query_all(self):  #定义一个方法查全部

        cursor=self.sqls   #这里用的是拿的上面实例属性

        sql_all='select user_id,mobile_code from  tz_sms_log  limit  5 '   #查询sql语句
        cursor.execute(sql_all)   #方法 execute方法，里面放sql语句

        all=cursor.fetchall()  #查询全部结果 是元组类型数据

        return all

    def  query_oen(self):

        cursor=self.sqls

        sql_one='select  user_id , mobile_code  from  tz_sms_log  limit  5'

        cursor.execute(sql_one)


        one=cursor.fetchone()

        return one


A_C=connect_mysql('lemon','lemon123',3306,'47.113.180.81','yami_shops')

print(A_C.query_all())

print(A_C.query_oen())