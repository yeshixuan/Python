'''
https://book.douban.com/subject_search?search_text=python&cat=1001&start=%s0
工具：selenium + lxml time request
'''

from selenium import webdriver
from lxml import etree
import time

def get_web():
    url = "https://book.douban.com/subject_search?search_text=python&cat=1001&start=%s0"

    # 浏览器启动配置、
    option = webdriver.ChromeOptions()

    # 隐藏那句话
    option.add_argument("disable-infobars")

    driver = webdriver.Chrome(chrome_options=option)

    # 最大化窗口
    driver.maximize_window()
    driver.get(url)
    time.sleep(3)
    driver.save_screenshot("doubanread.png")

    fn = "douban.html"
    with open(fn, 'w', encoding="utf-8") as f:
        f.write(driver.page_source)

    get_book(fn)
    time.sleep(5)
    driver.quit()

def get_book(fn):
    with open(fn, "r", encoding="utf-8") as f:
        html = f.read()
    tree = etree.HTML(html)

    # names = tree.xpath('//div[@class="title"]/a/text()')
    names = tree.xpath('//div[@class="title"]/a')
    points = tree.xpath('//span[@class="rating_nums"]')
    infos = tree.xpath('//div[@class="meta abstract"]')

    for name,point,info in zip(names,points,infos):
        print("{0}  评分：{1}  书籍信息：{2}".format(name.text, point.text, info.text))

if __name__ == '__main__':
    get_web()
