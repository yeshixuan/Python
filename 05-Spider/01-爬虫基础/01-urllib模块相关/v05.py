'''
利用parse模块模拟post请求
分析百度词典
分析步骤：
1. 打开F12
2. 尝试输入单词girl，发现每敲一个字母后都有请求
3. 请求地址是 http://fanyi.baidu.com/sug
4. 利用NetWork-All-Hearders，查看，发现FormData的值是 kw:girl
5. 检查返回内容格式，发现返回的是json格式内容==>需要用到json包
'''
from urllib import request, parse
import json
'''
大致流程是：
1. 利用data构造内容，然后urlopen打开
2. 返回一个json格式的结果
3. 结果就应该是girl的释义
'''

if __name__ == '__main__':
    url = "https://fanyi.baidu.com/sug"

    kw = input("Input your keyword:")
    # 存放用来模拟form数据，一定是dict格式
    data = {
        "kw":kw
    }

    # 需要使用parse模块对data进行编码
    # post请求必须是bytes格式
    data = parse.urlencode(data).encode()

    print(type(data))

    # 有了data, url，就可以尝试发出请求了
    # urlopen不能用请求头headers
    rsp = request.urlopen(url, data=data)

    json_data = rsp.read().decode()

    html = json.loads(json_data)

    text = html["data"][0]
    for k,v in text.items():
        print(k,":",v)

    # print(type(text))
    # print(text)