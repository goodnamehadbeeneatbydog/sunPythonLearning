#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Animal(object):

    def run(self):
        print("Animal is runing ...")


class Dog(Animal):
    def run(self):
        print("Dog is runing")


class Cat(Animal):
    def run(self):
        print("Cat is runing")


d = Dog()
d.run()
c = Cat()
c.run()


def twice_sun(animal):
    animal.run()
    animal.run()


twice_sun(Dog())


class Timer(object):
    def run(self):
        print("Timer is runing")


twice_sun(Timer())

print(type(123))

print(type('123'))

import types


def fn():
    pass


print(type(fn))
print(type(fn) == types.FunctionType)

print(isinstance(d, Dog))
print(isinstance(d, Animal))
print(isinstance(d, Cat))
isinstance('a', str)

isinstance(123, int)

isinstance(b'a', bytes)
# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。


# 使用dir()
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，
# 它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：

print(dir("123"))
print(dir(d))


# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，
# 我们可以直接操作一个对象的状态：

class MyObject(object):
    def __init__(self):
        self.x = 10

    def power(self):
        return self.x * self.x


obj = MyObject()

print(hasattr(obj, 'x'))

print(hasattr(obj, 'y'))
setattr(obj,'y',20)

print(hasattr(obj, 'y'))

print(getattr(obj, 'y'))
#如果试图获取不存在的属性，会抛出AttributeError的错误：
#可以传入一个default参数，如果属性不存在，就返回默认值：
print(getattr(obj, 'z',100))
print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))
fn = getattr(obj,'power')
print(fn())

# 一个正确的用法的例子如下：

# def readImage(fp):
#     if hasattr(fp, 'read'):
#         return readData(fp)
#     return None
# 假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，
# 则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。
# ，在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，
# 它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，
# 就不影响读取图像的功能。

