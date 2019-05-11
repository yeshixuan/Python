from urllib import request
import random

#代理
proxy_list = [
    {"http":"112.85.169.209:9999"},
    {"http":"114.113.222.229:80"},
    {"http":"115.221.126.250:9999"}
]
proxy = random.choice(proxy_list)
# print(proxy)

# 创建代理管理器
proxy_handler = request.ProxyHandler(proxy)

# 创建网络请求对象opener
opener = request.build_opener(proxy_handler)

url = "https://www.baidu.com"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

req = request.Request(url=url, headers=headers)
rsp = opener.open(req)
# rsp = request.urlopen(req)
# print(proxy)
# print(rsp)
html = rsp.read().decode()

print(html)
