'''
- css选择器
    - 使用soup.select, 返回一个列表
    - 通过标签名称: soup.select("title")
    - 通过类名： soup.select(".content")
    - id查找: soup.select("#name_id")
    - 组合查找: soup.select("div #input_content")
    - 属性查找: soup.select("img[class='photo'])
    - 获取tag内容： tag.get_text
'''
from urllib import request
from bs4 import BeautifulSoup
def get_info(info):
    url = 'https://hr.tencent.com/'+ info
    rsp = request.urlopen(url)
    html = rsp.read()

    soup = BeautifulSoup(html, 'lxml')
    td_list1 = soup.select('div[class="lightblue"]')
    td_list2 = soup.select('ul[class="squareli"]')
    print(len(td_list2))
    print(len(td_list1))
    print(td_list2)
    print(td_list1)
    print(td_list1[0].get_text())
    print(td_list2[0].get_text())
    print()
    print(td_list1[1].get_text())
    print(td_list2[1].get_text())

def qq():
    url = 'https://hr.tencent.com/position.php?&start=10#a'
    rsp = request.urlopen(url)
    html = rsp.read()

    # 提取数据
    # 用bs解析
    soup = BeautifulSoup(html, 'lxml')

    # 创建css选择器，得到相应tags
    tr1 = soup.select('tr[class="even"]')
    tr2 = soup.select('tr[class="odd"]')
    trs = tr1 + tr2

    for tr in trs:
        name = tr.select("td[class='l square'] a")[0].get_text()
        addr = tr.select("td")[3].get_text()
        time = tr.select("td")[4].get_text()
        catalog = tr.select('td')[1].get_text()
        print(name)
        print("职位类别："+catalog)
        catalog = tr.select('td')[2].get_text()
        print("招聘人数："+ catalog)
        print("工作地点：" + addr)
        print("发布时间：" + time)

        # 属性不用get_text()
        # info = tr.select("td a")[0].attrs["href"]
        info = tr.select("td a")[0]
        print(info["href"])




if __name__ == '__main__':
    info = 'position_detail.php?id=47101&keywords=&tid=0&lid=0'
    # get_info(info)
    qq()