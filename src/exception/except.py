#!/usr/bin/env python
# -*- coding:utf-8 -*-
import logging
logging.basicConfig(level=logging.INFO)
try:
    print("try ....")
    r = 10 / 0
    print("result : ", r)
except BaseException as e:
    print("except : ", e)
    logging.exception(e)
else:
    print("no error")
    logging.info("no error")
finally:
    print("finally...")
print("END")
#
#
# 最后，我们来看另一种错误处理的方式：
#
# # err_reraise.py
#
# def foo(s):
#     n = int(s)
#     if n==0:
#         raise ValueError('invalid value: %s' % s)
#     return 10 / n
#
# def bar():
#     try:
#         foo('0')
#     except ValueError as e:
#         print('ValueError!')
#         raise
#
# bar()
# 在bar()函数中，我们明明已经捕获了错误，但是，打印一个ValueError!后，又把错误通过raise语句抛出去了，这不有病么？
#
# 其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。好比一个员工处理不了一个问题时，就把问题抛给他的老板，如果他的老板也处理不了，就一直往上抛，最终会抛给CEO去处理。
#
# raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：
#
# try:
#     10 / 0
# except ZeroDivisionError:
#     raise ValueError('input error!')
# 只要是合理的转换逻辑就可以，但是，决不应该把一个IOError转换成毫不相干的ValueError。

# 断言
# 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代：
#
# def foo(s):
#     n = int(s)
#     assert n != 0, 'n is zero!'
#     return 10 / n
#
# def main():
#     foo('0')
# assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
#
# 如果断言失败，assert语句本身就会抛出AssertionError：
#
# $ python err.py
# Traceback (most recent call last):
#   ...
# AssertionError: n is zero!
# 程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert：
#
# $ python -O err.py
# Traceback (most recent call last):
#   ...
# ZeroDivisionError: division by zero
# 关闭后，你可以把所有的assert语句当成pass来看。
#
# logging
# 把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件：
#
# import logging
#
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)
# logging.info()就可以输出一段文本。运行，发现除了ZeroDivisionError，没有任何信息。怎么回事？
#
# 别急，在import logging之后添加一行配置再试试：
#
# import logging
# logging.basicConfig(level=logging.INFO)