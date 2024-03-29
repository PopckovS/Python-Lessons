

def func1():
    class Bank():
        """
        Условие:
            Пользователь делает вклад в размере a рублей сроком на years лет
            под 10% годовых (каждый год размер его вклада увеличивается на 10%.
            Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже
            будут проценты).

        Задача:
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


def func2():
    """
    Дан список чисел. Превратите его в список квадратов этих чисел.
    спользуем для этого 3 способа: циклом, лямбда, и генератор списков
    """

    my_list = [1, 2, 3, 4, 5]
    print("Первый способ я списка = ", my_list)
    for i in range(len(my_list)):
        my_list[i] *= my_list[i]
    print(my_list)

    my_list =  [2, 3, 4, 5, 6]
    print("Второй способ я списка = ", my_list)
    sortinf_func = lambda x: x*x
    my_list = list(map(sortinf_func, my_list))
    print(my_list)

    my_list = [3, 4, 5, 6, 7]
    print("Третий способ я списка = ", my_list)
    my_list = [ i*i for i in my_list ]
    print(my_list)


def func3():
    """
    Число-палиндром с обеих сторон (справа налево и слева направо) читается
    одинаково. Самое большое число-палиндром, полученное умножением двух
    двузначных чисел – 9009 = 91 × 99.

    Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
    """
    max_a, max_b = 0, 0

    for i in range(100, 1000):
        for j in range(100, 1000):
            num = str(i * j)
            if num == num[::-1]:
                max_a = i
                max_b = j
                result = num
                print("{i} * {j} = {num}".format(i=i, j=j, num=num))

    print("Наибольшее число путем умножения двух трех знач чисел {i} * {j} = {num}".
          format(i=max_a, j=max_b, num=result))

def check_simple_number(num):
    """
    Проверяет является ли целое число простым.
    :param num: Целое число
    :return: True/False
    """
    if type(num) is not int or num <=0:
        raise ValueError("Параметр должен быть целым положительным числом.")
    else:
        if (num==2 or num==3 or num==5) or (num%2!=0) and (num%3!=0) and (num%5!=0) and (num%7!=0):
            return True
        else:
            return False


def test_check_simple_number():
    """
    Метод прогоняет числа от 0 до 100 через метод check_simple_number
    """
    for num in range(1, 150):
        print("Число {num} = {result}"
              .format(num=num, result=check_simple_number(num))
              )

def is_prime(num):
    """
    Еще одна функция для проверки является ли число простым.
    :param num: Число
    :return: Текст с описанием, является ли число простым
    """
    for n in range(2, num):
        if num % n == 0:
            print("Число {num} не простое".format(num=num))
            break
        else:
            print("Число {num} простое".format(num=num))


# func1()
# func2()
func3()
