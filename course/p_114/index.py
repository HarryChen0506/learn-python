import os

# dir = os.path.dirname(__file__)
# file = os.path.join(dir, 'a.txt')
# stream = open(file, 'rt')
# res = stream.read()
# print(res)
# print(stream.name)
# line = stream.readline()
# print(line)
# line = stream.readline()
# print(line)

# stream.write('追加一段文字')
# stream.close()

# print(dir, file)

# path = os.path.abspath(__file__)
# p = os.path.splitext(path)
# print(p)

# a = os.getcwd()
# print(a)

# try


def demo():
    try:
        a = 5 / 1
        a == 5 and print('123')
        raise Exception('错误')
        # return a
    except Exception as err:
        print(err)


demo()
