#! /usr/bin/python3

def func1():
    """
    Пример реализации атрибута __slots__ в класса
    """
    class Point:

        STATIC_NAME = 'Статичное название'
        __slots__ = ['x', 'y', '__dict__']

        # Так будет ошибка ибо нельзя включать переменную класса
        # __slots__ = ['x', 'y', '__dict__', STATIC_NAME]

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def setCoords(self, x, y):
            self.x = x
            self.y = y

        def getCoords(self):
            return self.__slots__

    pt = Point(10, 20)

    pt.x = 1
    pt.y = 2
    pt.z = 55

    print(pt.getCoords())
    print(pt.z)


def func2():
    """
    Пример использование обьекта-свойства property с помощью
    которого можно описать методы доступа к атрибутам обьекта.
    """
    class Point:

        def __init__(self, x=0, y=0):
            self.__x = x
            self.__y = y

        def __checkValueOnNumber(self, value):
            if isinstance(value, int) or isinstance(value, float):
                return True
            return False

        # Методы работы с x
        def __getCoordX(self):
            print('__getCoordX')
            return self.__x

        def __setCoordX(self, x):
            print('__setCoordX')
            if self.__checkValueOnNumber(x):
                self.__x = x
            else:
                raise ValueError('Данные должны быть int и float')

        def __delCoordX(self):
            print('__delCoordX')
            del self.__x

        # Методы работы с y
        def __getCoordY(self):
            print('__getCoordY')
            return self.__y

        def __setCoordY(self, y):
            print('__setCoordY')
            if self.__checkValueOnNumber(y):
                self.__x = y
            else:
                raise ValueError('Данные должны быть int и float')

        def __delCoordY(self):
            print('__delCoordY')
            del self.__y

        coordX = property(__getCoordX, __setCoordX, __delCoordX)
        coordY = property(__getCoordY, __setCoordY, __delCoordY)

    pt = Point(10, 20)

    print('Использование X:')
    pt.coordX = 100
    print(pt.coordX)
    del pt.coordX

    print('\nИспользование Y:')
    pt.coordY = 200
    print(pt.coordY)
    del pt.coordY


def func3():
    """
    Второй способ, создания обьекта-свойства property
    при помощи декораторов, данный метод дублирует код
    и нарушает принцып DRY.
    Данный способ неправильный, правильно это определять
    класс Дескриптор, это позволит нне дублировать геттеры
    сеттеры и удаляторы.
    """
    class Point:
        def __init__(self, x, y):
            self.__x = x
            self.__y = y

        # Метод для проверки вносимых значений на число
        def __checkValueOnNumber(self, value):
            if isinstance(value, int) or isinstance(value, float):
                return True
            return False

        # ======= Методы для работы с атрибутом self.x =======
        @property
        def coordX(self):
            print('Геттер coordX через декоратор')
            return self.__x

        @coordX.setter
        def coordX(self, x):
            print('Сеттер coordX через декоратор')
            if self.__checkValueOnNumber(x):
                self.__x = x
            else:
                raise ValueError('Неправильный формат данных')

        @coordX.deleter
        def coordX(self):
            print('Удаление coordX через декоратор')
            del self.__x

        # ======= Методы для работы с атрибутом self.y =======
        @property
        def coordY(self):
            print('Геттер coordY через декоратор')
            return self.__y

        @coordY.setter
        def coordY(self, y):
            print('Сеттер coordY через декоратор')
            if self.__checkValueOnNumber(y):
                self.__y = y
            else:
                raise ValueError('Неправильный формат данных')

        @coordY.deleter
        def coordY(self):
            print('Удаление coordY через декоратор')
            del self.__y

    pt = Point(10, 20)

    print('Использование X:')
    pt.coordX = 100
    print(pt.coordX)
    del pt.coordX


def func4():
    """
    Пример работы  Дескриптора
    """

    class CoordValue:
        """Класс Дескриптора."""
        # def __init__(self, name):
        #     self.__name = name

        def __set_name__(self, owner, name):
            self.__name = name

        def __get__(self, instance, owner):
            return instance.__dict__[self.__name]

        def __set__(self, instance, value):
            instance.__dict__[self.__name] = value

        def __delete__(self, instance):
            del instance.__dict__[self.__name]

    class Point:
        """Класс для точки на плоскости, использует дескриптор"""
        coordX = CoordValue()
        coordY = CoordValue()

        def __init__(self, x=0, y=0):
            self.coordX = x
            self.coordY = y

    pt1 = Point()
    pt2 = Point()

    print('pt1.coordX = ', pt1.coordX, 'pt1.coordY = ', pt1.coordY)
    print('pt2.coordX = ', pt2.coordX, 'pt2.coordY = ', pt2.coordY)

    print('Вставка данных')
    pt1.coordX = 10; pt1.coordY = 20
    pt2.coordX = 100; pt2.coordY = 200

    print('pt1.coordX = ', pt1.coordX, 'pt1.coordY = ', pt1.coordY)
    print('pt2.coordX = ', pt2.coordX, 'pt2.coordY = ', pt2.coordY)

    print('='*10)

    print('pt1 = ', vars(pt1))
    print('pt2 = ', vars(pt2))
    del pt1.coordX
    del pt2.coordX
    print('pt1 = ', vars(pt1))
    print('pt2 = ', vars(pt2))


def func5():
    """
    Пример создания статического метода и его переопределение
    """
    class Point:
        __count = 0

        def __init__(self, x, y):
            Point.__count += 1
            self.x = x
            self.y = y

        @staticmethod
        def getCounter():
            return Point.__count

    pt1 = Point(1, 2)
    pt2 = Point(10, 20)

    def newGetCounter():
        return 55

    pt1.getCounter = newGetCounter

    print(pt1.getCounter())
    print(Point.getCounter())


def func6():
    """
    Паттерн singleton
    """
    pass


def func7():
    """
    Аннотации методов
    """
    class Point:
        def __init__(self, x:int=0, y:int=0):
            self.x = x
            self.y = y

        def setCoord(self, x:int=0, y:int=0):
            self.x = x
            self.y = y

        def getCoord(self) -> tuple:
            return self.x, self.y


    print(issubclass(Point, object))

    pt = Point(10, 20)
    print(pt.setCoord.__annotations__)
    print(pt.getCoord.__annotations__)


def func8():
    """
    Наследование
    """
    class Point:
        """Представление точки на плоскости координат по x и y"""
        def __init__(self, x:int=0, y:int=0):
            self.__x = x
            self.__y = y

        def __str__(self):
            return f"точка ({self.__x}, {self.__y})"


    class Prop:
        """"""
        def __init__(self, start:Point, end:Point, color:str, width:float):
            print("Метод __init__ класса Prop")
            self._start = start
            self._end = end
            self._color = color
            self._width = width


    class Line(Prop):
        def __init__(self, *args):
            print("Метод __init__ класса Line")
            # Вызываем инициализатор род класса, не правильно
            # Point.__init__(self, *args)

            # Правильный способ вызова инициализатора род класса
            super().__init__(*args)

        def drawLine(self):
            print(f"Рисуем линию: " \
                   f"{self._start}, {self._end}, {self._color}, {self._width}")

    class Rectangle(Prop):
        def drawLine(self):
            print(f"Рисуем Квадрат: " \
                   f"{self._start}, {self._end}, {self._color}, {self._width}")


    line = Line(Point(10, 10), Point(20, 20), 'red', 0.5)
    line.drawLine()
    print("Доступ к защищенному атрибуту _start = ", line._start)

    # rect = Rectangle(Point(100, 100), Point(200, 200), 'blue', 1.0)
    # rect.drawLine()


def func9():
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __delattr__(self, item):
            print('Попытка удалить атрибут = ', item)
            del self.__dict__[item]

    pt = Point(10, 20)
    print(pt.__dict__)
    del pt.x
    print(pt.__dict__)


def func10():
    """Синтаксис доступа к защищенному атрибуту обьекта."""

    class Point:
        def __init__(self, x, y, z):
            self.x = x
            self._y = y
            self.__z = z

    pt = Point(10, 20, 30)

    print("Point.__dict__ = ", Point.__dict__)
    print("pt.__dict__ = ", pt.__dict__)
    print("pt._Point__z = ", pt._Point__z)


# func1()
# func2()
# func3()
# func4()
# func5()
# func6()
# func7()
# func8()
# func9()
func10()












