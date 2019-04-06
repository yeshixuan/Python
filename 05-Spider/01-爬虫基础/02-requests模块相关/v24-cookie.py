'''
cookie requests可以自动处理cookie信息
    cookie = rsp.cookies
    cookie_dict = requests.utils.dict_from_cookiejar(cookie)
'''
import requests

proxy = {
    "http":"211.23.149.29:80",
    "https":"163.172.215.202:3128"
}
url = "http://www.renren.com/PLogin.do"

data = {
    "email":"",
    "password":""
}
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

# rsp = requests.post(url, data=data, headers=headers)
rsp = requests.get("http://www.baidu.com", proxies=proxy)
cookie = rsp.cookies
cookie_dict = requests.utils.dict_from_cookiejar(cookie)
print(cookie_dict)