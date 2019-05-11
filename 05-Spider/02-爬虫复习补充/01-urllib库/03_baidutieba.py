# """
# http://tieba.baidu.com/f?kw=%E8%8B%8F%E5%A6%99%E7%8E%B2&ie=utf-8&pn=200
# http://tieba.baidu.com/f?kw=%E8%8B%8F%E5%A6%99%E7%8E%B2&ie=utf-8&pn=300
#
# """
# from urllib import request,parse
#
# url = "http://tieba.baidu.com/f?"
# name = input("请输入贴吧名称：")
# page = input("请输入贴吧页数")
#
# for i in range(int(page)):
#     qs = {
#         "kw":name,
#         "pn":i*50
#     }
#     qs_data = parse.urlencode(qs)
#
#     url = url + qs_data
#
#     headers = {
#         "User-Agent":"Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
#     }
#
#     req = request.Request(url=url, headers=headers)
#     rsp = request.urlopen(req)
#
#     html = rsp.read().decode()
#     fn = r"03_baidutieba\{}.html".format(str(i+1))
#     with open(fn, "w", encoding="utf-8") as f:
#         f.write(html)
#
#     # print(html)

from urllib import request
from urllib import error

try:
    # base_url = "http://www.w3school.com.cn/json/index.asp"
    base_url = "http://www.w3shool.com.cn/json/index.asp"
    rsp = request.urlopen(base_url)
    content = rsp.read().decode("gbk")
    print(content)

except error.HTTPError as e:
    print(e)
except error.URLError as e:
    print("url错误异常")

