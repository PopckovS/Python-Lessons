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
    a_dict = {"one": 1, "two": 2, "three": 3}
    print('a_dict.keys() = ', a_dict.keys())
    print('type = ', type(a_dict.keys()))

    for key in a_dict:
        print(key)

    for key in a_dict.keys():
        print(key)



# func_1()
# func_2()
# func_3()
func_4()
