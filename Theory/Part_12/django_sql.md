Подключение к PostgreSQL
---

Для работы с PostgreSQL требуется установить модуль `psycopg2`

```
pip install psycopg2-binary
```

В файл с настройками `settings.py` устанавливаем параметры для
подключения

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django',
        'USER': 'user1',
        'PASSWORD': '123',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

---

Запросы через Модели
---
Послед создания модели данных, мы получаем доступ к API,
которая предоставляет CRUD операции к модели.

Класс модели представляет из себя таблицу базы данных, а 
экземпляр этого класса это конкретная запись в таблице.

Будем работать с 3 следующими моделями:

```python
from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()
```

---

**1. Создание новой записи методом `save()`**

Чтобы создать новую запись, создадим обьект модели, передадим
в обьект данные для именованных атрибутов, для сохранения записи
в таблице, вызываем метод `save()`.

```python
from .models import Blog

# Создание нового экземпляра модели, новой записи в таблице 
blog = Blog(name='Новый Блог №1', tagline='Все новости блога №1')
blog.save()
```
`save()` - Вызывает метод `INSERT` и записывает данные в таблицу,
до тех пор пока метод не вызван, обращения к Бд не будет.

Данный способ создает запись за 2 шага, есть другой метод
`create()` для создания записи за 1 шаг.

---

**2. Создание новой записи методом `create()`**

Другой способ создания новой записи, в один этап, это 
метод `create()` этот метод создает обьект модели, и тут же 
сохраняет его в таблице.

```python
blog = Blog.objects.create(name='Новый Блог №1', tagline='Все новости блога №1')
```

---

**3. Обновление записи с `ForeignKey`**

Если создаем запись модели `Entry` у которой одно из полей по 
связи 1:M связанно с моделью `Blog` то в это самое поле, которое 
отвечает за связь во `вторичной` таблицы поместим сущьность
`первичной` таблицы

```python
 from blog.models import Blog, Entry

 # Получаем запись модели Entry 
 entry = Entry.objects.get(pk=1)
 
 # Получаем запись модели Blog
 cheese_blog = Blog.objects.get(name="Cheddar Talk")
 
 # В поле blog что связывает между собой таблицы помещяем сущьность
 entry.blog = cheese_blog
 entry.save()
```

---

**4. Обновление записи с `ManyToManyField`**

Есть обьект модели `Entry` у которого есть поле `authors`
оно связано связью M : M моделью `Author` для того чтобы 
добавить обьект модели `Author` в поле `authors` требуется
использовать специальный метод `add()` 

Создаем запись `joe` модели `Author` и при помощи метода 
`add()` добавляем в `entry` что является обьектом модели
`Entry`

```python
from blog.models import Author

joe = Author.objects.create(name="Joe")
entry.authors.add(joe)
```

Это добавление одного обьекта в для связи, для добавления 
нескольких обьектов, просто передаем их все в тот же метод
`add()`

```python
from blog.models import Author

john = Author.objects.create(name="John")
paul = Author.objects.create(name="Paul")
george = Author.objects.create(name="George")
ringo = Author.objects.create(name="Ringo")

entry.authors.add(john, paul, george, ringo)
```

---

**5. Менеджер для доступа к записям таблицы `objects`**

`Managers` - Менеджер класса модели, доступный через 
атрибут `.objects` вызывается только у класса, и предоставляет
доступ к записям таблицы. 

`Managers` доступны только через классы модели, а не из
экземпляров модели, чтобы обеспечить разделение между 
операциями «уровня таблицы» и операциями «уровня записи».

Тут будет ошибка !

```python
b = Blog(name='Foo', tagline='Bar')
print(b.objects) 

# AttributeError: "Manager isn't accessible via Blog instances."
```

---

**6. Получение всех объектов методом  all()`**

Получение всех записей из таблицы возможно с помощью метода
`all()` используя менеджер класса модели.

Получить все существующие записи из таблицы

```python
all_entries = Entry.objects.all()
```

---

**7. Получение одного обьекта методом `get()`**

`get()` - Метод предназначенный для получения одной, и только
одной записи из таблицы, если записей больше чем одна то 
будет вызвано исключение типа `MultipleObjectsReturned`

Если запись найдена не будет, то будет вызвано исключение 
типа `DoesNotExist`

Получаем одну запись из таблицы, где первичное поле (чаще id)
это 1

```python
one_entry = Entry.objects.get(pk=1)
```

Оба исключения что одно `MultipleObjectsReturned` что другое
`DoesNotExist` хранятся в виде атрибута модели, так что если
хотя бы одно из исключений появляется, то будет отображаться как
`Entry.DoesNotExist` и `Entry.MultipleObjectsReturned`

---

**8. Использование фильтров `filter()`**

`filter()` - Возвращает новые `QuerySet` содержащие объекты,
соответствующие заданным параметрам поиска.

Получим категорию где `id = 3` и по нему найдем все записи в
модели `Women` которые по полю `cat` привязаны к 3-й категории.
```python
category_1 = category.objects.get(pk=3)
womens = Women.objects.filter(cat=cat_1)
```

Также функции поиска `all()` и `filter()` можно комбинировать 
между собой, к примеру можно с начала выбрать все что есть,
и тут же применить фильтр на полученное множество.

```python
category_1 = category.objects.get(pk=1)
womens = Women.objects.all().filter(cat=cat_1)
```

Получить все записи за 2006 год

```python
Entry.objects.filter(pub_date__year=2006)
```

Результатом уточнения `QuerySet` является `QuerySet`,
поэтому уточнения можно объединить в цепочку, то есть 
можно сколько угодно уточнять нашу фильтрацию, к примеру 
следующим образом : 

```python
Entry.objects
    .filter(headline__startswith = 'What')
    .exclude(pub_date__gte = datetime.date.today())
    .filter(pub_date__gte = datetime.date(2005, 1, 30))
```

---

**9. Использование фильтров `exclude()`**

`exclude()` - Возвращает новые `QuerySet` содержащие объекты,
которые не соответствуют заданным параметрам поиска.

Данный метод возвращает все что не удовлетворяет условию.

Получить все записи кроме записей за 2006

```python
Entry.objects.exclude(pub_date__year=2006)
```

---

**10. Ограничение полученных данных `LIMIT` и `OFFSET`**

Для получения определенного количества данных, эквивалентного 
применению `LIMIT` можно делать нарезку массивов.

Например, получаем все записи и из них, изымаем первые 
5 объектов, `но отрицательные индексы не поддерживаются !`

```python
Entry.objects.all()[:5]
```

---
Приставки в выборке данных из Модели
---












---

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

Второй способ, это исполнение SQl запросов и возвращает экземпляр
модели, если первый метод использует абсолютно чистый SQL код,
не привязанный ни к чему, то данный метод вызывается у модели,
исполняет SQL код, и возвращает обьекты этой модели.

Этот способ использует метод `raw()` у модели, этот метод 
принимает сырой SQL запрос, исполняет его и возвращает экземпляр
специального класса `django.db.models.query.RawQuerySet` точно 
такой же `RawQuerySet` который возвращает и обычная модель.

Метод `all()` вернет обьект типа `QuerySet` а метод `raw()`
вернет экземпляр класса `RawQuerySet`

```python
# QuerySet
womens = Women.objects.all()

# RawQuerySet
womens = Women.objects.raw()
```

К примеру есть такая модель `Women`

```python
class Women(models.Model):
    cat = models.ForeignKey('category', on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
```

Cоздадим 2 метода, один метод будет получать все записи при
помощи метода `all()` а другой будет получать все записи 
произвольным SQL запросом, с помощью метода `raw()` 

```python
def get_all_women_models_all():
    """Получить все записи методом all()"""
    womens = Women.objects.all()
    print('Метод get_all_women_models_all')
    show_all_women(womens)


def get_all_women_models_raw():
    """Получить все записи произвольным SQL и методом raw()"""
    womens = Women.objects.raw('SELECT * FROM women_women')
    print('Метод get_all_women_models_raw')
    show_all_women(womens)


def show_all_women(womens):
    """Метод для отображения результата"""
    print('womens = ', womens)
    for women in womens:
        print('type(women) = ', type(women))
        print('women = ', women)
        print('women.cat = ', women.cat)
        print('women.title = ', women.title)
        print('women.content = ', women.content)
        print('women.time_create = ', women.time_create)
        print('women.is_published = ', women.is_published)
```

Результат работы метода `raw()` как видим получаем экземпляр класса
`RawQuerySet` с описанием какой именно SQL запрос был выполнен : 

```python
    get_all_women_models_raw()

    # Вывод
    # Метод get_all_women_models_raw
    # womens =  <RawQuerySet: SELECT * FROM women_women>
     
    # type(women) =  <class 'women.models.Women'>
    # women =  women 2
    # women.cat =  Категори 2
    # women.title =  women 2
    # women.content =  women 2 women 2 women 2 women 2 women 2
    # women.time_create =  2021-08-25 03:21:31.263882+00:00
    # women.is_published =  True
    
    # type(women) =  <class 'women.models.Women'>
    # women =  women 1
    # women.cat =  Категори 1
    # women.title =  women 1
    # women.content =  women 1 women 1 women 1 women 1 women 1
    # women.time_create =  2021-08-25 03:21:00.430165+00:00
    # women.is_published =  True
```

Результат работы метода `all()` как видим получаем экземпляр 
класса `QuerySet` в котором будет указано какие именно обьекты 
моделей возвращаены.

```python
    get_all_women_models_all()

    # Вывод
    # Метод get_all_women_models_all
    # womens =  <QuerySet [<Women: women 2>, <Women: women 1>]>
    
    # type(women) =  <class 'women.models.Women'>
    # women =  women 2
    # women.cat =  Категори 2
    # women.title =  women 2
    # women.content =  women 2 women 2 women 2 women 2 women 2
    # women.time_create =  2021-08-25 03:21:31.263882+00:00
    # women.is_published =  True
    
    # type(women) =  <class 'women.models.Women'>
    # women =  women 1
    # women.cat =  Категори 1
    # women.title =  women 1
    # women.content =  women 1 women 1 women 1 women 1 women 1 
    # women.time_create =  2021-08-25 03:21:00.430165+00:00
    # women.is_published =  True
```
