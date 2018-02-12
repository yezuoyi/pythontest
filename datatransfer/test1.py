#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect("172.18.2.21", "omniv5", "ABCabc123", "omniv5_wms")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

def getDendencyInfo(tableName):
    sql = "select \
    TABLE_NAME,COLUMN_NAME,CONSTRAINT_NAME, REFERENCED_TABLE_NAME,REFERENCED_COLUMN_NAME \
    from INFORMATION_SCHEMA.KEY_COLUMN_USAGE \
    where \
    CONSTRAINT_SCHEMA = 'omniv5_wms' and REFERENCED_TABLE_NAME = '%s'" % (tableName)
    print(sql)

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        resultList = [];
        for row in results:
            record = list(row);
            resultList.append(record)
        return resultList
    except:
        print("Error: unable to fetch data")


# outboundorder outboundordervalueadded

tableName = 'outboundorder'
totalRecords = []

def queryAllDependency(tableName,totalRecords):
    tmpRecords = getDendencyInfo(tableName)
    if tmpRecords:
        totalRecords.extend(tmpRecords);
       # print("totalRecords =",totalRecords)
        for recorde in tmpRecords:
            queryAllDependency(str(recorde[0]), totalRecords)
    else:
        return;


queryAllDependency(tableName, totalRecords)
print(totalRecords)

print("-----------------")

totalRecords.reverse();
print(totalRecords)
    

# 关闭数据库连接
db.close()
