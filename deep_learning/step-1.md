## Глубокое обучение
Глубокое обучение - это подмножество машинного обучения,
захватывающая часть области ИИ.

### Типы
Существует 2 типа глубоково обучения:

1) С учителем - производится предсказывание результата, после 
   он сверяется с реальными полученными результатами, и в
   зависимости от разницы, происходит корректировка весов.
   
2) Без учителя - по суть это способ классификации, разделения
   данных на группы, для последующего обучения с учителем.

### Другая классификация
Другой способ клаччификации обучения это:

1) Параметрическое - Количество параметров(весов) строго 
   фиксированное, и обучение происходит в соответствии с этими
   весами.
   
2) Непараметрическое - это сложнее, тут нету параметров, но оно 
   вычисляются в процессе работы,оесть такой тип модели сам себя
   описывает и реалирует на изменение данных, добавляя новые веса.

### Процесс обучения с учителем, параметрический
Этот процесс состоит из 3 этапов:

1) Предсказание
2) Проверка
3) Корректировка

### Первый этап, Предсказание.
Вся суть заключается в весах, веса это своего рода 
чувствительность результата от данных.

Сложно говорить о смыслах и как машинам в зависимости от данных 
определять значение тех или иных данных, для решения этой задачи
мы переводим различные данные в единую систему счисления, а веса 
это параметр который говорит о ценности данных.

В целом все прсото, мы берем входные данные и умножаем их на 
веса, данных может быть много, и их количество зависит от задачи, 
у каждого типа данных есть свои веса, и если данных много то мы 
перемнажаем каждый тип данных на свои веса, а после сумируем их.

Полученный результат называется **взвешанной суммой весов** или 
по **скалярным произведением** скольку эти данные можно 
обьеденить в список из чисел, и для каждых данных будет 
число своего веса,о мы получаем 2 списка чисел.

Будем говорить о них как о векторах, скалярное произведени это 
перемножение значений двух векторов и соединение реззультата, для 
получения одного числа.

Пример простейшей нейронной сети из 3 точек данных и 3 весов:

    weight = [0.1, 0.2, 0]
    input = [8.5, 0.65, 1.2]

    def neural_network(input, weight):
        predict = 0
        for i in range(len(input)):
            predict += input[i] * weight[i]
        return predict

    predict = neural_network(input, weight)
    print(predict)

По сути вся работа в глубоком обучении, это умение работать 
с векторами.

Также веса могут быть и отрицательными, тогда это уменьшит 
вероятность а не увеличит ее.

### Сходство векторов
Скалярное произведение позволяет получить представление о сходстве 
2 векторов:

Представим что имеем 2 вектора:

    a = [1,0,1,0,1]
    b = [0,1,0,1,0]

Если мы получим скалярное произведение этих векторов, то увидим
след картину:

    w_summ(a, b) = 0
    w_summ(b, b) = 2

Если векторы полностью противоположны друг другу по элементам, то 
ответ будет = 0 как в случае с векторами a и b.

Если вектор схож сам с собой как b и b то его значение будет самым 
большим.

Про сути, нейронная сеть оценивает важность входных данных с точки 
зрения сходства этих данных с весами.

Вес может быть большфм но входные данные для него могут быть 
маленькими, и наоборот данные могут быть большими но вес маленьким,
наибоольшую ценность имеет то что дает наибольшее значение ппри 
сложении веса и данных.

### Numpy 
Это библиотека для работы с векторами, скалярное произведение 2
векторов в ней будет выглядеть след образом:

    import numpy as np

    weight = np.array([0.1, 0.2, 0])
    input = np.array([8.5, 0.65, 1.2])

    input.dot(weight)

### Прогнозирование с несколькими выходами
По мимо одного прогназирования на основе нескольких данных, также
можно по данным сделать несколько прогнозов:

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

    // Вывод
    [0.195, 0.13, 0.5850000000000001]

Общая суть проста у нас есть несколько весов, и одна входная точка 
данныых, далее прсото происходит перемножение данных на каждый из 
весов, и получаем список с выходными прогнозами.





















