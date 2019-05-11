from urllib import request,parse,error
from http import cookiejar
import json

def login():
    url = 'http://www.jobbole.com/wp-admin/admin-ajax.php'

    data = {
        'action': 'user_login',
        'user_login': 'augsnano',
        'user_pass': '123456789',
        'remember_me': '1',
        # 登陆后重新定向的地址
        'redirect_url': 'http://date.jobbole.com/5535/'
    }
    data = parse.urlencode(data).encode()

    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        "Connection": 'keep-alive'
    }
    f = r'cookie2.txt'
    cookie_handler = cookiejar.MozillaCookieJar()
    http_handler = request.HTTPCookieProcessor(cookie_handler)
    opener = request.build_opener(http_handler)

    req = request.Request(url,data=data,headers=headers)

    rsp = opener.open(req)

    html = rsp.read().decode()
    html = json.loads(html)
    print(html)
    cookie_handler.save(f,ignore_expires=True,ignore_discard=True)
def getInfo():
    url = 'http://date.jobbole.com/wp-admin/admin-ajax.php'

    data = {
        'action': 'jb_bookmark',
        'bookType': '1',
        'siteId': '10',
        'itemId': '5535',
        'itemType': '1'
    }
    data = parse.urlencode(data).encode()

    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        "Connection": 'keep-alive'
    }
    req = request.Request(url, data=data, headers=headers)
    f=r'cookie2.txt'
    cookie = cookiejar.MozillaCookieJar(f)
    cookie.load(f, ignore_discard=True, ignore_expires=True)
    cookie_handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(cookie_handler)

    rsp = opener.open(req)
    html = rsp.read().decode()
    html = json.loads(html)
    print(html)
    with open('jobole.txt','w',encoding='utf-8') as f:
        f.write(str(html))

if __name__ == '__main__':
    login()
    getInfo()
