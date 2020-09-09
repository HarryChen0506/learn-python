# 进程学习

from multiprocessing import Process
import os
import time

num = 0
data = []

def task_1(name):
    global num
    tasks = ['看书', '学习', '打游戏']
    for i in tasks:
        time.sleep(0.5)
        num += 1
        data.append(num)
        print('进程名: {}, 任务:{}  进程:{} 父进程:{} num:{} data:{}'.format(
            name, i, os.getpid(), os.getppid(), num, data))


def task_2(name):
    global num
    tasks = ['篮球', '足球', '乒乓球']
    for i in tasks:
        time.sleep(1)
        num += 1
        data.append(num)
        print('进程名: {}, 任务:{}  进程:{} 父进程:{} num:{} data:{}'.format(
            name, i, os.getpid(), os.getppid(), num, data))


p1 = Process(target=task_1, name='t1', args=('hhh',))
p2 = Process(target=task_2, name='t2', args=('ggg',))

p1.start()
p2.start()

time.sleep(5)
print('main process end', os.getpid())
print('data', data)


