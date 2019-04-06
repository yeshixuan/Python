import requests

baseurl = 'https://fanyi.baidu.com/sug'

data={
    # girl是翻译输入的英文内容，应该由用户输入，此处使用硬编码
    'kw':'girl'
}
headers = {
    'Content-Length':str(len(data))
}

rsp = requests.post(baseurl,data=data,headers=headers)
print(rsp.text)
print(rsp.json()) # 理解和json模块的区别
