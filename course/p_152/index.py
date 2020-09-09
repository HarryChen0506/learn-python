# for i in range(4):
#   if i == 3:
#     print('有3')
#     break
# else:
#   print('111')

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def say(self):
#         print('我是{},今年{}岁'.format(self.name, self.age))


# class Student(Person):
#     def __init__(self, name, age, grade):
#         self.grade = grade
#         super().__init__(name, age)

#     def say(self):
#         super().say()
#         print('我正在上{}年级'.format(self.grade))


# s = Student('harry', 20, 5)
# s.say()

# 单例模式

class A:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        return cls.__instance

    def __init__(self, name):
        self.name = name

    @classmethod
    def show(cls):
        print(cls.__instance)


a = A('hello')
print(dir(a))
a.show()

b = A('world')
b.show()
