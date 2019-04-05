'''
使用cookie登陆
http://www.renren.com/324901912/profile
必须再登陆状态下，cookie才有效
'''
from urllib import request, error
if __name__ == '__main__':
    url = "http://www.renren.com/965187997/profile"
    headers = {
        "Cookie": "anonymid=ju436x5je56ydz; depovince=GW; _r01_=1; JSESSIONID=abct4nO2i66Kk8xaWNTNw; ick_login=980a5863-a7f0-46a3-b82c-d3cbb42be049; jebecookies=63130de4-0129-4032-b149-f2f893607bdb|||||; _de=FDE3174024869784E481BC4A8D8B28816DEBB8C2103DE356; p=c0de56761f85203e318759b990aa419a2; first_login_flag=1; ln_uact=woyebiyun@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn321/20190105/2320/main_ba4W_27490000466d1986.jpg; t=f61f6a8199c996640b614462fff945422; societyguester=f61f6a8199c996640b614462fff945422; id=324901912; xnsid=125c5979; ver=7.0; loginfrom=null; jebe_key=789eed27-fd40-4691-8a67-21f770615094%7C90996c3f2fb5025e2dd0d4320f044278%7C1554470120581%7C1%7C1554470116933; wp_fold=0"
    }

    try:
        req = request.Request(url, headers=headers)
        rsp = request.urlopen(req)

        html = rsp.read().decode()
        print(html)

        with open("renren_cookie.html", "w", encoding="utf-8") as f:
            f.write(html)
    except error.URLError as e:
        print(e)
