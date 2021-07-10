Слабые ссылки и модуль weakref
---
---
В отличии от обычных ссылок не припятствуют сборщику мусора удалять обьект,
если на обьект остаются сильные ссылки то он не будет удален, но если 
остается только слабая ссылка то сборщик мусора его сьест.

Главная сфера их применения это работа с кешами и работа с большими словарями
содержащими большие обьекты которые не едолжны долго задерживаться в памяти.

Модуль `weakref` пользуется для работы со слабыми ссылками, 

    weakref.WeakKeyDictionary() 
    weakref.WeakValueDictionary
    finalize() - регистрирует функцию очистки

Для того чтобы обьект поддерживал слабые ссылки ему требуется хранить в себе 
некотрые указатель, это требует памяти, встроенные обьекты не всегда имеют 
такую выделенную память для поддержки слабых ссылок, у каждого обьекта в 
Python ь атрибут `__weakrefoffset__` который говорит сколько памяти у обьекта
выделено для поддержки слабых ссылок.

`__weakrefoffset__` - возвращает число байтов указывающее сколько памяти обьект 
выделяет для поддержки слабых ссылок, если возвращает ноль то значит не 
поддерживает. Собственные классы,пределенные самим пользоваетлем, имеют
стандартные 24 байта.

```python
    class Function:
        pass

    print('Function.__weakrefoffset__ = ', Function.__weakrefoffset__)
    print('type.__weakrefoffset__  =   ', type.__weakrefoffset__)
    print('int.__weakrefoffset__   =   ', int.__weakrefoffset__)
    print('str.__weakrefoffset__   =   ', str.__weakrefoffset__)
    print('bool.__weakrefoffset__  =   ', bool.__weakrefoffset__)
    print('list.__weakrefoffset__  =   ', list.__weakrefoffset__)
    print('dict.__weakrefoffset__  =   ', dict.__weakrefoffset__)
    print('tuple.__weakrefoffset__ =   ', tuple.__weakrefoffset__)
    print('set.__weakrefoffset__   =   ', set.__weakrefoffset__)
    print('float.__weakrefoffset__ =   ', float.__weakrefoffset__)

    # Вывод
    # Function.__weakrefoffset__ =  24
    # type.__weakrefoffset__ =  368
    # int.__weakrefoffset__ =  0
    # str.__weakrefoffset__ =  0
    # bool.__weakrefoffset__ =  0
    # list.__weakrefoffset__ =  0
    # dict.__weakrefoffset__ =  0
    # tuple.__weakrefoffset__ =  0
    # set.__weakrefoffset__ =  192
    # float.__weakrefoffset__ =  0
```
