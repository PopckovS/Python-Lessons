#! /usr/bin/python3

from custom_functions import trace
import os
import sys

def func1():
    """Генерировать можно как списки так и множества"""
    #  Тут мы генерируем обычный список, из четных
    #  элементов и умножаем каждый элемент на 10
    my_list = [ i*10 for i in range(10) if i%2==0]
    print(my_list)

    # Генерируем множество
    my_set = {i*10 for i in range(10) if i%2==0}
    print(my_set)

    var1 = {}
    print(var1)
    print(type(var1))


def func2():
    """Операции над множествами"""
    # Проверка на равенство множеств
    set1 = {1,2,3,4,5}
    set2 = {1,2,3,4,5}

    if set1 == set2:
        print("да")
    else:
        print("нет")

    # Проверка содержит ли одно множ в себе все элементы другова
    set1 = {1, 2, 3, 4, 5, 6}
    set2 = {1, 2, 3, 4, 5}

    print("set1 > set2 = ", set1>set2)


def func3():
    """set и frozenset"""
    set1 = set('hello')
    frset1 = frozenset('hello')

    print(type(set1), ' = ', set1)
    print(type(frset1),' = ', frset1)

    print(set1 == frset1)


def func4():
    """
    Задача:
    На вход подается строка, состоящая из круглых скобок.
    Выведите True, если скобки вложены правильно и False, если нет
    """

    # Первый способ через обычную функцию
    def check_balance(stricng):
        if string.count('(') == string.count(')'):
            return True
        return False

    # Второй способ через lambda
    lambda_check_balance = lambda var: var.count('(') == var.count(')')

    # string = "(()"
    string = "(())"

    print("lambda = ", lambda_check_balance(string))
    print("check_balance = ", check_balance(string))


def func4():
    """
    Задача:
    На вход подаются массив A и целое число K. Сделайте циклический
    сдвиг входного массива K раз и верните получившийся массив.
        A = [2, 5, 1, 4, 6] -> [6, 2, 5, 1, 4,]
        K = 1
    """
    def shake_list(my_list, iter):
        original = my_list.copy()

        for i in range(iter):
            last = [my_list.pop()]
            my_list = last + my_list

        return {"Оригинал":original, "Результат":my_list}

    my_list = [2, 5, 1, 4, 6]
    iter = 3
    print(shake_list(my_list, iter))


def func5():
    pass


# func1()
# func2()
# func3()
func4()


