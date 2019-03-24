#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/24 14:53
# @Author  : Yebiyun
# @Site    : 
# @File    : login.py
# @Software: PyCharm
import time
import os
import json

count = 0
status_flag = False
while count < 3:
    user = input("请输入账号：")
    file = user.strip() + ".json"
    if not os.path.exists(file):
        print("文件名不存在，请重新输入")
    else:
        fp = open(file, "r+", encoding="utf-8")
        j_user = json.load(fp)
        expire_dt = j_user["expire_date"]
        current_st = time.time()
        expire_st = time.mktime(time.strptime(expire_dt,"%Y-%m-%d"))
        if time.time() > expire_st:
            print("账号已过期！")
            break
        else:
            if j_user["status"] == 1:
                print("账号已被锁定！")
            else:
                while count < 3:
                    password = input("请输入密码:")
                    if password != j_user["password"]:
                        count += 1
                        if count == 3:
                            print("密码输错3次，账号被锁定")
                            j_user["status"] = 1
                            fp.seek(0)
                            fp.truncate()
                            json.dump(j_user,fp)
                            status_flag = True
                            break
                        else:
                            print("密码错误，请重新输入！")
                    else:
                        print("登陆成功！")
                        status_flag = True
                        break
    if status_flag:
        break