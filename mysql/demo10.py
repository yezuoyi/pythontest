__author__ = 'pythontab.com'
#导入pymysql的包
import pymysql
try:
    #获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
    conn=pymysql.connect(host='localhost',user='root',passwd='root',db='test',port=3306,charset='utf8')
    cur=conn.cursor()#获取一个游标
    cur.execute('select * from EMPLOYEE')
    data=cur.fetchall()
    for d in data :
        #注意int类型需要使用str函数转义
        print("ID: "+str(d[0])+'  用户名： '+d[1]+"  注册时间： "+d[2])
    cur.close()#关闭游标
    conn.close()#释放数据库资源
except  Exception :print("查询失败")