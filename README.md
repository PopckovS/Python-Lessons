giPython-Lessons
---
[comment]: <> (https://api.github.com/users/PopckovS)
Сборник теории и решения практических упражнений по python-3.8 
и многое другое.

[Ссылки на полезный материал.](links.md)

[Вопросы для разбора.](questions.md)

---

Теория Python :
---
 
1.  **Основное :**

    - [Основы Python](Theory/Part_1/Base.md )
    - [Разница версий и строки Unicod](Theory/Part_1/Version_difference.md )
    - [Области видимости LEGB](Theory/Part_1/Scopes_LEGB.md)
    - [Память в Си и память в Pyhton](Theory/Part_1/Memory_C_Python.md)
    - [Механизм управления памятью Pymalloc](Theory/Part_1/Memory_Pymalloc.md )
    - [Сборщик мусора](Theory/Part_1/Garbage_collector.md )
    - [Интерактивный режим REPL](Theory/Part_1/Interactive_mode_REPL.md )
    - [Аннотации методов аргументов](Theory/Part_1/Annotations.md )


2. **Типы данных в Python :**

    - [Типы данных](Theory/Part_2/Data_types.md)
    - [Boolean](Theory/Part_2/Boolean.md)
    - [Int и Float](Theory/Part_2/Integer_float.md)
    - [String](Theory/Part_2/String.md)
    - [None](Theory/Part_2/None.md)
    - [Списки - list](Theory/Part_2/List.md)
    - [Словарь - dict](Theory/Part_2/Dict.md)
    - [Множества - set, frozenset](Theory/Part_2/set.md )
    - [Кортеж - tuple](Theory/Part_2/Tuple.md)


3. **Операторы :**
    - [Арифметические операторы](Theory/Part_3/Arithmetic.md) (`+`, `-`, `*`, `/`, `//`, `%`, `**`)
    - [Побитовые Операторы](Theory/Part_3/Bitwise.md) (`&`, `|`, `^`, `>>`, `<<`, `~`)
    - [Операторы присваивания](Theory/Part_3/Assigment.md) (`=`, `+=`, `-=`, `/=`, `//=`)
    - [Оператор сравнения](Theory/Part_3/Comparison.md) (`==`, `!=`, `>`, `<`, `>=`, `<=`)
    - [Логические операторы](Theory/Part_3/Logical.md) (`and`, `or`, `not`)
    - [Операторы тождественности](Theory/Part_3/Identity.md) (`is`, `is not`)
    - [Операторы принадлежности](Theory/Part_3/Membership.md) (`in`, `not in`)


4. **Потоки управления :**
   
    - [Условие](Theory/Part_4/If_else.md) (`if`, `elif`, `else`)
    - [Тернарный оператор](Theory/Part_4/Ternary_operator.md )
    - [Цикл `for`](Theory/Part_4/For.md) ( и функция `range()` )
    - [Цикл `while`](Theory/Part_4/While.md)
    - [Блок `try` и `except`, `else`, `finally`](Theory/Part_4/Try.md)
    - [Прерывание `break`](Theory/Part_4/Break.md)
    - [Прерывание `continue`](Theory/Part_4/Continue.md)

   
5. **Функции :**

    - [Функции](Theory/Part_5/Functions.md)
    - [Замыкания функций](Theory/Part_5/Function_closures.md)
    - [Функции - lambda, map, filter, zip](Theory/Part_5/Function_lambda.md)
    - [Аргументы функции упаковка / распаковка](Theory/Part_5/Packing_and_unpacking_function_arguments.md)
    - [Аргументы функции по умолчанию](Theory/Part_5/Default_function_arguments.md)


6. **Обьекты :**

    - [Обьекты 1](Theory/Part_6/Object_1.md )
    - [Обьекты 2](Theory/Part_6/Object_2.md )
    - [Обьекты - функторы, @classmethod и @staticmethod, абстрактный метод, перегрузка ](Theory/Part_6/Object_3.md )
    - [Дескрипторы обьектов](Theory/Part_6/Descriptors.md )
    - [Модификаторы доступа public, protected, private](Theory/Part_6/Access_modifiers.md)
    - [Приватности в обьектах](Theory/Part_6/Privacy.md)
    - [Атрибут __slots__](Theory/Part_6/Mechanism__slots__.md )
    - [Наследование обьектов](Theory/Part_6/Inheritance.md )
    - [Магические методы ( dunder )](Theory/Part_6/Dunder_method.md )
    - [Паттерны программирования](Theory/Part_6/Pattern.md )
   

7. **Разное - 1 :**

    - [Итераторы и Выражения-генераторы ](Theory/Part_7/Iterators_expression_generators.md)
    - [Функции-генераторы yield](Theory/Part_7/Yield.md)
    - [Генерация списков](Theory/Part_7/List_comprehensions.md)
    - [Исключения - Exception](Theory/Part_7/Exceptions.md)
    - [Менеджеры контекста with](Theory/Part_7/With.md)
    - [Декораторы методов и классов](Theory/Part_7/Decorator.md)
    - [Функции all() any() ](Theory/Part_7/Function_all_any.md)
   

8. **Разное - 2 :**

    - [Файлы Ввод/Вывод](Theory/Part_8/File.md)
    - [Получение информации о памяти обьекта __sizeof__() и sys.getsizeof()](Theory/Part_8/Get_information_about_memory.md )
    - [Копирование copy() и deepcopy()](Theory/Part_8/Copy_object.md )
    - [Ellipsis ...](Theory/Part_8/Ellipsis.md)
    - [Особая распаковка (не функции)](Theory/Part_8/Unpacking.md)
    - [Функция enumerate](Theory/Part_8/Function_enumerate.md)
    - [Функции globals() locals() vars()](Theory/Part_8/Scopes_functions.md)
    - [Хэширование hash()](Theory/Part_8/Hash.md)
    - [Создание модулей](Theory/Part_8/Module.md)
    - [Как публиковать пакеты на PyPi](Theory/Part_8/pypi.md)
    - [Виртуальное окружение venv и freeze. Установка зависимостей.](Theory/Part_8/Virtual.md)


9. **Модули и API сервисы :**
   
    - Модуль os
      - [ Часть №1 ](Theory/Part_9/Module_os_1.md)
      - [ Часть №2 ](Theory/Part_9/Module_os_2.md)
    - [Модуль sys](Theory/Part_9/Module_sys.md)
    - [Модуль functools](Theory/Part_9/Module_functools.md) (полезные функции)
    - [Модуль weakref](Theory/Part_9/Module_weakref.md) (слабые ссылки)
    - [Модуль re](Theory/Part_9/Module_re.md) (регулярные выражения)
    - [Модуль random](Theory/Part_9/Module_random.md)
    - [Модуль time](Theory/Part_9/Module_time.md)
    - [Модуль Async](Theory/Part_9/Module_Async.md)
    - [Модуль crontab](Theory/Part_9/Module_crontab.md)
    - [Модуль pyperclip](Theory/Part_9/Module_pyperclip.md) (управление буфером обмена)
    - [Модуль pyshorteners](Theory/Part_9/Module_pyshorteners.md) (создание коротких ссылок)
    - [Модуль prettytable](Theory/Part_9/Module_prettytable.md) (красивые таблицы в консоле)
    - [Модуль webbrowser](Theory/Part_9/Module_webbrowser.md) (работа с браузером)
    - [Модуль requests](Theory/Part_9/Module_requests.md) (GET, POST запросы к ресурсам)
    - [Модуль socket](Theory/Part_9/Module_socket.md) (Работа с сокетами)
    - [Модуль moviepy](Theory/Part_9/Module_moviepy.md) (Редактирование видео)
    - [Модуль CSV](Theory/Part_9/Module_CSV.md) (Работа с форматом CSV)
    - Гео-данные
      - [ Yandex geocoder API, OpenStreetMap API, DaData API ](Theory/Part_9/Geo_data.md)
      
[comment]: <> (добавить модуль cmd)

10. **Интересные вопросы по Python :**

    - [Вопросы 1](Theory/Part_10/Questions_1.md)
    - [Вопросы 2](Theory/Part_10/Questions_2.md)
   

11. **Библиотеки :**
   
    - [Модуль numpy](Theory/Part_11/numpy)
      
         - [ Урок №1 ](Theory/Part_11/numpy/Lesson_1.md)
       
    - [Модуль matplotlib](Theory/Part_11/matplotlib)
         
         - [Установка, запуск, здание графиков и закраска. ](Theory/Part_11/matplotlib/Lesson_1.md)
         - [Множество графиков, ](Theory/Part_11/matplotlib/Lesson_2.md)
   
    - [Модуль Flask ](Theory/Part_11/Flask)   
         - [ Урок №1 ](Theory/Part_11/Flask/Lesson_1.md)
   

12. **Вопросы возникающие при работе с Postgres :**
      - [ Смена пароля для пользователя ](Postgres/pg_1.md)
      - [ Расширение timescaledb для PostgreSQL ](Postgres/timescaledb.md)
      - [ PostgreSQL, утилита `pg_dump` остановление БД ](Postgres/pg_dump.md)

---

Django 3.2 :
---
1. **Django :**
   
    - [Удобный сборник команд Django](Django/django_commands.md)
    - [Урок №1 ](Django/django_1.md) ( Установка, URL )
    - [Урок №2 ](Django/django_2.md) ( GET, POST, обработка исключений, 404 )
    - [Урок №3 ](Django/django_3.md) ( Модели, миграции, создание пользователей, модели и админка)
    - [Урок №4 ](Django/django_4.md) ( Supeuser, Получение данных из моделей )
    - [Урок №5 ](Django/django_5.md) ( Templates, Views, Jinja2, Фильтры шаблонов )
    - [Урок №6 ](Django/django_6.md) ( Подключение статических файлов )
    - [Урок №7 ](Django/django_7.md) ( Отправка Email, Установка ckeditor, настройка админки )
    - [Урок №8 ](Django/django_8.md) ( Связи между моделями, Form)
    - Модели
      - [Взаимодействие с Моделями, БД ](Django/django_sql_1.md)
      - [Модели](Django/django_models.md)
      - [Класс Meta для моделей](Django//django_sql_2.md)
      - [Модели и ORM](Django/django_sql_3.md)
      - [Поиск, приставки для фильтрации](Django/django_sql_4.md) ( objects.filter )
      - [QuerySets](Django/django_sql_5.md)
    - Миграции
      - [ Миграции ](Django/migrate_1.md)
      - [ Чистый SQL в миграциях  migrations.RunSQL ](Django/migrate_2.md) 
    - Транзакции
      - [ Транзакции ](Django/transactions_1.md)
    - Django Rest Framework (DRF)
      - [ Часть №1 ](Django/drf_1.md)
      - [ Часть №2 ](Django/drf_2.md) (API Фильтрация, Поиск, Сортировка)
      - [ Часть №3 ](Django/drf_3.md) (Аутентификация OAuth)
      - [ Часть №4 ](Django/drf_4.md) (Swagger)
    - Фикстуры
      - [ Экспорт данных из БД `dumpdata` ](Django/dumpdata_1.md)
      - [ Импорт данных из БД `loaddata` ](Django/loaddata_1.md)
    - Django + Celery
      - [ Часть №1 ](Django/celery_1.md) (Установка)
      - [ Часть №2 ](Django/celery_2.md) (Начало работы)
      - [ Часть №3 ](Django/celery_3.md) (Flower логер сообщений для Celery)
    - Сигналы Моделей
      - [ Часть №1 ](Django/signals_1.md)
    - Безопасность настроек, модуль django-environ
      - [ Переменные окружения и оболочки в Linux ](Django/environment_1.md)
      - [ Хранение данных в виртуальном окружении ](Django/venv_1.md)
    - Cookiecutter
      - [ Шаблоны Django проектов ](Django/cookiecutter_1.md)
    - Unit Test
      - [ Часть №1 ](Django/UnitTest_1.md)
    - Unit Test Django Rest Framework
      - [ Часть №1 ](Django/DRFUnitTest_1.md)
    - GeoDjango
      - [ Часть №1 ](Django/geo_django_1.md)
    - Django Admin
      - [ Часть №1 ](Django/django_admin_1.md) (регистрация моделей, `actions` Действия, `get_urls`)
      - [ Часть №2 ](Django/django_admin_2.md)
    - Django Utils
      - [ Часть №1 ](Django/django_utils_1.md)
    - Django middleware    
      - [ Часть №1 ](Django/mid_1.md)


---

Практика Python :
---

1) **Часть №1 :**

    - [Сборник примеров №1](Example/Practice_1/1.py)
    - [Сборник примеров №2](Example/Practice_1/2.py)
    - [Сборник примеров №3](Example/Practice_1/3.py)
    - [Сборник примеров №4](Example/Practice_1/4.py)
    - [Сборник примеров №5](Example/Practice_1/5.py)
    - [Дата и время](Example/Practice_1/6.py)
    - [Работа с модулем CSV ](Example/Practice_1/CSV/CSV.py)
    - [Программа для скачивания видео с YouTube](Example/Practice_1/get_videos.py)
    - [Игра Крестики-Нолики на 2 игрока, на чистом Python](Example/Practice_1/tic_tac_toe.py)
    - [Конвертация изображений и наложение изображений](Example/Practice_1/convertor_cover_img.py)
    - [Получение гео-данных по адресу](Example/Practice_1/dadata/get_geo_from_dadata.py) сервис `DaData`

2) **Часть №2**
   
   - [Решение мелких задачек по Python](Example/Practice_2/1.py)

---
GIT и Git-flow
---

- [Удобный сборник команд `git`](git/commands.md)
- [Общее описание](git/git_1.md) `git flow`
- [Конфликты, слияние и перебазирование](git/git_2.md) `git merge`, `git rebase`
    

---
Docker, Docker-compose
---

1. **Часть №1 :**
    
    - [Удобный сборник команд Docker](Docker/docker_commands.md)
    - [Docker](Docker/docker_1.md) (Images, Container)
    - [Dockerfile](Docker/docker_2.md)
    - [Docker Compose](Docker/docker_compose_3.md)

---
Алгоритмы и структуры данных
---
   1. [ Теория: Сложность алгоритмов, память, массивы, списки. ](Algorithm/Lesson_1.md)

   2. Бинарный поиск
      - [ Теория ](Algorithm/binary/binary.md) 
      - [ Практика ](Algorithm/binary/binary.py)

   3. Сортировка выбором
      - [ Теория ](Algorithm/selection/selection_sort.md)
      - [ Практика ](Algorithm/selection/selection_sort.py)

---
Тестирование и CI / CD
---

1. **Часть №1 :**
    
    - [Механизм CI / CD](Test/Lesson_CI_CD.md)

---

Разное
---

1. **Теория пограммирвоания :**

    - [Принципы KISS, DRY, SOLID, YAGNI](Other-theory/Part_1/KISS.md)
    - [REST, SOAP](Other-theory/Part_1/REST_SOAP.md)


2. **Теория :**

   - [AMQR Протокол](Other-theory/Part_2/AMQR.md)


3. **Паттерны и шаблоны проектирвоания :**

     - [Делегирование и Композиция](Other-theory/Part_3/pattern_1.md)