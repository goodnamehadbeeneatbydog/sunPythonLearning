def my_abs(n):
    if n >= 0:
        return n
    else:
        return -n


print(my_abs(-200))


def pop():
    pass


def my_abs1(x):
    if not isinstance(x, (int, float)):
        raise TypeError("参数类型错误")
    if x >= 0:
        return x
    else:
        return -x


# print(my_abs1('a'))

import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(1, 2, 3, math.pi / 6)
print(x, y)

r = move(1, 2, 3, math.pi / 6)
print(r)


def quadratic(a, b, c):
    if a == 0:
        return c / b
    d = b * b - 4 * a * c
    d1 = 4 * a * c - b * b
    print("d = %.2f" % d)
    if d == 0:
        return -b / (2 * a), -b / (2 * a)
    elif d > 0:
        return (-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a)
    elif d < 0:
        return (-b + math.sqrt(d1)) / (2 * a), (-b - math.sqrt(d1)) / (2 * a)


print(quadratic(1, 0, 1))


def my_power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(my_power(5, 2))
print(my_power(7))


def add_end(L=[]):
    L.append("END")
    return L


print(add_end([1, 2, 3]))

print(add_end())
print(add_end())
print(add_end())


def add_end(l=None):
    if l is None:
        l = []
    l.append("END")
    return l


# 定义函数参数，尽量使用不变变量
print(add_end())
print(add_end())
print(add_end())


# 可变参数的函数定义
def calc(*number):
    sums = 0
    for i in number:
        sums = sums + i
    return sums


print(calc(1, 2, 3))
list = [1, 2, 3]
print(calc(*list))  # *list表示把list这个list的所有元素作为可变参数传进去


# 关键字参数，关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict

def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'skill' in kw:
        pass

    print('name:', name, 'age:', age, 'other:', kw)


person('test', 20)

person('sunliang', 34, city='fuzhou', skill='java')

other = {'city': 'fuzhou', 'skill': 'java'}

person('sunliang', 34, **other)


# 如果要限制关键字参数的名字，就可以用[[命名关键字]]参数，例如，只接收city和job作为关键字参数。
# 只限定city,skill
def person1(name, age, *, city, skill):
    print('name:', name, 'age:', age, 'other:', city, skill)


person1('sunliang', 34, **other)
other.setdefault('a', 2)


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了

def person2(name, age, *args, city, skill):
    print(name, age, args, city, skill)


person2('a', 'b', 3, 4, 5, city='city', skill='skill')


# 命名关键字参数可以有缺省值，从而简化调用：
# 使用命名关键字参数时，要特别注意，如果没有可变参数，
# 就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数
def person(name, age, *args, city='beijin', skill='c++'):
    print(name, age, args, city, skill)


person('s', 10)


def f1(name, age=10):
    print(name, age)


f1('sun')


# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
# 这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


args = (1, 2, 3)
kw = {'d': 'dd', 'x': 99}
f1(*args, **kw)
f2(*args, **kw)


# 所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。

def product(*args):
    sum = 1
    for i in args:
        if not isinstance(i, (int, float)):
            raise TypeError("参数类型错误，只接受数字类型参数")

    for i in args:
        sum = sum * i
    print("所有参数相乘的结果为: ", sum)


product()
product(5)
product(5, 6)
product(2, 3, 4, 5)
product(3, 3, 3, 3, 3, 3, 3)
def product1(*args):
    sum = 1
    for i in args:
        if not isinstance(i, (int, float)):
            i=ord(i)

        sum = sum * i
    print("所有参数相乘的结果为: ", sum)
product1('a','b')
#Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
#默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
#要注意定义可变参数和关键字参数的语法：
#*args是可变参数，args接收的是一个tuple；
#**kw是关键字参数，kw接收的是一个dict。
#以及调用函数时如何传入可变参数和关键字参数的语法：
#可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
#关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
#使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
#命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
#定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。


def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(1))
print(fact(5))
print(fact(10))

