'''
url = "http://passport.pifa.yunmayi.com/login"
username: 57105
password: sfsfs
url = "http://pifa.yunmayi.com/"
'''
from urllib import parse, request
import requests
from http import cookiejar

import ssl
# 忽略安全问题
ssl._create_default_https_context = ssl._create_unverified_context

cookie = cookiejar.CookieJar()
cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()
opener = request.build_opener(cookie_handler, https_handler, http_handler)
def login():
    url = "http://passport.pifa.yunmayi.com/login"
    data = {
        "username":"",
        "password":""
    }
    data = parse.urlencode(data).encode()
    headers = {
        # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        # "Accept-Encoding": "gzip, deflate",
        # "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        # "Cache-Control": "max-age=0",
        # "Connection": "keep-alive",
        "Content-Length": len(data),
        # "Content-Type": "application/x-www-form-urlencoded",
        # "Cookie": "PHPSESSID=mnj3fgpvjg3fth9mkqmb1cn2t1",
        # "Host": "passport.pifa.yunmayi.com",
        # "Origin": "http://passport.pifa.yunmayi.com",
        # "Referer": "http://passport.pifa.yunmayi.com/login",
        # "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }

    req = request.Request(url, data=data, headers=headers)
    rsp = opener.open(req)

def defalt():
    url = "http://pifa.yunmayi.com/"

    rsp = opener.open(url)
    html = rsp.read().decode()
    print(html)

if __name__ == '__main__':
    login()
    defalt()