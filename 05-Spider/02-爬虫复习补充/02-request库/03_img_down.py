import requests
import os

# url = "http://img4.cache.netease.com/photo/0001/2006-07-14/2M0RCMQP00J60001.jpg"
url = "https://i.meizitu.net/2019/05/10b01.jpg"
root = "pics"
path = root + "/" + url.split("/")[-1]
headers = {
    "Referer": "https://www.mzitu.com/184179",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
}
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url,headers=headers)
        with open(path, "wb") as f:
            f.write(r.content)
            print("文件保存成功")
    else:
        print("文件已经存在")
except:
    print("爬取失败")