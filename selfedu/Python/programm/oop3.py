#! /usr/bin/python3

def func1():
    """Пример работы классов, передачу аргументов можно было сделать лучше"""

    class PK:
        """Класс представляет базовую комплектацию ПК"""
        def __init__(self, me_size, me_cd, model, cpu):
            self.__me_size = me_size
            self.__me_cd = me_cd
            self.__model = model
            self.__cpu = cpu

        def get_param(self) -> str:
            return f"Память: {self.__me_size}, Размер диска: {self.__me_cd} Модель: {self.__model} CPU: {self.__cpu} "

    class pesonalPK(PK):
        """Клаас для персонального компьютера"""
        def __init__(self, **args):
            self.__monitor = args['monitor']
            self.__mouse = args['mouse']
            self.__keyboard = args['keyboard']
            PK.__init__(self, args['me_size'], args['me_cd'],
                           args['model'], args['cpu'])

        def get_param(self) ->str:
            return PK.get_param(self) + f"Монитор: { self.__monitor} Мышь: {self.__mouse} Клавиатура: {self.__keyboard} "

    class notebookPK(PK):
        """Класс для ноутбука"""
        def __init__(self, **args):
            self.__size = args['size']
            self.__screen = args['screen']
            PK.__init__(self, args['me_size'], args['me_cd'],
                        args['model'], args['cpu'])

        def get_param(self) -> str:
            return PK.get_param(self) + f"Габариты: {self.__size} Экран: {self.__screen} "


    person = pesonalPK(me_size=10, me_cd=20, model='модель1', cpu=300, monitor='монитор', mouse='мышь', keyboard='клава')
    print(person.get_param())

    note = notebookPK(me_size=100, me_cd=200, model='модель2', cpu=600, size=555, screen='Экран Монитора')
    print(note.get_param())


def func2():
    """Пример работы наследования в классах"""
    class Point:
        def __init__(self, x=0, y=0):
            self.__x = x
            self.__y = y

        def __str__(self):
            return f"Точка: ({self.__x}, {self.__x})"

        def check_digital(self) ->bool:
            if isinstance(self.__x, int) or isinstance(self.__x, float) and \
                isinstance(self.__y, int) or isinstance(self.__y, float):
                return True
            return False

        def check_int(self) -> bool:
            if isinstance(self.__x, int) and isinstance(self.__y, int):
                return True
            return False

        def set_coord(self, x=0, y=0):
            if self.check_digital(x, y):
                self.__x = x
                self.__y = y
            else:
                raise ValueError("Координаты должны быть числами")


    class Prop:
        def __init__(self, start:Point, end:Point, color='red', width=1):
            print("Конструктор Prop")
            self._start = start
            self._end = end
            self._color = color
            self._width = width

        def setCoords(self, start, end):
            if start.check_digital() and end.check_digital():
                self._start = start
                self._end = end
            else:
                print("Координаты должны быть числами")

        def drawLine(self):
            """
            Это Абстрактный метод, который должен быть переопределен
            в дочерних классах
            """
            raise NotImplementedError("В дочернем классе должен быть переопред метод drawLine()")


    class Line(Prop):
        """Класс для представления линии"""
        def __init__(self, *args):
            print('Конструктор Line')
            super().__init__(*args)

        def drawLine(self) -> str:
            return f"Рисуем линию: {self._start} {self._end} Цвет: {self._color} Ширина: {self._width}"

        def setCoords(self, start:Point, end:Point=None):
            """Переопределенный от родителя метод, на проверку только int"""
            if end is None:
                if start.check_int():
                    self._start = start
                else:
                    print("Координаты должны быть целочисленными")
            else:
                if start.check_int() and end.check_int():
                    Point.set_coord(self, start, end)
                else:
                    print("Координаты должны быть целочисленными")


    class Rect(Prop):
        """класс для представления квадрата"""
        def __init__(self, *args):
            print('Конструктор Rect')
            super().__init__(*args)

        def drawLine(self) -> str:
            return f"Рисуем квадрат: {self._start} {self._end} Цвет: {self._color} Ширина: {self._width}"


    # Пример работы
    print("Первый:")
    line = Line(Point(10, 10), Point(20, 20))
    print(line.drawLine())

    # line.setCoords(Point(11, 11), Point(22, 22))
    line.setCoords(Point(-11, -11))
    print(line.drawLine())



    print("\n\nВторой:")
    rect = Rect(Point(100, 100), Point(200, 200), 'blue', 10)
    print(rect.drawLine())


def func3():
    """Пример разделения аргументов на части"""
    class One:
        def __init__(self, x, y):
            print('One = ', x, ' ', y)
            self._x = x
            self._y = y

    class Two(One):
        def __init__(self, string, number, *args):
            print('Two = ', args)
            self._string = string
            self._number = number
            super().__init__(*args)

        def show(self):
            return f"x = {self._x} y = {self._y} str = '{self._string}' num = {self._number}"

    my = Two('some string', 55, 10, 20)
    print(my.show())


def func4():
    """
    Пример множественного наследования.
    Без использования super() по этому данный способ не правильный.
    super() - следит за тем чтобы обходить каждый из классов родителей
    только по 1 разу не более, в то время как указаник конкретного
    класса родителя не только лишает мобильности но и может
    привести к рекурсии.
    """
    class Poss:
        def __init__(self, x, y, *args):
        # def __init__(self, x, y):
            self._x = x
            self._y = y
            Style.__init__(self, *args)

    class Style:
        # def __init__(self, name, style, *args):
        def __init__(self, name, style):
            self._name = name
            self._style = style
            # Poss.__init__(self, *args)

    class Point(Poss, Style):
    # class Point(Style, Poss):
        def draw(self):
            return f"x={self._x} y={self._y} name={self._name} style={self._style}"

    pt = Point(10, 20, 'Название', 'Стили')
    print(pt.draw())


def func5():
    """
    Правильная реализация множественного наследования при
    помощи super()
    """

    class Point:
        def __init__(self, x=0, y=0):
            self.__x = x
            self.__y = y

        def __str__(self):
            return f"x = {self.__x} y= {self.__y}"

    class Styles:
        def __init__(self):
            print("Конструктор Styles")
            super().__init__()

    class Pos:
        def __init__(self):
            print("Конструктор Pos")
            super().__init__()

    class Line(Pos, Styles):
    # class Line(Styles, Pos):
        def __init__(self, sp:Point, ep:Point,color="red", width=1,):
            self._sp = sp
            self._ep = ep
            self._color = color
            self._width = width

        def draw(self):
            print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")

    ln = Line(Point(10, 10), Point(100, 100), "green", 5)
    ln.draw()
    print(Line.__mro__)


def func6():

    class Clock:
        __DAY = 86400

        def __init__(self, secs:int):
            if not isinstance(secs, int):
                raise ValueError("Секунды должны быть целым числом")
            self.__secs = secs

        def getFormatTime(self):
            s = self.__secs % 60
            m = (self.__secs // 60) % 60
            h = (self.__secs // 3600) % 24
            return f"{Clock.__getForm(s)}:{Clock.__getForm(m)}:{Clock.__getForm(h)}"

        def __getForm(x):
            return str(x) if x>9 else "0"+str(x)

    cl = Clock(100)
    print(cl.getFormatTime())


def func7():
    """
    Функторы - обьекты классов которые можно использовать
    как функции.
    """

    class StripChars:
        """Класс функтор, удаляет из строки все не нужные символы"""
        def __init__(self, chars):
            self.__chars = chars

        def __call__(self, *args, **kwargs):
            if not isinstance(args[0], str):
                raise ValueError("Аргумент должен быть строкой")
            return args[0].strip(self.__chars)

    sc = StripChars('!')
    print(sc('Hello World!'))


def func8():
    """
    Замыкания, полнение функции с той обл видимости не в
    которой она вызывается а в которой она определена.
    """

    def strip_string(chars):
        def inner_function(string:str):
            return string.strip(chars)
        return inner_function

    x1 = strip_string('!')
    print('Работа с замыканиями 1:', x1("!Hello World!"))

    x2 = strip_string('!')
    print('Работа с замыканиями 2:', x2("!Helorld!"))





# func1()
# func2()
# func3()
# func4()
# func5()
# func6()
# func7()
func8()






