Тема: История Python
---
---

Python - прообразом для создания являются 2 языка, это `ABC` 
и `Modula-3`

`ABC` - язык без скобок, с отступами, откуда питон и взял свой 
визуальный стиль. 

`Modula-3` - был первым языком в котором была конструкция 
`try except` так же он был модульным языком, откуда и пошла 
модульность самого питона.

---

Интроспекция - динамичность языков программирования
---

**introspection** - способность объекта во время выполнения получить
информацию о его внутренней структуре.

Для интроспекции есть ряд методов которые помогают узнать информацию
об обьекте, такие методы как: `dir()`, `type()`, `isinstance()`,
`hasattr()`, `id()`

---

Байт код
---

При интерпретированнии создается Байт код, который никак не привязан
к архитектуре, и может выполняться в разных виртуальных машинах,
по дефолту используется интерпретатор `Cpython`, но есть и другие
вирт машины для его исполнения: PyPy(тот же Cpython только с JIT
компиляцией), Jpython(для Java),

Существую 2 несовместимых версии питона, 2 и 3 версии, главная 
причина это переход строк с байтового на Unicod и многие другие
изменения.

Модуль - это специальный класс который организует свое содержимое
в некое подобие объекта, Любой файл с `.py` задает модуль.:

    <module 'os' from '/usr/lib/python3.6/os.py'>
    <class 'module'>

У каждого модуля есть атрибут `__name__` который содержит название
модуля соответствующее названию файла, и не может называться с
цифр, ибо является идентификатором, и импортировать его не
получиться.

---

Все в питоне есть объект какого либо класса:
```python
    a = 54
    print(type(a))
    print(type(type(a)))

    # Вывод
    # <class 'int'>
    # <class 'type'>
```

--- 

РЕР8 - Это соглашение о программировании в питоне, которое содержит
рекомендации для повышения читаемости кода.