#! /usr/bin/python3

import numpy as np


def func1():
    """
    Простейший пример нейронной сети.
    Простой вес и одно входное значение.
    """
    weight = 0.1
    input = 8.5

    def neural_network(input, weight):
        return input * weight

    predict = neural_network(input, weight)
    print(predict)


def func2():
    """
    Множество входных точек данных с весами для них
    """
    weight = [0.1, 0.2, 0]
    input = [8.5, 0.65, 1.2]

    def neural_network(input, weight):
        """
        Возвращает скалярное произведение векторов.
        Вектора данных на вектор весов.
        """
        predict = 0
        for i in range(len(input)):
            predict += input[i] * weight[i]
        return predict

    predict = neural_network(input, weight)
    print(predict)



def func3():
    """
    Множество входных точек данных с весами для них
    скалярное произведенеи векторов при помощи NumPy
    """

    def neural_network(input, weight):
        return input.dot(weight)

    weight = np.array([0.1, 0.2, 0])
    input = np.array([8.5, 0.65, 1.2])

    predict = neural_network(input, weight)
    print(predict)


def func4():
    """
    Прогнозирование с одним входом и множеством
    выходов, тоесть на основе одних данных, несколько
    разных прогнозов.
    """
    def neural_network(input, weights):
        return ele_mul(input, weights)

    def ele_mul(number, vector):
        output = [0, 0, 0]
        for i in range(len(vector)):
            output[i] = number * vector[i]
        return output


    weights = [0.3, 0.2, 0.9]
    wirec = [0.65, 0.8, 0.8, 0.9]
    input = wirec[0]

    pred = neural_network(input, weights)
    print(pred)


# func1()
# func2()
# func3()
func4()


































