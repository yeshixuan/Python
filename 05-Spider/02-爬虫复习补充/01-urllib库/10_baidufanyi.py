"""
post请求
    post请求返回的一般都是json数据
https://fanyi.baidu.com
"""

from urllib import request, parse
import json
def bd_spider(content):
    url = "https://fanyi.baidu.com/sug"
    data = {
        "kw":content
    }

    data = parse.urlencode(data).encode()

    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        # "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "content-length":len(data),
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "cookie": "BAIDUID=1452556C82522122C3DDA2ED1B6244F0:FG=1; PSTM=1548584446; BIDUPSID=4DB097BC4BD2154DD80270D149325700; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1420_21104_28518_28769_28720_28964_28834_28585; BDSFRCVID=iPKOJeC6271Jk8j9cdvEhw6zyJLwxccTH6aI4fK-DHYyTu3qIgqSEG0PeM8g0Ku-JGzGogKKKgOTHICF_2uxOjjg8UtVJeC6EG0P3J; H_BDCLCKID_SF=tRk8oK-atDv5HJRNqRjV-tAjqxby26nbbg5eaJ5n0-nnhPb-bRKB-P04WHbN3fnNK67TQnbvfpovDnKRy6C5e55-jGDjqbQX2COXsROs2ROOKRcgq4bohjPt0-R9BtQmJJufolcofnFBHnbCQt7bjRI-y4vfhPJ2Qg-q3lI25qkVshnX2qOhDn_PbpQg0x-jLITuVn0MW-KVOl3uQPnJyUPUbPnnBUcm3H8HL4nv2JcJbM5m3x6qLTKkQN3TJMIEK5r2SCDMfC-a3e; PSINO=5; delPer=0; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1557657783; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1557657795; yjs_js_security_passport=063b3fb8f2504b0d3678149a1e594f3f40ead5b4_1557657800_js; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D",
        "origin": "https://fanyi.baidu.com",
        "referer": "https://fanyi.baidu.com/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
    }
    req = request.Request(url, data=data, headers=headers)
    rsp = request.urlopen(req)

    # post请求返回的一般是json格式
    text = rsp.read().decode()

    json_data = json.loads(text)
    for item in json_data["data"]:
        print(item["k"],item["v"])



if __name__ == '__main__':
    content = input("请输入你要翻译的内容：")
    bd_spider(content)