"""
XHR:post请求
没有给你接口怎么登陆:
1、用错误密码测试
2、post请求
3、要添加的数据
4、urllib默认get请求，post请求需要传进byte格式的参数
url = "https://www.huawei.com/en/accounts/LoginPost"
method:post
parm:
    userName:
    pwd:
    languages: zh
    fromsite: www.huawei.com
    authMethod: password
"""

from urllib import request,parse
from http import cookiejar

# 生成cookie对象
cookie = cookiejar.CookieJar()

# 生成cookie管理器
cookieHandler = request.HTTPCookieProcessor(cookie)

# 生成http请求管理器
httpHandler = request.HTTPHandler()

# 生成https请求管理器
httpsHandler = request.HTTPSHandler()

# 构建发起请求管理器
opener = request.build_opener(cookieHandler, httpHandler, httpsHandler)

# 构建登陆函数
def login(url):
    data = {
        "userName": "",
        "pwd": "",
        "languages": "zh",
        "fromsite": "www.huawei.com",
        "authMethod": "password"
    }

    # 拼接
    # data = parse.urlencode(data).encode()
    data = parse.urlencode(data)

    # data数据类型为bytes

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Length": len(data),
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": '',
        "Host": "www.huawei.com",
        "Origin": "https://www.huawei.com",
        "Referer": "https://www.huawei.com/cn/my-huawei/login?redirect=https%3a%2f%2fwww.huawei.com%2fcn%2fmy-huawei",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",

    }
    req = request.Request(url,data=bytes(data, "utf-8"), headers=headers)
    rsp = opener.open(req)

    content = rsp.read().decode()
    print(content)
if __name__ == '__main__':
    url = "https://www.huawei.com/en/accounts/LoginPost"
    login(url)