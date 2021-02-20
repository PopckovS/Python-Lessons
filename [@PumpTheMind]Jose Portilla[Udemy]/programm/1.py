#! /usr/bin/python3


def func1():
    """ Различные способы форматированного вывода данных в строках

    %s - стандартный вывод как одной так и кортежом переменных, с помощью str()
    %f - вывод числа float в форматированном виде
    %r - вывод переменной при помощи строкового представления repr()
    """
    var1 = 816
    print('Переменная var1 = %s' %var1)
    print('0 = %s, 1 = %s, 2 = %s ' %('hi', 'two', 3))

    var_float = 135.45
    print('var_float = %15.5f'%(var_float))

    var_str = 'строка'
    print('Вывод переенной var_str = %r'%var_str)


def func2():
    """list """
    my_list1 = ['one', 'two', 2, 3.14, 1.618]
    my_list2 = my_list1[:]

    my_list1 += 'new var'
    my_list2 += ['new var']

    print(my_list1)
    print(my_list2)

    del_element1 = my_list1.pop()
    del_element2 = my_list1.pop(1)

    print(del_element1)
    print(del_element2)

    print(my_list1)
    print(my_list2)

def func3():
    pass


func2()
