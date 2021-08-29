Модуль `functools`
---
---
1) `@functools.lru_cache` - Пример использования функции мемоизатора, 
также для этой функции будет доступен новый метод `.cache_info()`
   для вывода содержимого кеша.
   
```python
    import functools

    @functools.lru_cache(maxsize=128)
    def function(a, b):
        return a * b

    print(function(2, 5))
    print(function.cache_info())

    print(function(20, 50))
    print(function.cache_info())

    # Вывод
     
    # 10
    # CacheInfo(hits=0, misses=1, maxsize=128, currsize=1)
     
    # 1000
    # CacheInfo(hits=0, misses=2, maxsize=128, currsize=2)
```
---

Декораторы и `functools`, `wraps()`, `update_wrapper()`
---
Интересная вещь! Когда мы создаем декораторы, то у оборачиваемой
функции есть свой набор атрибутов, такие как: `__doc__` `__name__`
`__module__`

Эти атрибуты заменяются на содержимое функции обертки, и это не 
хорошо, это можно изменить присвоив этим атрибутам данные 
оборачиваемой функции, вот пример: 

```python
    def trace(function):
        def inner(*args, **kwargs):
            print('Название:{} Аргументы: {} {}'.format(function.__name__, args, kwargs))
            return function(*args, **kwargs)
        inner.__doc__ = function.__doc__
        inner.__name__ = function.__name__
        inner.__module__ = function.__module__
        return inner

    @trace
    def foo(x):
        """I am do anything useful"""
        return x

    print(foo(48))
    print('foo.__doc__ = ', foo.__doc__)
    print('foo.__name__ = ', foo.__name__)
    print('foo.__module__ = ', foo.__module__)

    # Вывод
    # 48
    # foo.__doc__ =  I am do anything useful
    # foo.__name__ =  foo
    # foo.__module__ =  __main__
```

Таким образом мы сохраняем атрибуты и не выдаем внутреннее содержимое 
нашего декоратора, это поведение можно реализовать самостоятельно 
как это было в примере, но это уже реализовано в `functools`

Для этого есть целых 2 метода:

1) `@functools.wraps(function)` - реализация через декоратор.


2) `functools.update_wrapper(inner, function)` - реализация просто 
   через функцию.
