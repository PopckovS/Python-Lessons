#! /usr/bin/python3

def func1():
    """
    @classmethod - Метод имеет аргумент cls с сылкой на класс.
    @staticmethod - Статичный метод, нету спец аргументов.
    """
    class Point:

        STATIC_NAME = "Статическое название"

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def get_coord(self):
            return self.x, self.y

        @staticmethod
        def static_method():
            return Point.STATIC_NAME

        @classmethod
        def class_meythod(cls):
            return cls.STATIC_NAME


def func2():
    import timeit

    class One:
        """Заменяет __dict__ атрибутом __slots__"""
        __slots__ = ['x', 'y']

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def get_coord(self):
            return self.x, self.y

    class Two:
        """Имеет атрибут __dict__"""

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def get_coord(self):
            return self.x, self.y

    x1 = One(10, 20)
    x2 = Two(100, 200)

    print(timeit.timeit(x1.get_coord))
    print(timeit.timeit(x2.get_coord))

    print('Класс с __slots__ :', x1.__sizeof__())
    print('Класс с __dict__ :', x2.__sizeof__(), x2.__dict__.__sizeof__())


def func3():
    """
    Реализация паттерна программирования 'Моносостояние'
    """
    class Monopattern():
        __atributs = {
            'id': 0,
            'name': None
        }

        def __init__(self):
            self.__dict__ = Monopattern.__atributs

    x1 = Monopattern()
    x2 = Monopattern()

    print(f'x1:{x1.__dict__} x2:{x2.__dict__}')

    x1.id = 15
    x2.name = 'Hello world'

    print(f'x1:{x1.__dict__} x2:{x2.__dict__}')

# func1()
# func2()
func3()

