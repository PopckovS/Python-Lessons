#! /usr/bin/python3

from custom_functions import trace
import os
import sys

def func1():
    """Обычный класс"""

    class Sample(object):
        pass

    x = Sample()

    print(x)
    print(type(x))


def func2():

    class Dog():

        # mammal - млекопитающие
        species = "mammal"

        def __init__(self, breed):
            self.breed = breed

        def show_info(self):
            print("species = ", Dog.species)
            print("breed = ", self.breed)


    dog_one = Dog(breed="Lab")
    dog_one.show_info()
    print(dog_one.species)

    dog_two = Dog(breed="Huskie")
    dog_two.show_info()
    print(dog_two.species)


def func3():
    """
    Заменить символ * в строке на ! заменить именно
    одиночный символ: 'aaa ** bbb  * eee * bcd ** '
    """
    string = 'aaa ** bbb  * eee * bcd ** '
    result = string.replace(' * ', '!')
    print(result)


def func4():
    """
    Если выписать все натуральные числа меньше 10,
    кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.

    Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
    """

    first = 10
    second = 1000

    def counter(max):
        my_tuple = (3, 5)
        result = 0
        for i in range(max):
            if i%my_tuple[0] == 0:
                # print(i)
                result +=i
            elif i%my_tuple[1] == 0:
                # print(i)
                result += i
        print("Результат = ", result)

    counter(first)
    counter(second)


def func5():
    """
    Вывести ряд Фибоначи
    """
    first, second, result = 1, 1, 1
    for i in range(5):
        print(result)
        result = second + first
        first = second
        second = result

def func6():
    """
    Вывести ряд Фибоначи при помощи рекурсии
    """
    def fi_rec(first, second):
        pass


def func7():
    """
    Найдите сумму всех четных элементов ряда Фибоначчи,
    которые не превышают четыре миллиона.
    """
    first, second, mass = 1, 1, 1
    result = 0

    while result <= 4000000:
        mass = second + first
        if mass % 2 == 0:
            print(mass)
            result += mass
        first = second
        second = mass

    print("Результат = ",result)


def func8():
    """
    Число-палиндром с обеих сторон (справа налево и слева направо) читается
    одинаково. Самое большое число-палиндром, полученное умножением двух
    двузначных чисел – 9009 = 91 × 99.

    Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
    """
    max_a, max_b = 0, 0

    for i in range(100, 1000):
        for j in range(100, 1000):
            num = str(i * j)
            if num == num[::-1]:
                max_a = i
                max_b = j
                result = num
                print("{i} * {j} = {num}".format(i=i, j=j, num=num))

    print("Наибольшее число путем умножения двух трех знач чисел {i} * {j} = {num}".
          format(i=max_a, j=max_b, num=result))



# func1()
# func2()
# func3()
# func4()
# func5()
# func6()
# func7()
func8()




# Передача аргументов. Как в питоне передаются изменяемые и неизменяемые
# объекты? По значению, указателю или еще как-то=)








