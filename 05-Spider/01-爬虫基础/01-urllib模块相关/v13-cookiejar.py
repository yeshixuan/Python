from urllib import request, parse, error
from http import cookiejar

# 创建cookiejar的实例
cookie = cookiejar.CookieJar()

# 生成cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)

# 创建http请求管理器
http_handler = request.HTTPHandler()

# 创建http请求管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)

def login():
    '''
    负责初次登陆
    需要输入用户名密码，用来获取cookie凭证
    :return:
    '''
    # 此url需要从登录form的action属性中提取
    url = "http://www.renren.com/PLogin.do"

    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
    # 此键值需要从登录form的两个对应input中提取name属性
    data = {
        "email":"131191442230",
        "password":"123456"
    }
    try:
        # 把数据进行编码
        data = parse.urlencode(data).encode()

        # 创建一个请求对象
        req = request.Request(url, data=data, headers=headers)

        # 使用opener发起请求
        rsp = opener.open(req)

    except error.URLError as e:
        print(e)

def getHomePage():
    url = "http://www.renren.com/965187997/profile"

    # 如果已经执行了login函数，则opener自动已经包含相应的cookie值
    rsp = opener.open(url)

    html = rsp.read().decode()
    with open("renren_cookiejar.html", "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == '__main__':
    login()
    getHomePage()

