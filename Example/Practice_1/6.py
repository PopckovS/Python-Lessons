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


func1()
