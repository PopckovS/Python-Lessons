Память в Python `__sizeof__()`  `sys.getsizeof()`
---

У каждого объекта в Python есть метод `__sizeof__()` этот метод
показывает сколько памяти, затрачивает питон в байтах на содержание
этого объекта, но этот метод выводит память самого объекта и только
его самого, помимо этого метода есть метод модуля `sys.getsizeof()`
который выводит и память объекта и дополнительно количество памяти
которе сборщик мусора затрачивает на хранение количества ссылок на
этот объект, и потому получается больше:

```python
    a = [1, 2, 3]
    print('sys.getsizeof(a) = ', sys.getsizeof(a))
    print('a.__sizeof__() = ', a.__sizeof__())

    # Вывод
    # sys.getsizeof(a) =  88
    # a.__sizeof__() =  64
```

Также есть и другая проблема, когда у нас есть некий обьект,
чтобы получить от него обьем занимаемой им памяти, оба метода
дадут лишь обьем памяти самого обьекта, но не обьектов вложенных
в него, таким образом мы получаем не весь обьем памяти, что тратится
на содержание обьектов.

```python
    a = [1, 2, [Point(10, 10), Point(10, 10), Point(10, 10)]]
    b = [1, 2, 3]

    # // Вывод для обоих обьектов
    
    # sys.getsizeof(obj) =  88
    # obj.__sizeof__() =  64

    # sys.getsizeof(obj) =  88
    # obj.__sizeof__() =  64
```

У нас есть 2 списка, применение обоих методов даст один и тот же
результат, память только самого списка, f не его вложенных объектов,
обы получить всю память затрачиваемую на хранение со всей вложенностью,
используется модуль`pympler`

### Модуль `pympler`
Этот модуль используется для дебага и трекинга, его подмодуль `asizeof`
имеет одноименный метод `asizeof()` который возвращает всю память,
что тратится на хранение всех объектов со всей вложенностью. 

```python
    from pympler import asizeof

    a = [1, 2, [Point(10, 10), Point(10, 10), Point(10, 10)]]
    b = [1, 2, 3]

    asizeof.asizeof(a)
    asizeof.asizeof(b)

    # Вывод в байтах
    # a = 184
    # b = 888
```