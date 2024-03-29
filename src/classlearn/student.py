#!/usr/bin/env python
# -*- coding:utf-8 -*-

#(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，
# 通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
class Student(object):
    # __init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，
    # 就可以把各种属性绑定到self，因为self就指向创建的实例本身。
    #
    # 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，
    # 但self不需要传，Python解释器自己会把实例变量传进去：
    def __init__(self, name, score):
        self.name = name
        self.score = score

    #和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，
    # 并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，
    # 所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数
    def print_score(self):
        print("%s : %s" % (self.name, self.score))




s1 = Student("sb", 88)
s2 = Student("逗逼", 99)

print(s1)
s1.print_score()
s1.name ="sb+"
s1.print_score()
s2.print_score()

# 小结
# 类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；
#
# 方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；
#
# 通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
#
# 和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：
#
# >>> bart = Student('Bart Simpson', 59)
# >>> lisa = Student('Lisa Simpson', 87)
# >>> bart.age = 8
# >>> bart.age
# 8
# >>> lisa.age
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Student' object has no attribute 'age'