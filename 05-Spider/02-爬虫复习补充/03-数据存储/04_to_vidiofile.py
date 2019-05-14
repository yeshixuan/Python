# open(filename, "wb") as f:
#     f.write()
"""
1.获取到下载文件的url，二进制方式下载
urllib,和模块提供的request.urlretrieve,此模块可以进行影评文件下载
        也支持远程数据下载到本地

urlretrieve(url, filename=None, reporthook=None, data=None
url:我们下载的下载url地址
filename:数据存储路径+文件名
reporthook:要求一个回调函数，连接上服务器或者相应数据传输下载完毕时触发该回调函数
            显示当前的下载进度
data: (filename, headers)元组
"""
"""
http://img.ivsky.com/img/tupian/li/201810/26/haian_fengjig-008.jpg
     //img.ivsky.com/img/tupian/li/201810/26/haian_fengjig-008.jpg
"""
from lxml import etree
from urllib import request
import requests
import os
import random
def Schedule(blocknum,blocksize,totalsize):
    '''
    显示下载速度
    :param blocknum: 已经下载的数据块
    :param blocksize: 数据块的大小
    :param totalsize: 远程文件大小
    :return:
    '''
    per = 100.9*blocknum*blocksize/totalsize
    if per > 100:
        per = 100
    print("当前下载进度为：{}".format(per))
user_agent_list = [
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
]
user_agent = random.choice(user_agent_list)
headers = {
    "User-Agent":user_agent
}

url = "https://www.ivsky.com/tupian/ziranfengguang/index_1.html"
rsp = requests.get(url, headers=headers)

html = etree.HTML(rsp.text)

img_urls = html.xpath("//div[@class='il_img']/a/img/@src")

for img_url in img_urls:
    img_url = "http:" + img_url
    root = "img"
    if not os.path.exists(root):
        os.mkdir(root)
    filename = img_url.split("/")[-1]
    request.urlretrieve(img_url,root+"/"+filename, Schedule)

