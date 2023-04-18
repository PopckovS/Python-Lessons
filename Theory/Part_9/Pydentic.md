Модуль Pydentic
---

Модуль python для валидации данных, проверки данных на соответствие
модели данных, валидации аргументов функций в соответствии с аннотациями.

Установка

    pip install Pydentic

`validate_arguments` - декоратор для валидации аргументов функции на 
соответствие типам данных описанных в аннотациях этого метода.

```python
from pydantic import validate_arguments

@validate_arguments
def func_1(arg1: str, arg2: int, arg3: list) -> bool:
    pass
    
func_1()
```
