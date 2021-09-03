Django Rest Framework (DRF)
---
---

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

Пагинация методом GET и Ленивая загрузка
---

[Почитать про пагинацию](https://sunscrapers.com/blog/the-ultimate-tutorial-for-django-rest-framework-pagination-part-4/)

Когда мы используем метод GET для доступа к API, по URL:`/book/`
то по дефолту получаем все найденные записи, их может быть много.

Тут есть несколько важных моментов, обьектов может быть очень 
много, и на получение данных из БД с последующей сериализацией,
и передачей всех обьектов на фронт может занять много времени.

Для таких ситуация есть механизм называемый `"Ленивая загрузка"`
суть механизма в том что мы получаем только часть обьектов, и 
только когда пользователь совершит действие на сайте, активируем
`JS` скрипт, который обратится к API и получит новую небольшую
партию записей.

`Пагинация API` - при обращении к url:`/book/` методом GET, мы 
дополнительно передам параметры, что отвечают сколько записей
выводить, и с каким отступом.

`Параметры пагинации:`

1) `limit` - где параметр limit, переданный в GET, определяет 
количество элементов которое требуется получить.

2) `offset` - определяет смещение относительно начала списка.

---

В файле `settings.py` добавим настройки для создания пагинации,
тут параметр `PAGE_SIZE` отвечает за то какое количество элементов
отдавать по дефолту.

```python
REST_FRAMEWORK = {
    ....
    'DEFAULT_PAGINATION_CLASS' : 'rest_framework.pagination.LimitOffsetPagination' ,
    'PAGE_SIZE': 100 ,
    ...
}
```

---

**Пример запроса**

Получить 1 единственную самую первую запись:

    http://127.0.0.1:8000/book/?limit=1

Ответ от сервера

    {
        "count": 4,
        "next": "http://127.0.0.1:8000/book/?limit=1&offset=1",
        "previous": null,
        "results": [
                {
                    "id": 1,
                    "name": "Книга-1",
                    "type": "",
                    "status": "",
                    "content": "Привет мир !",
                    "photo": "http://127.0.0.1:8000/media/photos/store/photo_2020-06-28_04-27-44.jpg",
                    "time_create": "2021-09-02T19:04:38.254089Z",
                    "time_update": "2021-09-02T19:04:38.254112Z",
                    "is_published": true
                }
        ]
    }
---





