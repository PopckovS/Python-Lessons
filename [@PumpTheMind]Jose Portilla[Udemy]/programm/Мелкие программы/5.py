#! /usr/bin/python3


from custom_functions import trace
import os

def func1():
    """Замените пробелы на указанные символы. Напишите метод
     для замены всех пробелов в строке на '%20'. Игнорируйте
     любые дополнительные пробелы в начале или конце строки.
    """
    string = " Первый Второй  Третий   Четвертый  "
    print(string)
    print(string.split())
    print(string.split(" "))

    string_len = len(string)-1
    left = ""
    right = ""

    for i in range(len(string)):
        if string[i] != ' ':
            print(i)
            break
        else:
            left += " "

    while string_len >0:
        if string[string_len] != ' ':
            print(string_len)
            break
        else:
            right += " "
            string_len -= 1

    result = left + '%20'.join(string.split()) + right
    print("Колич пробелов с права : {right} с лева : {left}".
          format(right=len(right), left=len(left))
          )
    print("'{result}'".format(result=result))


def check_simple_number(num):
    """
    Проверяет является ли целое число простым.
    :param num: Целое число
    :return: True/False
    """
    if type(num) is not int or num <=0:
        raise ValueError("Параметр должен быть целым положительным числом.")
    else:
        if (num==2 or num==3 or num==5) or (num%2!=0) and (num%3!=0) and (num%5!=0) and (num%7!=0):
            return True
        else:
            return False


def test_check_simple_number():
    """
    Метод прогоняет числа от 0 до 100 через метод check_simple_number
    """
    for num in range(1, 150):
        print("Число {num} = {result}"
              .format(num=num, result=check_simple_number(num))
              )

def is_prime(num):
    """
    Еще одна функция для проверки является ли число простым.
    :param num: Число
    :return: Текст с описанием, является ли число простым
    """
    for n in range(2, num):
        if num % n == 0:
            print("Число {num} не простое".format(num=num))
            break
        else:
            print("Число {num} простое".format(num=num))


def func2(arg1, arg2):
    print(arg1+arg2)


# func1()
# print(check_simple_number(7))
test_check_simple_number()
# is_prime(12)

