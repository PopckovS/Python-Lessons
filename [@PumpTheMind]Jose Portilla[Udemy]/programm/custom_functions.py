#! /usr/bin/python3

def trace(array):
    print('='*10)
    print('Тип данных: {type}'.format(type=type(array)))
    print('Строковое представление: {repr}'.format(repr=repr(array)))
    print('Вывод элементов:')
    print(array)
    print('='*10)


# trace([1,2,3,4,5])
# trace({'1':'1', '2':'2', '3':'3'})