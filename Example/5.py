import os
import sys


def func1():
    """
    Допуск к приватному атрибуту и методу обьекта
    """
    class Point:
        def __init__(self, one, two):
            self._list = one
            self.__private = two

        def my_public_method(self):
            print('Публичный метод')

        def __my_private_method(self):
            print('Приватный метод')

    pt = Point([10, 20, 30], "Приватная переменная")

    Point.my_public_method(pt)
    Point._Point__my_private_method(pt)

    print(pt.__dict__)
    print('='*20)
    print(Point.__dict__)


def func2():
    """
    Спец метод __getitem__ отрабатывает когда к
    обьекту обращаются как к элементу списка
    """
    from string import ascii_letters

    class MyContainer(object):

        def __getitem__(self, key):
            print('key = ', key)
            return ascii_letters[key]

    my_container = MyContainer()

    print(my_container[0])  # a
    print(my_container[16])  # q
    print(my_container[:])  # вывод всего алфавита

