'''
爬取豆瓣电影数据
了解ajax的基本爬取方式
一般使用json格式
'''
from urllib import request
import json

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=40&limit=20"

rsp = request.urlopen(url)

html = rsp.read().decode()

print(type(html))
data = json.loads(html)
print(type(data))
print(data)