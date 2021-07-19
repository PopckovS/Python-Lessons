#! /usr/bin/python3

import os
import sys


def func1():
    """
    Пример простейшей фабрики.

    Когда мы создаем внешнюю функцию, и она получает значение
    lo и hi эти значения остаются в ее поле видимости, когда мы
    возвращаем внутренюю функуию sorted_range которая уже будет
    использовать в работе те самые переменные lo и hi.
        Тоесть наша внутр функция которую мы вернули, сохраянет
    ссылки на переменные lo и hi внешней области видимости.
    Тоетсь мы имеем доступ к переменным которые не обьявлены явно
    в нашей функции.
        Тоесть наша внутреняя функция в своей local области
    берет значение из обл видимости enclosing
    """

    def fabric_sorted(lo: int, hi: int) -> list:
        def sorted_range(first, *args):
            result = []
            for element in (*first, ) + args:
                if lo <= element <= hi:
                    result.append(element)
            return result
        return sorted_range

    example_1 = fabric_sorted(100, 200)
    print(example_1(range(0, 300)))
    print(example_1(range(0, 151)))


def func2():
    """
    Пример декорторов функций.

    Делаем замену атрибутов: __doc__ __name__ __module__
    самостоятельно, также по мимо этого это можно сделать
    2 другими способами, модулем functools
    """

    def show_result(function, text):
        """Функция для вывода результатов"""

        print('\n', '='*10, text, '='*10)
        print(function(48))
        print(f'{function.__name__}.__doc__ = function.__doc__')
        print(f'{function.__name__}.__name__ = function.__name__')
        print(f'{function.__name__}.__module__ = function.__module__')

    def example_1():
        """Реализация самостоятельно"""

        def trace(function):
            def inner(*args, **kwargs):
                print('Название:{} Аргументы: {} {}'.format(function.__name__, args, kwargs))
                return function(*args, **kwargs)
            inner.__doc__ = function.__doc__
            inner.__name__ = function.__name__
            inner.__module__ = function.__module__
            return inner

        @trace
        def foo(x):
            """I am do anything useful"""
            return x

        show_result(foo, 'Реализация самостоятельно')

    def example_2():
        """
        Реализация через @functools.wraps(function)
        """
        import functools

        def trace(function):
            @functools.wraps(function)
            def inner(*args, **kwargs):
                print('Название:{} Аргументы: {} {}'.format(function.__name__, args, kwargs))
                return function(*args, **kwargs)
            return inner

        @trace
        def foo(x):
            """I am do anything useful"""
            return x

        show_result(foo, 'Реализация через @functools.wraps(function)')

    def example_3():
        """
        Реализация через functools.update_wrapper(inner, function)
        """
        import functools

        def trace(function):
            def inner(*args, **kwargs):
                print('Название:{} Аргументы: {} {}'.format(function.__name__, args, kwargs))
                return function(*args, **kwargs)
            functools.update_wrapper(inner, function)
            return inner

        @trace
        def foo(x):
            """I am do anything useful"""
            return x

        show_result(foo, 'Реализация через functools.update_wrapper(wrapper_func, function)')

    example_1()
    example_2()
    example_3()


def func3():
    """
    Еще примеры с декораторами, сложная тема!

    Создав глоб переменную clobal_enable_trae_wraps = True/false
    и делая проверку таково рода:
        return inner if clobal_enable_trae_wraps else function
    мы можем манипулировать будет работать обертка или нет,
    таким образом мы можем вкл/выкл ее активность.

    Видеоурок:
    https://www.youtube.com/watch?v=h_B3O5jWMi4&list=PLlb7e2G7aSpTTNp7HBYzCBByaE1h54ruW&index=4
    """

    import functools

    clobal_enable_trase_wraps = True

    def trace(handle):
        def decorator(function):
            @functools.wraps(function)
            def inner(*args, **kwargs):
                if clobal_enable_trase_wraps:
                    result = function(*args, **kwargs)
                    print('Функция обертка inner отработала')
                    print('Название:{} Аргументы: {} {}'.format(function.__name__, args, kwargs))
                    print('Результат: ', result)
                    return result
                else:
                    result = function(*args, **kwargs)
                    print('Результат: ', result)
                    return result
            return inner
            # return inner if clobal_enable_trase_wraps else function(*args, **kwargs)
        return decorator

    @trace(sys.stderr)
    def foo(x):
        """I am do anything useful"""
        return x

    foo(488)
    clobal_enable_trase_wraps = False
    foo(555)


def func4():
    """
    В самом python уже есть функция мемоизатор.
    Декоратор мемоизатор @functools.lru_cache()
    """
    import functools

    @functools.lru_cache(maxsize=128)
    def function(a, b):
        return a * b

    print(function(2, 5))
    print(function.cache_info())

    print(function(20, 50))
    print(function.cache_info())


def func5():
    """
    Примеры конвертациии символов в кодировке Юникода
    """

    # UTF-8
    a = 'hello world'
    print(list(map(ord, a)))

    # UTF - 16
    b = 'Привет мир'
    print(list(map(ord, b)))

    # UTF - 16
    c = '⏸'
    print(list(map(ord, c)))

    # UTF-16
    print(chr(9208))

    # UTF - 32
    print(chr(127025))


def func6():
    """
    Примеры методов строк.
    """

    print('.upper() Оригинал: "foo bar" =', 'foo bar'.upper())
    print('.lower() Оригинал: "foo bar" =', 'foo bar'.lower())
    print('.swapcase() Оригинал: "Foo Bar" =', 'foo bar'.swapcase())
    print('.title() Оригинал: "foo bar" =', 'foo bar'.title())
    print('.capitalize() Оригинал: "foo bar" =', 'foo bar'.capitalize())

    print(".rjust(20, '-') 'foo bar' = ", "foo bar".rjust(20, '-'))
    print(".ljust(20, '-') 'foo bar' = ", "foo bar".ljust(20, '-'))
    print(".center(20, '-') 'foo bar' = ", "foo bar".center(20, '-'))

    print('lstrip("[]") "foo bar" = ', '[]foo bar[]'.lstrip('[]'))
    print('rstrip("[]") "foo bar" = ', '[]foo bar[]'.rstrip('[]'))
    print('strip("[]") "foo bar" = ', '[]foo bar[]'.strip('[]'))

    print('split(",") "foo,,,bar" = ', 'foo,,,bar'.split(','))
    print('split() "foo zap bar" = ', 'foo zap bar'.split())

    my_list = ['a','b','c','d','e']
    print(','.join(my_list))

    str_1 = 'привет мир!'
    print(str_1, ' = ', 'привет' in str_1)

    str_2 = 'привет мир!'
    print(str_2, ' = ', 'привsdет' not in str_2)

    str_3 = 'привет мир!'
    print(str_3, ' = ', str_3.startswith('при'))

    str_4 = 'привет мир!'
    print(str_4, ' = ', str_4.endswith('мир!'))


def func7():
    """
    Примеры работы с файлами.
    """

    file_name = 'test.txt'
    file = open(file_name, 'w')

    print('Название файла: ', file_name)
    print('Файл: ', file)
    print('Тип файла: ', type(file))
    print('file.fileno() Номер файлового дескриптора: ', file.fileno())
    print('file.mode: ', file.mode)
    print('file.closed: ', file.closed)
    print('file.name: ', file.name)
    print('file.closed Файл закрыт ? : ', file.closed)
    print('sys.stdout : ', sys.stdout)

    result = input('Что записать в конец файла ? ')

    # 2 способа записи данных в файл
    file.write('Первая строчка\n')
    file.write('Вторая строчка\n')

    file.write(f'В файл записано: {result}')
    # print(f'В файл записано : {result}', file=file)

    file.close()
    if file.closed:
        print('\nФайл был закрыт\n')

    file = open(file_name, 'r')

    if not file.closed:
        print('***Файл снова открыт***')

    print('Считаем из файла текст: \n')

    # Далее 3 способа считать данные из текстового фала

    # Первый способ прочитать все сразу
    print(file.read())

    # Второй способ прочитать по одной строчек за раз
    # тоесть проитерироваться как по итерируемому обьекту
    # print(file.readline())
    # print(file.readline())
    # print(file.readline())

    # Схож со вторым способом, итерация по строчке
    # методом for
    # for line in file:
    #     print(line)

    file.close()
    if file.closed:
        print('\nФайл снова закрыт\n')


def func8():
    """
    Пример работы метода file.flush() который
    отправляет содержимое буфера в файл с которым работает.
    """
    import io

    file = open('test.txt', 'w+')

    print(sys.stdout)
    print(file)

    file.write('Этот текст\n')
    file.write('и он попадет на жесткий диск\n')
    file.write('и попадет он в файл еще до закрытия файла\n')
    file.write('метод file.flush() вызывает этот вывод\n')

    file.flush()

    file.write('А вот этот текст попадет после.')

    file.close()



# Раскоментите нужную функцию
# func1()
# func2()
# func3()
# func4()
# func5()
# func6()
# func7()
# func8()