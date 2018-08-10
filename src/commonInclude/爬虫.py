#!/usr/bin/env python3 告诉Linux,这是一个py可执行文件
# -*- coding: utf-8 -*- 告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码

from urllib import request

try:
    f = request.urlopen('https://api.douban.com/v2/book/2129650')
    fdata = f.read()
    print('status :', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s : %s' % (k, v))
    print('data : ', fdata.decode('utf-8'))
except BaseException as e:
    print('............')
finally:
    f.close()
