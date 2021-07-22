import csv


def func_1():
    """
    В директории csv-1 есть файл exp-1.csv
    Файл exp-1.csv содержит таблицу вида:

        full_name;    salare;   kpi
      Ivanov Alex;    100000;    5
     Smirnov Alex;    120000;    7
    Andreev Vadim;    110000;    4
      Petrova Ira;     90000;    3
    """

    def reader_to_csv():
        """
        Используя менеджер контекста with
        Получаем из файла csv данные и выводим их терминал.
        """
        with open("csv-1/exp-1.csv", newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')

            for row in reader:
                print(row['full_name'], ' | ', row['salare'], ' | ', row['kpi'])

    def write_to_csv():
        """
        Используя менеджер контекста with
        Записываем данные в csv файл.
        """
        with open("csv-1/exp-1-1.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile,  delimiter=';')

            writer.writerow(["row 1 el 1", "row 1 el 2", "row 1 el 3"])
            writer.writerow(["row 2 el 1", "row 2 el 2", "row 2 el 3"])
            writer.writerow(["row 3 el 1", "row 3 el 2", "row 3 el 3"])

    # Получаем данные и выводим в консоль
    reader_to_csv()
    # Создаем новый файл и записываем в него
    write_to_csv()


def func_2():
    """
    Использование метода csv.reader
    Простейший вывод содержимого файла с использованием with
    """
    # csv_path = "TB/TB_data_dictionary_2021-07-22.csv"
    csv_path = "csv-1/exp-1.csv"

    with open(csv_path, 'r') as file_obj:
        reader = csv.reader(file_obj)
        for row in reader:
            print(" ".join(row))


def func_3():
    """
    Использование метода csv.reader
    Для работы используем csv файл по пути TB/TB_data_dictionary_2021-07-22.csv
    тот файл содержит данные о людях болеющих туберкулезом.
    """
    def csv_reader(file_obj):
        """Читаем данные из csv файла."""
        reader = csv.reader(file_obj)
        for row in reader:
            print(" ".join(row))

    # csv_path = "TB/TB_data_dictionary_2021-07-22.csv"
    csv_path = "csv-1/exp-1.csv"
    with open(csv_path, "r") as f_obj:
        csv_reader(f_obj)


def func_4():

    def csv_dict_reader(file_obj):
        """
        Используя другой метод, csv.DictReader() получим данные из файла.
        Каждая строка в файле представляет из себя словарь,де ключами
        являются названия столбцов,
        """
        reader = csv.DictReader(file_obj, delimiter=',')
        for line in reader:
            print(line["first_name"]), # Вывод первого элемента новой строки
            print(line["last_name"])   # Вывод второго элемента новой строки

    with open("data.csv") as f_obj:
        csv_dict_reader(f_obj)


def func_5():
    """Пишем CSV файл"""

    def csv_writer(data, path):
        """
        Используя метод csv.writer() получим обьект writer и уже
        используя его метод writer.writerow() запишим данные в файл.
        """
        with open(path, "w", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')
            for line in data:
                writer.writerow(line)

    # В результате получим список со списками
    data = ["first_name,last_name,city".split(","),
            "Tyrese,Hirthe,Strackeport".split(","),
            "Jules,Dicki,Lake Nickolasville".split(","),
            "Dedric,Medhurst,Stiedemannberg".split(",")
            ]

    path = "output.csv"
    csv_writer(data, path)


def func_6():
    """
    Используя метод DictWriter создадим список со словарями,
    и запишим его в файл CSV
    """
    def csv_dict_writer(path, fieldnames, data):
        """
        Записываем в CSV файл данные используя DictWriter
        """
        with open(path, "w", newline='') as out_file:
            writer = csv.DictWriter(out_file, delimiter=';', fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)

    # Получим список со словарями
    data = ["first_name,last_name,city".split(","),
            "Tyrese,Hirthe,Strackeport".split(","),
            "Jules,Dicki,Lake Nickolasville".split(","),
            "Dedric,Medhurst,Stiedemannberg".split(",")
            ]

    # Финальный список что будет содержать все словари
    my_list = []
    # Список с первым рядом, в котором названия столбцов
    fieldnames = data[0]
    # Цикл проходится по всем спискам, создавая из них
    # словари и добавляя их к финальному списку
    for values in data[1:]:
        # print(fieldnames, values)
        inner_dict = dict(zip(fieldnames, values))  # Трансформ списка в словарь
        # print('inner_dict = ', inner_dict)
        my_list.append(inner_dict)  # Добавление словаря в финал список

    path = "dict_output.csv"
    csv_dict_writer(path, fieldnames, my_list)


# Раскоментите чтобы выбрать нужный вариант
# func_1()
# func_2()
# func_3()
# func_4()
# func_5()
# func_6()












