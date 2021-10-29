Unit Тесты в Django
---
---

Для Django и для DRF тесты пишутся по разному. 

```python
from django.test import TestCase
```



---
Вопросы для разбора:
---

Запуск конкретного теста 
    
    ./manage.py test api_img.tests.test_api

Что такое 
    
    self.client

Destroying test database for alias 'default'...

    Создает оперативную БД в памяти для тестирвоания ?

Запросы идут на 

    http://testserver
