'''
任务：
爬取斗鱼直播内容
https://www.douyu.com/directory/all
<h3 class="ellipsis">房间标签
<span class="dy-name ellipsis fl">米儿啊i</span>
<span class="dy-num fr"  >108万</span>
思路：
1. 利用selenium得到页面内容
2. 利用xpath或者bs等在页面中进行信息提取
'''

from selenium import webdriver
from bs4 import BeautifulSoup

class Douyu():
    # 用这种形式为后面的scrapy做铺垫
    # 初始化方法
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "https://www.douyu.com/directory/all"

    def douyu(self):
        self.driver.get(self.url)

        while True:
            # 用lxml解析
            soup = BeautifulSoup(self.driver.page_source, "lxml")

            # 返回当前页面所有房间列表和人数
            titles = soup.find_all("h3",{"class":"DyListCover-intro"})
            names = soup.find_all("h2", {"class":"DyListCover-user"})
            nums = soup.find_all("span", {"class":"DyListCover-hot"})
            for title,name,num in zip(titles,names,nums):
                print("房间：{0} 主播：{1} 人数：{2}".format(title.get_text(), name.get_text(), num.get_text()))
            break

    def destr(self):
        self.driver.quit()



if __name__ == '__main__':
    douyu = Douyu()
    douyu.setUp()
    douyu.douyu()
    douyu.destr()



