# import pkg01.p01
# import pkg01.p01 as pm

# stu = pkg01.p01.Student()
# stu = pm.Student()
# stu.say()

# from pkg01 import inInit, p01
# p01.sayHello()

#它导入的是__init__模块中的所有函数和类，不包括包中的其他模块
# from pkg01 import *
# inInit()

#导入该模块中的所有
# from pkg01.p01 import *

# 如果在__init__模块中设置了 __all__
# 进行from pkg01 import *时，会导入 __all__里指定的模块，不会导入init中的函数或内容
from pkg01 import *

p01.sayHello()