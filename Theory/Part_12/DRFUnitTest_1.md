Unit Test for DRF ( Django Rest Framework )
---
---
Для Django и для DRF тесты пишутся по-разному.

Классы для тестирования DRF расширяют классы для тестирования
самого Django.

`DRF APIRequestFactory` расширяет `Django RequestFactory`  
```python
from rest_framework.test import APIRequestFactory
```


```python
from rest_framework.test import APITestCase
```


