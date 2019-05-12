from urllib import request
from lxml import etree
url = "http://zuihaodaxue.com/zuihaodaxuepaiming2019.html"

rsp = request.urlopen(url)

html = rsp.read().decode()

# print(html)
html = etree.HTML(html)

trs = html.xpath("//tbody[@class='hidden_zhpm']/tr")

for tr in trs:
    num = tr.xpath("./td[1]")[0].text
    name = tr.xpath("./td[2]/div")[0].text
    point = tr.xpath("./td[4]")[0].text
    print("排名：" + num + " 学校名称：" + name + " 总分：" + point)

