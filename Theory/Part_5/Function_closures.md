Замыкания
---
Замыкания, полнение функции с той обл видимости не в которой она вызывается
а в которой она определена.

Создаем функцию `strip_string(chars)` которая принимает строчку, и в нутри 
функции определяем еще одну функцию `inner_function(string)` которая тоже 
принимает строчку, из функции верх уровня мы возвращаем функцию нижнего 
уровня, тоетсь ссылку на нее:

```python
    def strip_string(chars):
        def inner_function(string:str):
            return string.strip(chars)
        return inner_function

    x1 = strip_string('!')
    print('Работа с замыканиями 1:', x1("!Hello World!"))


    x2 = strip_string('!')
    print('Работа с замыканиями 2:', x2("!Helorld!"))

    # Вывод
    # Работа с замыканиями 1: Hello World
    # Работа с замыканиями 2: Helorld
```

В дальнейшем каждый раз вызывая ее мы будем получать ссфлку на функцию 
нижнего уровня, и вызывая ее в работу она будет исполняться в контексте
тех данных что были переданы в функцию верхнего уровня.

И каждый из экземпляров будет работать в своем контексте.