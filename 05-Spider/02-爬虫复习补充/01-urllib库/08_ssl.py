from urllib import request
import ssl

import gzip
from io import BytesIO

# ssl免验证
ssl._create_default_https_context = ssl._create_unverified_context

headers = {

        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        # "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie":"Jo0OQK=5C072C8DAE0CFB5BD09AB582766BC669A3B12286FCC97836AB2262E0065E65C1E2D6FE5A41F5E2143B623F99F95F312EF7FFCF5ADC99BED68B1153EA4FC910FF4287EA20E611224F11EFB4BD9AD05BFA505FB4BD9AD05BFA505558E68D2DBDDE9ACGJ1Z1Yg==",
        "Host": "inv-veri.chinatax.gov.cn",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
}

base_url = "https://inv-veri.chinatax.gov.cn/"

req = request.Request(url=base_url, headers=headers)
rsp = request.urlopen(req)

html = rsp.read()


# 解决方法1
#b'\x1f\x8b\x08”开头的数据是经过gzip压缩过的数据,需要解压
buff = BytesIO(html)
f=gzip.GzipFile(fileobj=buff)
res = f.read().decode()
print(res)

# 解决方法2 使用requests