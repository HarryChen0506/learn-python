# name = ['1', '2', '3']
# print('1' in name)
# print('4' in name)

# a = [1, 2, 3, 4, 5, 6]
# length = len(a)
# for i in range(length):
#     print('i', i)
#     if a[i] == 2 or a[i] == 3:
#         del a[i]
#         print(a)
#     if i >= len(a) - 1:
#         break
# print(a)

# i = 0
# while i < length:
#     if a[i] == 2 or a[i] == 3:
#         del a[i]
#         length -= 1
#         i -= 1
#     i += 1
# print(a)

# a = [1, 2, 3, 4, 5, 6]
# print(a[::-1])
# # print(a[-1::-1])
# a.append(7)
# print(a)
# a.extend([11,22,33])
# print(a)

# a.insert(0, 'abc')
# print(a)

# a = [1, 2]
# b = [1, 2, 3, 4, [1, 2, 3]]
# print(a in b)

# a = [1, 2]
# b = [1, 2]
# print(a == b)
# print(a is b)
# print(id(a))
# print(id(b))

# a = [1, 2, 3, 4, 5]
# print(a[-1])

# print(list(range(1, 20, 3)))
# print(list(10))

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a[:5:-1])
# print(a[5:0:-1])

# a = [1, 2, 3]
# b = a[::-1]
# print(a, b, a == b)
# a.clear()
# print(a)

# a = [1,2,3]
# print(help(enumerate))
# for i in enumerate(a):
# print(i)

# a = (1, 2)
# b, c = a
# print(a, b, c)

# a = (1, 1, 2)
# b = [1, 2, 3, 4]
# print(a, list(a), tuple(b), a.count(3))

# tup = (1,2,3,4)
# print(tup)
# print(*tup)

# print('------列表打散-------')
# lst = ['a', 'b', 'c']
# print(lst)
# print(*lst)

# def func_dic(name, age):
#     print(name, age)

# dic = {'name': '张三', 'age': 20}
# func_dic(**dic)

# a = (1,)
# b = (2, )
# a= a + b
# print(a)

# a = dict([(1, 2), (3, 4)])
# print(a)

# a = [1, 2, 3, 4, 5, 6]
# del a[2:4]
# print(a)

# a = {'name': 'harry', 'age': 10}
# print(a, a.items(), a.keys(), a.values())
# for key in a:
#   print(key)
# print(a['gender'])
# print(a.pop('name'), a)

# a = set([4, 6, 1, 1, 2, 3])
# a.add('123')
# a.update(['he', 'llo'])
# a.update('world')
# a.discard('你好')
# a.discard(1)
# print(a, type(a))

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# print(a - b)
# print(a, a.difference(b))
# print(a & b)
# print(a | b)

# a = {'name': 1}
# b = {'name': 1}
# print(a == b)
# print(a is b, id(a), id(b))

# print(type(str([1, 2, 3])))
# print(str((1,2,3,)))

# a = {'name': 'harry', "age": 10}
# print(list(a.items()))
