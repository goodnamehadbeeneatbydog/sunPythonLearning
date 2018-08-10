#!/usr/bin/env python3 告诉Linux,这是一个py可执行文件
# -*- coding: utf-8 -*- 告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码
import os

# print("process (%s) start..." % os.getppid())

# pid = os.fork()
#
# if pid ==0:
#     print("child process (%s) and parent is %s " %(os.getpid(),os.getppid()))
# else:
#     print("I (%s) just create a child process (%s)" %(os.getpid(),pid) )
#
# 由于Windows没有fork调用，上面的代码在Windows上无法运行。
# 由于Mac系统是基于BSD（Unix的一种）内核，所以，在Mac下运行是没有问题的，推荐大家用Mac学Python！
#
# 有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，
# 常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求。

from multiprocessing import Process


def run_proc(name):
    print("Run child process %s (%s)..." % (name, os.getpid()))


if __name__ == "__main__":
    print("parent process %s " % os.getpid())
    p = Process(target=run_proc, args=("test",))
    print('child process will start')
    p.start()
    p.join()
    print('child process end.')

from multiprocessing import Pool
import time, random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.randomm() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == "__main__":
    print('Parent process %s.' % os.getpid())
    p = Pool(2)
    for i in range(3):
        p.apply_async(long_time_task, args=(i,))

    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')


# import subprocess
# print('$ dir d:')
# r = subprocess.call(['dir', 'd:'])
# print('Exit code:', r)

