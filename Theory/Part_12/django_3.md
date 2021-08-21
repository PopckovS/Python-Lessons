Фреймворк Django №3
---
---

База данных, модели, миграции и подключение моделей к админке.
---

ORM (Object-Relation Mapping) - обьектно-реляционное отображение, суть 
данной системы заключается в представлении таблиц БД, в качестве классов
программного кода, и инкапсуляции самого кода от конкретной СУБД, это 
своего рода прослойка между кодом и таблицами, для одинаковой работы с
любой СУБД.

В файле настроек `<project_name>/settings.py` определение с какой Бд будем 
работать, описывается в настройке `DATABASES`, с параметрами для работы,

Начальные настройки для подключения к БД :
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
В этом словаре с настройками можно увидеть ряд параметров, рассмотрим 
эти параметры подробнее:

1) `ENGINE` - указывает СУБД с которой будем работать, для разных СУБД 
параметры разные:

```
    'django.db.backends.sqlite3'
    'django.db.backends.postgresql'
    'django.db.backends.mysql'
```

2) `NAME` - это название БД, если используется `SQLite` то указывается
полный путь к файлу, для указания на корень проекта в `settings.py`
самим Django предопределена специальная константа `BASE_DIR` которая
указывает на корень проекта.

В зависимости от выбранной СУБД количество настроек будет разным, для 
`sqlite3` статочно таких:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
      
        # В корне проекта лежит файл с БД sqlite3 
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Для использования PostgreSQL параметры будут другими:

```python
        DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'lessons-django',
            'USER': 'serg',
            'PASSWORD': '11',
            'HOST': '127.0.0.1',
            'PORT': '8000',
        }
    }
```

---
Начальная Миграция
---

В настройке `INSTALLED_APPS` по дефолту определены приложения для 
стандартной работы сайта, также мы и сами создаем и подключаем свои 
приложения, все эти приложения имеют свои модели, для того чтобы создать 
все эти таблицы, требуется запустить команду:

```
python3 manage.py migrate
```

`migrate` - команда просматривает все подключенные приложения и анализирует
модели в приложениях, если находит еще не примененные миграции то запускает 
их.

---
Создание моделей
---
Скажем мы хотим создать приложение `polls` которое будет создавать опрос
пользователей, нам потребуется создать 2 модели в приложении `polls`

1) Модель `Question` будет содержать 2 поля, Вопрос и Дату публикации. 

2) Модель `Choice` будет содержать 2 поля, Текст выбора и Подсчет голосов,
каждый `Choice` связан с `Question`.

В файле `polls/models.py` создадим наши модели, каждая модель будет 
задаваться как класс с именем в соответствии с таблицей в БД.

Тут все взаимодействие происходит через класс models, каждая модель 
наследуется от `django.db.models.Model` каждое свойство(поле) данного класса
реализуется как столбец таблицы и как класс наследуемый от `models`.

Каждое поле представлено своим классом:
   
1. `models.CharField` - реализует тип данных char
2. `models.DateTimeField` - дата/время
3. `models.ForeignKey` - внешний ключ
4. `models.IntegerField` - целое число

Обратим внимание, что мы не задаем первичный ключ в каждой из моделей,
он будет создан автоматически.

```python
# импорт модуля для создания моделей
from django.db import models

# модель для вопросов с 2 полями
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

# дель для выборов опросов
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

---
Создание миграции на модели
---

После того как модели для приложения `polls` созданы, на эти модели 
требуется создать миграции, миграции для моделей именно приложения `polls`
можно создать при помощи следующей команды:

```
python3 manage.py makemigrations polls

# Вывод
# Создана миграция с созданием 2 моделей/таблиц
Migrations for 'polls':
  polls/migrations/0001_initial.py
    - Create model Question
    - Create model Choice
```

После этого будет создана миграция именно и только для приложения `polls`
и будет помещена в пакет `polls/migrations` сформирована в файл 
`0001_initial.py` в последующем каждая новая миграция, на новую модель или 
изменение старых моделей будет сформирована и положена в новый файл миграции,
с номером по порядку.

---
Просмотр SQL кода, что создан миграцией 
---
Когда миграция на основе новых моделей создана, она еще не применена, то
есть миграция создана и заложена в файл `0001_initial.py` но еще не применена,
и в самой БД таблицы на ее основе не созданы.

Перед запуском миграции на исполнение, можно посмотреть тот `SQL` код
который будет применен этой миграцией, сделать это можно следующим способом.

Используем специальную утилиту `sqlmigrate` по следующему примеру, 
`sqlmigrate <project_name> <number_of_migration>` посмотрим `SQL` 
созданных моделей:

```
python3 manage.py sqlmigrate polls 0001


    BEGIN;
    --
    -- Create model Question
    --
    CREATE TABLE "polls_question" (
      "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
      "question_text" varchar(200) NOT NULL, 
      "pub_date" datetime NOT NULL
     );
    --
    -- Create model Choice
    --
    CREATE TABLE "polls_choice" (
      "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
      "choice_text" varchar(200) NOT NULL,
      "votes" integer NOT NULL,
      "question_id" bigint NOT NULL 
      REFERENCES "polls_question" ("id") DEFERRABLE INITIALLY DEFERRED
     );
    --
    --
    CREATE INDEX 
    "polls_choice_question_id_c5b4b260" ON "polls_choice" ("question_id");
    --
    COMMIT;
```

Именно этот `SQL` и будет выполнен при запуске миграции.

Первичные ключи созданы в таблицах автоматически, даже без описания их в 
самих моделях.

В классе моделей мы определяли названия классов с большой буквы, в запросе
видим что Django автоматически переводит название моделей в нижний регистр, и 
добавляет префикс в виде названия приложения, таким образом это позволяет
по первому слову таблицы сразу определить к какому приложению оно относится
`polls_choice` и `polls_question`.

Также при создании связи на уровне СУБД, название поля по которому будет 
создана связь, `question` автоматически получает `id` для указания, что это 
поле `question_id` служит связью.

Помимо просмотр SQL при помощи `sqlmigrate` также есть команда для проверки
ошибок в миграциях, для этого используем команду:

      python3 manage.py check

В результате получаем ответ:

      System check identified no issues (0 silenced)

---
Применение миграций `migrate`
---

Когда мы создали миграцию и посмотрели на ее `SQL` код, теперь ее 
требуется исполнить, для этого можно воспользоваться все той же командой
`python3 manage.py migrate` она анализирует все приложения, ищет все файлы
в папках миграций всех приложений, и сверяет не появилось ли там новых 
миграций, информация о том какие миграции уже были применены, хранятся в
специальных таблицах в БД.

```
python3 manage.py migrate

Operations to perform:
  Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
  Applying polls.0001_initial... OK
```

В выводе можно увидеть что для приложений: admin, auth, contenttypes, 
polls, sessions ведется поиск на новые миграции, в разделе 
`Running migrations` показаны какие миграции применены к БД, строка
`polls.0001_initial` говорит о том что для приложения `polls` применена
миграция `0001_initial`  файла `polls/migrations/0001_initial.py`

---

Еще о создании моделей
---

Создадим еще модель с названием `Women` и интересными полями.

```python
class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
```

1. `models.DateTimeField` - поле для определения даты/времени. 

```python
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
```

`auto_now_add` - этот параметр, указывает внесение даты/времени в момент
создания записи в БД, и больше она меняться не будет, хорошо подходит 
для создания поля указывающего на дату загрузки.

`auto_now` - автоматически задает дату/время, в момент изменения этой 
записи в БД.

2. `models.ImageField` - поле для хранения ссылки на загруженное фото,

```python
photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
```

`upload_to` - параметр указывает куда сохранять img, можно указывать
в виде шаблона с подкаталогами. По такому шаблону `/%Y/%m/%d/` 
картинки будут загружаться каждый день в новый каталог.

При использовании поля `models.ImageField` требуется библиотека `Pillow`
иначе будет ошибка такого рода:
```
ERRORS:
women.Women.photo: (fields.E210) Cannot use 
ImageField because Pillow is not installed.
        HINT: Get Pillow at https://pypi.org/project/Pillow/
         or run command "python -m pip install Pillow".
```

Установка Pillow
```
pip3 install Pillow
```

---

Константы `MEDIA_ROOT` `MEDIA_URl`
---

В модели мы можем определить поле типа `models.ImageField` для 
автоматической загрузки изображения, в папку по указанному пути, вот 
как это работает.

Если в поле модели мы указываем такой путь:

```python
    photo = models.ImageField(upload_to="Изображение")
```

То когда мы сделаем загрузку изображения на сайт, в корне сайта будет 
автоматически создана директория с названием `Изображение` и в нее 
будет помещен загруженный файл, и корневой каталог будет выглядеть так:

```
coolsite /
    coolsite  
    db.sqlite3  
    manage.py  
    polls  
    static  
    women  
    Изображение /
        Screenshot_from_2021-07-13_19-10-38.png
```

Это очень удобно, но есть одна проблема, если у м еня есть несколько 
моделей, и у каждой из моделей будут свое поле для загрузки изображений,
 мы будем получать новую директорию для каждой из моделей, к примеру так:

```python
class Model_1(models.Model):
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    
class Model_2(models.Model):
    photo = models.ImageField(upload_to="Изображение")
```

То мы получим следующую директорию:

```
coolsite /
    coolsite  
    db.sqlite3  
    manage.py  
    polls  
    static  
    women  
    photos / 
        2021 /
            08 /
                20 /
                    bass.png
    Изображение /
        Screenshot_from_2021-07-13_19-10-38.png
```

В файле `coolsite/settings.py` мы можем определить 2 константы: 

```python
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URl = '/media/'
```

Что нам это дает:

`os.path.join()` - соединяет строки вместе, при помощи специального
разделителя, который используется именно в текущей ОС, и возвращает
эту строку.

`BASE_DIR` - предопределенная константа, содержит в себе полный путь 
от корня всей ОС, до корня сайта.

`MEDIA_ROOT = os.path.join(BASE_DIR, 'media')` - эта константа будет
содержать полный путь от корня ОС, до папки `media` в корне сайта.

`MEDIA_ROOT` - когда эта константа определена, то при загрузки файлов
на сайт, будет создана директория `media` и в ней уже и будет созданы
директоии что были указаны в поле моделей.

И теперь наша структура будет выглядеть так:

```
coolsite / 
    coolsite  
    db.sqlite3  
    manage.py  
    polls  
    static  
    women
    media /
        photos / 
            2021 /
                08 /
                    20 /
                        bass.png
        Изображения / 
            2021 /
                08 /
                    20 /
                        Screenshot_from_2021-07-13_19-10-38.png
```

Таким образом структура загрузки изображений будет формироваться 
следующим образом `MEDIA_ROOT + models.ImageField()`

После того как мы создали модель с полем загрузки изображения, и 
подключили его модель в админку, а админке мы можем добавить запись
в БД, и загрузить картинку, однако открыть ее мы не сможем, для этого
потребуется сделать ряд изменений.

В файле `coolsite/settings.py` есть наши настройки, тут `MEDIA_ROOT` 
как мф уже выяснили, отвечает за директорию загрузки файлов.
```python
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URl = '/media/'
```

Другая же константа `MEDIA_URl` отвечает за то, по какому URL мы сможем
обращаться к этому файлу, устанавливаем ее в значение `/media/`

В файле `coolsite/urls.py` добавляем следующую запись с импортами нужных
модулей.

```python
"""coolsite URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from women.views import *

# Импорт для работы с статическими файлами
from django.conf.urls.static import static
from coolsite import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('women', include('women.urls')),
    path('polls', include('polls.urls'))
]

# Если мы в режиме DEBUG=True то добавляем специальный URL путь
# к статическим загруженным файлам в /media/
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
```

После этого все скаченные изображения будут доступны для просмотра, в
том числе и из админки.