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
     path('list', views.PostListView.as_view(), name=None),
]
```

Теперь если мы перейдем на URL `/list` то отработает метод 
представления от нашего API, сработает представление `PostListView`
которое наследуется от `ListAPIView` которое отрабатывает по 
методу `GET`, метод `GET` в архитектуре `REST` покажет нам все
записи по этой модели, модели к которой мы привязаны. 

---

Таким образом мы создали представление API которое отдает 
данные на `GET` запрос, теперь создадим другие методы, для 
создания полноценной `CRUD` системы

`POST` — это метод, используемый для создания новых ресурсов в
нашей базе данных либо для обновления старых.

Создадим представление API которое будут отрабатывать на метод 
`POST` и тем самым будет создавать новые сущности в модели, 
внешне это будет реализовано как отправка формы, загрузкой 
картинки.

```python
from ..models import Post
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response

class PostCreateView(generics.CreateAPIView):
    """API POST создать новую запись"""
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def create(self, request, *args, **kwargs):
        super(PostCreateView, self).create(request, args, kwargs)
        response = {
            "status_code": status.HTTP_200_OK,
            "message": "Successfully created",
            "result": request.data
        }
        return Response(response)
```

Тут метод `create` будет создавать новую запись по полученному 
`POST` запросу.

---

Добавим представление для получения одной записи, обновления 
записи и ее удаления, для отработки методов `GET` `PATCH` 
`DELETE`

```python
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def retrieve(self, request, *args, **kwargs):
        """Получить обьект"""
        super(PostDetailView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully retrieved",
                    "result": data}
        return Response(response)

    def patch(self, request, *args, **kwargs):
        """Обновление"""
        super(PostDetailView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully updated",
                    "result": data}
        return Response(response)

    def delete(self, request, *args, **kwargs):
        """Удаление ресурса"""
        super(PostDetailView, self).delete(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully deleted"}
        return Response(response)
```

Далее обновим наши url

```python
from django.urls import path
from . import views
from .api import views

urlpatterns = [
    path('list', views.PostListView.as_view(), name=None),
    path('create', views.PostCreateView.as_view(), name=None),
    path('<int:pk>', views.PostDetailView.as_view(), name=None)
]
```

Метод `PostListView` принимает `GET` запрос и отдает все что
найдено, при обращении к url:`list`

Метод `PostCreateView` принимает `POST` запрос и создает запись
по обращению на url:`create/`

Метод `PostDetailView` принимает любой из `GET` `PATCH` `DELETE`
методов, и при обращении по url:`15` применяет данный метод к 
записи с этим `id`

---














