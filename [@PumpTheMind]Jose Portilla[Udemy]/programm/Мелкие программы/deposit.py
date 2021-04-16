#! /usr/bin/python3

# Функция для удобного вывода содержимого
from custom_functions import trace
import os
import sys

class Account:
    """Банковский акаунт."""
    # TODO проверка на тип каждый отдельно,роверить этот вопрос.

    def __init__(self, name, balance):
        """Проверка имени на строку и депозита на положительное число."""
        try:
            if (type(name) is str) and ((type(balance) is int) or (type(balance) is float))\
                    and balance > 0:
                self.name = name
                self.balance = balance
            else:
                raise ValueError("Имя должно быть строкой, сумма числом.")
        except ValueError:
            raise

    def __str__(self):
        return self.show_info()

    def __repr__(self):
        return self.show_info()

    def show_info(self):
        """Показывает информацию об акаунте клиента."""
        return "Account owner: {name}\nAccount balance: {balance}". \
            format(name=self.name, balance=self.balance)

    def deposit(self, balance):
        """Добавление дегнег на акаунт."""
        if type(balance) is float or type(balance) is int:
            if balance > 0:
                self.balance += balance
            else:
                print("Сумма должна быть пожительным числом.")
        else:
            print("Сумма должна быть числом.")

    def withdraw(self, money):
        """Вывод денег с акаунта"""
        if type(money) is float or type(money) is int and 0 < money <= self.balance:
            self.balance -= money
        else:
            print("Сумма для вывода должна быть положительным числом и не превышать депозит.")


account_one = Account("John", 100)
account_two = Account("Willy", 200)

account_one.deposit(25)
account_two.withdraw(55)

print(account_one)
print(repr(account_two))





