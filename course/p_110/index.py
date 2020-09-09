from functools import reduce

# def a(a, b): return a+b

# a = lambda a,b: a+b
# print(a(1,2))


# a = reduce(lambda a, b: a-b, [1, 2, 3, 4, 5, 6])
# print(a)

# b = filter(lambda a: a > 10, [1, 3, 6, 11, 14, 16])
# print(list(b))

def sum(n):

    if n == 0:
        return 0
    elif n < 0:
      return n
    else:
        return n + sum(n-1)

print(sum(-10))