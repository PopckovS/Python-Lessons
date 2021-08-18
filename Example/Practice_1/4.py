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


# func1()
# func2()
# func3()
# func4()
# func5()
func6()