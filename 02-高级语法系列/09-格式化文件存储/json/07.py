import json

# 此时student是一个dict格式内容，不是json
student = {
    "name": "yeshixuan",
    "age": 18,
    "mobile": "15123356478"
}
print(type(student))

student_json = json.dumps(student)

print(type(student_json)) # str格式
print("JSON对象：{}".format(student_json))

stu_dict = json.loads(student_json) # dict格式
print(type(stu_dict))
print(stu_dict)
