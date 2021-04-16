#! /usr/bin/python3

def func1():
    """
    Что можно использовать в качестве ключей словаря:
    строки, числа, кортежи что содержат только неизменяемые
    типы данных
    """
    ml = {"one": 10, "two": 20, 3: 30, (1, 3): 40}

    print(ml)
    print("ml['one'] = ", ml['one'])
    print("ml[3] = ", ml[3])
    print("ml[(1, 3)] = ", ml[(1, 3)])


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
    """
    Вернуть суммму из чисел пришедшей строки.
    """
    def check_pluss_number(number: int) -> int:
        try:
            if isinstance(number, int) and number > 0:
                result = 0
                for elem in str(number):
                    result += int(elem)
                return result
            else:
                raise ValueError('Аргумент должен быть пожительным числом')
        except ValueError:
            raise

    var = 123
    # var = '123'
    # var = -123

    print(check_pluss_number(var))


def func4():
    """
    Получаем число и возвращаем максимальное число которое
    можно сделать из полученного количества символов.
    """
    def max_num_creator(str_number: int) -> str:
        max_item = '9'
        result = ''
        for i in range(str_number):
            result += max_item
        return result

    number = 5
    print(f'Для {number} = ', max_num_creator(number))


def func5():
    """
    Примере List comprehensions для генерации списков
    и не только списков
    """
    import random
    x = random.choice([1, 2, 3])
    print('Рандомно выбранное число: ', x)

    list1 = [elem for elem in range(1, 25, 2)]
    print(f'Тип: {type(list1)}  Содержимое: {list1}')

    tuple1 = (elem for elem in range(1, 11))
    tuple1 = tuple(tuple1)
    print(f'Тип: {type(tuple1)}  Содержимое: {tuple1}')

    set1 = {elem for elem in range(1, 11)}
    print(f'Тип: {type(set1)}  Содержимое: {set1}')

    dict1 = {elem: elem for elem in range(1, 11)}
    print(f'Тип: {type(dict1)}  Содержимое: {dict1}')


def func6():
    """
    Допуск к приватному атрибуту и методу обьекта
    """
    class Point:
        def __init__(self, one, two):
            self._list = one
            self.__private = two

        def my_public_method(self):
            print('Публичный методв')

        def __my_private_method(self):
            print('Приватный методв')

    pt = Point([10, 20, 30], "Приватная переменная")

    Point.my_public_method(pt)
    Point._Point__my_private_method(pt)

    print(pt.__dict__)
    print('='*20)
    print(Point.__dict__)


def func7():
    """
    Спец метод __getitem__ отрабатывает когда к
    обьекту обращаются как к элементу списка
    """
    from string import ascii_letters

    class MyContainer(object):

        def __getitem__(self, key):
            print('key = ', key)
            return ascii_letters[key]

    my_container = MyContainer()

    print(my_container[0])  # a
    print(my_container[16])  # q
    print(my_container[:])  # вывод всего алфавита


def func8():
    """
    Генераторы списков, и просто генераторы то разные вещи
    """
    # Это генератор списка
    a = [x**2 for x in range(10)]

    # А это просто генератор
    b = (x**2 for x in range(10))

    print(f'Генератор списков - Тип: {type(a)}  Значение: {a}')
    print(f'Генератор - Тип: {type(b)}  Значение: {b}')


def func9():
    """
    Итераторы и выражения-генераторы
    """
    # Список
    lt1 = [1, 2, 3]

    # Список превращается в итератор
    it = iter(lt1)
    print(it)

    # next() Функция что перебирает итерируемый обьект
    # очередно по его элементам, и только один раз
    print(next(it))
    print(next(it))
    print(next(it))
    # Дойдя до конца вернутся в начало невозможно

    print('Генератор')
    # Выражение-генератор, далее по нему можно проходится
    # и без функции next() просто вызывая этот элемент
    lt2 = (element for element in range(1000))

    # Первый проход выведет 0-100
    for elem in lt2:
        print(elem)
        if elem >= 100:
            break

    # Втрой проход выведет 100-200
    for elem in lt2:
        print(elem)
        if elem >= 200:
            break


def func10():
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = (i**2 for i in numbers)

    print(type(squared_numbers))

    # Даже проверка есть элемент в генератор приведет
    # к невозможности его повторного вызова
    print(4 in squared_numbers)
    print(4 in squared_numbers)

    # print(list(squared_numbers))
    # print(list(squared_numbers))




# func1()
# func2()
# func3()
# func4()
# func5()
# func6()
# func7()
# func8()
# func9()
func10()




















