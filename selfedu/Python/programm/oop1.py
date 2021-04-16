#! /usr/bin/python3

def func1():
    """
    Работа функции zip - генерация списков из
    столбцовых элементов
    """
    list1 = [7, 2, 3, 10, 12]
    list2 = [-1, 1, -5, 4, 6]

    zip_var = zip(list1, list2)
    gener_list = [x*y for x, y in zip_var]

    print(gener_list)

    # Ответ
    # [-7, 2, -15, 40, 72]


def func2():
    """
    Пример того как переменная обьекта с тем же именем может
    заменить собой статическую переменную класса.
    """
    class Point:
        x = 1
        y = 2

    print(Point.__doc__)
    print(Point.__name__)
    print(dir(Point))

    pt = Point()
    print(f"До изменений pt Point.x={Point.x} Point.y={Point.y}")
    print(f"pt до изменений pt.x={pt.x} pt.y={pt.y}")
    pt.x = 10
    pt.y = 20
    print(f"pt после изменений pt.x={pt.x} pt.y={pt.y}")
    print(f"После изменений pt Point.x={Point.x} Point.y={Point.y}")

    # print(vars(Point))
    # print(vars(pt))


def func3():
    """
    Пример использования метода getattr(obj, name, default=True)
    """
    class Point():
        x = 10
        y = 20

        def __init__(self):
            self.dinamic_x = 1
            self.dinamic_y = 2

    pt = Point()
    print(getattr(pt, 'dinamic_x'))
    print(getattr(pt, 'x'))
    print(getattr(pt, 'unknow', False))

    print('Point.x = ', getattr(Point, 'x'))


def func4():
    """
    Пример работы метода hasattr()
    """
    class Point():
        x = 10
        y = 20

        def __init__(self):
            self.dinamic_x = 1
            self.dinamic_y = 2

    pt = Point()
    print("Существует ли pt.dinamic_x = ", hasattr(pt, 'dinamic_x'))
    print("Существует ли pt.x = ", hasattr(pt, 'x'))

    print("Существует ли Point.dinamic_x = ", hasattr(Point, 'dinamic_x'))
    print("Существует ли Point.x = ", hasattr(Point, 'x'))


def func5():
    """
    Пример работы метода setattr() для установки значения
    новой переменной или переопределения значения старой.
    """
    class MyClass:
        x = 10
        y = 20

        def __init__(self, name, my_list):
            self.name = name
            self.my_list = my_list

    m = MyClass('Название', [1, 2, 3])

    print(m.__dict__)
    setattr(m, 'new_var', 55)
    setattr(m, 'name', 'Новое название')
    print(m.__dict__)

    print(MyClass.__dict__)
    setattr(MyClass, 'new_static_var', 777)
    print(MyClass.__dict__)

    print(isinstance(m, MyClass))
    print(type(m))
    if type(m) == MyClass:
        print('yes')
    else:
        print('no')


def func6():

    class Point3D:

        static_name = "Статическое название"

        def __init__(self, x=0, y=0):
            self.coords = [x, y]

        def setCoords(self, x, y):
            self.coords = [x, y]

        def getCoords(self):
            return tuple(self.coords)

        def getStaticName(self):
            return Point3D.static_name

    pt1 = Point3D(1, 2)
    pt1.setCoords(10, 20)
    x, y = pt1.getCoords()

    print('x = ', x)
    print('y = ', y)

    print("Вызов динамич метода через класс а не обьект")
    print(Point3D.getStaticName(pt1))
    print(Point3D.setCoords(pt1, x=100, y=200))
    print("Координаты = ", Point3D.getCoords(pt1))


def func7():
    """
    2 способа обращения к динамическим методам, один через
    обьект, другой через класс.
    """
    class Point:
        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y

        def setCoords(self, x, y):
            self.x = x
            self.y = y

        def getCoords(self):
            return self.x, self.y

    pt1 = Point()
    pt1.setCoords(10, 20)
    print('pt1 = ', pt1.getCoords())

    pt2 = Point()
    Point.setCoords(pt2, 10, 20)
    print('pt2 = ', Point.getCoords(pt2))


def func8():
    """
    Пример реализации магического класса __getattr__
    """

    class Point:

        def __init__(self, x, y):
            self.__x = x
            self.__y = y

        def __getattr__(self, item):
            print('Запрошен атрибут с названием = ', item)
            if item == 'name':
                return 'Класс для представления точки на плоскости'
            else:
                raise AttributeError

    pt = Point(1, 2)
    print('Делаем обращение к несуществующему элементу')
    print(pt.name)
    print(pt.age)


def func9():
    """
    Пример реализации магического класса __setattr__
    """
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __setattr__(self, key, value):
            print("попытка присвоить несуще аргумент.")
            print('name=', key, ' value=', value)
            self.__dict__[key] = value

    pt = Point(10, 20)
    print('pt.__dict__ = ', pt.__dict__)
    pt.name = 30
    print('pt.__dict__ = ', pt.__dict__)
    pt.name = 55
    print('pt.__dict__ = ', pt.__dict__)


def func10():
    """
    Пример реализации маг метода __delattr__
    """
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









