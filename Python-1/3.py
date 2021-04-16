#! /usr/bin/python3

def func1():
    """
    Метод декоратор на основании полученного аргумента
    проверяет наличие прав на доступ к методу.
    """

    permissions = ["user", "admin"]

    def check_permission(perm):
        def wrapper_permission(function):
            def check_wrapper(*args):
                if perm not in permissions:
                    raise ValueError("Нет доступа")
                result = function(*args)
                return result
            return check_wrapper
        return wrapper_permission

    @check_permission("user")
    def any_user():
        print('Есь доступ')

    @check_permission("admin")
    def for_admin():
        print('Для admin')

    any_user()
    for_admin()


def func2():
    """
    Создаем декоратор из класса без аргументов самого декоратора,
    методика такова, тоже есть 2 оборачивающих функции, внешняя
    принимает аргументом саму функцию, внутреняя принимает аргументом
    аргументы оборачиваемой функции. Последовательность:
        __init__(function) - Принимает функцию
        __call__(*args, **kwargs) - Принимает аргументы функции
    Тоетсь реализация этого способа, идет через маг метод __call__()
    """

    class MyDecorator:

        def __init__(self, function):
            # print(f'Отработал метод __init__ {function}')
            self._function = function

        def __call__(self, *args, **kwargs):
            # print('Отработал метод __call__')
            # print(args, type(args))
            # print(kwargs, type(kwargs))
            return self._function(*args, **kwargs)

    @MyDecorator
    def function(a, b):
        return a * b

    print(function(2, 5))


def func3():
    """
    Создание декоратора из класса, с приемом аргументов декоратора.
    Тут все аткже как и с декор из функций,сть обертка из 3 функций:
    __init__(decorator_arg) Принимает аргументы самого декоратора
    __call__(function) Принимает функцию
    wrapper(function_args) обертка над функцией, принимает арг функции
    """

    class MyDecorator:

        def __init__(self, decorator_arg):
            self._decorator_arg = decorator_arg
            self._function = None

        def __call__(self, function):
            self._function = function

            def wrapper(*args, **kwargs):
                result = self._function(*args, **kwargs)
                return f'{self._decorator_arg} {result}'
            return wrapper

    @MyDecorator('Р е з у л ь т а т : ')
    def function(a, b):
        return a * b

    print(function(10, 5))


def func4():

    import functools

    @functools.lru_cache()
    def fetch_data(items):
        """Do some serious work here"""
        result = [fetch_item_data(i) for i in items]
        return result

    def fetch_item_data(i):
        return i**2

    fetch_data([1,2,3,4,5])




# func1()
# func2()
# func3()
func4()




