'''
数据存储之mysql
Ubuntu环境安装mysql
    sudo apt-get update
    sudo apt-get inistall mysql-server
    sudo apt-get install mysql-client
    sudo apt-get install libmysqlclient-dev

登录数据库：
    sudo mysql -u root -p

msql数据库远程链接
    1. 修改 /etc/mysql/mysql.conf.d/mysqld.cnf
        找到bind-address = 127.0.0.1这一行吧他注释掉，或者改成0.0.0.0
    2.让root用户支持远程链接mysql数据库
    https://blog.csdn.net/radiantjeral/article/details/82632056

# python3操作mysql
    pip install pymysql
'''
'''
use mysql;
select user,host fromm user; 查看用户信息
create database ceshi;创建数据库
show databases;查看所有数据库
use ceshi；查看这个数据库
show tables;查看所有表
show create table BJTLXY；查看这个表
show create tables BJTLXY\G;
select * from BJTLXY;查看具体内容
select id,title,info from BJTLXY;查看这些信息
DESC qidian; 查看表的结构
truncate qidian; 格式化表

#create database db_lianjia character set utf8;
'''

# Python操作mysql创建数据库
import pymysql
## 创建表
# try:
#     # 获取一个数据库连接，注意：如果是utf8类型，需要定制数据库
#     # 打开数据库连接
#     '''
#     host="92.168.47.130", 数据库服务器地址
#     user="root",         登陆数据库用户
#      password="123456",  用户密码
#      db="ceshi",          所连接的数据库名
#       port=3306           数据库端口号，mysql默认3306
#       '''
#     db = pymysql.connect(host="192.168.47.130", user="root", password="123456", db="ceshi", port=3306)
#     # 创建游标，对数据库进行操作，使用cursor()方法
#     cursor = db.cursor()
#     # execute()执行sql语句
#     cursor.execute("DROP TABLES IF EXISTS FUXI")
#     # 使用预处理语句创建表
#     sql = """create table FUXI(
#     FIRST_NAME CHAR(20) NOT NULL,
#     LAST_NAME CHAR(20),
#     AGE INT,
#     SEX CHAR(1),
#     INCOME FLOAT)"""
#     cursor.execute(sql)
#     # cursor.close()
#     db.close()
# except Exception as e:
#     print("创建失败,原因：",e)


# # 数据库插入操作
# db = pymysql.connect(host="192.168.47.130", user="root", password="123456", db="ceshi", port=3306)
# # 使用cursor()创建游标对象
# cursor = db.cursor()
#
# # sql语句、
# # sql = "insert into FUXI(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)VALUES('liu','dana',18,'M','10000')," \
# #       "('ma','erna',54,'W','20000')"
# # 为了防止sql注入
# sql = "INSERT INTO FUXI(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)VALUES('%s','%s','%d','%c','%s')"%('liu','dana',18,'M','10000')
#
# try:
#     # 执行sql语句
#     cursor.execute(sql)
#     # 提交执行
#     db.commit()
#     print("执行成功")
# except Exception as e:
#     # 发生意外
#     db.rollback()
#     print("执行失败，原因：", e)
# db.close()


# 数据库查询操作
try:
    db = pymysql.connect("192.168.47.130","root","123456","ceshi",3306)
    cursor = db.cursor()
    cursor.execute("select * from FUXI")
    # data = cursor.fetchall()
    # data = cursor.fetchone()
    data = cursor.rowcount
    print(data)
    print("查询成功")
    cursor.close()
    db.close()
except Exception as e:
    print("查询失败")
    print(e)
'''
fetchall():接收全部返回结果
fetchone():获取下一个查询结果集
rowcount: 只读属性，返回执行语句影响的行数
'''