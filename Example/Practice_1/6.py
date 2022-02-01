import time

"""Различные способы работы с датой временем."""


def func1():
    """Использование таймера для вычисления скорости работы кода."""

    def fib(n):
        if n < 2:
            return n
        return fib(n - 2) + fib(n - 1)

    time_1 = time.perf_counter()
    time.sleep(1)
    print('fib(20) =', fib(10))
    time_2 = time.perf_counter()

    print(f'{time_1} - {time_2} = {time_2-time_1}')


def func2():
    """
    Написать функцию которая принимает список и возвращает
    True/False есть ли в списке дубликаты.
    """
    def check_dublicates(original: list) -> bool:
        return True if len(original) > len(set(original)) else False

    input = [1, 2, 3, 4, 5]
    print('Есть ли дубликаты: ', check_dublicates(input))


def func3():
    """Пример кеширования результатов вычисления."""
    import functools

    @functools.lru_cache()
    def fetch_data(items):
        """Пработа до отработки внутренней функции"""
        result = [fetch_item_data(i) for i in items]
        return result

    def fetch_item_data(i):
        return i**2

    fetch_data([1, 2, 3, 4, 5])


def func3(file_name):
    """ Напишите программу, которая принимает имя файла и выводит его расширение.
    Если расширение у файла определить невозможно, выбросите исключение.
    """
    try:
        if type(file_name) is not str:
            raise TypeError('Аргумент должен быть строкой.')
        file_split = file_name.split('.')
        if len(file_split) < 2:
            raise ValueError('Расширения файла не найдено.')
    except ValueError:
        print('У файла должно быть расширение')
    except TypeError:
        print('Аргумент должен быть строкой')
    else:
        print('Расширение файла = "{type}"'.format(type=file_split[-1]))


def func4(cross=5):
    """Есть список, вывести все элементы списка что меньше чем 5 """
    list_one = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    list_result = []

    # Формируем новый список
    for i in list_one:
        if i < cross:
            list_result.append(i)

    # Выводим отсортированный список
    for i in list_result:
        print(i)


def func5(list_one, list_two):
    """Найти пересечение списков"""
    if (type(list_one) is not list) or (type(list_two) is not list):
        print('Оба аргумента должны быть списками')
    elif (len(list_one) == 0) or (len(list_two) == 0):
        print('Списки должны быть не пусты')

    list_result = []

    # Поиск пересечений списков
    for elem_one in list_one:
        for elem_two in list_two:
            if elem_one == elem_two:
                list_result.append(elem_one)

    # Вывод получившегося списка
    print(list_result)



# func1()
# func2()
# func3()
# func4()
func5()

