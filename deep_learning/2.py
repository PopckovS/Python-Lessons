#! /usr/bin/python3

import numpy as np

"""
Сравение - Второй этап работы нейронной сети.
"""

def func1():
    """Вычисляем среднеквадратичную ошибку"""
    know_weight = 0.5 # вес
    input = 0.5 # значение

    goal_pred = 0.8 #

    # умножаем значение на вес
    pred = input * know_weight

    # Делаем ошибку положительным числом
    # умножая на саму себя
    error = (pred - goal_pred)**2

    print(error)

def func2():
    """
    Пример изменения веса методом холодно/горячо
    Когда результат не совпадает с прогнозом, мы меняем
    веса до тех пор пока ошибка не будет уменьшена.
    """
    def neural_network(input, weight):
        prediction = input * weight
        return prediction

    number_of_toes = [8.5]
    win_or_lose_binary = [1]

    input = number_of_toes[0]
    true = win_or_lose_binary[0]

    weight = 0.1 # вес
    lr = 0.01 # значение на которое изменяем вес

    # Без изменения веса
    # pred = neural_network(input, weight)

    # С изменением веса
    pred = neural_network(input, weight + lr)

    error = (pred - true) ** 2

    print("Чистая ошибка = ", error)


def func3():
    """
    Пример реализации метода холодно/горячо.
    Это более правильный способ работы, вес будет меняться
    до тех пор пока ошибка будет сведена почти к нулю.
    используем квадратичный метод
    """
    weight = 0.5
    input = 0.5
    goal_prediction = 0.8

    # Шаг изменения веса в каждой итерации
    step_amount = 0.001

    for iteration in range(1101):

        # Получаем прогноз и его ошибку
        prediction = input * weight
        error = (prediction - goal_prediction) ** 2

        print("Error:" + str(error) + " Prediction:" + str(prediction))

        # Расчет прогноза с повышением веса
        up_prediction = input * (weight + step_amount)
        up_error = (goal_prediction - up_prediction) ** 2

        # Расчет прогноза с понижением веса
        down_prediction = input * (weight - step_amount)
        down_error = (goal_prediction - down_prediction) ** 2

        # Если понижение веса дало меньшую ошибку чем его подьем
        # то понимжаем вес еще больше, и наоборот.
        if (down_error < up_error):
            weight = weight - step_amount
        elif (down_error > up_error):
            weight = weight + step_amount

        # В результате видим как прогноз увеличивается от 0.25 до
        # желаемых 0.8 в то время как ошибка уменьшается.
        # Error: 0.30250000000000005 Prediction:0.25
        # Error: 0.05904900000000297 Prediction:0.5569999999999939
        # Error: 1.0799505792475652e-27 Prediction:0.7999999999999672


def func4():
    """
    Другой способ метода холод/горячо
    Измеряется ошибка,пределяется направление и величина
    изменения на которую надо изменить вес.
    Используем метод градиентного спуска для получения отклонения.
    """
    weight = 0.5
    goal_pred = 0.8
    input = 0.5

    for iteration in range(20):
        # Делаем прогноз
        pred = input * weight

        # Квадратичный метод получения ошибки
        error = (pred - goal_pred) ** 2

        # Методом градиентного спуска получаем и направление
        # отклонения и его величину
        direction_and_amount = (pred - goal_pred) * input

        # Изменяем вес с помощью градиентного спуска
        weight = weight - direction_and_amount

        print("Error:" + str(error) + " Prediction:" + str(pred))

def func5():
    """Повтронение функции func4"""
    weight = 0.5
    goal_pred = 0.8
    input = 0.5

    print(f"вес = {weight} \n результат = {goal_pred} \n вход = {input}")
    print('=' * 20)
    print('=' * 20)

    for iteration in range(20):
        pred = input * weight
        print(f"Прогноз: {input} * {weight} = {pred}")

        error = (pred - goal_pred) ** 2
        print(f"Квадратичный метод :  {error}")

        direction_and_amount = (pred - goal_pred) * input
        print(f"Градиентный спуск: ({pred} - {goal_pred}) * {input} = {direction_and_amount}")

        loc = weight - direction_and_amount
        print(f"Изменяем веса:  {weight} - {direction_and_amount} = {loc}")
        weight = weight - direction_and_amount

        print("Error:" + str(error) + " Prediction:" + str(pred))
        print('='*20)





# func1()
# func2()
# func3()
# func4()
func5()








