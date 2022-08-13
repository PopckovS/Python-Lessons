import time

def func1():
    """
    Декорируем класс функцией которая реализует паттерн singleton
    """
    import functools

    def singleton(cls):
        instance = None

        @functools.wraps(cls)
        def inner(*args, **kwargs):
            nonlocal instance
            if instance is None:
                instance = cls(*args, **kwargs)
            return instance

        return inner

    @singleton
    class Noop:
        """Класс Noop может быть только в одном экземпляре."""

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def show(self):
            return f'self.x = {self.x} self.y = {self.y}'

    noop = Noop(10, 20)
    print('id(Noop) = ', id(Noop))
    print(noop.show())

    print()

    noop = Noop(55, 77)
    print('id(Noop) = ', id(Noop))
    print(noop.show())


def func2():
    """
    Даны два словаря:
    dictionary_1 = {'a': 300, 'b': 400} и
    dictionary_2 = {'c': 500, 'd': 600}. Объедините их в
    один при помощи встроенных функций языка Python.

    Копируем словарь и дополняем его новым словарем методом update()
    """
    d_1 = {'a': 300, 'b': 400}
    d_2 = {'c': 500, 'd': 600}

    print('\nd_1 = ', d_1)
    print('d_1.items() = ', d_1.items())
    print('\nd_2 = ', d_2)
    print('d_2.items() = ', d_2.items())

    d_3 = d_1.copy()
    d_3.update(d_2)
    print('\nd_3 = ', d_3)


def func3():
    """
    Дан словарь с числовыми значениями. Необходимо их все
    перемножить и вывести на экран.
    """
    my_dictionary = {'data1': 375, 'data2': 567, 'data3': -37, 'data4': 21}
    result = 1
    for i in my_dictionary.values():
        result *= i
    print(result)


def func4():
    """
    1) Создайте словарь, в котором ключами будут числа от
    1 до 10, а значениями эти же числа, возведенные в куб.

    2) Даны два списка одинаковой длины. Необходимо создать
    из них словарь таким образом, чтобы элементы первого
    списка были ключами, а элементы второго — соответственно
    значениями нашего словаря.
    """
    print('Решение первой задачи: ')
    result_dict = {i: i**3 for i in range(1, 11)}
    print(result_dict)

    print('\nРешение Второй задачи: ')
    keys = ['red', 'green', 'blue']
    values = ['#FF0000', '#008000', '#0000FF']
    res_dict = dict(zip(keys, values))
    print(res_dict)


def func5():
    """
    Создайте словарь из строки 'pythonist' следующим образом:
    в качестве ключей возьмите буквы строки, а значениями пусть
    будут числа, соответствующие количеству вхождений данной
    буквы в строку.
    """
    original = "pythonist"
    result_dict = { char:original.count(char) for char in original}
    print(result_dict)

def func6():
    """
    Свойства классов и примеры
    """

    class BigDataModel:

        def __init__(self, params=None):
            self.params = params if isinstance(params, list) else []
            # self._params = []

        @property
        def params(self):
            return self._params

        @params.setter
        def params(self, new_params):
            assert all(map(lambda i: i>0, new_params))
            self._params = new_params

        @params.deleter
        def params(self):
            del self._params

    model = BigDataModel()
    # model.params = [1, 2, -4]
    model.params = [1, 2]
    print(model.params)

    print('__mro__ указывает порядок вызова методов  множ наслед: ',
          BigDataModel.__mro__)

    print('BigDataModel.mro() = ', BigDataModel.mro())


def func7():
    """Вывести числа от 0 до 100
    кратные 3 заменить на Fizz
    кратные 5 заменить на Buzz
    кратные и 5 и 3 заменить на FizzBuzz
    """
    for num in range(0, 100):
        if (num % 5 == 0) and (num % 3 == 0):
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else:
            print(num)


def func8():
    """Есть предложение, если колич символ в слове чет вывести чет."""
    sentence = "Print every word in this sentence that has an even" \
               " number of letters"
    words = sentence.split(" ")

    for word in words:
        counter = len(word)
        if counter%2==0:
            print("Четное : '{word}' Колич символов : '{counter}'".
                  format(counter=counter, word=word)
                  )


def func9():
    """
    Разница между вызывами perf_counter() даст время
    прошедшее между их вызывами.
    """
    time_1 = time.perf_counter()
    time.sleep(1)
    time_2 = time.perf_counter()

    print(f'{time_1} - {time_2} = {time_2 - time_1}')


def func10():
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


# func1()
# func2()
# func3()
# func4()
# func5()
# func6()
# func7()
#func8()

