## Requests：让HTTP服务人来
- 虽然Python的标准库中 urllib模块已经包含了平常我们使用的大多数功能。但是它的API使用起来让人感觉不太好，而Requests自称“HTTP for Humans”，说明使用更方便简洁

        > Requests是唯一的一个非转基因的Python HTTP库，人类可以安全享用
- Requests是继承了urllib的所有特性，Requests支持HTTP链接保持和连接池，支持使用cookie保持会话，支持文件上传，支持自动确定响应内容的编码，支持国际化的URL和POST数据自动编码。

        > Requests的底层实现其实就是urllib3
        > Requests的文档非常完备，中文文档也相当不错，Requests能完全满足当前网络的需求，支持Python 2.6-3.x，而且能在PyPy下完美运行
        > 开源地址：[https://github.com/requests/requests]
        > 中文文档API[http://docs.python-requests.org/en/master/]http://cn.python-requests.org/zh_CN/latest/

## 安装方式
- 利用pip安装或者利用conda安装
    - pip install requests
    
## 基本GET请求（headers参数和parmas参数）
1. 最基本的GET请求可以直接用get方法 response = requests.get('http://www.baidu.com/")
    - 也可以这么写
        - response = requests.request('get',url)
2. 添加headers和查询参数
3. 如果想添加headers可以传入headers参数来增加请求头中的headers信息，如果想要将参数放到url中传递，可以利用parmas参数
    
         import requests
         kw = {"kw":"长城"}
         headers = {"User-Agent":'xxxxx'}
         # parmas 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
         response = requests.get(url,parmas=kw,headers=headers)
         # 查看相应的内容，response.text返回的是Unicode格式的数据(字符串)
         print(response.text)
         # 查看相应内容，response.content返回的是字节流数据
         print(response.content)
         # 查看完整url地址
         print(response.url)
         # 查看相应头部字符编码
         print(response.encoding)
         # 查看响应码
         print(response.status_code)
     - 注意：面试时问你requests的两种数据格式是什么，就是text和content
 - 使用response.text时，Requests会基于HTTP相应的文本编码自动解码成内容，大多数字符都能被无缝地解码
 
## 基本POST请求（data参数）
 1. 传入data数据
 > 对于POST请求来说，我们一般需要为他增加一些参数，那么最近本的传递方法可以利用data参数。
 >>> rsp = requests.post(url,data={'key':'value'})
 
## 代理
 - 如果需要使用代理，你可以通过为任意请求方法提供proxies参数来配置单个请求
 
             import requests
             #根据协议类型，选择不同的代理
             proxies={
             'http':'http://12.23.43.23:45434'
             }
             response = request.get('http://www.baidu.com',proxies=proxies)
             print(rsponse.text)
             
### 私密代理
        
          # 可能需要使用HTTP basic Auth, 可以这样
          # 格式为 用户名：密码@地理位置：端口地址
          proxy = { "http": "china:123445@192.168.1.123"}
          rsp = requests.get("http://baidu.com",proxies=proxy)
          
### web客户端验证
    
    
           如果遇到web客户端验证，需要添加auth= （用户名，密码） 
          auth=("test1","123435") #授权信息
          rsp = requests.get("http://www.baidu.com",auth=auth
          
### Cookie
        
            import requests
            rsp = requests.get('http://www.baidu.com')
            #返回CookieJar对象：
            cookiejar = rsp.cookies
            #将CookieJar转换成字典：
            cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
            print(cookiejar)
            print(cookiedict)
            
### Session
- 在requests里，session对象是一个非常常用的对象，这个对象代表一次用户会话：从客户端浏览器链接服务器开始，到客户端浏览器与服务器断开。
- 会话能让我们在跨请求时保持某些参数，比如在同一个Session实例发出短信请求之间保持cookie

#### 实现人人网登陆
            
            import requests
            # 1. 创建session对象，可以保存cookie值
            session = requests.session()
            # 2. 处理headers
            headers = {"User-Agent":"xxxxx"}
            # 3. 需要登陆的用户名和密码
            data = {'email':1212122,'password':'233223'}
            # 4. 发送附带用户名和密码的请求，并获取登陆后的cookie值，保存在ssion里
            session.post(url,data=data,headers=headers}
            # 5. session包含用户登陆后的cookie值，可以直接访问那些登陆后才能访问的页面
            response = session.get(url)
            # 6. 打印响应内容
            print(response.text)
            
### 处理HTTPS请求SSL证书验证
- Requests也可以为HTTPS请求验证SSL证书：https://kyfw.12306.cn/otn/
- 要想检查某个注意的SSL整数，你可以使用verify参数（也可以不写）

            import requests
            #也可以省略不写
            # response = requests.get(url, verify=True)#
            print(rsp.text)
            
            import requests
            rsp = requests.get(url)
        print(rsp.text)
        
### 网络图片的爬取和存储--结合os库和文件操作的使用
