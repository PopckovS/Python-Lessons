Python и ООП 1
---
---

Маг метод `__delattr__(self, item)`
---
Метод вызывается при попытке удалить атрибут объекта, а 
именно при использовании оператора `del` на атрибут объекта.

При этом при попытке удалить атрибут объекта которого не существует,
ошибки не будет.

Пример реализации:

```python
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
    
    # Вывод
    # {'x': 10, 'y': 20}
    # Попытка удалить атрибут =  x
    # {'y': 20}
```

---

Маг метод `__setattr__(self, key, value)`
---

Этот метод используется когда мы пытаемся присвоить объекту не
существующего атрибута, при попытке переопределить значение уже 
существующего атрибута.

Интересно то что этот метод вызывается всегда, даже в момент 
инициализации объекта, при присвоении начальных значений в 
методе `__init__()` он тоже вызываться.

В самом методе `__setattr__` нельзя присваивать значение следующим
синтаксисом:

```python
    self.name = x
```

Это вызовет повторный вызов самой функции `__setattr__` и приведет
к, пере наполнению стека вызовов, и рекурсии.

Присваивать новое значение следует через спец атрибут `self.__dict__`
который содержит в себе все переменные объекта в виде словаря.

Пример реализации:

```python
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
    
    # Вывод
    # попытка присвоить несуще аргумент.
    # name= x  value= 10
    # попытка присвоить несуще аргумент.
    # name= y  value= 20
    # pt.__dict__ =  {'x': 10, 'y': 20}
    # попытка присвоить несуще аргумент.
    # name= name  value= 30
    # pt.__dict__ =  {'x': 10, 'y': 20, 'name': 30}
    # попытка присвоить несуще аргумент.
    # name= name  value= 55
    # pt.__dict__ =  {'x': 10, 'y': 20, 'name': 55}
```

---
  
Маг метод `__getattr__(self, item)`
---

Магический метод, вызывается при попытках получить доступ к 
несуществующему атрибуту класса, в этом методе можно перехватить 
этот процесс и определить что именно возвращать когда пользователь
пытается получить несуществующий атрибут.

А можно определить поведение, что при обращении именно к определенному
параметру, отдавать некоторые данные, или поднять ошибку.

```python
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
```

---

Интересное о вызове методов объектов и классов
---

Когда мы передаем в функцию параметры, первый параметр это `self`
который представляет собой сам объект, этот метод можно вызывать 
у объекта.

Также помимо этого, этот же метод можно вызывать не только у 
объекта, но и как метод класса, только в качестве первого аргумента 
передать объект этого класса, просто обычно Python делает это
автоматически, здесь же мы делаем это в ручную.

```python
    class Point:

        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y

        def setCoords(self, x, y):
            self.x = x
            self.y = y

        def getCoords(self):
            return self.x, self.y
```
        
Есть 2 метода, геттер и сеттер, один кладет данные в объект 
другой берет данные из объекта, оба метода должны вызываться как
методы объекта. Сделаем вызов как от объекта, так и от класса.

Следующие 2 примера одинаковы:

```python
    pt1 = Point()
    pt1.setCoords(10, 20)
    print('pt1 = ', pt1.getCoords())

    pt2 = Point()
    Point.setCoords(pt2, 10, 20)
    print('pt2 = ', Point.getCoords(pt2))
```

---    

Метод `isinstance(obj, class)`
---

Метод позволяет проверить является ли объект экземпляром класса.

```python
    print(isinstance(m, MyClass))

    # Вывод
    # True
```
    
По сути этот метод можно полностью заменить проверкой с условием:

```python
    if type(m) == MyClass:
        print('yes')
    else:
        print('no')

    # Вывод 
    # True
```

---

Метод `getattr(obj, name, default=True)`
---

Метод позволяет получить значение переменной объекта, первый арг
это сам объект, второй это название переменной к которой мы хотим
обратиться, третий параметр дефолтно = True и даст ошибку если 
такого атрибута не существует, если установить в = False то ошибки 
не будет.

```python
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
    
    # Вывод
    # 1
    # 10
    # False
```
        
Также при помощи этого метода можно получать не только значение 
переменной объекта, но и переменной класса.

```python
     print('Point.x = ', getattr(Point, 'x'))
     
     # Вывод 
     # Point.x = 10
```

---

Метод `hasattr(obj, name)`
---

Метод проверяет, существует ли переменная в объекта вообще, и 
возвращает `True / False`

```python
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


    # Вывод
    # Существует ли pt.dinamic_x =  True
    # Существует ли pt.x =  True
    # Существует ли Point.dinamic_x =  False
    # Существует ли Point.x =  True
```

Как можно видеть из примера, функция проверяет не как объект так и 
класс на существование некой переменной, как статической, так и
динамической.

---

Метод `setattr(obj, name, value)`
---

Устанавливает переменную если ее не существовало ранее, и дает новое 
значение старой переменной.

```python
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
```
    
На этом примере можно увидеть что данный метод позволяет не только 
создавать новые переменные объекта так и изменять старые, также 
его можно использовать, чтобы создавать новые статические переменные
или заменять их.

---

Метод `delattr(obj, name)`
---

Удаляет атрибут что объекта что класса.

    delattr(m, 'name')

---

Атрибут класса/объекта/модуля `__dict__`
---

`__dict__` метод возвращает словарь который будет содержать в себе
все переменные объекта или класса.

```python
        class Point():
            x = 10
            y = 20
            def __init__(self):
                self.dinamic_x = 1
                self.dinamic_y = 2

        pt = Point()
        print(pt.__dict__)

        # Вывод
        # {'dinamic_x': 1, 'dinamic_y': 2}
```
        
Используется для получения не только переменных объекта, но и всей
кучи имен зарегистрированных в модуле.

Также можно использовать для получения таблицы символов класса, а не 
только объекта.

```python
        class Point():
            x = 10
            y = 20
            def __init__(self):
                self.dinamic_x = 1
                self.dinamic_y = 2

        print(Point.__dict__)

        # Вывод
        # {
        # '__module__': '__main__',
        # 'x': 10,
        # 'y': 20, 
        # '__init__': <function func3.Point.__init__ at 0x7f76726e09d8>,
        # '__dict__': <attribute '__dict__' of 'Point' objects>,
        # '__weakref__': <attribute '__weakref__' of 'Point' objects>,
        # '__doc__': None
        # }
```

---

Проверка объекта на `True / False`
---

В питоне объект считается False только если он пустой, то есть
если мы делаем проверку в которой нас интересует есть ли в объекте
хоть что-то, то можно сделать просто проверку как на условие `bool`

```python
    my_object = 'Test' # True example
    # my_object = '' # False example
    
    if len(my_object) > 0:
        print('my_object не пуст')
    
    if len(my_object):  # 0 преобразовывается к False
        print('my_object не пуст')
    
    if my_object != '':
        print('my_object не пуст')
    
    if my_object: # пустая строка преобразовывается к False
        print('my_object не пуст')

    # Вывод     
    # my_object не пуст
    # my_object не пуст
    # my_object не пуст
    # my_object не пуст
```