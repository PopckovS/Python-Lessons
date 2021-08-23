Фреймворк Django №6
---
---

Отправка Email
---

[Почитать по подробнее, про отправку Email](https://djangodoc.ru/3.2/topics/email/)

В самом python есть модуль `smtplib` я отправки почты, `Django` дает
обертку над ним, для этого используется `django.core.mail`

В файле настроек `coolsite/settings.py` определим константы для работы
почты через `smtp`:

```python
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "Тут email который будем использовать"
EMAIL_HOST_PASSWORD = "Пароль"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
```

Далее мы можем использовать отправку `Email` в видах:

```python
from django.core.mail import send_mail
from coolsite.settings import EMAIL_HOST_USER

def index(request):
    
    send_mail(
        'title of email: Hello World !',
        'body of email: Text',
        EMAIL_HOST_USER,
        ['Email кому отправляем'],
        fail_silently=False,
    )
    
    return render(request, 'python/section.html', context=context)
```

Также есть и другие методы для отправки писем:

`send_mass_mail` - для массовой отправки писем.

---
**Настройка Yandex**

В данном примере я использовал отправку через `smtp` сервер, от 
`yandex`  этого требуется зарегать почту на `yandex` и в настройках 
разрешить отправку почты через `smtp`

![](img/email_yandex.png)

Иначе мы будем проходить аутентификацию, но не будем иметь доступ
к отправке почты, и будет получать ошибку типа

```
(535, b'5.7.8 Error: authentication failed: 
    This user does not have access rights to this service')
```

---

**Использование других SMTP серверов**

В зависимости от того, какой SMPT сервер хотим использовать
для отправки писем с сайта, нужно указывать соответствующий
хост и порт этого сервера :

Настройки для `mail.ru`

```python
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_PORT = 2525
EMAIL_HOST_USER = "your@mail.ru"
EMAIL_HOST_PASSWORD = "password"
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
```

Настройки для `gmail.com`

```python
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = "your@gmail.com"
EMAIL_HOST_PASSWORD = "password"
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
```

Настройки для `yandex.ru`

```python
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "your@yandex.ru"
EMAIL_HOST_PASSWORD = "password"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
```

---
Настройка отображения модели в админке 
---

`list_display_links` - что является ссылкой на сам обьект
`search_fields` - по какис полям вести поиск в админке
`list_display` - Что показывать на дисплее админки

```python
from django.contrib import admin
from .models import python_section, python_lesson

class python_section_admin(admin.ModelAdmin):
    """Управление разделами Python уроков в админке"""
    list_display = ('id', 'title', 'time_create', 'is_published')
    list_display_links = ('id', 'title', 'time_create')
    search_fields = ('id', 'title')


class python_lesson_admin(admin.ModelAdmin):
    """Управление уроками для Python в админке"""
    list_display = ('id', 'title', 'time_create', 'is_published')
    list_display_links = ('id', 'title', 'time_create')
    search_fields = ('id', 'title')

    
# Register your models here.
admin.site.register(python_section, python_section_admin)
admin.site.register(python_lesson, python_lesson_admin)
```

