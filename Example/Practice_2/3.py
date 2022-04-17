
def func1():
    """
    Декорируем класс функцией которая реализует паттерн singleton
    """
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


func1()
