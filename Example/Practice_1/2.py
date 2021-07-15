#! /usr/bin/python3

import os
import sys


def func1():
    """
    Пример простейшей фабрики.

    Когда мы создаем внешнюю функцию, и она получает значение
    lo и hi эти значения остаются в ее поле видимости, когда мы
    возвращаем внутренюю функуию sorted_range которая уже будет
    использовать в работе те самые переменные lo и hi.
        Тоесть наша внутр функция которую мы вернули, сохраянет
    ссылки на переменные lo и hi внешней области видимости.
    Тоетсь мы имеем доступ к переменным которые не обьявлены явно
    в нашей функции.
        Тоесть наша внутреняя функция в своей local области
    берет значение из обл видимости enclosing
    """

    def fabric_sorted(lo: int, hi: int) -> list:
        def sorted_range(first, *args):
            result = []
            for element in (*first, ) + args:
                if lo <= element <= hi:
                    result.append(element)
            return result
        return sorted_range

    example_1 = fabric_sorted(100, 200)
    print(example_1(range(0, 300)))
    print(example_1(range(0, 151)))

