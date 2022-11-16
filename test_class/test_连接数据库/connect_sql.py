


import pymysql

class Connect_sql:


    def __init__(self,host,port,usname,pwd,db_address):
        self.host=host
        self.port=port
        self.usname=usname
        self.pwd=pwd
        self.db=db_address

    def query_all(self):

        connect_all=pymysql.connect(host=self.host,
                        port=self.port,
                        user=self.usname,
                        password=self.pwd,
                        db=self.db
                        )

        cursor = connect_all.cursor()

        sql_all='select  user_id,mobile_code  from  tz_sms_log  limit  5'
        result1=cursor.execute(sql_all)
        result_all=cursor.fetchall()
        return result_all

    def query_one(self):

        connect_one=pymysql.connect(host=self.host,
                        port=self.port,
                        user=self.usname,
                        password=self.pwd,
                        db=self.db
                        )

        cursor = connect_one.cursor()

        sql_one='select  user_id,mobile_code  from  tz_sms_log  limit  5'
        result2=cursor.execute(sql_one)
        result_one=cursor.fetchone()
        return result_one


a_connect=Connect_sql('47.113.180.81',3306,'lemon','lemon123','yami_shops')

print(a_connect.query_all())

print(a_connect.query_one())




