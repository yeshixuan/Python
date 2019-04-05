import urllib

if __name__ == '__main__':
    url = "http://stock.eastmoney.com/news/1407,20170807763593890.html"

    rsp = urllib.request.urlopen(url)

    print(type(rsp))
    print(rsp)

    print("URL： {0}".format(rsp.geturl()))
    # 返回meta信息
    print("Info: {0}".format(rsp.info()))
    print("Code: {0}".format(rsp.getcode()))

    html = rsp.read()

    html = html.decode()

    print(html)

