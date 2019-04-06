from lxml import etree

html = etree.parse("./v32.html")
print(type(html))

rst = html.xpath("//book")
print(type(rst))
print(rst)

rst = html.xpath("//book[@category='sport']")
print(rst)

rst = html.xpath("//book[@category='sport']/year")
print(rst)
print(type(rst[0]))
print(rst[0].tag)
print(rst[0].text)

rst = html.xpath("//book[@category='sport']/year/text()")
print(rst)
