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


# func_1()
# func_2()
# func_3()


