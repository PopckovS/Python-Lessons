import os
import sys


def func1():
    """
    Сколько памяти вв байтах занимают различные структуры данных ?
    использование __slots__ в виде list или tuple снижает потребление
    памяти.
    """
    print('dict().__sizeof__() = ', dict().__sizeof__())
    print('list().__sizeof__() = ', list().__sizeof__())
    print('tuple().__sizeof__() = ', tuple().__sizeof__())
    print('set().__sizeof__() = ', set().__sizeof__())

    class Point_1:
        def __init__(self, name):
            self.name = name

    class Point_2:
        __slots__ = ('name',)

        def __init__(self, name):
            self.name = name

    pt1 = Point_1('первый')
    pt2 = Point_2('второй')
    print('pt1 = ', pt1.__sizeof__(), pt1.__dict__.__sizeof__())
    print('pt2 = ', pt2.__sizeof__(), pt2.__slots__.__sizeof__())


def func2():
    """

    """
    import weakref

    class SimplClass:
        pass

    print('Обычный класс SimplClass.__weakrefoffset__ = ', SimplClass.__weakrefoffset__)
    print('type.__weakrefoffset__ = ', type.__weakrefoffset__)
    print('int.__weakrefoffset__ = ', int.__weakrefoffset__)
    print('str.__weakrefoffset__ = ', str.__weakrefoffset__)
    print('bool.__weakrefoffset__ = ', bool.__weakrefoffset__)
    print('list.__weakrefoffset__ = ', list.__weakrefoffset__)
    print('dict.__weakrefoffset__ = ', dict.__weakrefoffset__)
    print('tuple.__weakrefoffset__ = ', tuple.__weakrefoffset__)
    print('set.__weakrefoffset__ = ', set.__weakrefoffset__)
    print('float.__weakrefoffset__ = ', float.__weakrefoffset__)

    # class DictClass:


def func3():
    """
    Примеры того как выводить память обьектов, разными методами
    pympler, __sizeof__, sys.getsizeof
    """

    from pympler import asizeof

    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    def get_memory(obj):
        print(f'\nОбьект: {obj}')
        print('sys.getsizeof(obj) = ', sys.getsizeof(obj))
        print('obj.__sizeof__() = ', obj.__sizeof__())
        print('pympler.asizeof.asizeof(obj)  = ', asizeof.asizeof(obj))

    a = [1, 2, 3]
    b = [1, 2, [1, 2, 3]]
    с = [1, 2, [Point(10, 10), Point(10, 10), Point(10, 10)]]
    d = Point(10, 10)

    get_memory(a)
    get_memory(b)
    get_memory(с)
    get_memory(d)
