'''
http://tieba.baidu.com/f?kw=%E8%8B%8F%E5%A6%99%E7%8E%B2&ie=utf-8&pn=100
http://tieba.baidu.com/f?kw=%E8%8B%8F%E5%A6%99%E7%8E%B2&ie=utf-8&pn=150
'''

from urllib import request, parse

def get_tieba(kw, pn):
    for i in range(pn):
        page = str(i * 50)
        url = "http://tieba.baidu.com/f?"

        data = {
            "kw": kw,
            "ie": "utf-8",
            "pn": page,
        }
        data = parse.urlencode(data).encode()

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }

        req = request.Request(url, data=data, headers=headers)

        rsp = request.urlopen(req)

        html = rsp.read().decode()

        with open("./baidu/{}.html".format(str(i+1)), "w", encoding="utf-8") as f:
            f.write(html)



if __name__ == '__main__':
    get_tieba("苏妙玲", 10)