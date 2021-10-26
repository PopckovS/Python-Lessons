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


def func3():
    """
    Итераторы и выражения-генераторы
    """
    # Список
    lt1 = [1, 2, 3]

    # Список превращается в итератор
    it = iter(lt1)
    print(it)

    # next() Функция что перебирает итерируемый обьект
    # очередно по его элементам, и только один раз
    print(next(it))
    print(next(it))
    print(next(it))
    # Дойдя до конца вернутся в начало невозможно

    print('Генератор')
    # Выражение-генератор, далее по нему можно проходится
    # и без функции next() просто вызывая этот элемент
    lt2 = (element for element in range(1000))

    # Первый проход выведет 0-100
    for elem in lt2:
        print(elem)
        if elem >= 100:
            break

    # Втрой проход выведет 100-200
    for elem in lt2:
        print(elem)
        if elem >= 200:
            break


def func4():
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


def func5():
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


def func6():
    """
    Функция декоратор memorize() кеширует значения функции func()
    сохранение происходит в словаре, если значение уже было
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


def func7():
    """
    Что можно использовать в качестве ключей словаря:
    строки, числа, кортежи что содержат только неизменяемые
    типы данных
    """
    ml = {"one": 10, "two": 20, 3: 30, (1, 3): 40}

    print(ml)
    print("ml['one'] = ", ml['one'])
    print("ml[3] = ", ml[3])
    print("ml[(1, 3)] = ", ml[(1, 3)])


def func8():
    """
    Класс менеджера контекста для обработки списков
    """
    class VectorTesting:
        """
        Класс создает менеджер контекста.

        Принимает вектор и защищает его от изменений
        если что-то пошлео не так, для работы создается
        временный вектор, если ошибок не было то сохраняем
        измененный вектор.
        """

        def __init__(self, vector):
            self.__vector = vector

        def __enter__(self):
            self.temp = self.__vector[:]
            return self.temp

        # return False - обработка исключений передается на более
        # верхний уровень. True -  будет уходить на ур выше.
        def __exit__(self, exc_type, exc_val, exc_tb):
            if exc_type is None:
                self.__vector[:] = self.temp
            return False

    # Пример работы с вектором
    vector_1 = [1, 2, 3]
    vector_2 = [5, 5, 5]
    # vector_2 = [5, 5]
    print('vector_1 = ', vector_1)
    print('vector_2 = ', vector_2)

    # Складываем 2 вектора одинаковой длинны
    try:
        with VectorTesting(vector_1) as vector_temp:
            for i in range(len(vector_temp)):
                vector_temp[i] += vector_2[i]
    except Exception as e:
        print('Произошло исключение = ', e)

    print('Новый vector_1 = ', vector_1)


def func9():
    """
    Использование метода copy или метода copy.copy
    из модуля copy дает одиноковые результаты работы.
    Это дает поверхностное копирование shallow copy
    """
    import copy

    print('Использование обычного copy:')
    my_list_1 = [1, 2, 3, 4, 5, [1,2,3]]

    # my_list_2 = my_list_1.copy()
    my_list_2 = copy.copy(my_list_1)

    print('До изменения')
    print(f'my_list_1 : {my_list_1}')
    print(f'my_list_2 : {my_list_2}')

    print('\nИзменение')
    print('my_list_2[0] = 555')
    print('my_list_2[5][0] = 777\n')
    my_list_2[0] = 555
    my_list_2[5][0] = 777

    print('\nПосле изменения')
    print(f'my_list_1 : {my_list_1}')
    print(f'my_list_2 : {my_list_2}')



def func10():
    """
    Использование метода deepcopy из модуля copy
    дает полное глубокое рекурсивное копирование.
    """
    import copy

    print('Использование глубокого deepcopy метода:')
    my_list_1 = [1, 2, 3, 4, 5, [1, 2, 3]]

    my_list_2 = copy.deepcopy(my_list_1)

    print('До изменения')
    print(f'my_list_1 : {my_list_1}')
    print(f'my_list_2 : {my_list_2}')

    print('\nИзменение')
    print('my_list_2[0] = 555')
    print('my_list_2[5][0] = 777\n')
    my_list_2[0] = 555
    my_list_2[5][0] = 777

    print('\nПосле изменения')
    print(f'my_list_1 : {my_list_1}')
    print(f'my_list_2 : {my_list_2}')





# func1()
# func2()
# func3()
# func4()
# func5()
# func6()
# func8()
# func8()
# func9()
func10()

