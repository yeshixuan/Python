'''
URLError的使用
'''

from urllib import request, error

if __name__ == '__main__':
    # url = "http://www.baidddddddddddddddddddu.com"
    # url = "https://www.baidddddddddddddddddddu.com"
    url = "http://www.sipo.gov.cn/www"
    try:
        req = request.Request(url)
        rsp = request.urlopen(req)

        html = rsp.read()
        print(html)
    # 越是子类的越放上面
    except error.HTTPError as e:
        print("HTTPError: {0}".format(e.reason))
        print("HTTPError: {0}".format(e))
    except error.URLError as e:
        print("URLError: {0}".format(e.reason))
        print("URLError: {0}".format(e))

    except Exception as e:
        print(e)