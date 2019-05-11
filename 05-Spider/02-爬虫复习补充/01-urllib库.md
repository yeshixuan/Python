# 就业方向
- 数据分析、人工智能、python的web开发，爬虫

# 网络爬虫是否合法
- 盗亦有道
    - Robots协议（爬虫协议）：通过它告诉你引擎有哪些页面可以爬取，哪些页面不可爬取
    - 淘宝机器人：https://www.taobao.com/robots.txt
    
# 关于Python爬虫，我们需要学习的有：
1. Python基础语法学习（基础知识）
2. HTML页面的内容抓取（数据抓取） 
3. HTML页面的数据提取（数据清洗）
4. Scrapy框架以及scrapy-redis分布式策略（第三方框架）
5. 爬虫（Spider）,反爬虫(Anti-Spider),反反爬虫（Anti-Anti-Spider）之间的斗争...

# Python爬虫流程
- 主要分为三部分：（1）获取网页：------（2）解析网页（获取数据）------存储数据

## 三个流程的技术实现
1. 获取网页
    - 获取网页的基础技术：urllib，requests,selenium
    - 获取网页的进阶技术：多线程怕抓取，登陆抓取，突破ip显示和服务器抓取
2. 解析网页
    - 解析网页的基础技术：re正则表达式，BeautifulSoup和lxml
    - 解析网页的进阶技术：解决中文乱码
3. 存储数据
    - 存储数据的基本技术：存入txt文件和存入csv文件
    - 存储数据的进阶技术：存储mysql, mongoDB数据库中

## 搭建python爬虫平台
- Python的安装
- 集成环境Anconda安装
- 使用pip工具安装第三方库

## urllib库的基本使用
- urllib是python中请求url链接的官方标准库
- 在Python中主要为urllib和urllib2，在python3中整合成了urllib
- urllib2在python3.x中被改为urllib.request
- 而urllib3则是增加了链接池等功能，两者相互都有互补的部分
- urllib官方地址：https://docs.python.org/3/library/urllib.html

## urllib.request
- urllib中，request这个模块主要负责构造和发起网络请求，并在其中加入Headers,Proxy等
### 对于静态地址，直接根据url进行数据的抓取

## 发起GET请求
        
        from urllib import request
        rsp = request.urlopen('http://www.baidu.com')
        type(rsp)
        Out[6]:http.client.HTTPResponse
        print(rsp.read().decode())# 数据为二进制数据需转码

## 发起POST请求
- urlopen()默认的访问方式为GET，当在urlopen()方法中传入data参数是，则会发起post请求
- 注意：传入的data数据需要为bytes格式
- 设置timeout参数还可以设置超时时间，如果请求时间超出，那么会抛出异常
    from urllib import request
    rsp = request.urlopen('http://httpbin.org',data=b"word=hello",timeout=10)
    print(rsp.red().decode()

## 添加Headers
- 通过urllib发起的请求会有默认的一个Headers：“User-Agent":"Python-urllib/3.6",指明请求时由urllib发送的。
- 所以遇到一些User-Agent的网站是，我们需要自定义Headers,而这需要借助于urllib.request中的Request对象。
    
    from urllib import request
    url = 'http://httpbin.org/get'
    headers = {"User-Agent":""}
    需要使用url和headers生成一个Request对象，然后将其传入urlopen方法中
    req = request.Request（url，headers=hearder)
    rsp = request.urlpen(req)
    print(rsp.read().decode())
    
## Request对象
- 如上所示，urlopen()方法中不止可以传入字符串格式的url,也可以传入一个Request对象来扩展功能，Request对象如下所示：
    class urllib.request.Request(url,data=None,headers={},crigin_req_host=None,unverifiable=False,method=None)
- 构造Request对象必须传入url参数，data数据和headers都是可选的
- Request方法可以使用method参数来自由选择请求的方法，比如PUT，DELETE等，默认GET

## urllib.parse
- urllib.parse是urllib中用来解析各种数据格式的模块

## urllib.parse.quote
- 在urllib中，是只能使用ASCII中包含的字符的，也就是说。ASCII不包含的特殊字符，以及中文等字符都不可以在urllib中使用的，而我们有时候又有将中文字符加入到url中的需求，例如百度的搜索地址：https://www.baidu.como/s?wd=南北
    - ?之后的wd参数，则是我们搜索的关键字，那么我们事先的方法就是将特殊字符进行url编码，转换成url可以传输的格式，urllib中可以使用quote()方法来实现这个功能。》》》
        from urllib import parse
        >>> keyword = “南北”
        >>> parse.quote(keyword)
        '%E5%24%E2#.....'
- 如果需要将编码后的数据转换回来，可以使用unquote()方法 >>> parse.unquote('%E5%24%E2#.....')
  '南北'

## urllib.parse.urlencode
- 在访问url时，我们常常需要传递很多的url参数，而如果用字符串的方法却拼接url的话，会比较麻烦，所以urllib中提供了urlencode这个方法来凭借url参数
    >>> from urllib import parse
    >>> params = {'wd':'南北','code':'i','height':'188'}
    >>> parse.urlencode(params)
    'wd=%E5%24%E2#.....&code=1&height=188'
    
## urllib.error
- 在urllib中主要设置了两个异常，一个是URLError,一个是HTTPError，HTTPError是URLError的子类
- HTTPError还包含了三个属性：
    - code: 请求的状态码
    - reason：请求的原因
    - headers：相应的报头
    
## 添加Coikie
- 为了请求时能带上Cookie的信息，我们需要重新构造一个opener
- 使用request.build_opener方法来进行构造opener,将我们想要传递的cookie配置到opener中，然后使用这个opener的open方法来发起请求
    
    from http import cookiejar
    form urllib import request
    url = 'http://httpbin.org/cookies
    .创建一个cookiejiar对象
    cookie = cookiejar.CookieJar()
    .使用HTTPCookiePrcessor创建cookie处理器
    cookies = request.HTTPCookieProcessor(cookie)
    .并以它为参数创建opener对象
    opener = request.build_opener(cookies)
    .使用这个opener来发起请求
    rsp = opener.open(url)
    print(rsp.read().decode())
    
- 或者也可以把这个生成的opener使用install_opener方法来设置为全局的，则之后使用urlopen方法发起请求时，都会带上这个cookie
    
    .将这个opener设置为全局的opener
    request.install_opener(opener)
    rsp = request.urlopen(url)
    
## 设置Proxy代理
- 使用爬虫来爬取数据的时候，常常需要使用代理来隐藏我们的真实IP
    
    from urllib import request
    url = 'http://httpbin.org/ip'
    proxy = {'http':'23.45.23.11:80','https':'34.234.42.123:8080'}
    .创建代理处理器
    proxies = request.ProxyHandler(proxy)
    .创建opener对象
    opener = request.build_opener(proxies)
    rsp = opener.open(url)
    print(rsp.read().decode())