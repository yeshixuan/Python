import requests
from lxml import etree
import os
# def down(url):
#     headers = {}
#     rsp = requests.get(base_url, headers=headers)
#     html = etree.HTML(rsp.text)
#     return html
# @down
def mz_spider(base_url, headers):
    rsp = requests.get(base_url, headers=headers)
    html = etree.HTML(rsp.text)

    #获取详情页信息
    img_src = html.xpath('//ul[@id="pins"]/li/a/@href')
    for img_url in img_src:
        defail_spider(img_url)
def defail_spider(img_url):
    headers = {
        "Upgrade-Insecure-Requests": "1",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
    }
    rsp = requests.get(img_url)
    html = etree.HTML(rsp.text)

    # 获取标题
    title = html.xpath("//h2/text()")[0]
    # 获取图片总的页数
    page_num = html.xpath('//div[@class="pagenavi"]/a/span/text()')[-2]

    print(title)
    # print(page_num)
    get_img(title, page_num,img_url)

def get_img(title, page_num,img_url):
    headers = {
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3)",
    }
    for i in range(int(page_num)):
        url = img_url + "/" + str(i+1)
        print(url)
        rsp = requests.get(url,headers=headers)
        html = etree.HTML(rsp.text)

        img_href = html.xpath("//div[@class='main-image']/p/a/img/@src")[0]

        # print(img_href)
        headers = {
            "Referer": url,
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        }
        # 不能创建两级文件夹
        root = "meizitu/" + title
        path = root + "/" + img_href.split("/")[-1]
        rsp = requests.get(img_href,headers=headers)
        try:
            if not os.path.exists(root):
                os.mkdir(root)
            if not os.path.exists(path):
                with open(path, "wb") as f:
                    f.write(rsp.content)
                    print("{}保存成功".format(path))
            else:
                print("图片已存在")
        except Exception as e:
            print("爬取失败原因：",e)






if __name__ == '__main__':
    headers = {
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "accept-language":"zh-CN,zh;q=0.9,en;q=0.8",
        "cache-control":"max-age=0",
        "cookie":"Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1557720067; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1557720208",
        "if-modified-since":"Sun, 12 May 2019 16:02:51 GMT",
        "referer":"https://www.mzitu.com/",
        "upgrade-insecure-requests":"1",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.3",
    }

    for i in range(1,2):
        base_url = "https://www.mzitu.com/page/{}/".format(str(i))
        mz_spider(base_url, headers)
