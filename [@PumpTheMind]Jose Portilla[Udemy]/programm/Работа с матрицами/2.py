#! /usr/bin/python3

from random import randint
import numpy
import sys

"""Имеется матрица, где больше нечетных элементов над или под диагональю.
Используем модуль NumPy "sudo pip3 install numpy"
"""

class Matrix():

    def __init__(self, column=5, row=5, min=1, max=10):
        """Инициализация полей класса с проверкой на правильность ввода """
        # Словарь с ошибками
        self.errors = {}
        # Количество строк и Колонок
        self.column = self.checkColumnRow('Колонка', column)
        self.row = self.checkColumnRow('Строка', row)
        # Min и Max диапозон значений
        self.min = self.checkMaxMin(min)
        self.max = self.checkMaxMin(max)
        # Списки с матрицей, диагональю
        self.diagonal = []
        self.matrix = []
        # Списки с колич нечет элементов над и под диагнональю
        self.over = []
        self.under = []

        # Если есть ошибки то мы их выводим и останавливаем работу
        if len(self.errors) > 0:
            self.showErrors()

    def showErrors(self):
        """если есть ошибки то они будут показаны а скрипт завершен"""
        for key, val in self.errors.items():
            print('Ошибка {key} : {val}'.format(key=key, val=val))
        sys.exit()

    def checkColumnRow(self, name, val):
        """Проверка правильности ввода колонок и строк"""
        if type(val) is int:
            if val > 2:
                return val
            else:
                self.errors['ErrorValue'] = '{n} должно быть больше чем 2'.format(n=name)
        else:
            self.errors['ErrorType'] = 'Тип должен быть int'

    def checkMaxMin(self, val):
        """Проверка правильности ввода min max диапозона чисел"""
        if type(val) is int:
            return val
        else:
            self.errors['ErrorType'] = 'Тип должен быть int'

    def generateMatrix(self):
        """Если нету ошибок генерирует матрицу"""
        if len(self.errors) > 0:
            self.showErrors()
        else:
            self.matrix = numpy.array([
                    [randint(self.min, self.max) for i in range(self.column)] for j in range(self.row)
                ])
            self.countDiagonal()
            self.countResult()

    def countDiagonal(self):
        """Метод посчитывает в Матрице элементы ее диагонали"""
        row = 0
        column = 0
        # for elem in self.matrix:
        while row < self.row and column < self.column:
            self.diagonal.append(self.matrix[row][column])
            row += 1
            column += 1

    def countResult(self):
        """Метод высчитывает количество нечетных элементов над и под диагональю"""
        # print('Вывод всех эдементов матрицы :')
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                # Над диагональю
                if j > i:
                    if (self.matrix[i][j] % 2) != 0:
                        self.over.append(self.matrix[i][j])
                # Под диагональю
                elif j < i:
                    if (self.matrix[i][j] % 2) != 0:
                        self.under.append(self.matrix[i][j])

    def showResult(self):
        """Показывает нечет.элементы над/под диагональю"""
        print({'Над диагональю': self.over, 'Под диагональю':self.under})
        over = len(self.over)
        under = len(self.under)
        if(over == under):
            print('Над {over} == {u} Под'.format(over=over, under=under))
        elif over > under:
            print('Над {over} больше чем {under} под'.format(over=over, under=under))
        else:
            print('Под {under} больше чем над {over}'.format(over=over, under=under))

    def getMatrix(self):
        """Возвращает матрицу"""
        return self.matrix

    def showMatrix(self):
        """Показывает матрицу"""
        print('Матрица :\n {matrix}'.format(matrix=self.getMatrix()))

    def getDiagonal(self):
        """Получает элементы диагонали"""
        return self.diagonal

    def showDiagonal(self):
        """Показывает диагональ"""
        print('Вывод элементов диагонали : {diagonal}'.format(diagonal=self.getDiagonal()))


mt = Matrix(column=5, row=5, min=1, max=10)
mt.generateMatrix()
mt.showMatrix()
mt.showDiagonal()
mt.showResult()
