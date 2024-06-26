"""
接口(java)-抽象类(python)
"""


class Animal:
    def bar(self):
        pass


class Dog(Animal):
    def bar(self):
        print("汪汪汪!")


class Cat(Animal):
    def bar(self):
        print("喵喵喵")


animal = Cat()
animal.bar()
