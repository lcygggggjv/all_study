

import pymysql


#第一步；连接数据库，连接对象

connects=pymysql.connect(host='47.113.180.81',
                         port=3306,
                         user='lemon',
                         password='lemon123',
                         db='yami_shops')


print(connects)

#第二步，获取游标

cursor=connects.cursor()
print(cursor)

#第三步，使用sql语句

sql='select  user_id,mobile_code  from  tz_sms_log  limit  5'

result=cursor.execute(sql)  #execute方法，里面放sql语句

#第四步，获取查询结果

# tser=cursor.fetchone()   #获取一个  ,如果没单独写新的游标，存在游标被取走情况，例如，fetchone在上面，下面在取，会少一个，被前面取走，fetchmany同理
tser=cursor.fetchmany(result)   #获取全部，下面重新定义一个，这里取完，下面依然可以继续取


curso2=connects.cursor()   #重新写一个游标，再定义一个变量，写sql ，获取查询结果，不会变

sql2='select  user_id,mobile_code  from  tz_sms_log  limit  5'
result2=cursor.execute(sql2)

tser2=cursor.fetchmany(result)    #获取全部

print(tser)
print(tser2)
