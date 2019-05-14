import pymysql

# 数据库删除操作
db = pymysql.connect("192.168.47.130", "root", "123456", "ceshi", 3306)
cursor = db.cursor()

# 创建删除sql语句
# sql = "delete from FUXI where INCOME > 10000"
sql = "delete from FUXI where INCOME > '%f'"%9999
try:
    cursor.execute(sql)
    db.commit()
    print("删除成功")
except Exception as e:
    db.rollback()
    print("删除失败,原因：",e)
cursor.close()
db.close()