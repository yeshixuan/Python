'''
利用selenium模拟豆瓣登陆
需要输入验证码
思路：
1. 选择账户登录
2. 输入账号密码登陆

'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = "https://accounts.douban.com/passport/login?source=book"

driver = webdriver.Chrome()
driver.get(url)

time.sleep(4)

# 账号登陆
driver.find_element_by_class_name("account-tab-account").click()
time.sleep(1)

driver.find_element_by_id("username").send_keys("sfsfsfs")
time.sleep(1)

driver.find_element_by_id("password").send_keys("sfsfsfsf")
time.sleep(1)

# driver.find_element_by_class_name("btn btn-account").click() 不可行
driver.find_element_by_xpath('//a[@class="btn btn-account btn-active"]').click()
# driver.find_element_by_xpath('//*[@id="account"]/div[2]/div[2]/div/div[2]/div[1]/div[4]/a').click()
time.sleep(4)

driver.save_screenshot("logined.png")

with open("douban.html", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

driver.quit()

