#! /usr/bin/python3

import os


def func1():
    """
    Пример использования метода list.extend(list)
    extend - метод списка который добавляет список в конец.
    """
    my_list = ["Lion", "Tiger", "Bear", "Cheetah", "Puma"]
    list_to_add = ["Leopard", "Lynx"]

    my_list.extend(list_to_add)
    print(my_list)
    # ['Lion', 'Tiger', 'Bear', 'Cheetah', 'Puma', 'Leopard', 'Lynx']

    my_list = ['X', 'Y', 'Z']
    my_list.extend('abcd')

    print(my_list)
    # ['X', 'Y', 'Z', 'a', 'b', 'c', 'd']



def func2():
    """
    Примеры использования:
    os.walk - создает генераторы с содержимым для переданного пути
    os.path.join - соединяет пути в соответствии с текущей ос
    """
    test_dir = 'test-dir'

    gener = os.walk(test_dir)

    # for root, dirs, files in gener:
    #     print(root, dirs, files)

    print(next(gener))
    print(next(gener))

    print(os.path.join(r'C:\Python27\Tools\pynche', 'ChipViewer.py'))
    # C:\\Python27\\Tools\\pynche\\ChipViewer.py


def func3():
    """
    Пример создания списка всех путей к файлам в директории.
    В результате сканирования будет получено:
        ('test-dir', ['test-dir-2'], ['test.txt'])
        ('test-dir/test-dir-2', [], ['test-2.txt'])
    Дайнный пример соединяет файлы с их корнями, возвращает в виде
    списка, и заносит в финальный список.
        В результате получим:
    ['test-dir/test.txt', 'test-dir/test-dir-2/test-2.txt']
    """

    def magic(test_dir):
        acc = []
        for root, dirs, files in os.walk(test_dir):
            acc.extend(os.path.join(root, file) for file in files)
        return acc

    test_dir = 'test-dir'
    print('Пути к файлам:')
    print(magic(test_dir))


def func4():

    def func1(a, b):
        print(a * b)

    def testing():
        pass

    print(func1)
    print(func1.__code__)
    testing.__code__ = func1.__code__
    testing(2, 5)


def func5():
    """
    Различные мелкие примеры
    """

    print('='*20)
    a = 54
    print(type(a))
    print(type(type(a)))

    print('=' * 20)
    print('Проверка по значнеию None == None', None == None)
    print('Проверка по ссылке None == None', None is None)

    print('=' * 20)
    print(23423423324235325345353453453453453434534553534534534**23)

    print('=' * 20)
    str_1 = 'привет мир'
    str_2 = b'hello world'

    print('Unicod строка: ', str_1)
    print('Байтов строка: ', str_2)

    print(f'Тип Unicod роки: {type(str_1)}\nТип Байт строк: {type(str_2)}')

    print('=' * 20)
    list_1 = ['a', 'b', 'c']
    list_2 = ['d', 'f']
    list_3 = list_1 + list_2
    print(list_3)

    print('=' * 20)
    print(chr(65))
    print(ord('A'))

    print('=' * 20)
    переменна = "Да это работает"
    print(переменна)

    class МойКласс:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    обьект_моего_классса = МойКласс(10, 20)
    print(обьект_моего_классса.__dict__)

    print('=' * 20)
    a = {}
    print(a)
    print(type(a))

    print('=' * 20)
    print('Проверка есть ли значение в словаре')
    my_dict = {'a': 10, "b": 20, "c": 30}
    print('10 в значениях словаря: ', 10 in my_dict.values())
    print('a в значениях словаря: ', 'a' in my_dict)

    print('=' * 20)
    print('Тернарный оператор')
    var = 500
    result = True if var >= 100 else False
    print(f'var = {var} result = {result}')

    print('=' * 20)

    some = range(1, 11)
    print(some)
    print(type(some))

    my_list = list(some)
    print(my_list)
    print(type(my_list))


def func6():
    """
    Пример упаковка и распаковка аргументов функции.

    Когда мы передаем в функцию ряд аргументов, они приходят как
    кортеж, это называется упаковка и делается она при помощи *
    Но также есть и обратный процесс распаковки, уже получив корртеж,
    мы можем распаковать его в просто в ряд переменных.
    """

    def function_1(*args):
        print('Пример с распаковкой:')
        print(type(args))
        print(*args)

    def function_2(*args):
        print('\nПример без распаковки:')
        print(type(args))
        print(args)

    function_1(1,2,3,4)
    function_2(1,2,3,4)


def func7():
    """
    Красивый пример поиска минимального значения в неком пределе.

    По скольку нам требуется чтобы было что сортировать, то нам
    необходимо чтобы в функцию приходил хотябы один аргумент, для
    этого реализуем сразу 2 аргумента в функцию def min(first, *args)
    аргумент first обезательный аргумент так что мы точно получим
    хотябы 1 аргумент для сортировки, а потом просто в условии цикла
    обьеденяем их в кортеж по которому будем идти (first, ) + args

    Таким образом мы обязуем передавать хотябы 1 аргумент, и в тоже
    время работаем с ними как с единым кортежем.
    """

    import math

    def find_min(first, *args, min_inf=-math.inf, max_inf=math.inf):
        result = max_inf
        for element in (first, ) + args:
            if element < result and min_inf < element < max_inf:
                result = element
        # return max(result, min_inf)

    print(find_min(88, 12, 13, -5, min_inf=0, max_inf=255))
    print(find_min(12, 13, -5))


def func8():
    """
    Инициализация аргументов в функции по умолчанию.

    Когда в функции инициализируютсяаргументы по умолчанию ?
    интересный вопрос! это происходит один раз, при компиляции в
    байт код, тоесть однажды сделаные аргументы будут существовать
    далее, даже в последующих вызовах функции.

    После первой инициализации аргументы функции по умолчанию
    сохраняются в специальном атрибуте function.__defaults__
    этот атрибут содержит кортежи с данными которые и являются
    аргументами по умолчанию.
    """

    def tools(function):
        xs = [1, 1, 2, 3]
        print(function(xs))
        print('Аргументы по умолчанию', function.__defaults__)

    # Демонстрация как не надо делать
    def wrong_way():
        print("Как не надо делать")

        def unique(iterable, seen=set()):
            acc = []
            for item in iterable:
                if item not in seen:
                    seen.add(item)
                    acc.append(item)
            return acc

        tools(unique)
        tools(unique)

    # Демонстрация как надо делать
    def right_way():
        print("\nКак стоит поступать")

        def unique(iterable, seen=None):
            acc = []
            seen = set(seen or [])
            for item in iterable:
                if item not in seen:
                    seen.add(item)
                    acc.append(item)
            return acc

        tools(unique)
        tools(unique)

    wrong_way()
    right_way()


def func9():
    """
    Различные примеры распаковки.

    Распаковать можно не только структуры данных но и
    обычные строки.
    """
    x, y, z = 'abs'
    print(x, y, z)

    a, *b = 10, (20, 30), (40, 50)
    print(a, b)

    x, y = b
    print(x, y)

    first, *second, last = range(1, 5)
    print(f'first = {first} second = {second} last = {last}')




# func1()
# func2()
# func3()
# func4()
# func5()
# func6()
# func7()
# func8()
func9()






