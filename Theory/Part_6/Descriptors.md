Дескрипторы и механизм DRY
---
---

`DRY` на помощь для осуществления используя дескрипторы

Обьекты-свойства `property`
---
Когда мы определяем скрытый атрибут для обьекта, чтобы иметь 
к нему доступ мы определяем геттеры и сеттеры, методы через 
которые имеем доступ к скрытому свойству.

Мы можем обращаться к этим методам и вызывать их из вне.

Класс `property` позволяет нам создать обьект который будет
храниться как атрибут класса, этот атрибут будет своего рода
псевдонимом для нужного нам атрибута обьекта.

Далее мы связываем наши методы геттеры и сеттеры и метод для 
удаления с этим псевдонимом, и далее производя вставку или 
извлечение или удаление этого псевдонима, то будут вызываться
методы связанные с ним.

Вот как это работает:

```python
     class Point:

        def __init__(self, x=0, y=0):
            self.__x = x
            self.__y = y

        def __checkValueOnNumber(self, value):
            if isinstance(value, int) or isinstance(value, float):
                return True
            return False

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


        coordX = property(__getCoordX, __setCoordX, __delCoordX)


    pt = Point(10, 20)

    print('Использование X:')
    pt.coordX = 100
    print(pt.coordX)
    del pt.coordX

    # Вывод
    # Использование X:
    # __setCoordX
    # __getCoordX
    # 100
    # __delCoordX
```

Вот что мы имеем, у нас есть 3 метода: сеттер, геттер и для удаления
атрибута обьекта `self.x` 

1) `__getCoordX` - вставка
2) `__setCoordX` - кладет
3) `__delCoordX` - удаляет

Эти методы могут быть как защищенные так и обычные, все они работают 
с одним и тем же атрибутом обьекта, далее мы связываем их через:

    coordX = property(__getCoordX, __setCoordX, __delCoordX)

Первый параметр это геттер, которой сеттер и третий для удаления,
после этого у нас в классе будет создан атрибут `coordX` к которому
и будут привязаны все 3 метода.

И теперь когда мы выполняем операции с этим новым атрибутом, будут 
работать связанные с ним методы.

Данный процесс связывания должен происходить в самом конце класса,
ибо язык интерпретируемый и этих методов не будет существовать на
момент связывания если мы укажем их в конце.

    coordX = property(__getCoordX, __setCoordX, __delCoordX)

---

Обьекты-свойства ё через Декораторы
---
Помимо обычного использования `property` их можно использовать 
через декораторы, след способом:

```python
        @property
        def coordX(self):
            print('Геттер coordX через декоратор')
            return self.__x


        @coordX.setter
        def coordX(self, x):
            if self.__checkValueOnNumber(x):
                self.__x = x
            else:
                raise ValueError('Неправильный формат данных')


        @coordX.deleter
        def coordX(self):
            print('Удаление coordX через декоратор')
            del self.__x
```

Тут все очень интересно, раньше каждому методу мы давали уникальное 
название, теперь все методы будут иметь одно название, и это название
того свойства в котором мы хранили обьект `property` то есть все методы 
будут иметь одно и то же название, в данном случае это `coordX`

Теперь все методы имеют одно название, и далее мы обрамляем их 
декораторами, тут есть ряд правил:

1) Метод, который выполняет роль геттера, является базовым, он 
получает декоратор `@property`

2) Все остальные методы получают декоратор в виде названия того
свойства в котором хранится обьект `property` то есть декоратор
вида `@coordX`

3) Остальные методы получаю декораторы с дополнительным именем.

Геттер - `@property`
Сеттер - `@coordX.setter`
Удаление - `@coordX.deleter`

Таким образом мы получаем все 3 метода.

Вот пример такой программы:

```python
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
```

---

`property` и принцыпы `DRY`
---

Но все эти методы выполняют обработку свойства `coordX` которое
отвечает за атрибут обьекта `self.x` В таком случае если мне
понадобится сделать методы для `self.y` должен ли я определить
еще 3 метода для него ?

Да это можно сделать, но это будет избыточным решением, и нарушением 
принцыпа DRY(не повторять свой код).

Для решения этой задачи существует способ `Дескриптор классов` 

---

Дескрипторы классов
---

Дескрипторы часто используются в `ORM` или фреймворках, но самому
писать их приходится довольно редко.

Если говорить о сути Дескрипторов, то это класс обьект которого 
становится атрибутом в классе что его использует, суть класса
дескриптора в том что при помощи спец магических методов, и реализует
создание, вставку, извлечение или удаление некого значения, которое 
будет содержаться как атрибут в базовом классе.

---

Магические методы Дескрипторов:

- `__set__(self, instance, value)` Вносит значение в атрибут
главного класса.


- `__get__(self, instance, owner)` Возвращает значение атрибута
из главного класса.


- `__delete__(self, obj)` Удаляет его.


- `__set_name__(self, owner, name)` Для присваивания атрибуту
главного класса того же имени, что и у обьекта в котором хранится
экземпляр Дескриптора. `name` - обладает именем атрибута в котором
- хранится дескриптор.

Главная суть этих методов, в том что аргумент `instance` определяется 
питоном автоматически, и содержит в себе экземпляр того класса который
использует дескриптор.

Общая суть дескрипторов заключается в том, чтобы сократить размер
кода, и позволить использовать один набор методов Дескриптора для
множества различных атрибутов.

Главный класс:

```python
       class Point:
           """Класс для точки на плоскости, использует дескриптор"""
           coordX = CoordValue('coordX')
           coordY = CoordValue('coordY')
   
           def __init__(self, x=0, y=0):
               self.coordX = x
               self.coordY = y
```

Как видим в главном классе мы добавляем атрибут 
`coordX = CoordValue('coordX')` в котором будет храниться обьект 
дескриптора, и в него передает название `coordX` именно это название
и будет использовано для создания атрибута обьекта для главного класса.

Класс Дескриптора:

```python
       class CoordValue:
           """Класс Дескриптора."""
           def __init__(self, name):
               self.__name = name
   
           def __get__(self, instance, owner):
               return instance.__dict__[self.__name]
   
           def __set__(self, instance, value):
               instance.__dict__[self.__name] = value
   
           def __delete__(self, instance):
               del instance.__dict__[self.__name]
```

Атрибут `instance` хранит обьект главного класса, по этому через
него мы и создаем новый атрибут обьекта, в методе `__init__`
хранится название по которому будет создаваться атрибут, название
класса дескриптора само по себе не имеет значения.

Начиная с 3.6 версии питона, появился еще один метод `__set_name__()` 
его суть проста, он позволяет автоматизировать создание одноименного 
атрибута.

Новый класс Дескриптора:

```python
    class CoordValue:
        """Класс Дескриптора."""
        def __set_name__(self, owner, name):
            self.__name = name

        def __get__(self, instance, owner):
            return instance.__dict__[self.__name]

        def __set__(self, instance, value):
            instance.__dict__[self.__name] = value

        def __delete__(self, instance):
            del instance.__dict__[self.__name]
```

Метод инициализатор более не нужен, имя вносится при помощи
`__set_name__`

Новый главный класс:

```python
       class Point:
           """Класс для точки на плоскости, использует дескриптор"""
           coordX = CoordValue()
           coordY = CoordValue()
   
           def __init__(self, x=0, y=0):
               self.coordX = x
               self.coordY = y
```

Как видим можно убрать название, оно будет передано автоматически.

Вызовем работу класса:

```python
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
    
    # Вывод
    
    # pt1.coordX =  0 pt1.coordY =  0
    # pt2.coordX =  0 pt2.coordY =  0
    # Вставка данных
    # pt1.coordX =  10 pt1.coordY =  20
    # pt2.coordX =  100 pt2.coordY =  200
    # ==========
    # pt1 =  {'coordX': 10, 'coordY': 20}
    # pt2 =  {'coordX': 100, 'coordY': 200}
    # pt1 =  {'coordY': 20}
    # pt2 =  {'coordY': 200}
```

---

Приоритет Дескпритора
---

Вот что у нас происходит, атрибут в котром хранится дескритор,
называется `coordX` и атрибут обьекта в котором будет храниться
значение созданное дескриптором будет иметь название `coordX`

При обращении к атрибуту:

```python
      pt1 = Point()
      pt1.coordX
```

Питон автоматических отдает приоритет этого вызова дескриптору, а не
атрибуту обьекта, это реализовано автоматически.

---

2 Типа Дескрипторов
---

В питоне существуют Дескрипторы 2 типов:

- Дескриптор данных - реализует все методы работы с данными


- Дескриптор не данных - реализован только один метод `__get__()` и
метод `__set_name__()`

Суть Дескриптора не данных, в том, чтобы возвращать всегда статичное 
значение.

Пример дескриптора не данных:

```python
    class NoDataDescriptor:
        """Класс Дескриптора."""
        def __set_name__(self, owner, name):
            self.__name = name

        def __get__(self, instance, owner):
            return 'Данные которые не меняются'
```
