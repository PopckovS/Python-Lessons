#! /usr/bin/python3

from custom_functions import trace
import os
import sys

def func1():
    """
    Дана строка с целыми числами 'a1b2c3'
    Преобразуйте строку так, чтобы вместо этих чисел стояли их кубы.
    """
    string =  'a1b2c3'
    pass


def func2():
    """Мелкие примеры кода"""
    print("="*10)
    # -2.3333333333333335
    print(7/-3)

    print("=" * 10)
    # Для создания кортежца из одного элемента требуется поставить
    # одну запятую,
    var1 = ('',)
    print(var1[0])
    print(type(var1[0]))
    print(type(var1))

    print("=" * 10)
    print(range(3))
    print(list(range(3)))

    print("=" * 10)
    # Строки можно соеденить таким способом
    string1 = '123''456'
    string2 = '123'+'456'
    print(string1)
    print(string2)

    print("=" * 10)
    print(7//3)
    print(-7//3)
    print((7//3) + (-7//3))

    print("=" * 10)
    string = 'key'*3
    string = string[2]+string[4]
    # Будет ошибка выход за пределы
    # string += string[6]
    print(string)


def func3():
    """Задачки на списки"""

    print('='*20)
    # Дан список некоторых целых чисел, найдите значение 20 в нем и,
    # если оно присутствует, замените его на 200. Обновите список
    # только при первом вхождении числа 20.
    my_list = [1, 2, 55, 43, 20, 154, 20, 67, 20]
    print(my_list)
    for i in range(len(my_list)):
        if my_list[i] == 20:
            my_list[i] = 200
            break
    print(my_list)


    print('=' * 20)
    # Другой способ решения этой задачи использовать метод index
    list1 = [5, 10, 15, 20, 25, 50, 20]
    print(list1)
    index = list1.index(20)
    list1[index] = 200
    print(list1)


    print('=' * 20)
    # Необходимо удалить пустые строки из списка строк
    # TODO функция filter
    list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
    resList = list(filter(None, list1))
    print(resList)



def func4():
    """
    Дан список чисел. Превратите его в список квадратов этих чисел.
    спользуем для этого 3 способа: циклом, лямбда, и генератор списков
    """

    my_list = [1, 2, 3, 4, 5]
    print("Первый способ я списка = ", my_list)
    for i in range(len(my_list)):
        my_list[i] *= my_list[i]
    print(my_list)

    my_list =  [2, 3, 4, 5, 6]
    print("Второй способ я списка = ", my_list)
    sortinf_func = lambda x: x*x
    my_list = list(map(sortinf_func, my_list))
    print(my_list)

    my_list = [3, 4, 5, 6, 7]
    print("Третий способ я списка = ", my_list)
    my_list = [ i*i for i in my_list ]
    print(my_list)



def func5():

    str1 = "Hello, world!"
    str2 = ', world!'
    print(str1+str2)
    # Строки можно сложить но нельзы вычесть
    # print(str1-str2)

    # В Питоне можно делать так, мы сразу создаем кортеж и тут же
    # берем его срез
    x, y, z = (1,2,3,4,5,6,7,8,9,10)[2::3]
    print(x)
    print(y)
    print(z)

    # TODO как работает copy() ?
    l1 = [1, [2,3], 4]
    l2 = l1.copy()
    l2[1][1] = 7
    print(l1)
    print(l2)


    # При итерации по словарю в него попадают ключи
    d = {0:'a', 1:'b', 2:'c'}
    for i in d:
    # for i in d.keys():
        print(i)

    # TODO Лямбда ыункции можно запускать сразу с передачей аргумента в них
    print(   (lambda x:(x+3)*5/2)(3)  )

var= 34
def func6():
    # Эта функция выводит словарь со всеми глобальными переменными
    print(globals())

def func7():
    one = 1
    two = 'два'
    print(locals())

def func8():

    class  My_Class():

        static_var = 'Это статичная переменная класса'

        def __init__(self, name, my_list):
            self.name = name
            self.my_list = my_list

            # Можно самостоятельно добавить или переопределить __dict__
            # self.__dict__ = {'one':1, 'two':2}
            # self.__dict__['one'] = 1
            # self.__dict__['two'] = 2

    var1 = My_Class('Название Первое', [1, 2, 3, 4, 5])
    var2 = My_Class('Название Второе', ['one', 'two'])

    # print(vars(var1))
    # print(vars(var2))
    # print(vars(My_Class))

    print(var1.__dict__)
    print(var2.__dict__)
    print(My_Class.__dict__)



# func1()
# func2()
# func3()
# func4()
# func5()
# func6()
# func7()
func8()


# Суматоры полусуматоры алу мантисы

# Стандарты PEP8
# Модуль time ыечает за время
# Что такое канал pipe ? Поток ввода вывода между 2 программами
# Перезапись содержимого файла путем <<w>>
# instance узнатья вля обьект экз класса






















