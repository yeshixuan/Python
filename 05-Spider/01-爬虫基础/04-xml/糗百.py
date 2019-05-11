'''
爬去糗事百科，页面自己来找
分析：
1. 需要用到requests爬去页面，用xpath，re来提取数据
2. 可提取信息 用户头像连接，段子内容，点赞，好评次数
3. 保存到json文件中

大致分三部分
1. down下页面
2. 利用xpath提取信息
3. 保存文件落地
'''
import requests
from lxml import etree

url = 'https://www.qiushibaike.com/text/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8'
}
# 下载
rsp = requests.get(url, headers=headers)
html = rsp.text

#把页面解析成html
html = etree.HTML(html)

rst = html.xpath('//div[contains(@id,"qiushi_tag_")]')
print("**************")
print(len(rst))

i = 0
t = ""
for r in rst:
    i += 1
    # # 如果不进行以下两行的操作，会把所有的内容都打印出来，
    # # 把它转化为字符串再解析成html，相当于把其中一个div单独提出来了
    # s = etree.tostring(r)
    # r2 = etree.HTML(s)
    # 使用text()能把span里被br阻隔的内容全部提取出来，
    # 如果这里不适用text()，而是再后面用item.text，只能选出第一段，
    # 但是使用text（）的话，一个段子出来的结果时一个列表，还需要把每一段进行拼接

    # .表示当前节点，不写点很麻烦,看上面两条
    rst = r.xpath('.//div[@class="content"]/span/text()')
    store = ""
    for item in rst:
        store += item.strip()

    t += "\n"+str(i)+".\n"+store

with open("qiubai.txt",'w',encoding='utf-8') as f:
    f.write(t)


