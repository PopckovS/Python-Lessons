Создание Миграции
---
---

Миграции - это способ, которым Django распространяет изменения сделанные 
с моделями, на схемы базы данных.

---

Создание миграции для новой модели, когда мы создаем новые модели, они 
еще не отслеживаются, для создания миграции на новую модель, используется
следующая команда.

    ./manage.py makemigrations

В каждом приложении Django, есть директория `migrations` которая сама по 
себе, является пакетом python, каждый раз когда мы создаем миграции, в этой
директории создается новый файл, это файл миграций, его название задается 
специальным образом, с указанием номера миграции и краткого описания 
изменений, к примеру так: `0002_alter_message_geo_location.py`

Так же есть и специальный файл `0001_initial.py` который генерируется 
первым.

---

При создании файла с миграцией, генерируется новый класс с различными
атрибутами, к примеру такой класс, если модели наследуются от класса
`models.Models` то миграции от класса `migrations.Migration`

Атрибут `initial` указывает, является ли эта миграция первой для приложения 
или нет.

Атрибут `dependencies = []` это зависимость, от другой миграции, ибо нельзя
менять какие-либо поля в таблице если эта таблица не была создана.

Атрибут `operations = []` это список с объектами, где каждый объект, это 
определенный тип, к примеру такие:

`migrations.CreateModel` - создание модели

`migrations.RenameField` - переименование полей модели

`migrations.AddField` - добавить поле

```python
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=60, verbose_name='Категория')),
                ('tag', models.CharField(max_length=255, verbose_name='Теги')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=60, verbose_name='Вид карточки')),
                ('date_time', models.DateTimeField(verbose_name='Дата и время')),
                ('address', models.CharField(max_length=120, verbose_name='Адрес')),
                ('description', models.TextField(verbose_name='Описание происшествия')),
                ('geo_location', models.CharField(max_length=120, null=True, verbose_name='Координаты')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='parse.category', verbose_name='Категория обращения')),
            ],
        ),
    ]
```

---







