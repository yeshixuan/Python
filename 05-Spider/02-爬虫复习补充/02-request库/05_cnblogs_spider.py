
"""
URL = "
https://www.cnblogs.com/cate/python/#p2
"""
import requests
from bs4 import BeautifulSoup

headers = {
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "accept-language":"zh-CN,zh;q=0.9,en;q=0.8",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
}
for i in range(1):
    url = "https://www.cnblogs.com/cate/python/#p{}".format(str(i+1))

    rsp = requests.get(url, headers=headers)

    soup = BeautifulSoup(rsp.text, "lxml")
    # titles = soup.find_all("a",{"class":"titlelnk"})
    titles = soup.select("h3 a[class='titlelnk']")
    hrefs = soup.select("a[class='lightblue']")
    names = soup.find_all("a", {"class":"lightblue"})
    pinluns = soup.select("span[class='article_comment'] ")
    reads = soup.select("span[class='article_view'] ")
    print(len(titles))
    print(len(names))
    print(len(hrefs))
    print(len(pinluns))
    for title,href,name,pinlun,read in zip(titles,hrefs,names,pinluns,reads):
        print(title.get_text())
        print(href["href"])
        print(name.get_text())
        comment = pinlun.get_text().strip().split("(")[0] + ":" + pinlun.get_text().strip().split("(")[1].strip(")")
        print(comment)
        view = read.get_text().strip().split("(")[0] + ":" + read.get_text().strip().split("(")[1].strip(")")
        print(view)
