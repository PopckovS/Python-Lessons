#! /usr/bin/python3

from custom_functions import trace
import os

def func1():
    """Различные примеры генерации списков"""

    l = [letter for letter in "word"]
    print("Генерация цикла словом 'word' :", l)

    odd = [ number for number in range(0, 11) if number%2==0]
    print("Генерация цикла с условием на четность : {odd}".format(odd=odd))

    for_for = [ i*j for j in range(0, 3) for i in range(0, 3) ]
    print("Генерация с вложенным циклом 'for' : %s"%for_for)

    celsius = [0, 10, 20.1, 34.5]

    # Формула расчета градуса Фаренгейта, где C - цельсия.
    # (C * 9/5)+32  Пример, при 0 градусов по цельсию (0*9/5)+32 = 32

    celsius = [0, 10, 20.1, 34.5]
    farenhait = [ (temp*9/5)+32 for temp in celsius]

    print("Расчет градусов по Цельсию и Фаренгейту")
    print("Цельсия : %s"%celsius)
    print("Фаренгейт : %s"%farenhait)

    odd_list = [num for num in range(0, 10) if num % 2 == 0]
    print("Четными элементами %s"%odd_list)

    odd_list_2 = [num+2 for num in range(0, 10) if num%2==0]
    print("Четными элементами сложенными с '+2' %s"%odd_list_2)


def func2():
    """Генерация списка в списке"""

    for_list = [x**2 for x in range(0, 11)]

    # Вторая форма записи for_for_list = [ x**2 for x in for_list]
    for_for_list = [ x**2 for x in [x**2 for x in range(0, 11)] ]

    print("2 Списка,бычная генерация и цикл в цикле :")
    print("Список при помощи 'for' : {for_list}".format(for_list=for_list))
    print("Генерация списка в списке :%s"%(for_for_list))


def func3():
    """Вывести слова начинающиеся на букву 's' из строки."""

    string = 'Print only the words that start with s in this sentence'
    print("Строка :%s"%string)
    split_sting = string.split(' ')

    print("Вывод слов начинающихся с  буквы 's' :")
    counter = 0
    for word in split_sting:
        if word[0] == 's':
            print("Слово {counter} : {word}".format(counter=counter,word=word))
        counter += 1

def func4():
    """Вывести все четные(even) в диапозоне range(0, 10)"""

    # Первый способ
    print("Вывод четных элементов, первый способ")
    for elem in range(0, 10):
        if elem%2==0:
            print(elem)

    # Второй способ
    my_even_list = [elem for elem in range(0, 10) if elem%2==0]
    print("Вывод четных элементов, с помощью генератора списков")
    print(my_even_list)


def func5():
    """Используя генератор списков, создать список в диапозоне
    от 0 до 50 делимые на 3 без остатка.
    """
    my_list = [elem for elem in range(0, 51) if elem%3==0]
    print("Список где каждый элемент делится на 3 без остатка")
    print(my_list)

    for elem in my_list:
        print("{elem} % 3 = {result}".format(elem=elem, result=elem%3))


def func6():
    """Есть предложение, если колич символ в слове чет вывести чет."""
    sentence = "Print every word in this sentence that has an even" \
               " number of letters"
    words = sentence.split(" ")

    for word in words:
        counter = len(word)
        if counter%2==0:
            print("Четное : '{word}' Колич символов : '{counter}'".
                  format(counter=counter, word=word)
                  )

def func7():
    """Вывести числа от 0 до 100
    кратные 3 заменить на Fizz
    кратные 5 заменить на Buzz
    кратные и 5 и 3 заменить на FizzBuzz
    """
    for num in range(0, 100):
        if (num % 5 == 0) and (num % 3 == 0):
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else:
            print(num)

def func8():
    """Есть предложение, составить список из первых букв каждого его слова
       используя генератор списков.
    """
    sentence = "Create a list of the first letters of every word in this string"
    my_list = [word[0] for word in sentence.split(" ")]
    print(my_list)


# func1()
# func2()
# func3()
# func4()
# func5()
# func6()
# func7()
func8()







