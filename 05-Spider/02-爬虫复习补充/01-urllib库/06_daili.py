from urllib import request

isProxy = input("please input is daili? y/n:")

# 有代理
proxy_1 = request.ProxyHandler({"http":"112.85.169.209:9999"})

# 无|代理
proxy_2 = request.ProxyHandler()

opener = request.build_opener(proxy_2)

if isProxy == "y":
    opener = request.build_opener(proxy_1)

url = "https://www.baidu.com"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

req = request.Request(url, headers=headers)

rsp = opener.open(req)

html = rsp.read().decode()

print(html)