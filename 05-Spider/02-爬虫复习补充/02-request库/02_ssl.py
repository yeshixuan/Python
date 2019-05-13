import requests

url = "https://kyfw.12306.cn/otn/"
rsp = requests.get(url,verify=True)
print(rsp.text)