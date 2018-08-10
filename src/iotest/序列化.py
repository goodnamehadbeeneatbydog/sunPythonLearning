#!/usr/bin/env python3 告诉Linux,这是一个py可执行文件
# -*- coding: utf-8 -*- 告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码

import pickle

d = dict(name='Bob', age=10, score=88)

print(pickle.dumps(d))

f = open("test.txt", 'wb')

pickle.dump(d, f)
f.close()

f = open("test.txt", "rb")
d = pickle.load(f)
print(d)
f.close()

import json

j_str = json.dumps(d)
print(j_str)
j_str2 = json.loads(j_str)
print(j_str2)


# Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，
# 我们更喜欢用class表示对象，比如定义Student类，然后序列化：

class JsonTest:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def JsonTest2json(j):
    return {
        'name': j.name,
        'age': j.age

    }


jt = JsonTest("sb", 100)
jd = json.dumps(jt, default=JsonTest2json)
print(jd)

print(json.dumps(jt,default=lambda obj:obj.__dict__))

def json2obj(str):
    return JsonTest(str['name'],str['age'])


print(json.loads(jd,object_hook=json2obj))
