"""
CSV(comma-Separated Value) 逗号分隔符
CSV文件是由任意的数据记录组成，记录间以某种换行符分割，每行记录由换行符组合
ID,UserName,Age,Country
1001,dana,18,China
1002,huanglaoban,28,china
"""

import csv
headers = ["ID","UserName","Age","Country"]
rows = [
    (1001,"luidana",18,"Beijing"),
    (1002,"haohuai",23,"Jinan"),
    (1003,"mila",34,"Japan"),
]
with open("test.csv","w") as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)