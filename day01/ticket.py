# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 11:28:40 2018
快捷键 ctrl +
新建python文件
baocun
执行代码：ctrl +回车
@author: lenovo
"""
#一次申请一个变量
a=3
a,xixi,ming=30,40,50
#一次申明多个变量
xj='小娇'
yanzhi=5.0
#自动补全
print(xj+yanzhi)
#将其他类型准换为字符串
b=str(yanzhi)
c='3.9'
d=float(c)
print(xj+str(yanzhi))
print(xj+'\t'+str(yanzhi))
#字符窜中出现大括号，表示占位符

print('今天温度是{}天气是{}星期{}'.format(10,'晴天','一'))
"""
"""
#列表list,
usemoney=12,20,30,19,20
usemoney[1]
usemoney2=[12,20,30,19,20]
usemoney2[0]
#字典
a=[0,1,2,3,4,5,6]
print('今天是星期{}'.format(a[0]))
print('今天是星期{}'.format(a[1]))
print('今天是星期{}'.format(a[2]))
print('今天是星期{}'.format(a[3]))
print('今天是星期{}'.format(a[4]))
print('今天是星期{}'.format(a[5]))
print('今天是星期{}'.format(a[6]))






