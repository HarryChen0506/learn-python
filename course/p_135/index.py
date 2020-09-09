# 类
import sys


class Person:
    name = 'csc'

    def __init__(self):
        self.name = 'world'
        self.__age = 100

    def say(self, d=1, value='hhh'):
        print('hello', self.name, value, d)
        print(self.__age)

    def __str__(self):
        return 'nnnnn'

    @property
    def age(self):
        return self.__age

    # @age.setter
    # def age(self, age):
    #     self.__age = age

    @classmethod
    def demo(cls):
        print('demo')


one = Person()
# one.say(value='1234')
print(dir(Person))
# print(one._Person__age)
# print(one.age)
# one.age = 12
# print(one.age)
# one.demo()
# Person.demo()

# print(sys.getrefcount(one))
# print(one)
# print(dir(Person))
# print(dir(one))
