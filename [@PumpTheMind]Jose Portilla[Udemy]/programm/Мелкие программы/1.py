#! /usr/bin/python3

from custom_functions import trace

def func1(cross=5):
    """Есть список, вывести все элементы списка что меньше чем 5 """
    list_one = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    list_result = []

    # Формируем новый список
    for i in list_one:
        if i < cross:
            list_result.append(i)

    # Выводим отсортированный список
    for i in list_result:
        print(i)

def func2(list_one, list_two, mod=0):
    if (type(list_one) is not list) or (type(list_two) is not list):
        print('Оба аргумента должны быть списками')
    elif (len(list_one) == 0) or (len(list_two) == 0):
        print('Списки должны быть не пусты')

    list_result = []

    # Первый способ, нестрогое и строгое на основе аргумента mod
    for elem_one in list_one:
        for elem_two in list_two:
            if elem_one == elem_two:
                list_result.append(elem_one)

    # Вывод получившегося списка
    print(list_result)

# func1()
func2(
    # list_one=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
    list_two=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
    # list_two=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    list_one=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    mod=0
)



