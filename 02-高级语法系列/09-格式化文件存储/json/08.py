import json

data = {"name":"haha", "age":12}

with open("haha.json", "w", encoding="utf-8") as f:
    json.dump(data, f)


with open("haha.json", "r", encoding="utf-8") as f:
    d = json.load(f)
    print(d)