Сборник команд для работы с Django
---

**Разное**

    # Если порт завис, бывает такое в PyCharm
    sudo kill -9 `sudo lsof -t -i:8000`

---
**Django** 

    pip3 install django

    python3 -m django --version

    django-admin startproject ste_name

    python3 manage.py runserver

    python3 manage.py startapp project_name

    python3 manage.py makemigrations

    python3 manage.py migrate

    # Посмотреть SQL запрос
    python3 manage.py sqlmigrate polls 0001

    # Проверка небыло ли ошибок в SQL миграциях
    python3 manage.py check

    python3 manage.py createsuperuser

    # Собрать статические файлы в файле static
    python3 manage.py collectstatic

---
**Установка**

    pip3 install psycopg2-binary

    pip3 install django-filter

    pip3 install djangorestframework

---
**Зависимости**

    pip3 freeze > reauirements.ru

    pip3 install -r reauirements.ru

    # Описание API
    pip3 install drf-yasg

---
**Celery**

    pip3 install celery

    celery -A project-name worker -l debug

---
**Celery + Flower**

    pip3 install flower
    
    celery -A project_name flower --address=127.0.0.6 --port=5566
