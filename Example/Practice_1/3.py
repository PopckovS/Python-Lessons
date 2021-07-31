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



def func4():
    """
    Сколько памяти занимают различные обьекты в Python.

    None - это ничего а занимает 16 байт
    int - числа почти всегда одинаково 32 байта
    dict - хуже всего это словарь 240 байт

    Использование __slots__ в качестве tuple почти в 3 раза
    уменьшает размер хранимых значенией.
    """
    from pympler import asizeof

    def show_memory(obj):
        print(str(obj), ' = ', asizeof.asizeof(obj))

    show_memory(None)
    show_memory(3)
    show_memory(30000000)
    show_memory(30.45)
    show_memory([])
    show_memory({})
    show_memory(tuple())
    show_memory(set())
    show_memory('Hello world !')
    show_memory('')

    class Rect_1:
        def __init__(self, x1,x2,x3,x4):
            self.x1 = x1
            self.x2 = x2
            self.x2 = x2
            self.x2 = x2

    class Rect_2:
        # __slots__ = ['x1','x2','x3','x4']
        __slots__ = ('x1', 'x2', 'x3', 'x4')

        def __init__(self, x1, x2, x3, x4):
            self.x1 = x1
            self.x2 = x2
            self.x2 = x2
            self.x2 = x2

    print('Rect_1 : ', asizeof.asizeof(Rect_1(0, 0, 0, 0)))
    print('Rect_2 : ', asizeof.asizeof(Rect_2(0, 0, 0, 0)))


def func5():
    """
    Модуль pympler

    muppy.get_objects() - метод считывает все существующтие
    обьекты в Python вызывая этот метод 2 раза в разный
    промежуток времени, мы можем выявить какие обьекты были
    созданы с первого среза.

    summary.get_diff() - выявляет какие обьекты как разницу между
    двумя срезами.

    summary.print_() - красиво выводит на экран обьекты и память
    ими занимаемую.
    """
    from pympler import asizeof
    from pympler import muppy
    from pympler import summary

    print('\nИспользование muppy :')
    alll_obj_1 = muppy.get_objects()

    data = list(range(1000))

    alll_obj_2 = muppy.get_objects()

    sum1 = summary.summarize(alll_obj_1)
    sum2 = summary.summarize(alll_obj_2)

    summary.print_(summary.get_diff(sum1, sum2))


def func6():
    """
    Интересное о строках

    Механизм создания ссылок на строки можно легко сломать !
    Форматирование при помощи + требует гораздо больше времени
    чем использование метода .format() для сложения требуется:
        Метод + требует: 2.3470056476071477e-06
        Метод format() требует: 6.971997208893299e-06
    """

    import time

    a = "sgfsdgsgsfgd"
    b = "sgfsdgsgsfgd"
    print('id(a) == id(b) : ', id(a) == id(b))
    print('a is b : ', a is b)

    a1 = 'a'*40
    b1 = 'a'*40
    print('\nid(a1) == id(b1) : ', id(a1) == id(b1))
    print('a1 is b1 : ', a1 is b1)

    print('\nid(2*3*3) == id(2*3*3) : ', id(2*3*3) == id(2*3*3))
    print('2*3*3 is 2*3*3 : ', 2*3*3 is 2*3*3)

    # Подсчет конкатенацией +
    time1 = time.perf_counter()
    print('10'+' '+' '+'20'+' '+'30'+' '+'40'+' '+'50'+' '+'60')
    time2 = time.perf_counter()
    print(f"{time2} - {time1} = {time2 - time1}")

    # Подсчте при помощи метода format()
    time1 = time.perf_counter()
    print('{0} {1} {2} {3} {4} {5}'.format(10,20,30,40,50,60))
    time2 = time.perf_counter()
    print(f"{time2} - {time1} = {time2 - time1}")


def func7():
    """
    """
    a = 40
    b = 20
    большее_число = a if a > b else b
    print(большее_число)

    class Point:
        """Описние класса"""
        static_x = 10
        static_y = 20

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def show(self):
            print(self.x, self.y)

    obj = Point(100, 200)
    print(dir(Point))
    print(dir(obj))

    print('\n')
    # help(Point)
    help(obj)


def func8():
    """
    Различные примеры работы разных функций.
    """
    name = "M234onica"
    print(name.isalnum())

    name = "M3onica Gell22er "
    print(name.isalnum())

    name = "Mo3nicaGell22er"
    print(name.isalnum())

    name = "133"
    print(name.isalnum())

    name = "133!"
    print(name.isalnum())

    print('Мы находимс в : ', os.getcwd())

    string1 = "flyiNg"
    string2 = "flyiNgz"
    print(f'{string1} : ', max(string1))
    print(f'{string2} : ', max(string2))

    nums = ["one", "two", "three", "four", "five", "six", "seven"]
    s = " ".join(nums)
    print(s)


def func9():
    """Различные примеры кода."""
    first = 'a'
    second = 'ф'

    print(first > second)
    # print(ord(first), ord(second))

    def facto(n):
        if n == 1:
            return 1
        return n * facto(n - 1)

    print(facto(4))

    string = 'I love Python'
    print(f'Вывести все буквы t в строчке "{string}" : ')
    for i in range(len(string)):
        if string[i] == 't':
            print(string[i])

    print(f'Вывести строку "{string}" без пробелов : ')
    for i in range(len(string)):
        if string[i] != " ":
            print(string[i], end='')
    print('\n')
