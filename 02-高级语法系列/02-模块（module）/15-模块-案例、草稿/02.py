# 借助于importlib包可以实现导入以数字开头的模块名称
import importlib

# 相当于导入了一个叫做01模块并把导入模块赋值给modu
modu = importlib.import_module("01")

stu = modu.Student()
stu.say()