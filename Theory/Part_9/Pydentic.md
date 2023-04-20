Модуль Pydentic
---

Модуль python для валидации данных, проверки данных на соответствие
модели данных, валидации аргументов функций в соответствии с аннотациями.

Установка

    pip install Pydentic

---

`validate_arguments` - декоратор для валидации аргументов функции на 
соответствие типам данных описанных в аннотациях этого метода.

```python
from pydantic import validate_arguments

@validate_arguments
def func_1(arg1: str, arg2: int, arg3: list) -> bool:
    pass
    
func_1()
```

---

С помощью `pydantic`, можно определять модель с описанием структуры данных, 
данные будут валидироваться по описанной для них аннотации, поддерживается
аннотация с помощью модуля `typing`.

```python
from pydantic import BaseModel

class PersonModel(BaseModel):
    name: str
    age: int
```

Для более сложной валидации данных, `pydantic` предоставляет 2 декоратора:

`@validator("название атрибута")` - метод принимает одно значение, значение
конкретного атрибута модели, и проверяет его, если проверка не пройдена то
вызываем исключение `ValueError`.

`@root_validator` - метод принимает все атрибуты модели, что позволяет делать 
сложные проверки с участием всех атрибутов модели.

Пример модели для валидации данных
```python
from typing import List, Union
from pydantic import BaseModel, validator, root_validator
from datetime import datetime

class SearchModel(BaseModel):
    """Validate model for Search parameters in Google Earth Engine."""
    category: Category  # Класс категории
    subjects: List[Subject]  # Класс объекта
    age: int
    start_date: datetime
    end_date: datetime
    married: bool
    name: str

    @validator("age")
    def check_age(cls, age):
        """Проверка возраста"""
        if 18 <= age <= 100:
            raise ValueError("Age error")
        return age

    @root_validator
    def check_date_range(cls, values):
        """Проверка дат"""
        start_date, end_date = values["start_date"], values["end_date"]
        if end_date >= start_date:
            raise ValueError("Data range error")
        return values

    @root_validator
    def check_subjects(cls, values):
        """Проверяем что все субьекты принадлежат одной категории"""
        category, subjects = values["category"], values["subjects"]
        for sub in subjects:
            if sub.category.id != category.id:
                ValueError("Not all subject in onne category")
        return values
```
