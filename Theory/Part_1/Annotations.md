Аннотации аргументов методов
---
---
Мы можем в качестве подсказки указывать какого типа должны быть
аргументы передающиеся в `метод/функцию`, также указывать тип возвращаемого
значения, это не налагает каких либо ограничений, передавать можно все что 
угодно, это служит лишь аннотацией для программиста:

```python
    def __init__(self, x:int = 0, y:int = 0) -> str:
        self.x = x
        self.y = y
        return "Обьект создан" 
```

Указание происходит через двоеточие, указание возвращаемого значения 
через стрелку.

Также в случае если метод имеет аннотации у него появляется специальный 
атрибут `__annotations__`

`__annotations__` - это словарь, который содержит в себе список аннотаций.

Пример:
```python
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

    # Вывод
    # True
    # {'x': <class 'int'>, 'y': <class 'int'>}
    # {'return': <class 'tuple'>}
```