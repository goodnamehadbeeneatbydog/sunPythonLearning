#!/usr/bin/env python3 告诉Linux,这是一个py可执行文件
# -*- coding: utf-8 -*- 告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码


with open("D:\\test.txt") as f:
    print("f.readline() = ", f.readline())
    print("f.read() = ", f.read())

with open("D:\\test.txt") as f1:
    for line in f1.readlines():
        print(line.strip())

# file-like Object
# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。
# 除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，
# 只要写个read()方法就行。
#
# StringIO就是在内存中创建的file-like Object，常用作临时缓冲。

with open("d:\\test.jpg","rb") as img:
    print(img.read())

# 字符编码
# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
#
# >>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
# >>> f.read()
# '测试'
# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，
# 因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，
# 表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
#
# >>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')


# 写文件和读文件是一样的，唯一区别是调用open()函数时，
# 传入标识符'w'或者'wb'
# 表示写文本文件或写二进制文件：
with open("d:\\test.txt","w") as f2:
    f2.write("SB")
    f2.write("dsb")


from io import StringIO
f = StringIO()
f.write("Hello ")
f.write("   ")
f.write("World!")
print(f.getvalue())

f1 = StringIO("Hello World!")
while True:
    s = f1.readline()
    if s =="":
        break
    print(s.strip())

from io import BytesIO

b = BytesIO()
b.write("中文".encode("utf-8"))
print(b.getvalue())

b1 =  BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(b1.read())