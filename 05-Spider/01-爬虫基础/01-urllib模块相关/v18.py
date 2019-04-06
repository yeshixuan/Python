from urllib import request, parse
import json

if __name__ == '__main__':
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    kw = input("关键字")
    data = {
        "i": kw,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "15545423979047",
        "sign": "825cf7bfdb63cb3092b9ef9241592c53",
        "ts": "1554542397904",
        "bv": "9c4fffad2fb69d08cd130e408e0f8108",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME",
        "typoResult": "false"
    }
    data = parse.urlencode(data).encode()
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        # "Accept-Encoding": "gzip, deflate",
        # "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Length": len(data),
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=533311125@10.168.8.64;OUTFOX_SEARCH_USER_ID_NCOO=1708835487.6402843;JSESSIONID=aaaaIlm0FI31kfSDD8XNw; ___rl__test__cookies=1554542397897",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    req = request.Request(url, data=data, headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    print(html)
