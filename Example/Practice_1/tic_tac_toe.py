# Функция для удобного вывода содержимого
import os
import sys


class TicTacToe:

    """
    Игра в крестики нолики.

    Класс реализует игру в крестики нолики для 2 игроков,
    каждый из игроков имеет возможность выбирать себе имя и фигуру.
    """

    # Стандартные символы для заполнения ячеек
    CROSS = 'x'
    CIRCLE = 'o'

    # Стандартный символ для заполнения пустотных ячеек
    EMPTY = " "

    def __init__(self):
        # Словарь с тремя списками, это матрица для заполнения крест/нолик
        self.all_list = {
            "A": [TicTacToe.EMPTY]*3,
            "B": [TicTacToe.EMPTY]*3,
            "C": [TicTacToe.EMPTY]*3
        }

        # Данные об игроках, выбранная фигура и значение для заполнения списков
        self.gamer_one = { "figure":TicTacToe.CROSS, "name":"First"}
        self.gamer_two = { "figure":TicTacToe.CIRCLE,"name":"Second"}

        # Текущий игрок
        self.current_player = self.gamer_one

        # Количество сделанных шагов игроками
        self.counter_move = 0

        # Победитель
        self.winner = None

        # Первоначальная анкетат для игроков, вы бор фигуры и имен для игроков
        self.question_choose()


    def question_choose(self):
        """
        Выбор имен для игроков. ли игрок выбрали имя то его больше об этом
        не спрашивать. Первый игрок выбирает фигуру которую будет играть.
        """
        choose_name = False

        while True:
            try:
                if not choose_name:
                    self.gamer_one['name'] = input("Name for first player ? ")
                    self.gamer_two['name'] = input("Name for second player ? ")
                    choose_name = True

                answer = input("Choose figure for gamer '{name}' ('x' or 'o') ? :"
                               .format(name=self.gamer_one['name']))

                if answer == TicTacToe.CROSS:
                    self.gamer_one['figure'] = TicTacToe.CROSS
                    self.gamer_two['figure'] = TicTacToe.CIRCLE
                    break
                elif answer == TicTacToe.CIRCLE:
                    self.gamer_one['figure'] = TicTacToe.CIRCLE
                    self.gamer_two['figure'] = TicTacToe.CROSS
                    break
                else:
                    print("Please, choose 'x' or 'o' for first gamer.")

            except EOFError:
                print("\nExit from game with (Ctrl + D)")
                sys.exit()
            except KeyboardInterrupt:
                print("\nExit from game with (Ctrl + C)")
                sys.exit()

        print("'{name}' gamer pick a '{figure}'".format(
            name=self.gamer_one['name'], figure=self.gamer_one['figure']))
        print("'{name}' gamer pick a '{figure}'".format(
            name=self.gamer_two['name'], figure=self.gamer_two['figure']))


    def start(self):
        """
        Цикл заполнения ячеек таблицы до победы одного из игроков.
        Запуск цикла, показать таблицу пользователю, сдлеать проверку на победителя
        если победителя пока что нету, то дать пользователю заполнить ячейку,
        повторять процесс до тех пор пока не будет найден победитель.
        Проверка на победителя производится только после 5 шагов, только тогда
        кто то может победить.
        """

        print("*** Start game. ***")
        while True:
            self.show_table_char()
            if self.counter_move >= 5:
                if self.check_finish():
                    self.show_winner()
                    break
            self.choose_move()
            self.change_player()
        print("*** End game. ***")


    def show_winner(self):
        """Выводим победителя, если он есть и ничью если его нету."""
        if self.winner is None:
            print("Победителя нету, ничья.")
        else:
            print("Победитель игрок по имени '{winner}' ".format(winner=self.current_player['name']))
        print("Игра закончена на {num} ходу".format(num=self.counter_move))


    def check_finish(self):
        """
        Проверяем заполнена ли выйгрышная комбинация.
        Есть 8 победных комбинаций, все их можно разделить на 3 категории:
        горизонтальные, вертикальные, диагональные.
        """
        if self.check_horizontal_list() or self.check_vertical_list() \
                or self.check_diagonal_list() or self.check_diagonal_revers_list():
            self.change_player()
            self.winner = self.current_player
            return True
        elif self.counter_move == 9:
            self.winner = None
            return True
        return False


    def check_diagonal_revers_list(self):
        """Проверка по обратной диагонали"""
        if self.all_list["A"][2] == self.all_list["B"][1] == self.all_list["C"][0] != TicTacToe.EMPTY:
            return True
        return False


    def check_diagonal_list(self):
        """Проверка по диагонали"""
        if self.all_list["A"][0] == self.all_list["B"][1] == self.all_list["C"][2] != TicTacToe.EMPTY:
            return True
        return False


    def check_vertical_list(self):
        """Проверка по вертикали"""
        for i in range(0, 3):
            if self.all_list["A"][i] == self.all_list["B"][i] == self.all_list["C"][i] != TicTacToe.EMPTY:
                return True
        return False


    def check_horizontal_list(self):
        """Проверка на горизонтальные"""
        for elem in self.all_list.values():
            if elem[0] == elem[1] == elem[2] != TicTacToe.EMPTY:
                return True
        return False


    def choose_move(self):
        """
        Выбор ячеек игроками.
        Принимаем введеннйю ячейку, если введено верно то заполняем нужный
        элемент списка, меняем текущего игрока и даем ему заполнить свою ячейку.
        """
        while True:

            try:
                choose = input("Player '{name}' choose ?".format(name=self.current_player["name"]))

                if (len(choose) == 2) and (choose[0] in self.all_list.keys()) \
                        and ((int(choose[1])-1) in range(0,3)):

                    if self.all_list[choose[0]][int(choose[1]) - 1] == TicTacToe.EMPTY:
                        if self.current_player['figure'] == TicTacToe.CROSS:
                            self.all_list[choose[0]][int(choose[1]) - 1] = TicTacToe.CROSS
                        elif self.current_player['figure'] == TicTacToe.CIRCLE:
                            self.all_list[choose[0]][int(choose[1]) - 1] = TicTacToe.CIRCLE
                        self.counter_move += 1
                        break
                    else:
                        print("Ячейка {choose} уже заполнена, выберите другую.".format(choose=choose))
                else:
                    print("Введите позицию в виде буква и число, к примеру так: B2 или A1 ")

            except EOFError:
                print("\nExit from game with (Ctrl + D)")
                sys.exit()
            except KeyboardInterrupt:
                print("\nExit from game with (Ctrl + C)")
                sys.exit()


    def change_player(self):
        """Переключение текущего игрока"""
        if self.current_player == self.gamer_one:
            self.current_player = self.gamer_two
        else:
            self.current_player = self.gamer_one


    def show_table_char(self):
        """
        Красивый вывод состояния таблицы крестики нолики.
        Вариант со строками.
        """
        print("    1  2  3 ")
        print("A ", " | ".join(self.all_list["A"]))
        print("B ", " | ".join(self.all_list["B"]))
        print("C ", " | ".join(self.all_list["C"]))


# Запуск игры
if __name__ == '__main__':
    game = TicTacToe()
    game.start()
