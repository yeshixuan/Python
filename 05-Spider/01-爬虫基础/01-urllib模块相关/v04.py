from urllib import request, parse

'''
掌握对url进行参数编码的方法
需要使用parse模块
'''

if __name__ == '__main__':
    base_url = "http://www.baidu.com/s?"
    wd = input("Input your keyword:")

    # get方法，利用参数给服务器传递信息
    # 要想使用data, 需要使用字典结构
    qs = {
        "wd":wd
    }

    # 转换url编码
    qs = parse.urlencode(qs)
    # print(qs)

    full_url = base_url + qs
    print(full_url)

    # 如果直接用可读的才参数的url，是不能访问的
    # rsp = request.urlopen("http://www.baidu.com/s?wd=大熊猫")
    rsp = request.urlopen(full_url)

    html = rsp.read()

    html = html.decode()
    print(html)
