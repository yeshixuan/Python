"""
session 模拟一次回话
    ss = requests.session()
    ss.post(url,data=data,headers=headers)
    rsp = ss.get(url)

ssl证书
    rsp = requests.get(url,verify=False)
"""
import requests

proxy = {
    "http":"211.23.149.29:80",
    # "https":"163.172.215.202:3128"
}
# 创建session对象，可以保持cookie值
ss = requests.session()

url = "https://fanyi.baidu.com/sug"
data = {
    "kw":"girl"
}
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

rsp = ss.post(url,data=data, headers=headers, proxies=proxy, verify=False)

print(rsp.text)
print(rsp.json())
