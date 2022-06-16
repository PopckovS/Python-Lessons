#! /usr/bin/python3

def func1():
    """
    Пример реализации атрибута __slots__ в класса
    """
    class Point:

        STATIC_NAME = 'Статичное название'
        __slots__ = ['x', 'y', '__dict__']

        # Так будет ошибка ибо нельзя включать переменную класса
        # __slots__ = ['x', 'y', '__dict__', STATIC_NAME]

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def setCoords(self, x, y):
            self.x = x
            self.y = y

        def getCoords(self):
            return self.__slots__

    pt = Point(10, 20)

    pt.x = 1
    pt.y = 2
    pt.z = 55

    print(pt.getCoords())
    print(pt.z)


def func2():
    """
    Пример использование обьекта-свойства property с помощью
    которого можно описать методы доступа к атрибутам обьекта.
    """
    class Point:

        def __init__(self, x=0, y=0):
            self.__x = x
            self.__y = y

        def __checkValueOnNumber(self, value):
            if isinstance(value, int) or isinstance(value, float):
                return True
            return False

        # Методы работы с x
        def __getCoordX(self):
            print('__getCoordX')
            return self.__x

        def __setCoordX(self, x):
            print('__setCoordX')
            if self.__checkValueOnNumber(x):
                self.__x = x
            else:
                raise ValueError('Данные должны быть int и float')

        def __delCoordX(self):
            print('__delCoordX')
            del self.__x

        # Методы работы с y
        def __getCoordY(self):
            print('__getCoordY')
            return self.__y

        def __setCoordY(self, y):
            print('__setCoordY')
            if self.__checkValueOnNumber(y):
                self.__x = y
            else:
                raise ValueError('Данные должны быть int и float')

        def __delCoordY(self):
            print('__delCoordY')
            del self.__y

        coordX = property(__getCoordX, __setCoordX, __delCoordX)
        coordY = property(__getCoordY, __setCoordY, __delCoordY)

    pt = Point(10, 20)

    print('Использование X:')
    pt.coordX = 100
    print(pt.coordX)
    del pt.coordX

    print('\nИспользование Y:')
    pt.coordY = 200
    print(pt.coordY)
    del pt.coordY


# func1()
func2()












