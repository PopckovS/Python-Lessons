#! /usr/bin/python3


from custom_functions import trace
import os
import math

"""Решение задач из теста по Python"""

def func1(rad):
    """
    Расчитать обьем сферы по радиусу
    Формула расчета: V = (4/3)*pi*r**3
    При радиусе v = 5 правильный ответ 523.5987755982989
    """
    v = (4 / 3) * (math.pi) * (rad ** 3)
    print(v)


def func2(num, low, high):
    """
    Первый вариант
    Функция должна принимать 3 аргумента и проверять входит ли число
    в указанный диапозон.
    """
    if low <= num <= high:
        return True
    return False


def func21(num, low, high):
    """
    Второй вариант
    Функция должна принимать 3 аргумента и проверять входит ли число
    в указанный диапозон.
    """
    return num in range(low, high)


def func3(string):
    """
    Функция должна посчитать количество символов в верх и низ
    регистр в веденной строке.
    """
    if type(string) is str:
        upp = 0
        low = 0
        other = 0
        for char in string:
            if char.isupper():
                upp += 1
            elif char.islower():
                low += 1
            else:
                other +=1
        print("Всех элементов {all}".format(all=len(string)))
        print("Низ.рег: {low} Верх.рег: {upp}".format(low=low, upp=upp))
        print("Остальных: {other}".format(other=other))
        print("Всего: {low} + {upp} + {other} = {all}".format(all=len(string), low=low, upp=upp, other=other))
    else:
        raise ValueError("Аргумент должен быть строкой.")


def func4(in_list):
    """
    Первый вариант
    Принимает список, и возвращает этот же список но только с
    уникальными элементами.
    """
    if type(in_list) is list and len(in_list) > 1 :
        return list(set(in_list))
    else:
        raise ValueError("Аргумент должен быть списком, и иметь больше одного элемента.")


def func41(in_list):
    """
    Второй вариант
    Принимает список, и возвращает этот же список но только с
    уникальными элементами.
    """
    if type(in_list) is list and len(in_list) > 1 :
        result_list = []
        for elem in in_list:
            if elem not in result_list:
                result_list.append(elem)
        return result_list
    else:
        raise ValueError("Аргумент должен быть списком, и иметь больше одного элемента.")



def func5(in_list):
    """
    Функция принимает список и перемножает его элементы.
    С начала происходит проверка что это список, иначе исключение, далее
    каждый элемент перемножается на превыдущий, если же какойто из элементов
    не является типом int/float то исключение.
    """
    if type(in_list) is list and len(in_list) > 1:
        result = 1
        for elem in in_list:
            if (type(elem) is int) or (type(elem) is float):
                result *= elem
            else:
                raise ValueError("Значения списка должны быть числами.")
        return result
    else:
        raise ValueError("Аргумент должен быть списком, и иметь больше 1 элемента.")


def func6(string):
    """
    Функция проверяет является ли ввденная строка полиндромом.
    """
    if (type(string) is str) and (len(string) > 0) :
        return string == string[::-1]
    else:
        ValueError("Аргумент должен быть строкой, и иметь хотябы 1 символ.")



def func7(sentence):
    """
    Первый вариант
    Функция принимает строку и проверяет является ли строка панграмой.
    Тоесть встречавется ли каждая буква алфавита в строке хотябы 1 раз.
    """
    from string import ascii_lowercase as alphabet

    for char in alphabet:
        if sentence.find(char) == -1:
            return False
    return True


def func71(sentence):
    """
    Второй вариант
    Функция принимает строку и проверяет является ли строка панграмой.
    Тоесть встречавется ли каждая буква алфавита в строке хотябы 1 раз.
    """
    from string import ascii_lowercase as alphabet

    # print(sentence)
    # my_list = set(sentence)
    # print(my_list)
    # my_list = list(my_list)
    # my_list.sort()
    # print(my_list)

    alphaset = set(alphabet)
    return alphaset <= set(sentence.lower())



# func1(5)

# print(func2(5, 1, 10))
# print(func21(5, 1, 10))

# func3("Hello Mr. Rogers, how are you this fine Tuesday?")

# print(func4([1,1,1,2,2,3,3,3,4,4,5,5,6,6,7]))
# print(func41([1,1,1,2,2,3,3,3,4,4,5,5,6,6,7]))

# print(func5([1, 2, 3, -4]))
# print(func5("ewsrgf"))
# print(func5([1, "sdf", 3, -4]))

# print(func6("hello"))
# print(func6("helleh"))

print(func7("The quick brown fox jumps over the lazy dog"))
print(func71("The quick brown fox jumps over the lazy dog"))





