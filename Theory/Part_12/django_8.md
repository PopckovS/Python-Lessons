Фреймворк Django №8
---
---

Создание связей между моделями
---

[Почитать про связи моделей тут](https://djbook.ru/rel3.0/topics/db/models.html#relationships) 

При создании связей между таблицами, мы можем использовать 3 класса
они следующие:


`models.ForeignKey()` - для связей M:1

`models.ManyToManyField()` - для связей M:M

`models.OneToOneField()` - для связей 1:1

---

Пример `ForeignKey`
---

Примером создания таких связей служат 2 модели, категории уроков, 
и сами уроки, у модели что реализует одну запись принадлежащую
какой то из категорий, мы реализуем поле класса `ForeignKey()`

```python
class python_section(models.Model):
    """Разделы"""
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(blank=True, verbose_name="Описание")

class python_lesson(models.Model):
    """Уроки по разделам"""
    python_section = models.ForeignKey(
                                python_section, 
                                on_delete=models.CASCADE, 
                                verbose_name="Родительский раздел"
                                )
    title = models.CharField(max_length=255)
    content = RichTextUploadingField(config_name='default', blank=True)
```

Модель категории называется `Первичной` а модель, что является ее
подчиненной(зависящей от первичной), называют `Вторичной`

При создании такой связи, первый аргумент указывает на `Первичную`
модель, от которой будет зависеть наша запись, второй параметр
указывает как себя вести при удалении родительского раздела,
скажем тоже удалять все подчиненные записи.

```python
    python_section = models.ForeignKey(
                                python_section, 
                                on_delete=models.CASCADE
                                )
```

Есть одно правило, когда мы создаем поле для, связь во `Вторичной`
таблице, то к этому полю в конце, дается приставка `_id` таким 
образом, если мы создаем поле для связи `python_section` то в 
таблице оно будет выглядеть как `python_section_id` и так же к 
нему можно и обращаться как к полю класса.

```python
lesson = python_lesson.objects.get(pk=1)
lesson.python_section_id
```

Ограничения при удалении родительской записи.
---

Как определять ограничения при удалении родительского раздела:

- `on_delete = models.CASCADE` - При удалении записи из `первичной` 
модели, удалить все записи из `вторичной` модели.


- `on_delete = models.PROTECT` - Запретить удалять записи из 
`первичной` модели если она используется во `вторичной` модели,
то есть если есть хотя бы одна запись во `вторичной` модели 
удалять из `первичной` модели эту запись нельзя.


- `on_delete = models.SET_NULL` - Если из `первичной` модели удалили
запись к которой была привязана `вторичная` модель, то во
вторичной модели это поле связи, принимает значение `NULL`


- `on_delete = models.SET_DEFAULT` - тоже что и метод `SET_NULL` но 
в место значения `NULL` ставится дефолтное значение, которое 
определено в параметре `default`


- `on_delete = models.SET()` - То же самое, но устанавливается 
пользовательское значение.


- `on_delete = models.DO_NOTHING()` - Ничего не делать, при удалении
записи в `первичной` модели, во вторичной с этим полем, ничего не 
произойдет, и запись в поле останется висеть, и указывать в пустоту.

---

Индексы в Моделях
---

Индексы, указывая в полем модели параметр `db_index=True` мы делаем
поле индексированным, и поиск по нему будет вестись быстрее.

```python
name = models.CharField(max_length=100, db_index=True)
```
---
Какие могут возникнуть проблемы !
---

Когда мы создаем 2 модели сразу, первичную и вторичную, и в них еще
нет записей то все окей, но в случае если мы уже создали вторичную
таблицу `Women` и внесли в нее записи, и только после этого создаем 
первичную таблицу, и при этом не задаем `null=True` в поле
которое отвечает за взаимосвязь, то получается что у нас есть записи
в которых нет ссылки на родительскую категорию, и нет возможности
заполнить это поле `NULL` значением которое мы могли бы туда 
вставить, возникает конфуз.

К примеру эти 2 таблицы:
```python
from django.db import models
from django.urls import reverse


class category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

class Women(models.Model):
    cat = models.ForeignKey('category', on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
```

В случае если пытаемся создать миграции 
`python3 manage.py makemigrations` тогда `Django` спросит что ему 
делать в такой ситуации:  

```python
Please select a fix:
 1) Provide a one-off default now 
    (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: 

```

Так `Django` предупреждает об ошибке, для того чтобы это изменить, 
указать что делать с непустыми записями, добавим `null=True` и тогда
все записи что уже существуют нол не имеют ссылку на `первичную` таблицу
получат значение `null`

```python
cat = models.ForeignKey('category', on_delete=models.PROTECT, null=True)
```

---

**Создание записей в БД**

Можем создавать новые запись в бд, из кода при помощи следующей
команды:

```python
from .models import category

category.objects.create(name='Категория 3')
```

---

**Обновление всех записей по определенному полю**

Обновлять можно при помощи метода `update` который возвращает 
количество измененных полей.

```python
from .models import category

womens = Women.objects.all()
result = womens.update(cat_id=1)
print(result)

# Вывод
#  2
```
---

---
Формы отправки в Django
---

Класс `Form` в Django используется для описания логической структуры 
формы, так же как и использование моделей для описания таблиц в БД,
так образом каждое поле формы будет представлено своим классом.

Импортировать его можно так:
```python
from django import forms
```

Для работы с формами используется отдельный модуль, создадим его 
со стандартным названием `forms.py` импортируем модуль, и создадим 
класс, который будет служить для описания формы, как и модель для 
описания таблицы.

Тут поле `your_name` будет описывать 

```python
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
```
