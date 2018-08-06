#!/usr/bin/env python3 告诉Linux,这是一个py可执行文件
# -*- coding: utf-8 -*- 告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码

import os
print(os.name)
#如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。

# 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。
# print(os.uname())

print(os.environ)
print(os.environ.get("PATH"))

#操作文件和目录的函数一部分放在os模块中，
# 一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：

pwd = os.path.abspath(".")
print(pwd)
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，
# 这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
#
# part-1/part-2
# 而Windows下会返回这样的字符串：
#
# part-1\part-2
npwd = os.path.join(pwd,"testdir")
print(npwd)
os.mkdir(npwd)
os.rmdir(npwd)

print(os.path.splitext("D:\\text.txt"))

import shutil

# 幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，
# 它们可以看做是os模块的补充。

print([x for x in os.listdir(".") if os.path.isdir(x)])

print([x for x in os.listdir(".") if os.path.splitext(x)[1] ==".py"])
