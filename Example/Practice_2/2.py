
def func1():

    class Test1():
        """
        Класс будет реагировать на операторы, сравнивать их
        по количеству символов.
        """

        def __init__(self, name):
            self.name = name

        def __eq__(self, other):
            print(f"self = {len(self.name)}", self)
            print("other = ", other)
            if len(self.name) == other:
                return True
            return False


    t1 = Test1('Names')
    print(t1==5)


def func2():
    class Point():
        """
        Представляет точку на плоскости
        """
        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y


    pt = Point(1, 2)
    print(f"x = {pt.x} y={pt.y}")

    print("Тут мы можем изменить значения переменных из вне")
    pt.x = 100
    pt.y = 'abc'
    print(f"Новые значения x = {pt.x} y={pt.y}")




def func3():
    class Point2():

        def __init__(self, x=0, y=0):
            self.__x = x
            self.__y = y

        def show(self):
            print(f"x = {self.__x} y = {self.__y}")

        def setCoords(self, x, y):
            self.__x = x
            self.__y = y

        def getCoords(self):
            return self.__x, self.__y


    p2 = Point2(10, 20)
    p2.show()

    p2.setCoords(100, 200)
    p2.show()

    x, y = p2.getCoords()
    print(x)
    print(y)

    print(p2.getCoords())
    print(type(p2.getCoords()))

    # Это выведет ошибку, ибо поля приватны
    # print(p2.__x)
    # print(p2.__y)



def func4():

    class Point3():

        def __init__(self):
            pass

        def getCoords(self):
            return  self.__x, self.__y

        def setCoords(self, x, y):
            if (isinstance(x, int) or isinstance(x, float)) and \
                    (isinstance(y, int) or isinstance(y, float)):
                self.__x = x
                self.__y = y
            else:
                print("Координаты должны быть числами")


    pt3 = Point3()

    pt3.setCoords(10, 20)
    print(pt3.getCoords())

    pt3.setCoords("10", 20)
    print(pt3.getCoords())


def func5():

    class Point4():
        static_count = 0

        def __init__(self):
            self.dinamic_x = 10


    def show(x, title=''):
        print('='*10, title, '='*10)
        print('print = ', x)
        print('type = ', type(x))

    po = Point4()
    ps = Point4

    show(po, 'Обьект')
    show(ps, 'Статический')


def func6():
    """
    Можно использовать класс обращаясь к нему на прямую
    """

    class Point():
        static_name = "Статическое название"
        static_number = 10
        def __init__(self, name):
            self.dinamic_name = name

    print(Point)
    print(type(Point))


    # Как видим создание любых переменных с ссылками на класс
    # ведет к одному и томуже классу
    p1 = Point
    p2 = Point

    print(p1.static_name)
    print(p1.static_number)
    p1.static_number = 20

    print(p2.static_name)
    print(p2.static_number)


# func1()
# func2()
# func3()
# func4()
# func5()
func6()
