#!/usr/bin/python3
import pymysql

# 打开数据库连接
db = pymysql.connect("172.18.2.21", "omniv5", "ABCabc123", "omniv5_wms")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

list = [
    ['parcelproductqty', 'outboundParcelId',
     'FKtlxm6pdsso9lv9pwj76axr0hg', 'outboundparcel', 'id'],
    ['warehouseid', 'id', 'FKsfvw4shdvf19fobtljnrej9k3',
     'outboundordervalueadded', 'id'],
    ['outboundordervasitem', 'outboundOrderValueAddedId',
     'FKb6prkkl5nv7hl13aq68gntvpd', 'outboundordervalueadded', 'id'],
    ['scanorder', 'outboundOrdId',
     'FK5x66e8q3gndsswo9kqie8b8g2', 'outboundorder', 'id'],
    ['reonshelfinfo', 'orderId',
     'FKbks3bc7mhggpx7nexep9mcucp', 'outboundorder', 'id'],
    ['outboundvirtualparcel', 'outboundOrderId',
     'FKp3kgat1ghtgatpyqnnivii4uk', 'outboundorder', 'id'],
    ['outboundproduct', 'outboundOrderId',
     'FKd9yup8a78chwyntjwu7n88c45', 'outboundorder', 'id'],
    ['outboundparcel', 'outboundOrderId',
     'FK3n1rdel8n5tnpksh2hvww2vhi', 'outboundorder', 'id'],
    ['outboundordervalueadded', 'outboundOrderId',
     'FKihbvqwrweqgp80ytpqtgl09tf', 'outboundorder', 'id'],
    ['confirmoutbound', 'outboundOrdId',
     'FKrjvstet3f8q3ljrg1568cmey1', 'outboundorder', 'id']
]


def getDendencyInfoLocalList(tableName, list):
    results = []
    for record in list:
        if record[3] == str(tableName):
            results.append(record)
    return results


result = getDendencyInfoLocalList('outboundorder', list)

tableList = ['t1', 't2', 't3']


def deleteCurrentRecord(tableName, primaryKeyId):
	sql = "delete from %s where id= %d" % (tableName, primaryKeyId)
	try:
		# 执行SQL语句
		print(sql)
		cursor.execute(sql)
		# 提交修改
		db.commit()
	except:
		# 发生错误时回滚
		db.rollback()
		print("some error .")


def queryPrimaryKey(record, id):
    sql = "select id from %s where %s = %Ld" % (record[0], record[1], id)
    try:
        print(sql)
        cursor.execute(sql)
        results = []
        result = cursor.fetchall()
        for row in result:
            results.append(row[0])
        return results
    except:
        print("Error: unable to fetch data")


def processRecord(tableName, primaryKeyId):
	result = getDendencyInfoLocalList(tableName, list)
	print(result)
	if result:
		for record in result:
			recordIds = queryPrimaryKey(record, primaryKeyId)
			print("recordIds==", recordIds)
			try:
				for recordId in recordIds:
					processRecord(record[0], recordId)
			except :
				print("TypeError: 'NoneType' object is not iterable")

		deleteCurrentRecord(tableName, primaryKeyId)

	else:
		# 为空时，删除这些表
		deleteCurrentRecord(tableName, primaryKeyId)


tableName = 'outboundorder'


def processTables(tableName):
    # get record from tableName save to records
    records = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

    # 循环每一条记录处理依懒关系
    processRecord(tableName, primaryKeyId)


# print(result)


processRecord(tableName, 273)

# 关闭数据库连接
db.close()
