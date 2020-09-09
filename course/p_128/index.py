# name = ['a', 'c', 'b']
# res = [i+'-->' for i in name]
# print(res)

# res = [(x,y) for x in range(3) for y in range(4)]
# print(res)

# generator
# res = (i for i in range(10))
# print(res, type(res), res.__next__())
# for i in res:
#   print(i)

# def demo():
#     n = 0
#     while True:
#         if n > 10:
#             return
#         yield n
#         n += 1


# res = demo()

# while True:
#     try:
#         print(next(res))
#     except:
#         break

# def fibo(length):
#     a, b = 0, 1
#     n = 1
#     while True:
#         if n > length:
#             break
#         yield b
#         a, b = b, a + b
#         n += 1
#     return 'abcs'


# res = fibo(10)
# try:
#     while True:
#         print(next(res))
# except Exception as err:
#     print(err)


# def gen():
#     n = 1
#     while n <5:
#         temp = yield n
#         print(temp)
#         n += 1
#     return '没有更多了'

# res = gen()
# print(next(res))
# print(next(res))
# print(next(res))

# from collections.abc import Iterable

# a = [1,2,3]
# print(isinstance(a, Iterable))

a = iter([1, 2, 3])
print(next(a))
print(next(a))
print(next(a))
