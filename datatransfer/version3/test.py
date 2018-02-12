#!/usr/bin/python3
#coding:utf-8

import pymysql

import config

import logging
logging.basicConfig(filename='log1.log',
                    format='%(asctime)s -%(name)s-%(levelname)s-%(module)s:%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=logging.DEBUG)


# 打开数据库连接
db = pymysql.connect(config.host, config.userName,
                     config.passWord, config.dataBase)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

#查出tableName的依懒关系
def getDendencyInfo(tableName):
    sql = "select \
    TABLE_NAME,COLUMN_NAME,CONSTRAINT_NAME, REFERENCED_TABLE_NAME,REFERENCED_COLUMN_NAME \
    from INFORMATION_SCHEMA.KEY_COLUMN_USAGE \
    where \
    CONSTRAINT_SCHEMA = '%s' and REFERENCED_TABLE_NAME = '%s'" % (config.dataBase, tableName)

    print(sql)
    logging.info(sql)

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
        logging.info("Error: unable to fetch data")

#删除指定记录
def deleteRecords(tableName,column,value):
    sql = "delete from %s where %s = %d" % (tableName,column,value)
    try:
        # 执行SQL语句
        print(sql)
        logging.info(sql)
        cursor.execute(sql)
        # 提交修改
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()


#一次查出tableName的表
def queryAllDependency(tableName,totalRecords):
    tmpRecords = getDendencyInfo(tableName)
    if tmpRecords:
        totalRecords.extend(tmpRecords);
       # print("totalRecords =",totalRecords)
        for recorde in tmpRecords:
            queryAllDependency(str(recorde[0]), totalRecords)
    else:
        return;

#删除当前记录
def deleteCurrentRecord(tableName, primaryKeyId):
    sql = "delete from %s where id= %d" % (tableName, primaryKeyId)
    try:
        # 执行SQL语句
        print(sql)
        logging.info(sql)
        cursor.execute(sql)
        # 提交修改
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
        print("some error .")

#查出主键和外键的依懒关系
def queryPrimaryKey(record, id):
    sql = "select id from %s where %s = %Ld" % (record[0], record[1], id)
    try:
        print(sql)
        logging.info(sql)
        cursor.execute(sql)
        results = []
        result = cursor.fetchall()
        for row in result:
            results.append(row[0])
        return results
    except:
        print("no data")
        logging.info("no data")

#将依懒关系保存到本地内存，不用每删除一条记录要与数据库交互一次
def getDendencyInfoLocalList(tableName, list):
    results = []
    for record in list:
        if record[3] == str(tableName):
            results.append(record)
    return results

#递归处理每一天记录，直到找没有外键依懒的进行删除


def processRecord(tableName, primaryKeyId):
    result = getDendencyInfoLocalList(tableName, totalRecords)
    #print(result)
    if result:
        for record in result:
            recordIds = queryPrimaryKey(record, primaryKeyId)
            print("recordIds==", recordIds)
            logging.info("recordIds==%s", str(recordIds))
            try:
                for recordId in recordIds:
                    processRecord(record[0], recordId)
            except:
                print("no record will be delete")
                logging.info("no record will be delete..")

        deleteCurrentRecord(tableName, primaryKeyId)

    else:
            # 为空时，删除这些表
        deleteCurrentRecord(tableName, primaryKeyId)




def getIds(tableName,createdDate):
    #sql = 'select * from outboundorder where createdDate < '2017 - 06 - 16''
    sql = "select id from %s where createdDate < '%s'"%(tableName,createdDate)
    try:
        print(sql)
        logging.info(sql);
        cursor.execute(sql)
        results = []
        result = cursor.fetchall()
        for row in result:
            results.append(row[0])
        return results
    except:
        print("no data")
        logging.info("no data")


totalRecords = []

createdDate = input("输入日期：")

for table in config.tables:
    print("current table %s is processing...",table)
    logging.info("current table %s is process...",table)
    totalRecords.clear()
    #从数据库里查出tableName表，所有的依懒关系，保存到totalRecords
    ids = getIds(table,createdDate)
    if ids:
        queryAllDependency(table, totalRecords)
        print(totalRecords)
        logging.info(totalRecords)
        print("-----------------")
        logging.info("--------------")
        for id in ids:
            processRecord(table, id)
    else:
        print("table no data will be process==>",table)
        logging.info("table no data will be process==>%s",str(table))

            



#从数据库里查出tableName表，所有的依懒关系，保存到totalRecords
#queryAllDependency(tableName, totalRecords)

#print(totalRecords)

#print("-----------------")

# 关闭数据库连接
db.close()
