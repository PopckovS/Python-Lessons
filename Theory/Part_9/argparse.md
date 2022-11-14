Модуль argparse
---

Это модуль позволяющий нам работать с аргументами переданными в скрипт python 
через терминал, с его помощью можно сделать программу гибкой, задавая нужное 
программы в зависимости от получаемых параметров.

Пример 
```python
import argparse

# создание нового объекта argparse с описанием
parser = argparse.ArgumentParser(description='Service version #1')

# указываем какие обязательные аргументы может принимать скрипт
parser.add_argument('arg_int', type=int, help='Input dir for videos')
parser.add_argument('arg_str', type=str, help='Output dir for videos')

# получаем аргументы, которые может принимать скрипт
parser_args = parser.parse_args()
print(parser_args)
```

---

```python
import parser

# указываем аргумент с дефолтным значением
parser_arge = parser.add_argument(
                '-m', 
                type=int, 
                default=2,
                help='Provide an integer, default: 2'
            )

# Получаем значение переданного параметра
print(parser_arge.m)
```

