'''
findall案例
'''
import re

pattern = re.compile(r'\d+')

s = pattern.findall("i am 18 years odl and 185 high")

print(s)

s = pattern.finditer("i am 18 years odl and 185 high")

print(type(s))

for i in s:
    print(i.group())

s = "woshifsowfs8989sfsfs"
l = s.split("8989")
print(l)
l = re.sub("8989", "mmmm", s)
print(l)
l = s.replace("8989","wwww")
print(l)