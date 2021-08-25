Непосредственное выполнение SQL запроса
---

**Метод №1**

Первый способ, это выполнение полностью сырых запросов, тут
выполняется SQL запрос полностью минуя уровень модели, сделать
это можно при помощи прямого соединения с БД, импортируем :

```python
from django.db import connection
```

По скольку данный метод открывает соединение с БД, его следует
и закрывать, так что следует использовать менеджер контекста:

Следующие 2 метода эквивалентны 
```python
# Через менеджер контекста
with connection.cursor() as cursor:

# Через закрытие соединение в конце работы
c = connection.cursor()
try:
    c.execute(...)
finally:
    c.close()
```

`connection.cursor()` - Метод возвращает обьект предоставляющий
доступ к соединению с БД.

`cursor.execute(sql, [params])` - Метод для создания SQL запроса.

`cursor.fetchone()` - Получить первую одну запись из сделанного 
SQL запроса.

`cursor.fetchall()` - Получить все записи из сделанного SQL проса.

Пример с получением всех записей из таблицы :
```python
from django.db import connection

def select_all_from_category():
    """Получить все записи из таблицы women_category"""
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM "women_category";')
        row = cursor.fetchall()
    return row
```

В SQL запрос можно передавать параметры через `%s` и передаем 
параметры вторым аргументом, тут можно сделать этот метод, 
методом конкретной модели, таким образом мы можем снабдить модель 
большим количеством методов, для работы конкретно с этой моделью.

```python
from django.db import connection

def my_custom_sql(self):
    """Обновляем поле и получаем его же"""
    with connection.cursor() as cursor:
        cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
        cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
        row = cursor.fetchone()
    return row
```

---

Метод №2












