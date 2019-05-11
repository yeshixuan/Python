'''
任务：
1. 通过selenium模拟对页面元素的控制

'''

from selenium import webdriver
import time

driver = webdriver.Chrome()
url = "https://www.baidu.com"
driver.get(url)

# 通过js来控制网页内容
# 需要先把js写出来
# 通过execute_script执行

# 美化输入框，输入框id是kw
js = "var q=document.getElementById('kw');q.style.border='2px solid red';"

# 执行代码
driver.execute_script(js)
time.sleep(3)
driver.save_screenshot("redbaidu.png")

# js隐藏相应元素，我们这里吟唱logo
img = driver.find_element_by_xpath('//*[@id="lg"]/img[1]')

# faderout()淡出
driver.execute_script('$(arguments[0]).fadeOut()',img)
time.sleep(3)
driver.save_screenshot("noimg.png")

# 滚动滑动条到最底下
js = "$('.scroll_top'').click(function(){$('html, body').animate({scrollTop:'0px'}, 800)});"
driver.execute_script(js)

time.sleep(3)
driver.save_screenshot('nullbaidu.png')

driver.quit()