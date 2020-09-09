# 进程学习 进程池

from multiprocessing import Process, Pool
import os
import time
import random

# tasks = ['看书', '学习', '打游戏', '篮球', '足球', '乒乓球']


def foo(name):
    time.sleep(random.random() * 2)
    print('进程名:{} 进程id:{} 父进程id:{} '.format( name, os.getpid(), os.getppid()))


pool = Pool(5)
tasks = ['看书', '学习', '打游戏', '篮球', '足球', '乒乓球']
for task in tasks:
    pool.apply_async(func=foo, args=(task,))
pool.close()
pool.join()

print('main process end', os.getpid())
