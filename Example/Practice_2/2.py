
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


# func1()
# func2()
func3()