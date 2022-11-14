
import pymysql
from pymysql.cursors import DictCursor
from test_项目搭建5.config.configs import config

class conect_sql:

    #使用字典解包，定义的参数名要一致才行
    def __init__(self,user=None,password=None,host=None,port=None,db=None,**kw):  #可以先设置关键字参数为空，后面初始化传,后面是剩余关键字参数

        self.connect=pymysql.connect(user=user,   #
            password=password,
            host=host,
            port=port,
            cursorclass=DictCursor,   #导入dictcursor类  得到字典
            db=db)

        #
        # self.connect=pymysql.connect(**config.db)   #调用config配置文件，**解包字典



    def query_all(self,sql):   #作为形式参数，传参
        #初始化游标
        cursor=self.connect.cursor()   #对应上面实例属性

        self.connect.commit()  #体检事务，指拿到最新的值

        cursor.execute(sql)   #execute方法对应上面的sql参数

        result_all=cursor.fetchall()  #使用方法cursor.fetch all 获取全部

        cursor.close()  #得到结果要记得关闭游标
        return result_all  #记得返回值

    def query_one(self,sql):

        cursor=self.connect.cursor()

        self.connect.commit()  # 体检事务，指拿到最新的值
        cursor.execute(sql)

        result_one=cursor.fetchone()

        cursor.close()
        return result_one

    def close(self):
        #关闭连接  连接完数据要关闭
        self.connect.close()


# a_x=conect_sql('lemon','lemon123','47.113.180.81',3306,'yami_shops')  #实例化，初始化
#
# print(a_x.query_all(sql='select  user_id,mobile_code  from tz_sms_log  limit 5'))
# print(a_x.query_one(sql='select  user_id,mobile_code  from tz_sms_log  limit 2'))


if __name__ == '__main__':

    a_connrct=conect_sql(**config.db)  #初始化

    rs=a_connrct.query_one('select  user_id,mobile_code  from tz_sms_log  limit 2')  #上传sql参数

    print(rs)   #得到手机号，和验证码

