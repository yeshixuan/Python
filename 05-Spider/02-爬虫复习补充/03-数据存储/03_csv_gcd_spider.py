import csv
import requests
from lxml import etree
import re
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
}
url = "http://www.seputu.com/"
rsp = requests.get(url, headers=headers)
html = etree.HTML(rsp.text)

titles = html.xpath('//*[@class="mulu"]')

rows = []
for item in titles:
    title = item.xpath(".//h2/text()")
    if len(title)>0:
        title = title[0]
        infos = item.xpath(".//li/a/@title")
        hrefs = item.xpath(".//li/a/@href")
        for info,href in zip(infos,hrefs):
            # print(info)
            pattern = re.compile(r"\s*\[(.*)\]\s*(.*)")
            match = pattern.search(info)
            time = match.group(1)
            # real_title = info.split("]")[-1]
            real_title = match.group(2)
            # print(real_title)
            content = (title, real_title, href, time)
            # print(content)
            rows.append(content)


headers = ["title", "real_title", "href", "date"]
with open("gcd_csv.csv", "a", newline="", encoding="utf-8") as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)