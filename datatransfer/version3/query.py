#!/usr/bin/python3

import pymysql
import datetime
# 打开数据库连接
db = pymysql.connect("172.18.2.21", "omniv5", "ABCabc123",
                     "omniv5_wms",  charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
#sql = "SELECT * FROM EMPLOYEE WHERE INCOME > '%d'" % (1000)

sql = "select * from outboundorder where id = 59831"
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()

   # num_fields = len(cursor.description)

    #print("results=",results);

    resultList = list(results[0])

    #print("resultList =", resultList)

    #resultListNew = [ 'NULL' if x is None else x for x in resultList]

    #print("resultListNew =", resultListNew)

    dateList = [x.strftime('%Y-%m-%d %H:%M:%S')
                if isinstance(x, datetime.datetime) else x for x in resultList]

    #print("dateList =", str(dateList).replace('NULL',NULL))

    #sql2 = "values(%s)" % (",".join( str(x) for x in resultListNew))
    #print("sql2 = ",sql2)

   # sql3 = str(dateList).replace("\'NULL\'", 'NULL').replace("[","(").replace("]",");")

    sql3 = str(dateList).replace("None", "NULL").replace("[", "(").replace("]", ");")

    #print("sql3=",sql3)

    field_names = [i[0] for i in cursor.description]

    #values = [i[0] for i in results[0]];
    #print("values =",values)
    sql1 = "insert into outboundorder ('%s') VALUES " % (
        "','".join(field_names))
    #print(sql1)

    sql = sql1 + sql3

    print("sql =", sql)

    #values = "values('')

except:
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()
