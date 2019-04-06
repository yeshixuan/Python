from urllib import request
from bs4 import BeautifulSoup


url = 'http://www.baidu.com'

rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

# print(soup.prettify)

titles = soup.select("title")
print(titles)

print("==" * 20)
# metas = soup.select("meta")
# metas = soup.select("meta[content='IE=Edge']")
metas = soup.select("meta[http-equiv='X-UA-Compatible']")
print(metas)