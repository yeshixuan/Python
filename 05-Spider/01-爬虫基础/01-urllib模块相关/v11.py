from urllib import request, error

if __name__ == '__main__':
    url = "http://www.renren.com/965187997/profile"

    try:
        rsp = request.urlopen(url)

        html = rsp.read().decode()
        print(html)
        with open("rsp.html", "w", encoding="utf-8") as f:
            f.write(html)
    except error.URLError as e:
        print(e)