


import pymysql

class Connect_sql:

    def __init__(self,host,port,usname,pwd,db_adres):

        self.py_connect=pymysql.connect(host=host,     #实例py——connect属性，依次填写
                        port=port,
                        user=usname,
                        password=pwd,
                        db=db_adres
                        )
        self.cursor = self.py_connect.cursor()

        # self.sql_x = 'select  user_id,mobile_code  from  tz_sms_log  limit  5'
    # def cursor_k(self,cursor):  #实例cursor方法
    #     # self.cursor=cursor
    #     cursor= self.py_connect.cursor()   #这里直接拿上面实例的py属性运行.cursor（）方法
    #     self.cursor = cursor
        #上面cursor继续实例

    # def sqls(self):
    #     self.sql_x='select  user_id,mobile_code  from  tz_sms_log  limit  5'  #查询sql  继续实例属性


    def query_all(self):

        # cursor=self.cursor    #对应cursor属性
        cursor = self.cursor


        sql_all='select  user_id,mobile_code  from  tz_sms_log  limit  5'
        excutes=cursor.execute(sql_all)  #执行一下excute命令（）填写全部或单个
        result_all=cursor.fetchall()
        return result_all

    def query_one(self):

        cursor = self.cursor

        sql_one='select  user_id,mobile_code  from  tz_sms_log  limit  5'

        excutes=cursor.execute(sql_one)
        result_one=cursor.fetchone()
        return result_one


a_connect=Connect_sql('47.113.180.81',3306,'lemon','lemon123','yami_shops')

print(a_connect.query_all())

print(a_connect.query_one())