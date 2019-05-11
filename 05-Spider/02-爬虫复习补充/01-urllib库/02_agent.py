"""
http://www.langlang2017.com/index.html
http://www.langlang2017.com/route.html
http://www.langlang2017.com/FAQ.html
"""
from urllib import request
import random
def spider(url):
    user_agent_list = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    ]

    # 随机获取useragent
    user_agent = random.choice(user_agent_list)

    # 设置headerst头部信息
    headers = {
        "User-Agent":user_agent
    }

    # 构建request对象
    req = request.Request(url=url, headers=headers)
    # print(type(req))
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    # print(html)

    name = url.split("/")[-1]
    # print(name)
    with open(name, "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == '__main__':
    url_list = [
        "http://www.langlang2017.com/index.html",
        "http://www.langlang2017.com/route.html",
        "http://www.langlang2017.com/FAQ.html"
    ]


    for url in url_list:
        spider(url)