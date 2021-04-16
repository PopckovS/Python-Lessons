#! /usr/bin/python3

import time

def fibo(n):
    """Вычисление ряда Фибоначи"""
    fib1 = 1
    fib2 = 1
    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
    return fib2


def func1():
    """
    Разница между вызывами perf_counter() даст время
    прошедшее между их вызывами.
    """
    time_1 = time.perf_counter()
    time.sleep(1)
    time_2 = time.perf_counter()

    print(f'{time_1} - {time_2} = {time_2 - time_1}')


def func2():
    """Вычисление времени исполнения функции."""
    time_1 = time.perf_counter()
    result = fibo(1000)
    time_2 = time.perf_counter()

    print(f'{time_1} - {time_2} = {time_2 - time_1:0.4f}')
    print(f'Результат счета фисла фибоначи {result}')


def func3():
    """
    Пример простейшего функции-декоратора для подсчета
    времени исполнения кода.
    """

    def decorator_timer(func):
        def wrapper(*args):
            time_1 = time.perf_counter()
            result = func(*args)
            time_2 = time.perf_counter()
            print(f'Время исполнения программы: {time_1} - {time_2} = {time_2 - time_1:0.4f}')
            return result
        return wrapper

    @decorator_timer
    def fibo(n):
        """Вычисление ряда Фибоначи"""
        fib1 = 1
        fib2 = 1
        i = 0
        while i < n - 2:
            fib_sum = fib1 + fib2
            fib1 = fib2
            fib2 = fib_sum
            i = i + 1
        return fib2

    print('Счет числа фибоначи с декоратором: ', fibo(1000))


def func4():
    """
    Пример реализации отслежки времени выполнения при помощи классов.
    Своего класса ошибок и класса что работает с модулем time
    """
    class TimerError(Exception):
        pass

    class MyTimer:

        def __init__(self):
            self._start_time = None
            self._all_time = []
            self._all = 0

        def start(self):
            """Запускает таймер"""
            if self._start_time is not None:
                raise TimerError('Таймер уже работает.')
            print('Таймер запущен')
            self._start_time = time.perf_counter()

        def sleep(self, seconds: int):
            """Таймер засыпает"""
            time.sleep(seconds)

        def stop(self):
            """Останавливает таймер"""
            if self._start_time is None:
                raise TimerError('Таймер еще не запущен.')
            print('Таймер остановлен')
            time_result = time.perf_counter() - self._start_time
            self._all_time.append(time_result)
            self._all += time_result
            self._start_time = None
            print(f'Время выполнения: {time_result:0.4f}')

        def show_all_time(self):
            print(f'Все время по частям: {self._all_time}')
            print(f'Все время : {self._all}')

    # 4 раза вызываем на исполнение код для накопления таймера
    tr = MyTimer()

    for number in range(1, 5):
        print(f'Попытка  №{number}')
        tr.start()
        tr.sleep(1)
        result = fibo(1000)
        tr.stop()

    print(f'Ряд Фибоначи: {result}')
    tr.show_all_time()


def func5():
    pass


    # class MyTimer:
    #     # def __init__(self, *args):
    #     #     print(args)
    #     #     print('__init__')
    #
    #     def __call__(self, function):
    #         # print(function)
    #         # print('__call__')
    #         def wrapper():
    #             function()
    #         return wrapper
    #
    #
    # @MyTimer()
    # def func():
    #     print('func')












# func1()
# func2()
# func3()
# func4()
func5()




