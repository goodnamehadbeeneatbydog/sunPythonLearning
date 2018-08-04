myList =["1","2","3","4"]
print(myList[0:3])
print(myList[2:4])
print(myList[-2:])
print(myList[-2:-1])
myList = list(range(100))
print(myList[3:67])
print(myList[:10])
print(myList[10:20])
print(myList[10:20:2])
print(myList[::5])
print(myList[:])
myTuple =(1,2,3,4,5,6,7,8,9)
print(myTuple[0:3])
print(myTuple[0:9:3])
L ="我的字符串"
print(L[:3])
print(L[::2])

d=['1','2','3','4']
for i in d:
    print(i)

d={'a':1,'b':2,'c':3}

for k in d:
    print(k,d[k])
for v in d.values():
    print(v)
for k,v in d.items():
    print(k,v)

for ch in 'ABC':
    print(ch)

from collections import Iterable

print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))

for i,value in enumerate(['a','b','c']):
    print(i,value)

for x,y in [(1,2),(3,4),(5,6)]:
    print(x,y)

#列表生成器
print(list(range(11)))
print(list(range(1,11)))

L=[]
for i in range(1,11):
    L.append(i*i)
print(L)
print([x*x for x in range(1,11)])
L =[x*x for x in range(11) if x%2==0]
print(L)
L =[m+n for m in 'ABC' for n in 'XYZ']
print(L)

import os
print(os.listdir('.'))
print([d for d in os.listdir('.')])

d ={'a':'x','b':'y','c':'z'}
for k,v in d.items():
    print(k,"=",v)
print([k+"="+v for k,v in d.items()])

L =["HELLO","WORD","I'M","JAVA"]
print([s.lower() for s in L])
L =[1,2,3,'A',"B","C"]
print([s.lower() for s in L if isinstance(s,str)])

#生成器，在使用的时候才生出列表
g =(x*x for x in range(1,11))
for n in g:
    print("n=",n)

def fib(max):
    n,a,b=0,0,1
    while n<max :
        print(b)
        a,b=b,a+b
        n = n+1
    return 'done'

print(fib(3))
print(fib(10))
def fib(max):
    n,a,b=0,0,1
    while n<max :
        yield b
        a,b=b,a+b
        n = n+1
    return 'done'

f = fib(6)
next(f)
next(f)
next(f)

def myodd():
    print("step 1")
    yield(1)
    print("step 2")
    yield(3)
    print("step 3")
    yield(5)

o = myodd()
next(o)
next(o)
next(o)
# next(o)

for n in fib(9):
    print("fib = ",n)

g = fib(9)

while True:
    try:
        x = next(g)
        print("g=",x)
    except StopIteration as e:
        print("generator return value :",e.value)
        break

# 我们已经知道，可以直接作用于for循环的数据类型有以下几种：
#
# 一类是集合数据类型，如list、tuple、dict、set、str等；
#
# 一类是generator，包括生成器和带yield的generator function。
#
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
#
# 可以使用isinstance()判断一个对象是否是Iterable对象：


# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
#
# 可以使用isinstance()判断一个对象是否是Iterator对象：


# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
#
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：

from collections import Iterator
print(isinstance(iter([]),Iterator))

# 你可能会问，为什么list、dict、str等数据类型不是Iterator？
#
# 这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
#
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。