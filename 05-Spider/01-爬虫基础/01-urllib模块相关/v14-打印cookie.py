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
        "email":"13119144223",
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

url = "http://www.baidu.com"

def proxy():
    # 使用代理步骤
    # 1. 设置代理地址
    proxy = {"http": "27.208.26.148:8060"}
    # 创建ProxyHandler
    proxy_handler = request.ProxyHandler(proxy)
    # 创建Opener
    opener = request.build_opener(proxy_handler)
    # 安装Opener
    request.install_opener(opener)

    # 现在如果访问url,则使用代理服务器
    try:
        rsp = request.urlopen(url)
        html = rsp.read().decode()
        # print(html)
    except error.URLError as e:
        print(e)
if __name__ == '__main__':
    '''
    执行完login之后，会得到授权之后的cookie
    我们尝试吧cookie打印出来
    '''
    proxy()
    login()
    print(cookie)
    for item in cookie:
        print(type(item))
        print(item)
        for i in dir(item):
            print(i)
