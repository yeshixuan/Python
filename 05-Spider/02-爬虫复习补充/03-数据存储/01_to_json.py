# """
# python对json文件操作为编码与解码
# dumps   字符串
# dump    json对象 可以通过fp文件流写入文件
#
# 解码：
#        loads
#        load
# """
# import json
# str = [{"username":"daochang","age":18}]
# print(type(str))
# json_str = json.dumps(str)
# print(type(json_str))
# str1 = json.loads(json_str)
# print(type(str1))

import requests
from bs4 import BeautifulSoup
import json
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
}
url = "http://www.seputu.com/"

rsp = requests.get(url, headers=headers)

soup = BeautifulSoup(rsp.text, "lxml")
content = []
for mulu in soup.find_all(class_="mulu"):
    # 标题
    title = mulu.find("h2")
    if title:
        # print(title.string)
        title = title.string
        list = []
        for a in mulu.find(class_='box').find_all("a"):
            print(a.get("href"),a["title"])
            list.append({"href":a.get("href"),"box_title":a["title"]})
        content.append({"title":title, "contnet":list})
with open("gcd.json", "a", encoding="utf-8") as fp:
    json.dump(content, fp, indent=4, ensure_ascii=False)