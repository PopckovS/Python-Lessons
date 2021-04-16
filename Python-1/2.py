#! /usr/bin/python3

def func1():
    """
    Разница между обычной функцией и функцией-генератором
    что использует yield для создания обьекта итератора.
    """

    def get_all_average(N):
        """
        Обычная функция. при N = 100 размер ее будет
        равен = 888 байт.
        """
        avs = []
        count = 0
        s = 0
        for i in range(1, N+1):
            count += 1
            s += i
            # print(f'{s} / {count} = {s/count}')
            avs.append(s/count)
        return avs

    print('Байт памяти 1-й функции: ', get_all_average(100).__sizeof__())

    def get_number():
        """
        Обычная функция, возвращает список, размер этой
        функции при списке в range(100) имеет размер 984 байт
        """
        return list(range(100))

    x = get_number()
    print('Байт памяти 2-й функции: ', x.__sizeof__())

    def get_yield_number():
        """
        Функция-генератор, использует оператор yield
        для создания обьекта генератора, и благодоря тому
        что является итератором, занимает всего 64 байт
        """
        for x in range(100):
            yield x
        print('Это никогда не будет выведено ')

    s = get_yield_number()

    print('Функция-генератор: ', s)
    print('Память функции-генератора: ', s.__sizeof__())

    print(next(s))
    print(next(s))
    print(next(s))
    print(next(s))


def func2():
    """
    Особенность работы циклов for в Python
    и использование класса enumerate
    """
    def func_for_1():
        """
        Перебор списка, с заменой всех его элементов, но
        они не изменятся, ибо element - содержит ссылку
        на элемент списка, и мы меняем ссылку а не список.
        """
        print('Первая функция')
        ml_1 = [1, 2, 3, 4, 5]
        print(f'Список до : {ml_1}')

        for element in ml_1:
            element = '+'

        print(f'Список после : {ml_1}')

    def func_for_2():
        """
        Один из способов иметь допуск не к ссылке в к
        самим значениям списка, при помощи индексов.
        """
        print('Вторая функция')
        ml_2 = [1, 2, 3, 4, 5]
        print(f'Список до : {ml_2}')

        for iter in range(len(ml_2)):
            ml_2[iter] = '+'

        print(f'Список после : {ml_2}')

    def func_for_3():
        """
        Пример работы с применением класса enumerate()
        который принимает последовательность, и возвращает
        кортеж из индекса и значения.
        """
        print('Третия функция')
        ml_3 = [1, 2, 3, 4, 5]
        print(f'Список до : {ml_3}')

        for iter, value in enumerate(ml_3):
            print(f'{iter} = {value} || ml_3[{iter}] = {ml_3[iter]}')

        print(f'Список после : {ml_3}')

    func_for_1()
    func_for_2()
    func_for_3()


def func3():
    """
    Пример декоратора, тут все прсото мы определяем
    функцию-декоратор, которая возвращает функцию обертку,
    которая принимает внешнею функцию и работает с ней.
    """

    def Decorator1(func):
        def wrapper(*args):
            func(*args)
        return wrapper

    @Decorator1
    def func1(x, y):
        print(f'func1 x = {x} y = {y}')

    func1(10, 20)


def func4():
    """
    Пример декоратора с аргументами, тут будет тройная
    вложенность функций, внешний слой принимает аргументы
    ссамого декоратора, внутренний слой принимает функцию с
    которой работает, а третий слой, работает как непосредственная
    обертка над функцией которую мы декорируем.
    """

    def Decorator1(input_arg):
        def the_real_decorator(func):
            def wrapper(*args):
                result = func(*args)
                return f'input_arg={input_arg} '+result
            return wrapper
        return the_real_decorator


    @Decorator1(55)
    def func1(x, y):
        # print(f'func1 x = {x} y = {y}')
        return f'func1 x = {x} y = {y}'

    print(func1(10, 20))


def func5():
    """
    Декоратор из класса,
    """

    class Decorator:

        __static_name = None
        __static_id = None
        __static_num = None

        def __init__(self, *args):
            print(f'args = {args}')
            print(f'тип args = {type(args)}')
            print(f'Получено = {args[0]}')
            print('Отработал меод:  __init__')

        def __call__(self, *args, **kwargs):
            print('Отработал меод:  __call__')

    @Decorator
    def func1():
        print('Hello world')

    func1()


def func6():
    """Использование таймера для вычисления скорости работы кода."""
    import time

    def fib(n):
        if n < 2:
            return n
        return fib(n - 2) + fib(n - 1)

    time_1 = time.perf_counter()
    time.sleep(1)
    print('fib(20) =', fib(10))
    time_2 = time.perf_counter()

    print(f'{time_1} - {time_2} = {time_2-time_1}')


def func7():
    """
    Функция декоратор memorize() кеширует значения функции func()
    ссохранение происходит в словаре, если значение уже было
    вычислено, то просто возвращаем его.
    """
    import time

    def memorize(function):
        mem = {}

        def wrapper(*args):
            if args in mem:
                print('Кешировано ', end='')
                time.sleep(1)
                return mem[args]
            result = function(*args)
            mem[args] = result
            time.sleep(2)
            print('Не Кешировано ', end='')
            return result

        return wrapper

    @memorize
    def func(a, b) -> int:
        """Результаты рработы функции будут кешированы"""
        return a * b


    def start():
        """
        Метод запускает в обработку 5 запросов к декорируемой
        функции, первый запрос не кешируется и исполняется с задержкой,
        второй запрос кешируется.
        """
        a = 2
        b = 5

        def work(counter, a, b):
            time_1 = time.perf_counter()
            print(f'№{counter} Значение: {func(a, b)} ', end='')
            time_2 = time.perf_counter()
            print(f'Время исполнения: {time_2 - time_1}')

        for counter in range(1, 6):
            work(counter, a, b)
            work(counter, a, b)
            a += 1
            b += 1

    start()


def func8():
    """
    Декоратор обрабатывает исключение деления на ноль.
    """

    class ZeroDeleteError(Exception):
        """Класс обработки исключения деления на ноль"""

        def __init__(self, message):
            super().__init__()
            self._message = message

        def getMessage(self):
            return self._message


    def check_error(function):
        def wrapper(*args):
            try:
                result = function(*args)
                return result
            except ZeroDivisionError:
                # raise ZeroDeleteError('Ошибка, деление на ноль запрещено.')
                zr = ZeroDeleteError('Ошибка, деление на ноль запрещено.')
                print(zr.getMessage())
        return wrapper

    @check_error
    def func1(a, b):
        return a / b

    print(func1(10, 5))
    print(func1(10, 0))


# func1()
# func2()
# func3()
# func4()
# func5()
# func6()
# func7()
func8()












