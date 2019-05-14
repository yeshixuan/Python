import pymysql

# 数据库连接操作
db = pymysql.connect("192.168.47.130", "root","123456", "ceshi", 3306)
#创建游标
cursor = db.cursor()

# SQL更新
sql = "update FUXI set age = age - 1 where first_name='%s'"%("ma")

try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交sql到数据库模块
    db.commit()
    print("更新成功")
except Exception as e:
    # 发生错误请回家
    db.rollback()
    print("执行失败，原因：",e)

cursor.close()
db.close()