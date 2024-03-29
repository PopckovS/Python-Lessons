Исключения
---
---

Исключения это классы, что перехватывают и обрабатывают ошибки возникающие
во время выполнения программы, они имеют свою собственную структуру 
наследования.

Иерархия пирамиды исключений начинается с класса `BaseException` него идут:

1) `Exception` - класс для почти всех исключений, если хотим создать 
свой класс исключений то наследуемся от него.


2) `GeneratorExit`


3) `SystemExit` - Вызывается когда вызываем метод sys.exit()


4) `KeyboardInterrupt` - Завершение программы комбинацией Ctrl+C

---

**Различные исключения:**

`AssertionError` - Исключения, что вызываются при помощи оператора
`assert`.

`ImportError` - Ошибка импортирования модуля, когда модуля не 
существует.

`NameError` - Ошибка имени, имя переменной функции или класса не 
найдено.

`AttributeError` - Если обращаемся к атрибуту которого нет.

`LookupError` - Базовый класс для исключений, что связаны с обращением к
не тому элементу структуры: 

`KeyError` - ошибка ключа 

`IndexError` - ошибка индекса

`ValueError` - Используется когда другие более информативные исключения
не применимы

`TypeError` - Ошибка типа, если делаем операцию со значениями разных
типов

---

Исключение
---
Помимо обычного автоматического перехвата исключений в блоке `try`
мы также можем и сами вызывать исключения по своему желанию. 
Сделать это можно 2 способами:

1) Создать свой собственный класс и наследоваться от общего класса 
исключений, в методе `__init__()` вызвать конструктор родителя.


2) Можно при помощи оператора `raise` вызвать нужное нам исключение
из списка стандартных исключений и перехватить его в блоке `except`

Существует стандартный набор исключений, из которого можно выбрать
требуемое и поднимать его при необходимости. К примеру таким образом.

    raise ValueError("Несоответствующее значение")

    raise TypeError('Аргумент должен быть строкой.')

---

Стек вызовов исключений 
---
Как можем помнить есть такой алгоритм как `стек` реализующий принцип
"первый пришел последний, ушел" и вот тут то как раз исключения и
проявляют всю свою силу, отличии от проверок `if`. Да конечно можно
писать программу проверяя все пи помощи `if` но исключения позволяют
перехватить ошибку на какой бы глубине стека вызовов она не находилась.

Если исключение произошло, то оно будет путешествовать со своего 
уровня, на самый верхний. Исключение можно ловить на любом уровне,
независимо от того, где оно произошло. Главное, чтобы ловушка была
на уровне таком же или выше.

---

Свои исключения
---
При написании собственных модулей, хорошим тоном является создание
своих собственных исключений, специфических именно для нашего модуля,
для этого наследуемся от класса `Exception`.

---

Перехват исключений. Модуль `traceback`
---
Когда исключение перехвачено, можем вызвать его параметры, исключение
имеет 2 главных параметра, `e.args` и специальный объект
`e.__traceback__` :

```python
    import traceback

    try:
        1 + '42'
    except Exception as e:
        print('e.args: ', e.args)
        print('e.__traceback__: ', e.__traceback__)
        traceback.print_tb(e.__traceback__)
```

`traceback` - модуль предоставляет методы для форматирования и вывода
на печать трассировок стека программ `Python`, этот модуль хорошо
подходит для удобного вывода на экран стеков вызова.

`traceback.print_tb()` - Метод модуля для вывода на экран стека
вызовов.

---

Блок `finally`
---

`finally` - блок, что завершает работу `try except` и исполняется в
любом случае, его хорошо использовать для чистки от неосвобожденных
ресурсов, примеру для закрытия открытых дескрипторов файлов, однако
в таком случае эту очистку требуется делать в ручную, в то время как
использование механизма with, позволяет автоматически очищать
неосвобожденные ресурсы, такие как дескриптор файла.
---

```python
    try:
        file = open('file.txt', 'w+')
    except КакоенибИсключение:
        ...
    finally:
        file.close()
```

---
Свои собственные исключения
---

В процессе работы мы можем не ограничиваться только теми исключениями
которые нам поставляет `python` из коробки, по скольку все исключения это
классы, то мы можем их расширять, и создавать свои собственные исключения.

В данном примере, мы получим исключения либо когда число слишком маленькое
либо когда оно слишком велико. 
```python
import random

class MyBaseError(Exception):
    pass

class ValueErrorBig(Exception):
    pass

class ValueErrorSmall(Exception):
    pass

while True:
    _num = random.randint(1, 10)
    print('_num = ', _num)
    try:
        if _num > 7:
            raise ValueErrorBig
        elif _num < 3:
            raise ValueErrorSmall
    except ValueErrorSmall:
        print('ValueErrorSmall')
        break
    except ValueErrorBig:
        print('ValueErrorBig')
        break
```

---
Пример кастомизации класса исключений, метод `__str__` используется для вывода
исключения.

```python
class MyException(Exception):
    def __init__(self, value, message="Сообщение об ошибке"):
        """Переопределяем родительский метод, добавляем свои данные"""
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        """Выводит само сообщение об ошибке"""
        return "{} -> {}".format(self.value, self.message)

raise MyException(value=500)
```

