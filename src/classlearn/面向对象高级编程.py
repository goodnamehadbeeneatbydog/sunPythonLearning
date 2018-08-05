#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Sdudent(object):
    #使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
    __slots__ = ("test", "name", "set_age", "age", "score")
    pass


s = Sdudent()
s.name = "sb"
print(s.name)


def set_age(self, age):
    self.age = age


from types import MethodType

s.set_age = MethodType(set_age, s)
s.set_age(33)
print(s.age)


# 但是，给一个实例绑定的方法，对另一个实例是不起作用的
# 为了给所有实例都绑定方法，可以给class绑定方法：

def set_score(self, score):
    self.score = score


Sdudent.set_score = set_score

s.set_score(15)
print(s.score)

# 使用__slots__
# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
#
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：


class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError("score must be an integer")
        if value <0 or value >100:
            raise ValueError("scor must between 0~100")
        self._score = value

s = Student()
s.score = 90
print(s.score)