print("hello")
print(abs)
f = abs
print(f)
print(f(-10))


# 高阶函数
def addh(x, y, f):
    return f(x) + f(y)


print(addh(1, -9, abs))
import math

print(addh(1, 7, math.log2))


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5])
# map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，
# Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
print(list(r))

print(list(map(str, [1, 2, 3, 4, 5])))

# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce


def add1(x, y):
    return x + y


print(reduce(add1, [1, 2, 3, 4, 5]))


# 当然求和运算可以直接用Python内建函数sum()，没必要动用reduce。
#
# 但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：
def fn1(x, y):
    return x * 10 + y


print(reduce(fn1, [1, 2, 3, 4, 5]))


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(reduce(fn1, map(char2num, '34567')))
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    return reduce(fn1, map(char2num, s))


print(str2int("988"))


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(str2int("9876"))


def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


def not_emp(s):
    return s and s.strip()


print(list(filter(not_emp, ['A', 'B', '', None, 'C', '    '])))


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_div(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_div(n), it)


for n in primes():
    if n < 20:
        print(n)
    else:
        break

print(sorted([3, 86, 3, 998, 73, 86, 234, -44, -88, -21, -54]))

print(sorted([3, 86, 3, 998, 73, 86, 234, -44, -88, -21, -54], key=abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.upper))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum;


print(lazy_sum(1, 2) == lazy_sum(1, 2))
print(lazy_sum(1, 2)() == lazy_sum(1, 2)())


def count1():
    fs = [];
    for i in range(1, 4):
        def ff():
            return i * i

        fs.append(ff)
    return fs


f1, f2, f3 = count1()
print(f1(), f2(), f3())


def count2():
    fs = []

    def ff(j):
        def g():
            return j * j

        return g

    for i in range(1, 4):
        fs.append(ff(i))
    return fs


f1, f2, f3 = count2()
print(f1(), f2(), f3())


def now1():
    print("1111")


f = now1
print(f())
print(f.__name__)

import functools


def log1(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        print("call %s():", fn.__name__)
        return fn(*args, **kw)

    return wrapper


@log1
def now2():
    print("22222")


f2 = now2
print(f2())
print(f2.__name__)


def log2(text):
    def dt(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kw):
            print("---%s %s:" % (text, fn.__name__))
            return fn(*args, **kw)

        return wrapper

    return dt


@log2("fucking")
def now3():
    print("3333")


print("----", now3())

print(int("12345"))
# int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换：
print(int("12345", base=8))
print(int("12345", 8))
print(int("12345", base=16))


def int2(x, base=2):
    return int(x, base)


print(int2("1000000"))

import functools

int3 = functools.partial(int, base=2)
# functools.partial的作用就是，把一个函数的某些参数给固定住（
# 也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
print(int3("100101100111"))
print(int3("1234456", base=8))

kw = {"base": 2}
print(int("100101100111", **kw))
max2 = functools.partial(max, 10)
print(max2(1, 2, 3))
print(max2(1, 2, 99))
# 实际上会把10作为*args的一部分自动加到左边，也就是
# max2(5, 6, 7)
# 相当于：
#
# args = (10, 5, 6, 7)
# max(*args)
# 结果为10。
