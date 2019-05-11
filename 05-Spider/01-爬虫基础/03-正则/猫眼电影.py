'''
利用正则来爬取猫眼定影
1.url:https://maoyan.com/board
2. 把电影信息尽可能多地拿下来

分析
1. 一个影片的恩日弄是以dd开始的单元
2. 在单元内存在异步电影的所有信息

思路：
1. 利用re把dd内容都给找到
2. 对应找到的每一个dd,用re挨个查找需要的信息

方法就是三步走：
1. 把页面down下来
2. 提取dd党员为单位的内容
3. 对每一个dd,进行单独信息提取
'''
from urllib import  request

# 1.下载页面内容
url = "http://maoyan.com/board"

rsp = request.urlopen(url)
html = rsp.read().decode()

# 2 按dd提取出内容来，缩小处理范围
import re
# 小括号的作用，表明只要小括号中的
s = r'<dd>(.*?)</dd>'

#不加re.S就读不出来，S代表可见字符
pattern = re.compile(s, re.S)

films = pattern.findall(html)
# print(films)
# print(len(films))

# s = r'<dd>([\s\S]*?)</dd>'
# pattern = re.compile(s)
# filems = pattern.findall('<dd>sf sf\nsf</dd>')
# print(filems)

# 3. 从每一个dd中单独提取出需要的信息
i = 0
for film in films:
    i += 1
    print("第{0}名：".format(i))
    # 提取电影名称
    s = r'<a.*?title="(.*?)"'
    pattern = re.compile(s)
    title = pattern.findall(film)[0]
    print(title)

    s = r'<p.*?"star">(.*?)</p>'
    pattern = re.compile(s,re.S)
    star = pattern.findall(film)[0].strip()
    print(star)

    s=r'<p.*?releasetime">(.*?)</p>'
    pattern = re.compile(s, re.S)
    time = pattern.findall(film)[0].strip()
    print(time)

    s = r'<p.*?integer">(.*?)</i>'
    pattern = re.compile(s, re.S)
    point1 = pattern.findall(film)[0]
    s = r'fraction">(.*?)</i></p>'
    pattern = re.compile(s, re.S)
    point2 = pattern.findall(film)[0]
    print(point1+point2)
    print()


