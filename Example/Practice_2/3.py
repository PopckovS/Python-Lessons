
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


# func1()
# func2()
func3()
