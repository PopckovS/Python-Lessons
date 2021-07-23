import random


def selection_sort(array, type_sort='asc'):
    """
    Метод реализует сортировку выборкой.
    
    :param array: должен быть списком для сортировки.
    :param type_sort: аргумент что принимает параметры "asc" или "desc"
    и в зависимости от этого сортирует по возрастанию или убыванию.
    :return: None
    """
    print('Array for sorting : ', array)
    counter = 0
    result_aray = []

    # Цикл для определения
    while True:
        # Каждый раз устанавливаем длину списка заново, что бы
        # не выйти за границу списка
        array_len = len(array)
        current, number = array[0], 0

        # Если в начальном списке остался 1 элемент то он автоматически
        # является минимальным, добавляем его и выходим из цикла
        if array_len == 1:
            result_aray.append(array[0])
            break

        # Проходимся по списку и сравниваем наше значение с
        # каждым знач в списке, и определяем большее
        for j in range(array_len):
            counter += 1
            if type_sort == 'asc':
                if current < array[j]:
                    number = j
                    current = array[j]
            elif type_sort == 'desc':
                if current > array[j]:
                    number = j
                    current = array[j]


        # Добавляем элемента в финальный список и
        # удаляем из изначального массива
        result_aray.append(current)
        del array[number]

    print('Результат :')
    print('Количество шагов = ', counter)
    print('Финальный массив = ', result_aray)


random_array = [random.randint(0, 10) for i in range(1, 11)]
selection_sort(random_array, 'asc')
# selection_sort(random_array, 'desc')
