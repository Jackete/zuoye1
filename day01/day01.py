# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 16:35:35 2018
系统输入
@author: lenovo
"""

city=input("请输入城市拼音:")
print(city)
address="http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996 "
print(address.format(city))
#查看当前城市天气
#查看其它城市天气
#保存当前城市天气
print("1.查看当前城市天气2.查看其它城市天气3.保存当前城市天气")
menno=input("请输入菜单:")
if menno=="1":
    print("1.查看当前城市天气")
if menno=="2":
    print("2.查看其它城市天气")
if menno=="3":
    print("3.保存当前城市天气")