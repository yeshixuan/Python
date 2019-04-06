import requests
# 代理有可能报错，如果使用人数多，考虑安全问题，可能会被强行关闭
# 1. 代理
proxy = {
    "https":"58.241.186.90:43043",
    "http":"120.210.219.103:8080"
}

#2. 如果是购买的好用的代理地址，
#   代理验证，可能需要使用HTTP basic Auth
    # 格式为 用户名：密码@代理地址：端口
proxy1 = {
    "http": "china:12343543@103.92.12.34:8080"
}

#3. 如果遇到web客户端验证，需要添加auth=(用户名，密码）
auth = {'yusername','password'}
# rsp = requests.get("http://www.baidu.com", auth=auth)

rsp = requests.request("get", "http://www.baidu.com", proxies=proxy)
print(rsp.text)
