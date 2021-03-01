#! /usr/bin/python3

from custom_functions import trace
import os

def func1(my_object):

    if len(my_object) > 0:
        print('my_object не пуст')
    else:
        print('Пуст')

    if len(my_object):  # 0 преобразовывается к False
        print('my_object не пуст')
    else:
        print('Пуст')

    if my_object != '':
        print('my_object не пуст')
    else:
        print('Пуст')

    if my_object: # пустая строка преобразовывается к False
        print('my_object не пуст')
    else:
        print('Пуст')

def func2():
    """Нахождение подстроки в строке
    Метод find() возвращает декс первого совпадения или -1
    string.find(substring,start,end)
    substring: где искать
    start: индес с которого начинать искать подстроку, по умолч это 0
    end: индекс на котором перестать искать, по умолч это вся строка
    """

    string = "Добро пожаловать!"
    string = "Дбро пожаловать!"
    print(string.find("о"))
    print("Индекс первой буквы 'о':", string.find("о"))

def func3():
    string = 'Hi there'
    # string = 'Hello world'

    # Стандартный поиск
    if string.find('Hi') != -1:
        print('Да эта строка присутствует, ее позиция: %s' %(string.find('Hi')))
    else:
        print('Подстроки не найдено')

    # Другой способ поиска
    if 'Hi' in string:
        print('Да эта строка присутствует')
    else:
        print('Подстроки не найдено')

def func4():
    my_list = ['первый', 'второй', 'третий', 'четвертый']
    print('Вывод списка методом print: ', my_list)
    print('Вывод списка методом join: {list}'.format(list=' , '.join(my_list)))

def func5():
    make_sum = lambda x, y: x + y
    result = make_sum(1, 5)
    print(result)

def func6():
    """Увеличим значение спика в *2 двумя разными способами."""
    my_list = [1, 2, 3, 4, 5]
    print(my_list)

    # Стандартное использование списка, оно не работает как ожидается
    for i in my_list:
        i = i * 2

    # Использование через индексы, работает как надо
    for i in range(len(my_list)):
        my_list[i] *= 2

    # Работа через аноним функцию с использованием map()
    map(lambda x: x*2, my_list)

    print(my_list)

def func7():
    my_tuple1 = (1, 3.14, "Hello World!")
    my_tuple2 = 1, 1, "one", "one", "one", "two", 3

    print(my_tuple2)
    print(my_tuple2.index("one"))
    print(my_tuple2.count("one"))

def func8():
    file_name = 'text-test.txt'

    # Создаем файл и записываем в него три строчки
    f = open(file_name, "w")
    f.write("Первая строчка\nВторая строчка\nТретья строчка")
    f.close()

    # Откррываем файл и считываем из него данные
    f = open(file_name)

    # Выводим все строчки файла
    print(f.read())

    # После вывода курсор находится в конце, вернем его
    # на начальную позицию
    f.seek(0)

    #
    for line in f:
        print('[-] {line}'.format(line=line))

    f.seek(0)
    print(f.readlines())

    if os.path.isfile(file_name):
        print(f'Файл с названием %s существует'%file_name)
        delete_or_not = input("Удалить файл с названием %s ? введите yes если да : "%file_name)
        if type(delete_or_not) is str and delete_or_not == "yes":
            print("Файл '%s' удален."%file_name)
            os.remove(file_name)
        else:
            print("Файл '%s' Не был удален." % file_name)

    if(os.path.isdir('__pycache__')):
        print("Директория существует ")


# func1('Test')
# func1('')

# func2()

# func3()

# func4()

# func5()

# func6()

# func7()

func8()







