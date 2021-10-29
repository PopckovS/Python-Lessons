Django Rest Framework (DRF)
---
---

Страница API системы 
---

При переходе на URL `/book` мы попадем в обработку API, само
обращение к этому URL, то это GET обращение и мы получим список
всех элементов, ее можно просматривать через 2 режима:

`/book/?format=api` - просмотр данных в специальном режиме, 
в котором можно иметь допуск к форме отправки, для создания 
`POST` запроса

`/book/?format=json` - Традиционный просмотр в `JSON` формате

---

Создаем API для модели Book
---

Создадим стандартную модель, для сущности `Book` в созданном нами
приложении `store`

Файл `/store/models.py`
```python
class Book(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True, verbose_name='Текст')
    photo = models.ImageField(upload_to="photos/store/", blank=True, verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

```

Создадим Сериалайзер для этой модели и будет обрабатывать все поля 

Файл `/store/serializers.py`

```python
from rest_framework.serializers import ModelSerializer
from store.models import Book

class BooksSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
```

Создадим представление для отработки сериалайзера

Файл `/store/views.py`
```python
from rest_framework.viewsets import ModelViewSet
from store.models import Book
from store.serializers import BooksSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
```

`ModelViewSet` - специальное представление модели, которое по 
дефолту описывает все методы `CRUD` операций `API` стемы для 
данной модели `Book`

Далее создадим URL для отработки этого представления

Способ создания `URL` для `API` через класс `SimpleRouter`, для
этого в ядре всего проекта, в главный файл `urls.py` добавим
```python
# Импортируем SimpleRouter из DRF
from rest_framework.routers import SimpleRouter
# Импортируем вид созданный для API
from store.views import BookViewSet

# Создаем роутер 
router = SimpleRouter()
# Регистрируем в нем наше представление с указанием
# того URL на которы йон будет отрабатывать
router.register(r'book', BookViewSet)

urlpatterns = [
    ...
]

# Добавляем URL для API к нашим основным URl
urlpatterns += router.urls
```

---



Используем `Filters`, `Search`, `Ordering` для модели `Book`
---

- [Про фильтрации почитать тут](https://www.django-rest-framework.org/api-guide/filtering/)

Установка пакета для фильтрации.

    pip3 install django-filter

Теперь в наших представлениях, мы можем создать дополнительный 
атрибут `filter_backends`, который будет отвечать за фильтрации
через URL по которому мы будем обращаться к API

---

Фильтр `DjangoFilterBackend`
---

Это точный поиск данных по переданному параметру

`/store/views.py`
```python
from django_filters.rest_framework import DjangoFilterBackend

class BookViewSet(ModelViewSet):
    """Все CRUD к модели Book"""
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    
    # Указываем класс который будет фильтровать
    filter_backends = [DjangoFilterBackend]

    # Указываем поля по которым можно проводить фильтрацию
    filter_fields = ['name']
```

После этого укажем новый атрибут `filter_fields` который будет 
принимать список с полями по которым можно будет фильтровать.

Фильтр `DjangoFilterBackend`

При установке фильтра 

```python
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name']
```
Запрос будет вестись на прямую, при таком запросе

    http://127.0.0.1:8000/book/?name=222

Будут выведены только те записи у которых `name = 222`

---

Фильтр `SearchFilter`
---

Специальный поиск по пересечению, ищет по нескольким полям, и
возвращает те данные которые пересекаются, поиск ведется при 
помощи специального параметра `search`

```python
from rest_framework import filters

class BookViewSet(ModelViewSet):
    ...
    filter_backends = [..., filters.SearchFilter]
    ...
    search_fields = ['type', 'status']
```

Определив специальную переменную `search_fields` в ней указываем
все поля по которым будет вестись поиск.

Пример `?search=1` вернет те записи где, имеется пересечение те
записи где `type=1` и `status=1`

---

Сортировка `OrderingFilter` в API
---

Сделаем сортировку для API, импортируем `OrderingFilter`

```python
from rest_framework.filters import SearchFilter, OrderingFilter

class BookViewSet(ModelViewSet):
    ...
    filter_backends = [..., OrderingFilter]
    ...
    ordering_fields = ['type', 'status']
```

Определив специальную переменную `ordering_fields` в нее передаем
поля по которым будет вестись сортировка, данный метод использует
параметр `ordering` в который передаем поле для сортировки.

Примеры:

Отсортировать все по `status`

    http://127.0.0.1:8000/book/?ordering=status

Отсортировать все по `type` 

    http://127.0.0.1:8000/book/?ordering=type

Также в сортировке можно сортировать `DESC` в обратном направлении,
для этого требуется указать поле с отрицательным знаком

    http://127.0.0.1:8000/book/?ordering=-status
    http://127.0.0.1:8000/book/?ordering=-type
