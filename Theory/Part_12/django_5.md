Фреймворк Django №4
---
---

Представления и шаблоны
---

Методы представлений(виды) отрабатывают соответствующий им URL адрес,
создадим 4 URL пути для работы 4 представлений, для опросов пользователей.

Наши URL адреса `/polls/urls.py` :

```python
urlpatterns = [
    # URL: /polls/ Домашняя страница
    path('', views.index, name='home'),

    # URL: /polls/<id:int>/ Показать вопрос по ID
    path('<int:question_id>', views.detail, name='detail'),

    # URL: /polls/<id:int>/results/ Показать результат опроса по ID
    path('<int:question_id>/results/', views.results, name='results'),

    # URL: /polls/<id:int>/vote/ Проголосовать по ID
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

Наши виды `/polls/views.py` с методами что будут отрабатывать на URL : 

```python
def index(request):
    """
    Главный метод, показывает все вопросы.
    URL: /
    """
    return HttpResponse("Показывает все вопросы")


def detail(request, question_id: int):
    """
    Показать конкретный вопрос по его id
    URL: /<question_id>/detail
    """
    return HttpResponse(
        f"Показать конкретный вопрос по его id = {question_id}"
    )


def results(request, question_id: int):
    """
    Показать результат по конкретному вопросу по его id
    URL: /<question_id>/results
    """
    response = f"Показать результат по конкретному \n " \
               f"вопросу по его id = {question_id}"
    return HttpResponse(response)


def vote(request, question_id: int):
    """
    Голосование по вопросу по его id
    URL: /<question_id>/vote
    """
    return HttpResponse(f"Голосование по вопросу {question_id}")
```

Каждое из представлений выполняет одно из двух действий, возвращает
обьект типа HttpResponse или создает исключение Http404

В процессе работы можно выполнять все остальное, как в контроллере,
читать из Бд генерировать файлы и прочее...



