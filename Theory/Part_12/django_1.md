Фреймворк Django №1
---
---
Создание проекта
---
Создали виртуальное окружение, далее работаем с вирт-окруж, 
устанавливаем ядро Django:

     pip3 install django

Посмотреть все доступные команды можно:

    django-admin

    # Вывод
    Available subcommands:
    [django]
        check               compilemessages
        createcachetable    dbshell
        diffsettings        dumpdata
        flush               inspectdb
        loaddata            makemessages
        makemigrations      migrate
        runserver           sendtestemail
        shell               showmigrations
        sqlflush            sqlmigrate
        sqlsequencereset    squashmigrations
        startapp            startproject
        test                testserver

Создаем новый проект django такой командой 
`django-admin startproject Название_сайта`:

    django-admin startproject coolsite

После этого будет создана новая директори `coolsite` в которой будет  
еще одна под директория `coolsite` и файл `manage.py`

`coolsite` - пакет с конфигурациями проекта.

`manage.py` - Через него происходит вся работа с сайтом, это утилита
которая будет выполнять работу от `django-admin`

---
Запуск сайта
---
Для запуска встроенного отладочного сервера самого Django, переходим в 
проект и запускаем сервер такой командой:

    python3 manage.py runserver

Сайт запустится на стандартном для него лок хосте, на дефолтном порту
`http://127.0.0.1:8000/` выйти и остановить сервер можно стандартной командой
`CONTROL-C`.

Для изменения порта следует точно указывать порт в ручную:

    python3 manage.py runserver 4000

По дефолту проект работает с SQLite и при первом запуске, будет создан
файл `db.sqlite3` для работы с БД.

---
Создание приложения
---
Суть философии Django в создании отдельно функционирующих приложений,
каждое из которых можно переиспользовать в других проектах.

Для создания нового приложения, переходим в корень сайта и создаем 
новое приложение с названием `women` это создаст новое приложение с 
одноименным названием:

    python3 manage.py startapp women

При создании нового приложения, мы получим след структуру:

    women /

        migrations /    # Хранение миграций Бд только для этого приложения
            __init__.py

        __init__.py
        admin.py        # Для связи приложения с админ панелью сайта
        apps.py         # Для настройки приложения
        models.py       # Для хранения ORM моделей для связи с БД
        tests.py        # Модуль для тестирвоания
        views.py        # Для хранения представлений приложения

После создания приложения, требуется зарегистрировать его в самом проекте,
для этого в файле настроек `collsite/settings.py` где хранятся подключения
стандартных приложений, дополним подключением нашего приложения:

    INSTALLED_APPS = 
    [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    
        # Наши приложения
        'women.apps.WomenConfig'
    ]

Где строка `women.apps.WomenConfig` будет указывать на обращение к 
приложению `women` его файлу `apps.py` и классу что в нем находится 
`WomenConfig` этот класс ответственен за настройки нашего приложения.

---
Создание первого представления для приложения и URL для него 
---
В самом приложении есть файл `views.py` в котором и будем создавать 
виды для приложения, создадим в нем функцию `index` которая принимает
параметр в виде спец обьекта класса `HttpRequest` который содержит 
информацию о запросе, и возвращаем спец обьект класса `HttpResponse`
с ответом на запрос.

```python
    from django.http import HttpResponse
    from django.shortcuts import render
    
    # Отображение главной страницы
    def index(request):
        return HttpResponse("Страница приложения women")
```
Так мы создали наше первое представление, теперь для его работы, нужно 
связать его с url адресом.

В файле `coolsite/urls.py` добавим наш путь, в список `urlpatterns`
добавляем `path('women/', index)` где `women/` есть URL к которому 
привязан вид, а `index` есть указание на функцию которая отображает 
главный вид, но для работы всего этого требуется импортировать эту 
функцию `from women.views import index`

```python
# Импорт видов от приложения women
from women.views import index

urlpatterns = [
    # Админ панель сайта
    path('admin/', admin.site.urls),

    # Подключаем приложение women
    path('women/', index)
]
```

Данный подход к созданию URL возможен, но нарушает инкапсуляцию приложения,
используем другой подход, суть его в том чтобы все URL пути приложения 
были описаны внутри самого приложения, а внешне в сам проект, все эти
URL пути будут подключены одной строчкой, которая будет родительским
путем для всех дочерних URL приложения. 

Что делаем, все url для приложения `women` переносим из `collsite/urls.py`  
во внутренний для приложения `women/urls.py`

`collsite/urls.py` будет содержать корень для всех url путей приложения:

```python
urlpatterns = [
    # Админ панель сайта
    path('admin/', admin.site.urls),

    # Подключаем URL для приложения women
    path('women/', include('women.urls'))
]
```

`women/urls.py` будет содержать все внутренние url пути для приложения: 

```python
# Импорт видов от приложения women
from women.views import index, categories

# URL внутри приложения women
urlpatterns = [
    path('', index),
    path('categories', categories),
]
```

Как это работает, берем корень пути `women/` и соединяется с каждым
внутреннем путем, в результате получаем след пути:

    women/    # Отработает вид index
    women/categories  #Отработает вид categories
    
---
Паттерны в URL
---
Помимо стандартных url путей, можно делать их динамичными, указывая 
паттерны, которые будут передаваться в качестве параметров, 
которые можно использовать для получения данных из БД:

URL пути:
```python
urlpatterns = [
    path('', index),
    path('categories/<int:catID>', categories),
]
```

В виде он приходит в качестве параметра:
```python
def categories(request, catID: int):
    return HttpResponse(f"<h1>Статья категории {catID}</h1>")
```

Использовать в качестве паттерна можно следующие типы:

    str  - строка, исключая символ /
    int  - числа включая 0
    slug - все спец символы, и числа и строки "4532dfg" но только латиница
    uuid - цифры включая дефис
    path - любая строка включая /

По мимо `path()` можно использовать` re_path()` который задает регулярное 
выражение, по которому будет связан URL с видом.

К примеру такое регулярное выражение ищет 4 цифры после слова `archive/`
и эти 4 цифры будут переданы в вид в качестве переменной с названием `year`

```python
# URL паттерн
re_path(r'^archive/(?P<year>[0-9]{4})', archive),

# Вид что его отображает
def archive(request, year):
    return HttpResponse(f"<h1>Архив по годам {year}</h1>")
```




