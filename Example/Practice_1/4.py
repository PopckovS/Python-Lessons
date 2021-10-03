import os
import sys


def func1():
    """ Три способа убрать пробелы из строчки.

    1) Во первых это метод place(" ", "")
    2) При помощи split разбиваем строчку на список и соединяем
    снова в строчку при помощи join
    3) Генератором списка фильтруем от пробелов, и генерируем новый
    список, где каждый элемент будет отдельным символом и соединяем
    методом join
    """
    string = 'aaa bbb ccc ddd eee'

    # Первый способ
    string1 = string.replace(" ", "")
    print(string1)

    # Второй способ
    string2 = ''.join([elem for elem in string if elem != " "])
    print(string2)

    # Третий способ
    string3 = ''.join(string.split())
    print(string3)


def func2():
    """
    Проблема индексов !
    Как думаете что выведет этот код ?
    """
    nums = [1, 2, 5, 10, 3, 100, 9, 24]

    for i in nums:
        print(i)
        if i < 5:
            nums.remove(i)

    print('\nФинальный результат: ', nums)


def func3():
    """
    Примеры различных итераций по структурам.

    enumerate() - возвращает кортеж из ключа и значения послед.
    при этом действует на list, tuple, set

    Для итерации по словарям следует использовать метод
    items() - который возвращает кортеж из ключа и значения.
    """
    print('Пример enumerate:')
    nums = [10, 22, 55, 34, 88]
    # nums = (10, 22, 55, 34, 88)
    # nums = {10, 22, 55, 34, 88}
    # nums = {'a': 'aa', 'b': 'bb', 'c': 'cc', 'd': 'dd'}
    for key, val in enumerate(nums):
        print(f'{key} : {val}')

    print('\nПример dict.items()')
    dicts = {'a': 'aa', 'b': 'bb', 'c': 'cc', 'd': 'dd'}
    for key, val in dicts.items():
        print(f'{key} : {val}')


def func4():
    """
    Вывод елочки из указанного количества символов.
    К примеру так:
        *
        **
        ***
        ****
        *****
    """
    char = str(input('Введите символ: '))
    max_line = int(input('Количество линий '))
    for i in range(1, max_line+1):
        for j in range(1, 1+i):
            print(char, end='')
        print('\n')


def func5():
    """
    Вывоод елочки, от 0 до указанного числа, пример:
        1
        2 3
        4 5 6
        7 8 9 10
        ...
    """

    # Вывод чисел от 0 до введенного, в виде елочки
    number = 1
    max = int(input('Ведите число :'))
    line_min = 0
    line_max = 1

    while number <= max:
        if line_min == line_max:
            line_min = 0
            line_max += 1
            print('\n')

        # Опционально, для красивого вывода, можно заменить на
        # print(number, end=' ')
        if number == max:
            print(number)
        else:
            print(number, end=' ')

        number += 1
        line_min += 1


def func6():
    """
    Разница между get() и доступу по ключу к словарей.

    Если элемента не сущ-ет то обращение по ключу даст ошибку,
    в то время как метод .get() ошибки не даст, вернет только None
    или дефолтное значение если оно указано.
    """
    person = {'name': 'Phill', 'age': 22}

    # Тут будет ошибка, по несущ-му ключу обращаться нельзя
    # print(person['some-value'])

    print('Name: ', person.get('name'))
    print('Age: ', person.get('age'))
    print('Salary: ', person.get('salary'))
    print('Salary: ', person.get('salary', 0.0))


def func7():
    """
    Пример использования Monkey Patching
    """
    import math

    # Backup the original value before monkey patching
    original_pi = math.pi
    print(math.pi)  # Output: 3.141592653589793

    # Now monkey patch pi to have the value 3.14
    math.pi = 3.14
    print(math.pi)  # Output: 3.14

    # Remove the patch
    math.pi = original_pi
    print(math.pi)  # Output: 3.141592653589793


def func8():
    """
    3 способа инвертировать список.
    Требуется развернуть список на изнанку.
    """
    import copy

    alist = [1, 2, 3, 4, 5]

    a = copy.copy(list(reversed(alist)))
    b = alist[::-1]

    c = copy.copy(alist)
    c.reverse()

    print('a = ', a, ' id = ', id(a))
    print('b = ', b, ' id = ', id(b))
    print('c = ', c, ' id = ', id(c))

    print('\n Другой пример')
    alist = [[1, 2], [3, 4]]
    new_list = [x for el in alist for x in el]
    # new_list = [el for el in alist]
    print(new_list)


def func9():
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


def func10():
    """
    Примере List comprehensions для генерации списков
    и не только списков
    """
    import random
    x = random.choice([1, 2, 3])
    print('Рандомно выбранное число: ', x)

    list1 = [elem for elem in range(1, 25, 2)]
    print(f'Тип: {type(list1)}  Содержимое: {list1}')

    tuple1 = (elem for elem in range(1, 11))
    tuple1 = tuple(tuple1)
    print(f'Тип: {type(tuple1)}  Содержимое: {tuple1}')

    set1 = {elem for elem in range(1, 11)}
    print(f'Тип: {type(set1)}  Содержимое: {set1}')

    dict1 = {elem: elem for elem in range(1, 11)}
    print(f'Тип: {type(dict1)}  Содержимое: {dict1}')


def func11():
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

def func12():
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

# func1()
# func2()
# func3()
# func4()
# func5()
# func6()
# func7()
# func8()
# func9()
# func10()
# func11()
func12()