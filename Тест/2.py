"""#! /usr/bin/python3
"""

import sys


def func_1():
    func_range = range(1, 11)
    print('type(func_range) = ', type(func_range))
    print('func_range = ', func_range)

    func_xrange = xrange(1, 11)
    print('type(func_xrange) = ', type(func_xrange))
    print('func_xrange = ', func_xrange)


def func_2():
    var_1 = range(1, 11)
    print('var_1 = ', var_1)

    var_2 = range(1, 11, 2)
    print('var_2 = ', var_2)

    var_3 = range(1, 11, -1)
    print('var_3 = ', var_3)


def func_3():
    for number in range(5):
        print('number = ', number)

    for num in [0, 1, 2, 3, 4]:
        print('num = ', num)


def func_4():
    a_dict = {"two": 2, "three": 3, "one": 1 }
    print('a_dict.keys() = ', a_dict.keys())
    print('type = ', type(a_dict.keys()))

    for key in a_dict:
        print(key)

    for key in a_dict.keys():
        print(key)


def func_5():
    a_dict = {"C": 3, "B": 2, "A": 1}
    keys = a_dict.keys()

    keys = sorted(keys)

    print('a_dict.keys() = ', a_dict.keys())
    print('sorted(a_dict.keys()) = ', keys)

    for key in keys:
        print(key)

    print('')

    for key in keys:
        print(a_dict[key])


def func_6():
    a_dict = {"C": 3, "B": 2, "A": 1}
    keys = sorted(a_dict.keys())

    for key in keys:
        print(key, ' = ', a_dict[key])


def func_7():
    iter = 10
    while iter >= 0:
        print(iter)
        iter -= 1

    print('')

    iter = 0
    while iter <= 10:
        print(iter)
        iter += 1


def func_8():
    for i in range(1, 11):
        print('i = ', i)
    else:
        print('Блок else')

    print('')

    for i in range(1, 11):
        if i == 5:
            print('i равен 5 ')
            break
        print('i = ', i)
    else:
        print('Блок else')

    print('')

    for i in range(1, 11):
        if i == 5:
            print('i равен 5 ')
            continue
        print('i = ', i)
    else:
        print('Блок else')



# func_1()
# func_2()
# func_3()
# func_4()
# func_5()
# func_6()
# func_7()
func_8()