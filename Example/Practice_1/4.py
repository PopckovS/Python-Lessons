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


