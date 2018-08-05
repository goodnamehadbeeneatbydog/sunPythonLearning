#!/usr/bin/env python
# -*- coding:utf-8 -*-

from enum import Enum,unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name,member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
    #value属性则是自动赋给成员的int常量，默认从1开始计数。

@unique
class WeekDay(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = WeekDay.Sun
print(day1,day1.value,WeekDay(1))




