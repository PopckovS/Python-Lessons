import math


def binary_search_1(unknown, diapason_floor, diapason_ceil, limit_of_search=None):
    """
    :param unknown: the number what we search
    :param diapason_floor: floor of slice
    :param diapason_ceil: ceil of slice
    :param limit_of_search: limit of steps of search
    :return:
    """
    diapason = list(range(diapason_floor, diapason_ceil+1))
    counter = 0
    current_number = round(len(diapason)/2)

    while True:
        counter += 1
        if unknown == current_number:
            print('We found your number, is : ', current_number)
            print('Number of steps : ', counter)
            break

        diapason_len = round(len(diapason)/2)
        current_number = diapason[diapason_len]

        # If the unknown number is less than the current
        if unknown > diapason[diapason_len]:
            diapason = diapason[diapason_len:]
        # If the unknown number is higher than the current
        elif unknown < diapason[diapason_len]:
            diapason = diapason[:diapason_len]

        if limit_of_search is not None and counter == limit_of_search:
            print('Maximum step limit exceeded : {limit}'.format(limit=limit_of_search))
            break


binary_search_1(10, 0, 100, 200)

