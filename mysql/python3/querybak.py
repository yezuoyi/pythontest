#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "root", "test")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchone()
    
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print ("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
               (fname, lname, age, sex, income ))
    num_fields = len(cursor.description)
    values = [i[0] for i in results]
    field_names = [i[0] for i in cursor.description]
    sql1 = "insert into EMPLOYEE('%s')"%("','".join(field_names))
    print(sql1)
    print("num_fields=%s,field_names=%s", (values, field_names))
except:
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()
