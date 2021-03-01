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

def func2(list_one, list_two):
    """Найти пересечение списков"""
    if (type(list_one) is not list) or (type(list_two) is not list):
        print('Оба аргумента должны быть списками')
    elif (len(list_one) == 0) or (len(list_two) == 0):
        print('Списки должны быть не пусты')

    list_result = []

    # Поиск пересечений списков
    for elem_one in list_one:
        for elem_two in list_two:
            if elem_one == elem_two:
                list_result.append(elem_one)

    # Вывод получившегося списка
    print(list_result)

def func3(file_name):
    """ Напишите программу, которая принимает имя файла и выводит его расширение.
    Если расширение у файла определить невозможно, выбросите исключение.
    """
    try:
        if type(file_name) is not str:
            raise TypeError('Аргумент должен быть строкой.')
        file_split = file_name.split('.')
        if len(file_split) < 2:
            raise ValueError('Расширения файла не найдено.')
    except ValueError:
        print('У файла должно быть расширение')
    except TypeError:
        print('Аргумент должен быть строкой')
    else:
        print('Расширение файла = "{type}"'.format(type=file_split[-1]))


def func4():
    class Arithmetic():
        """Класс для выполнения арифметических операций"""

        def __init__(self, first_arg, second_arg, operation):
            self.operations = ('+', '-', '*', '/')
            self.tuple_arg = self.CheckArguments(first_arg, second_arg)
            self.operation = self.CheckOperation(operation)
            self.showResult(self.ExecuteOperation(self.tuple_arg, self.operation))

        def showResult(self, result):
            print("{one} {operation} {two} = {result}".format(
                one=self.tuple_arg[0],
                two=self.tuple_arg[1],
                operation=self.operation,
                result=result)
            )

        def ExecuteOperation(self, tuple_arg, operation):
            if operation == '+':
                return tuple_arg[0] + tuple_arg[1]
            elif operation == '-':
                return tuple_arg[0] - tuple_arg[1]
            elif operation == '*':
                return tuple_arg[0] * tuple_arg[1]
            elif operation == '/':
                return tuple_arg[0] / tuple_arg[1]

        def CheckOperation(self, operation):
            """Проверка является ли операция одной из разрешенных"""
            try:
                if operation in self.operations:
                    return operation
                else:
                    raise ValueError('Неизвестная операция')
            except:
                raise

        def CheckArguments(self, first_arg, second_arg):
            """Проверка аргументов на числа или строки которые можно привести к числам."""
            try:
                first_arg = int(first_arg)
                second_arg = int(second_arg)
            except ValueError:
                print('Аргументы должны быть числом или строкой которую можно привести к числу.')
            else:
                return (first_arg, second_arg)

    at = Arithmetic('1', '5', '+')


def func5():
    class Bank():
        """
            Пользователь делает вклад в размере a рублей сроком на years лет
        под 10% годовых (каждый год размер его вклада увеличивается на 10%.
        Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже
        будут проценты).
            Написать класс bank, принимающая аргументы a и years, и возвращающую
        сумму, которая будет на счету пользователя.
        """

        def __init__(self, summ, years):
            self.checkArguments(summ, years)
            self.percent = 1.10
            self.summ = summ
            self.years = years
            self.result = self.summ
            self.GetResultForYears()

        def ShowResult(self):
            print("Сумма {summ} под '{percent}' на {years} лет = {result}".format(
                summ=self.summ,
                percent=self.percent,
                years=self.years,
                result=self.result
            ))

        def GetResultForYears(self):
            for i in range(self.years):
                self.result = self.GetResultForYear(self.result, self.percent)
                print(self.result)
                print(i)

        def GetResultForYear(self, summ, percent):
            return summ * percent

        def checkArguments(self, summ, years):
            try:
                summ = float(summ)
                years = int(years)
            except:
                print("Сумма и год должны быть числами")
                raise

    bank = Bank(1000, 3)
    bank.ShowResult()


# Запуск функций в работу
# func1()

# func2(
#     list_one=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
#     list_two=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
# )

# func3('Название файла.py')
# func3('Название файла')

# func4()

# func5()
