#!/usr/bin/env python3 告诉Linux,这是一个py可执行文件
# -*- coding: utf-8 -*- 告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码

# import jqdatasdk
# jqdatasdk.auth("15695918375", "918375")
# price = jqdatasdk.get_price("000001.XSHE", "2017-01-01", "2017-12-31")
#print(price)
#name=input("please input your name :")
#print("hello "+name)
print(1.23e-4)
print('''多行测试
啊啊啊啊
...1111''')
print(True)
print(True and False
      )
print(False and False)
print(3>2)

print(True or False)

print(False or False)
print(None
      )
print(10/3)
print(10//3)
#字符函数
print(ord("孙"))
print(ord("亮"))
print(chr(23385))
print(chr(20142))

print("%d,%d"%(ord("孙"),ord("亮")))
print("%s%s"%(chr(23385),chr(20142)))
print("%2d-%02d" % (3,1))
print("%.2f" % 3.14159)
print("今日涨幅 %.2f%%" % 5.6487)
r1 = 72
r2 = 85
r = (r2-r1)*100/r1
print("成绩提升幅度 %.2f%%" % r)

classmate = ["小王","老王","小明"]
print(classmate)
print(len(classmate))
print("%s,%s,%s" %(classmate[0],classmate[1],classmate[2]))
print("%s,%s,%s" %(classmate[-1],classmate[-2],classmate[-3]))
classmate.append("大明")
print(classmate)
classmate.insert(1,"大老王1")
print(classmate)
classmate.pop()#默认删除最后一位
print(classmate)
classmate.pop(1)
print(classmate)
classmate[1]="老王+1"
print(classmate)
L =["混杂组",123,True]
print(L)
L.insert(1,False)
print(L)
L[1]=["1",False]
print(L)
print(len(L))
classmate=("老王","小王","大王")
print(classmate)
print(len(classmate))
classmate =("laowang",)
print(classmate)
t=("1","2",["a","b"])
print(t)
t[2][0]="A"
t[2][1]="B"
print(t)
age=20
if age>=18:
    print("成年人")
else:
    print("未成年人")

# s = input("请输入出生年 : ")
# birth = int(s)
# if birth >2000:
#     print("00后")
# else:
#     print("非00后")

height=1.75
weight=85
bmi = weight/(height*height)
print(bmi)
if bmi <=18.5:
    print("太轻了")
elif bmi >=32:
    print("严重肥胖")
elif bmi <=25:
    print("正常")
elif bmi <=28:
    print("过重")
elif bmi <32:
    print("肥胖")


names=["bob","cload","java"]
for name in names:
    print(name)

ran = list(range(5))
print(ran)
sum =0
r=list(range(101))
for x in r:
    sum = sum+x
print(sum)

n=1
while n<=100:
    if n>15:
        break
    if n>=10:
        n=n+1
        continue
    print("this is %d" % n)
    n =n+1
print("END")


m={'a':1,'b':2}
print(m['a'])
print(m.get('a'))
m['a']=100
print(m.get('a'))
if 'b' in m:
    print(m.get('b'))
print(m.get('c',200))#第二参数为默认值
m.setdefault("c",400)
print(m)
m.pop('c')
print(m)
s = set([1,1,2,3,3,5,5])
print(s)
s.add(99)
print(s)
s.remove(99)
print(s)
s1=set([1,2,4,9,7])
s2=set([2,9,8,5,3])
print(s1 & s2)
print(s1 | s2)
print(abs(-23))
print(max(1,5,444,9987,3823))
print("int('123')=%d,int(12.34)=%d,float('12.34')=%.2f" %(int('123'),int(12.34),float('12.34')))
a=abs
print(a(-100))
n1=255
n2=10000
print(str(hex(n1)),str(hex(n2)))
