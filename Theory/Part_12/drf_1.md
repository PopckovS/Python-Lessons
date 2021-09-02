Django Rest Framework (DRF)
---
---

DRF это фреймворк для создания RESTful-интерфейсов.

Установка DRF
```
pip3 install djangorestframework
```

Подключаем в список с приложениями, сам `DRF` в `settings.py`

```python
INSTALLED_APPS = [
    ...
    # Add it here
    'rest_framework', 
    ...
]
```

---

Создадим модель для постов, с текстом и картинкой.

```python
from django.db import models

class Post(models.Model):
    """Модель для работы с статьями"""
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name='Фото')

    def __str__(self):
        return self.title
```

---

Создание сериализатора `serializer`
---

Для хранения данных нашего API, создадим в приложении для которого
хотим создавать это API, создадим новую директорию `api`

`api` - Директория в приложении где будем хранить наше API

Создадим в нем, следующие файлы:

`api/serializers.py` - тут будут храниться сериализаторы, которые
позволяют переводить структуру данных или объекта в формат,
который можно сохранить или передать, а впоследствии восстановить
обратно.

`api/views.py` - тут будем хранить виды, которые будут отвечать 
на какой `URL` и какой метод `HTTP` запроса отрабатывать.

Файл `api/serializers.py`
```python
from ..models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Post"""
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'is_featured', 'image')
```
В сериализаторе `api/serializers.py`создадим класс, который будет
наследоваться от `ModelSerializer`

`ModelSerializer` - класс, который предоставляет удобный ярлык
для создания сериализаторов, которые работают с экземплярами
конкретной модели и наборами запросов.

`model` - Атрибут в котором указываем модель для которой создаем API

`fields` - Указываем кортеж с полями модели которые будут 
сериализованы.

---

Создаем представления `views`
---

`api/views.py` - тут будем хранить представление, она принимает на
вход веб-запрос и возвращает ответ.

```python
from ..models import Post
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
```

Наша функция представления будет наследоваться от 
`generics.ListAPIView`

`ListAPIView` - Используется для конечных точек, доступных только
для чтения, для представления коллекции экземпляров модели, 
отрабатывает на метод `GET` то есть отдает данные пользователю.

`queryset` - переменная которая будет хранить в себе данные 
получаемые из модели.

`serializer_class` - переменная хранит в себе функцию нашего 
сериализатора. 

---

Создание URL на представление API
---

В нашем приложении для которого создаем API систему, в файле 
`urls.py` создадим `URL` который будет направлен на представление.

Как и любое другое представление, представление от API тоже
отрабатывает на URL, для этого используется специальный метод
`as_view()` который передаем в вид.

```python
from django.urls import path
from . import views
from .api import views

urlpatterns = [
    path('', views.PostListView.as_view(), name=None)
]
```

---

























