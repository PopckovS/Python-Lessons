#! /usr/bin/python3

from custom_functions import trace
from random import randint
import numpy
import sys

"""Имеется матрица, где больше нечетных элементов над или под диагональю.
Используем модуль NumPy "sudo pip3 install numpy"
"""

class Matrix():

    def __init__(self, column=5, row=5, min=1, max=10):
        self.errors = {}
        self.column = self.checkColumnRow('Колонка', column)
        self.row = self.checkColumnRow('Строка', row)
        self.min = self.checkMaxMin(min)
        self.max = self.checkMaxMin(max)
        self.diagonal = []
        self.matrix = None
        self.over = []
        self.under = []
        if len(self.errors) > 0:
            self.showErrors()

    def showErrors(self):
        for key, val in self.errors.items():
            print('Ошибка {key} : {val}'.format(key=key, val=val))
        sys.exit()

    def checkColumnRow(self, name, val):
        if type(val) is int:
            if val > 2:
                return val
            else:
                self.errors['ErrorValue'] = '{n} должно быть больше чем 2'.format(n=name)
        else:
            self.errors['ErrorType'] = 'Тип должен быть int'

    def checkMaxMin(self, val):
        if type(val) is int:
            return val
        else:
            self.errors['ErrorType'] = 'Тип должен быть int'

    def showMatrix(self):
        print(self.matrix)

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
        """Метод возвращает из Матрицы элементы ее диагонали"""
        row = 0
        column = 0
        # for elem in self.matrix:
        while row < self.row and column < self.column:
            self.diagonal.append(self.matrix[row][column])
            row += 1
            column += 1


    def showDiagonal(self):
        print(self.diagonal)

    def countResult(self):
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
        print({'Над диагональю': self.over, 'Под диагональю':self.under})
        o = len(self.over)
        u = len(self.under)
        if(o==u):
            print('Над {o} == {u} Под'.format(o=o, u=u))
        elif o>u:
            print('Над {o} больше чем {u} под'.format(o=o, u=u))
        else:
            print('Под {u} больше чем над {o}'.format(o=o, u=u))


mt = Matrix(column=5, row=5, min=1, max=10)
mt.generateMatrix()
mt.showMatrix()
mt.showDiagonal()
mt.showResult()
