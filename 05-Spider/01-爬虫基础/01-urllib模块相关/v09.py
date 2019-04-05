'''
访问一个网址
更改自己的UserAgent进行伪装
'''
from urllib import request, error

if __name__ == '__main__':
    # url = "http://www.baidu.com"
    url = "https://www.baidu.com"

    try:
        # 使用head方法伪装UA
        # headers = {}
        # headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36"

        # 使用add_header方法
        req = request.Request(url)
        req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36")
        # req = request.Request(url, headers=headers)
        rsp = request.urlopen(req)

        # rsp = request.urlopen(url)
        html = rsp.read()
        print(type(html))
        print(html)
    except error.URLError as e:
        print(e)