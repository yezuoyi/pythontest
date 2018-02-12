#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
import pymysql.cursors

#获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
#port 必须是数字不能为字符串
db = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='test',
                             port=3306,
                             charset='utf8')



# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE WHERE INCOME > '%d'" % (1000)
try:
    with db.cursor() as cursor:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            # 打印结果
            print(fname+":"+lname+":"+age+":"+sex)
         db.commit()
except:
   print ("Error: unable to fecth data")

# 关闭数据库连接
db.close()