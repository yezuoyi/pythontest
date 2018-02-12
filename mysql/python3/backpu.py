#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "root", "test")

cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)

tweets = open("keywords.txt", "w")

cursor.execute(sql)
for row in cursor:
    print(tweets, row[0])
tweets.close()
db.close()