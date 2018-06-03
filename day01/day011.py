# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 16:49:31 2018
联网
@author: lenovo
"""
#引用其他工具包 import 包名/类名
import urllib.request as r
city=input("请输入城市拼音:")
address="http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996 "
#print(address.format(city))
info=r.urlopen(address.format(city)).read().decode('utf-8','ignore')
#print(info)
#json(dict)格式包
import json
data=json.loads(info)
#查看当前城市天气
#查看其它城市天气
#保存当前城市天气
print("1.当前城市温度{}".format(data["main"]["temp"])+"\n"+"2.当前城市天气情况{}".format(data["weather"][0]["description"])+"\n"+"3.当前城市气压{}".format(data["cod"]))

print("1.查看当前城市天气"+"\n"+"2.查看当前城市天气"+"\n"+"3.保存当前城市压强")
menno=input("请输入菜单:")
if menno=="1":
    print("1.当前城市温度{}".format(data["main"]["temp"]))
if menno=="2":
    print("2.当前城市天气情况{}".format(data["weather"][0]["description"]))
if menno=="3":
    print("3.当前城市气压{}".format(data["cod"]))