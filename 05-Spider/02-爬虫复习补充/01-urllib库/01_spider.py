# from urllib import request
# url = "http://www.baidu.com"
# rsp = request.urlopen(url)
# print(rsp)
# content = rsp.read().decode()
# print(type(content))
# print(content)

'''
url = "http://www.w3school.com.cn/php/index.asp"
'''

from urllib import request
response = request.urlopen("http://www.w3school.com.cn/php/index.asp")
content = response.read().decode("gbk")
print(content)
