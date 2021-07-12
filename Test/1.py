#! /usr/bin/python3

def func_1():
    print('5 + 3 = ', 5 + 3)

    print('20 - 5 = ', 20 - 5)

    print('5 * 5 = ', 5 * 5)

    print('10 / 5 = ', 10 / 5)

    print('5 / 3 = ', 5 / 3)


def func_2():
    print('2 ** 2 = ', 2**2)
    print('2 ** 3 = ', 2**3)

    print('2 // 3 = ', 2//3)
    print('3 // 3 = ', 3//3)
    print('4 // 3 = ', 4//3)
    print('4 / 3 = ', 4/3)


def func_3():
    print('5 % 3 = ', 5%3)
    print('10 % 3 = ', 10%3)
    print('10 % 3.3 = ', 10%3.3)


def func_4():
    a = 10
    print('a = ', a)

    a += 5
    print('10 + 5 = ', a)

    a -= 3
    print('15 - 3 = ', a)

    a /= 3
    print('12 / 3 = ', a)

    a *= 3
    print('4 * 3 = ', a)

    a //= 6
    print('12 / 6 = ', a)

    a **= 4
    print('2 ** 4 = 2 * 2 * 2 * 2 = ', a)

    a %= 3
    print('16 % 3 = ', a)


def func_5():
    print('4 < 5 = ', 4 < 5)
    print('10 > 5 = ', 10 > 5)
    print('7 <= 7 = ', 7 <= 7)
    print('0 >= 0 = ', 0 >= 0)
    print('3 == 3 = ', 3 == 3)
    print('3 == 3.0 = ', 3 == 3.0)

    print('1 == True = ', 1 == True)
    print('7 == True = ', 7 == True)
    print('0 == False = ', 0 == False)

    print('1 != 10 = ', 1 != 10)


def func_6():

    if 7 > 1 and 5 > 3:
        print('ДА')
    else:
        print('НЕТ')

    a = 7 > 5 and 2 > 1
    print(a)

    a = 7 > 7 or 2 > -1
    print(a)

    if not(not(1)):
        print('да')
    else:
        print('нет')


def func_7():

    if 5 == 5:
        print('5 == 5 = ', True)

    if 5 is 5:
        print('5 is 5 = ', True)

    if 5.0 == 5:
        print('5.0 == 5 = ', True)

    if 1 == True:
        print('1 == True = ', True)

    if 1 is not True:
        print('1 is True = ', True)
    else:
        print('1 is True = ', False)


def func_8():
    list_str = ['ferret', 'cat', 'dog']
    print('list_str = ', list_str)
    print('"fox" in list_str = ', 'fox' in list_str)
    print('"dog" in list_str = ', 'dog' in list_str)

    print('me' in 'disappointment')


def func_9():
    score = int(input("Введите вашу оценку: "))

    if score >= 90:
        print("Отлично! Ваша оценка А")
    elif score >= 80:
        print("Здорово! Ваша оценка - B")
    elif score >= 70:
        print("Хорошо! Ваша оценка - C")
    elif score >= 60:
        print("Ваша оценка - D. Стоит повторить материал.")
    else:
        print("Вы не сдали экзамен")


def func_10():
    var = 500
    result = True if var >= 100 else False
    print(f'var = {var} result = {result}')

    x, y = 25, 50
    big = x if x > y else y
    print(big)


def func_10():


# func_1()
# func_2()
# func_3()
# func_4()
# func_5()
# func_6()
# func_7()
# func_8()
# func_9()
func_10()

