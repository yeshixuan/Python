import requests

url = "https://item.jd.com/1250438.html"
try:
    response = requests.get(url) # 发起get请求
    print(response.status_code) # 获取状态码
    print(response.url) # 获取完整url地址
    print(response.encoding)
    print(response.apparent_encoding) # 获取原文编码类型
    response.encoding = response.apparent_encoding # 解决乱码
    print(type(response.text)) # 响应得到字符串
    print(type(response.content)) # 响应得到字节流
    # print(response.text)
    print(response.cookies)
    CookiesJar = response.cookies
    print(CookiesJar)
    cookie = requests.utils.dict_from_cookiejar(CookiesJar)
    print(cookie)
except Exception as e:
    print(e)
