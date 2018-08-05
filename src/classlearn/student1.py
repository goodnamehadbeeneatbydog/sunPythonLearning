#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Student(object):

    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print("%s : %s" %(self.__name,self.__score))

    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_name(self,name):
        self.__name = name
    def set_score(self,score):
        self.__score = score
# 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，
# 并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量
# ，所以，不能用__name__、__score__这样的变量名。
#
# 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，
# 但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，
# 但是，请把我视为私有变量，不要随意访问”。
#
# 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。
# 不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
# 所以，仍然可以通过_Student__name来访问__name变量：