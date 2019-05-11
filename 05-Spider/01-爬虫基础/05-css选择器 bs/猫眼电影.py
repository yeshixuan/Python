'''
利用bs来爬取猫眼电影
1.url:https://maoyan.com/board
2. 把电影信息尽可能多地拿下来

- css选择器
    - 使用soup.select, 返回一个列表
    - 通过标签名称: soup.select("title")
    - 通过类名： soup.select(".content")
    - id查找: soup.select("#name_id")
    - 组合查找: soup.select("div #input_content")
    - 属性查找: soup.select("img[class='photo'])
    - 获取tag内容： tag.get_text
    - 获取属性内容： tag['src']
'''
import requests, re
from bs4 import BeautifulSoup
from urllib import request

url = 'https://maoyan.com/board'
rsp = requests.get(url)

#  apparent_encoding通过调用chardet.detect()来识别文本编码. 但是需要注意的是，这有些消耗计算资源
rsp.encoding = rsp.apparent_encoding

print(type(rsp.text))
soup = BeautifulSoup(rsp.text, 'lxml')

# nums = soup.select("i[class='board-index board-index-1']")
names = soup.select("p[class='name'] a")
stars = soup.select("p[class='star']")
times = soup.select("p[class='releasetime']")
img_add = soup.select("img[class='board-img']")
scores = soup.select("p[class='score']")

for i in range(10):
    num =  soup.select("i[class='board-index board-index-{}']".format(i + 1))
    num = "排名：" + num[0].get_text()
    print(num)
    print(names[i].get_text())
    print(stars[i].get_text().strip())
    print(times[i].get_text())
    print("封面图片链接：" + img_add[i]["data-src"])
    print("评分：" + scores[i].get_text())
    print()

# # print(len(names))
# # 两种方式都行
# # print(nums[0].get_text())
# print(nums[0].text)
#
# print(names[0].get_text())
# print(stars[0].get_text().strip())
# print(times[0].get_text())
# # 类似字典
# print(img_add[0]["data-src"])
# print(scores[0].get_text())


