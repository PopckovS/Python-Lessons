import time

"""Различные способы работы с датой временем."""


def func1():
    """Использование таймера для вычисления скорости работы кода."""

    def fib(n):
        if n < 2:
            return n
        return fib(n - 2) + fib(n - 1)

    time_1 = time.perf_counter()
    time.sleep(1)
    print('fib(20) =', fib(10))
    time_2 = time.perf_counter()

    print(f'{time_1} - {time_2} = {time_2-time_1}')


def func2():
    """
    Написать функцию которая принимает список и возвращает
    True/False есть ли в списке дубликаты.
    """
    def check_dublicates(original: list) -> bool:
        return True if len(original) > len(set(original)) else False

    input = [1, 2, 3, 4, 5]
    print('Есть ли дубликаты: ', check_dublicates(input))


def func3():
    """Пример кеширования результатов вычисления."""
    import functools

    @functools.lru_cache()
    def fetch_data(items):
        """Пработа до отработки внутренней функции"""
        result = [fetch_item_data(i) for i in items]
        return result

    def fetch_item_data(i):
        return i**2

    fetch_data([1, 2, 3, 4, 5])




func1()
func2()
