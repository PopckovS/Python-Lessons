Фреймворк Django
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
Создание первого представления для приложения
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




