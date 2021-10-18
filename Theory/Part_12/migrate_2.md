Чистый SQL в миграциях
---
---

В миграциях мы применяем изменения в модели на реальные объекты
таблиц в БД, к примеру создав модель в миграции она будет отображена
как метод `migrations.CreateModel()`

Но так же в миграциях можно использовать и чистый SQL запрос, сделать
это можно с помощью метода `migrations.RunSQL()`

```python
from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('bigdata', '0007'),
    ]

    operations = [
        migrations.RunSQL(
            """
            INSERT INTO public.customer (id, name)
            VALUES 
                (1, 'Первый клиент'), (2, 'Второй клиент') 
            """
        )
    ]
```

Таким образом можно выполнять любой SQL запрос в миграциях.
