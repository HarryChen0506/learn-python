import random


# def add(a=1):
#     print(a)

# add(1, b=1)

# print(add(a=3, c=2, b=10))
# print(add(**{'a': 1, 'b': 2}))
# a = {'a': 1, 'b': 2}
# add(1, a)

# def demo(a, b=10, c=12, **kwargs):
#     print(a, b, c, kwargs)


# demo(1)
# demo(1, b=100)
# demo(1, c=2, b=3, ho=100)

# def demo(a, *args, **kwargs):
#     print(a, args, kwargs)


# demo(1)
# demo(1, (1, 2, 3))
# demo(1, 3, c=12, d=(1, 2, 3), ho='123')

# def demo(a, b=3, **kwargs):
#     print(a, b, kwargs)


# demo(1, ff='123F')

# def demo():
#     a = 10

#     def func():
#         nonlocal a
#         a += 1
#         print(a)

#     return func


# f1 = demo()
# print(id(f1))
# f1()
# f1()

# f2 = demo()
# print(id(f2))
# f2()


# def before(func):
#     def wrapper(*args, **kwargs):
#         print('---before')
#         func(*args, **kwargs)
#     return wrapper

# @before
# def a(*args, **kwargs):
#     print('--->a', args, kwargs)


# a('hello', 'world', a='123')
