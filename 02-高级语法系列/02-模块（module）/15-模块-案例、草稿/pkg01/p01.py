# 包含一个学生类
# 一个sayHello函数，
# 一个打印语句

class Student():
    def __init__(self, name="NoName", age=15):
        self.name = name
        self.age = age

    def say(self):
        print("My name is {}".format(self.name))

def sayHello():
    print("这是类外面的函数哦")

if __name__ == '__main__':
    print("我是模块p01。")