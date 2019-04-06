import requests

url = "http://www.baidu.com"

# # 两种方式
# # 使用get请求
# # rsp = requests.get(url)
# rsp = requests.request("get", url)
#
# print(type(rsp))
# print(type(rsp.text))
# print(rsp.text)        # str
# print(type(rsp.content))
# print(rsp.content)     # bytes

url = "http://www.baidu.com/s?"

# wd = input("请输入要搜索的关键字：")
data = {
    "wd":"大熊猫"
}
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

rsp = requests.get(url, params=data, headers=headers)

# print(rsp.text)
# print(rsp.content)
print(rsp.url)
print(rsp.encoding)
print(rsp.status_code)       # 请求返回码
print(rsp.request)
print(rsp.cookies)