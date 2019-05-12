"""
post请求：
    一般网址是不会变的
http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
v1.js肯定不是
"""
"""
Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Connection: keep-alive
Content-Length: 238
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: OUTFOX_SEARCH_USER_ID=533311125@10.168.8.64; OUTFOX_SEARCH_USER_ID_NCOO=1708835487.6402843; JSESSIONID=aaaGD91zL-5TBclWwTRQw; ___rl__test__cookies=1557658975395
Host: fanyi.youdao.com
Origin: http://fanyi.youdao.com
Referer: http://fanyi.youdao.com/
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36
X-Requested-With: XMLHttpRequest
"""
"""
i: kw
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
salt: 15576589754008
sign: b98a623ff2775acbea816642655d60c4
ts: 1557658975400
bv: 015fc184d636e7721670f9f2ddb71146
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_REALTlME
"""
"""
i: girl
salt: 15576591798430
sign: 0d59cb3beee6685b0b84c943a1daeb30

"""
"""
r = "" + (new Date).getTime()
salt:i = r + parseInt(10 * Math.random(), 10)
salt:"" + (new Date).getTime() + parseInt(10 * Math.random(), 10)
sign: n.md5("fanyideskweb" + e + i + "@6f#X3=cCuncYssPsuRUE")
sign: n.md5("fanyideskweb" + kw + salt + "@6f#X3=cCuncYssPsuRUE")
"""
from urllib import request, parse
import time
import random
import hashlib
import json

def get_salt():
    salt = str(int(time.time() *1000)) + str(random.randint(0,9))
    return salt
def get_md5(content):
    m = hashlib.md5()
    m.update(bytes(content, "utf-8"))
    sign = m.hexdigest()
    return sign
def get_sign(key,salt):
    content = "fanyideskweb" + key + salt + "@6f#X3=cCuncYssPsuRUE"
    sign = get_md5(content)
    return sign

def fanyi(key):
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    salt = get_salt()
    data = {
        "i":key,
        "from":"AUTO",
        "to":"AUTO",
        "smartresult":"dict",
        "client":"fanyideskweb",
        "salt":salt,
        "sign":get_sign(key, salt),
        "bv":"015fc184d636e7721670f9f2ddb71146",
        "doctype":"json",
        "version":"2.1",
        "keyfrom":"fanyi.web",
        "action":"FY_BY_REALTlME",
    }
    data = parse.urlencode(data).encode()

    headers = {
        "Accept":"application/json, text/javascript, */*; q=0.01",
        "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
        "Connection":"keep-alive",
        "Content-Length":len(data),
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie":"OUTFOX_SEARCH_USER_ID=533311125@10.168.8.64; OUTFOX_SEARCH_USER_ID_NCOO=1708835487.6402843; JSESSIONID=aaaGD91zL-5TBclWwTRQw; ___rl__test__cookies=1557658975395",
        "Host":"fanyi.youdao.com",
        "Origin":"http://fanyi.youdao.com",
        "Referer":"http://fanyi.youdao.com/",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        "X-Requested-With":"XMLHttpRequest",
    }

    req = request.Request(url, data=data, headers=headers)
    rsp = request.urlopen(req)

    html = rsp.read()
    json_data = json.loads(html)

    try:
        items = json_data["smartResult"]["entries"]
        for item in items:
            print(item)
    except Exception as e:
        print("无法正确翻译您输入的内容！")


if __name__ == '__main__':
    while True:
        key = input("请输入要翻译的内容(按q退出)：")
        if key == "q":
            break
        fanyi(key)