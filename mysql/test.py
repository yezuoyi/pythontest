#coding=utf-8
#导入pymysql的包
import pymysql
import pymysql.cursors

#获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
#port 必须是数字不能为字符串
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='test',
                             port=3306,
                             charset='utf8')
try:
    #获取一个游标
   with connection.cursor() as cursor:
       sql ="SELECT * FROM EMPLOYEE WHERE INCOME > '%d'" % (1000)
       cout = cursor.execute(sql)
       print("数量： " + str(cout))

       for row in cursor.fetchall():
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            # 打印结果
            print(fname+":"+lname+":"+str(age)+":"+sex+":"+str(income))
       connection.commit()

finally:
    connection.close()
