Декораторы из функций
---

Декораторы - срабатывают раньше чем сама функция которая ими обернута, 
так что если в декораторе есть вывод чего то в терминал, то оно будет
выведено на экран раньше чем обернутая ими функция.

Функции в питоне это объекты, их можно передавать как аргументы, 
механизм декораторов это передача функции которую мф хотим исполнить 
в другую функцию в качестве аргумента.

Обычный декоратор:

```python
    def Decorator1(func):
        def wrapper(*args):
            func(*args)
        return wrapper

    @Decorator1
    def func1(x, y):
        print(f'func1 x = {x} y = {y}')

    func1(10, 20)

    # Вывод
    # func1 x = 10 y = 20
```

Указывая декоратор `@Decorator1` мы тем самым вызываем в работу 
функцию `Decorator1` эта функция принимает в качестве аргумента 
функцию `func1()` и внутри себя создает еще одну функцию обертку 
`wrapper(*args)` здесь аргументы *args являются теми самыми аргументами
`10, 20` которые получила первоначальная функция, и уже внутри функции 
обертки `wrapper()` мы можем вызвать на исполнения функцию `func1()`

Декоратор с аргументами:

Помимо обычной работы мы можем еще создать 
декоратор который сам по себе принимает аргументы и работает с ними,
для этого требуется сделать еще одну вложенность:

```python
    def Decorator1(input_arg):
        def the_real_decorator(func):
            def wrapper(*args):
                result = func(*args)
                return f'input_arg={input_arg} '+result
            return wrapper
        return the_real_decorator


    @Decorator1(55)
    def func1(x, y):
        # print(f'func1 x = {x} y = {y}')
        return f'func1 x = {x} y = {y}'

    print(func1(10, 20))

    # Вывод
    # input_arg=55 func1 x = 10 y = 20
```

Создадим ужу одну функцию обертку `Decorator1(input_arg):` поверх всех 
тех что уже были, где аргумент `input_arg` и будет нашим аргументом 
декоратора, а далее просто по вложенности возвращаем из функции 
внутреннею функцию.

---

Декоратор из класса без аргументов
---

Для реализации декоратора из класса, этот класс должен быть `callable`
то есть доступен для вызова как функция, что возможно только при
определении в этом классе магического метода `__call__`

Декораторы из классов, делаются по такой же методике, то есть 2 или 3 
функции для обертки, только теперь в качестве оберток будут выступать 
методы класса.

Это делается через методы `__init__() __call__()` метод `__init__()`
принимает функцию, а метод `__call__()` аргументы функции, и 
возвращает результат работы функции.

То есть у нас сразу же создается экземпляр класса нашего декоратора
и за ним этот объект декоратора вызывается как функция.

```python
    class MyDecorator:

        def __init__(self, function):
            self._function = function

        def __call__(self, *args, **kwargs):
            return self._function(*args, **kwargs)

    @MyDecorator
    def function(a, b):
        return a * b

    print(function(2, 5))

    # Вывод
    # 10
```

---

Декоратор из класса с аргументами
---

Методика та же самая только теперь у нас 3 обертки, метод
`__init__(decorator_arg)` принимает аргументы самого декоратора,
метод `__call__(function)` принимает функцию которую мы оборачиваем
декоратором, и в методе `__call__` создаем еще одну обертку котора
и будет принимать аргументы самой функции `wrapper(*args, **kwargs)`
и эу эта непосредственная обертка и выполняет работу с функцией.

```python
    class MyDecorator:
    
        def __init__(self, decorator_arg):
            self._decorator_arg = decorator_arg
            self._function = None
    
        def __call__(self, function):
            self._function = function
    
            def wrapper(*args, **kwargs):
                result = self._function(*args, **kwargs)
                return f'{self._decorator_arg} {result}'
            return wrapper
    
    @MyDecorator('Р е з у л ь т а т : ')
    def function(a, b):
        return a * b
    
    print(function(10, 5))
    
    # Вывод
    # Р е з у л ь т а т :  50
```

---

Декорирование самих классов
---
Сами классы можно декорировать, причем декоратором класса должен
быть декоратор класс, функции декорируем функциями, классы декорируем
классами.

```python
    import functools

    def singleton(cls):
        instance = None

        @functools.wraps(cls)
        def inner(*args, **kwargs):
            nonlocal instance
            if instance is None:
                instance = cls(*args, **kwargs)
            return instance

        return inner

    @singleton
    class Noop:
        """Класс Noop может быть только в одном экземпляре."""

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def show(self):
            return f'self.x = {self.x} self.y = {self.y}'

    noop = Noop(10, 20)
    print('id(Noop) = ', id(Noop))
    print(noop.show())

    print()

    noop = Noop(55, 77)
    print('id(Noop) = ', id(Noop))
    print(noop.show())


    # Вывод
    # id(Noop) =  140718501138080
    # self.x = 10 self.y = 20
 
    # id(Noop) =  140718501138080
    # self.x = 10 self.y = 20
```

То есть один раз создав объект с переданными в него параметрами,
то далее мы будем работать только с этим объектом.
