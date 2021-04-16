#! /usr/bin/python3

# Функция для удобного вывода содержимого
from custom_functions import trace
import os
import sys


def func1():
    class My_class():
        """Это статическая переменная класса"""
        static_var = "Статическая переменная класса"

        def __init__(self, x, y):
            """Это динамические переменные обьекта"""
            self.x = x
            self.y = y

        def show(self):
            print("Динамические:", self.x, self.y)
            print("Статические:", My_class.static_var)

    print("Статические:", My_class.static_var)
    obj = My_class(10, 20)
    obj.show()


def func2():
    class Point():
        static_count = 10

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def setCoords(self, x, y):
            self.x = x
            self.y = y

        def getCoords(self):
            print(f"getCoords {self.x}, {self.y}")

        @staticmethod
        def geCountOne():
            print(f"geCountOne = {Point.static_count}")

        def geCountTwo():
            print(f"geCountTwo = {Point.static_count}")

    pt = Point(1, 2)

    pt.getCoords()
    pt.setCoords(10, 20)
    pt.getCoords()

    Point.geCountOne()
    Point.geCountTwo()


def func3():
    pass







# func1()
# func2()
func3()







