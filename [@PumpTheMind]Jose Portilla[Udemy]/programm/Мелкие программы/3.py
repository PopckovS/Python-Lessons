#! /usr/bin/python3

from custom_functions import trace
import os

def func1():
    """Множества set"""
    my_list = [1, 1, 2, 2, 2, 3, 3, 4, 4]
    my_set = set()

    my_set.add(1)
    my_set.add(2)
    # Добавление нового значения в множество не сработает
    # множество содержит только уникальные значения
    my_set.add(2)

    print("Переменная my_list с типом {type} содержит {my_list}"
          .format(my_list=my_list, type=type(my_list)))

    print("Переменная my_set с типом {type} содержит {my_set}"
          .format(my_set=my_set, type=type(my_set)))

    my_list = set(my_list)

    print("Заменяем тип переменной list на set и значения в переменной "
          "становится: {my_list}"
          .format(my_list=my_list)
          )

def func2():
    print("Маленький тест по знанию Python")
    test_label = " *** Тест {number} № ***"

    # Посчитать
    print(test_label.format(number=1))
    print(4*(6+5))
    print(4*6+5)
    print(4+6*5)

    # Чему равен тип вычислений ?
    print(test_label.format(number=2))
    x = 3 + 1.5 + 4
    print(type(x))
    print(x)

    # Найти квадрат и корень числа
    print(test_label.format(number=3))
    import math
    print(math.sqrt(16))
    print(16**0.5)
    print(4**2)

    # Вывести символ "e" из строки используя индексирование
    print(test_label.format(number=4))
    string = "Hello"
    print(string[1])


    # Развернуть строку используя индексы 2 метода
    print(test_label.format(number=5))
    print(string[::-1])


    # Использовать 2 методы чтобы извлечь "o" из строки
    print(test_label.format(number=6))
    print(string[-1])
    print(string[4])


    # Создать список с 3 нулями двумя способами
    print(test_label.format(number=7))
    my_list1 = [0,0,0]
    my_list2 = [0]*3
    print(my_list1)
    print(my_list2)


    # Есть список, замените в нем слово "hello" на "goodbye"
    print(test_label.format(number=8))
    my_list = [1, 2,[3,4,'"hello"']]
    print(my_list)
    my_list[2][2] = "goodbye"
    print(my_list)


    # Отсортировать данный список
    print(test_label.format(number=9))
    l = [3,4,5,5,6]
    l.sort()
    print(l)


    # Используя ключи и индексирование, извлечь "hello" следующих
    # словарей
    print(test_label.format(number=10))
    d = {'simply_key':'hello'}
    print(d['simply_key'])

    d = {'k1':{'k2':'hello'}}
    print(d['k1']['k2'])

    d = {'k1':[{'nest_key':['this is deep', ['hello']]}]}
    print(d['k1'][0]['nest_key'][1][0])


    # Использовать множества чтобы найти уникальные значения в списке
    print(test_label.format(number=11))
    l = [1,2,33,4,4,11,22,3,3,2]
    l = set(l)
    print(l)

    # Проверить равенство чему оно равно ?
    print(test_label.format(number=12))
    l_one = [1,2,[3,4]]
    l_two = [1,2,{'k1':4}]

    # False
    result = l_one[2][0] >= l_two[2]['k1']
    print(result)


def func3():
    """Сортировка списка с переводом в множество не работает."""
    l = [1, 2, 33, 4, 4, 11, 22, 3, 3, 2]
    l.sort()
    print(l)
    l = set(l)
    print(l)

    my_set = set([1, 2, 33, 4, 4, 11, 22, 3, 3, 2])
    print(my_set[0])


def func4():
    my_set = set([1, 2, 33, 4, 4, 11, 22, 3, 3, 2])

    for elem in my_set:
        print(type(elem), elem)


def func5():
    """Удаляем элементы из множества 3 способами"""
    num_set = {1, 2, 3, 4, 5, 6}

    num_set.discard(5)
    num_set.remove(4)

    delete_element = num_set.pop()

    print("Элемент что был рандомно удален методом 'pop()' = ", delete_element)
    print(num_set)

def func6():
    set_one = set([1,2,3,4,5])
    set_two = set([6,7,8,9,10])

    set_new = set_one.union(set_two)
    print("Вывод обьедененных множеств: ", set_new)

    x = {1, 2, 3}
    y = {4, 5, 6}
    z = {7, 8, 9}

    output =  x.union(y, z)
    print("Вывод еще одного обьеддененного множества: ", output)

def func7():
    """2 способа добавить слово в список по элементам"""

    # Первый способ
    l = list()
    for letter in "word":
        l.append(letter)
    print(l)

    # Второй способ
    my_list = []
    my_list += "word"
    print(my_list)


def func8():
    from random import randint

    my_list = [letter for letter in "word"]
    print(my_list)


    # Генерирцем матрицы
    # Обычный список
    matrix_one = [ randint(0, 10) for i in range(3) ]

    # Количество строк/колонок
    column = 3
    row = 3

    # Диапозон значений матрицы max/min
    max = 10
    min = 0

    # Генерация матрицы
    matrix_two = [ [randint(min, max) for c in range(column)] for r in range(row) ]

    print(matrix_one)
    print(matrix_two)

def func9():

    my_list = [number for number in range(1, 11)]
    print(my_list)

# func1()
# func2()
# func3()
# func4()
# func5()
# func6()
# func7()
# func8()
func9()
