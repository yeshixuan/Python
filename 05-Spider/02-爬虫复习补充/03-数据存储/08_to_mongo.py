'''
mongoDB：非关系型数据库
mongoDB属于更加适合爬虫的数据库
mongoDB是一个基于分布式文件存储的数据库，由C++编写
主要为web应用提供可扩展的高性能的数据存储解决方案

概念说明：
SQL:        MOgoDB:        说明：
database    database       数据库
table       collection     表/集合
row         document       行/文档
colume      field          字段/域
inde        index          索引
primary     primary        主键/_id为主键

安装，mongoDB
    ubuntu安装mongoDB
        https://www.cnblogs.com/shileima/p/7823434.html
        sudo apt-get install mongodb

如何Python操作mongodb
    pip install pymongo

'''
import pymongo

# # 查询mongdb
# # # 连接mongdb数据库
# # # client = pymongo.MongoClient()
# # # print(client)
# # client = pymongo.MongoClient("192.168.47.130", 27017)
# #
# # # 获取到数据库，连接数据库
# # db = client.KG_DB
# #
# # # 获取集合
# # std = db.songs
# #
# # # 获取数据
# # datas = std.find()
# # print(datas,type(datas))
# #
# # for data in datas:
# #     # print(data['singer'])
# #     # 获取集合中的字段属性
# #     print(data.keys())


# 插入文档
client = pymongo.MongoClient("192.168.47.130", 27017)
db = client.abc
post = {
    'name':'miudana',
    'sex':'w',
    'age':'28',
    'class':['database','python','java','math','数据分析','linux'],
    'income':'2000000'
}
# 构建post对象
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print("post id is:", post_id)
print("创建成功")

