Фреймворк Django №2
---
---

Обработка GET и POST запросов
---
В видах, первый параметр, что мы получаем в метод это `request` он
содержит в себе информацию о запросе, включая GET, POST.

```python
def categories(request, catID: int):
    if request.GET:
        print(request.GET)

    if request.POST:
        print(request.POST)

    return HttpResponse(f"<h1>Статья категории {catID}</h1>")

    # При запросе типа 
    # http://127.0.0.1:8000/categories/34?name=Gagarin&type=pop
    # В терминале увидим вывод информации:     
    # <QueryDict: {'name': ['Gagarin'], 'type': ['pop']}> 
```
---
Обработка исключений
---
В файле с настройками `settings.py` есть переменная, что отвечает за
настройку отладки, при параметре `True` мы находимся в режиме отладки,
при котором страница `404` отображает дополнительную информацию для 
разработчика.

```python
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
```

Чтобы переключить сайт в боевой режим, и не выводить дополнительную 
информацию, и при обращении к несуществующей странице показывать стандартную 
`404` страницу, переопределим параметр отладки, и добавим хост к которому 
будет разрешено обращаться.

```python
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1']
```

---
Переопределение страницы ошибок
---
В главном файле настроек `settings.py` можно переопределить системную 
переменную `handler404` присвоить ей функцию, которая будет отрабатывать 
при ошибке 404

```python
from women.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('women.urls'))
]
handler404 = pageNotFound
```

Саму функцию для обработки ошибок можно поместить в виды любого приложения,
такая функция должна возвращать обьект спец класса `HttpResponseNotFound`
и принимать 2 параметра, с информацией запроса и возникшей ошибкой.

```python
from django.http import HttpResponse, HttpResponseNotFound

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена, ошибка 404</h1>")
```

В случае если требуется в любом другом виде, при неком условии отобразить 
страницу 404, то сделать это можно при помощи спец метода `Http404()`

```python
from django.http import HttpResponse, Http404

def archive(request, year):
    if int(year) > 2021:
        raise Http404()
    return HttpResponse(f"<h1>Архив по годам {year}</h1>")
```

Аналогичным образом можно переопределять страницы ошибок, и при других 
ситуациях:

    handler500 - Ошибка сервера
    handler403 - Доступ запрещен
    handler400 - Невозможно обработать запрос

Но все эти страницы ошибок будут срабатывать, если `DEBUG = False` иначе
мы всегда будем видить страницу с отладочной информацией.

---
Создание Редиректов 301, 302
---

301 - Ресурс перемещен на постоянной основе.

302 - Ресурс перемещен на временной основе.

Импортируем спей функцию `redirect()` которой указываем куда делать 
перенаправление, при определенных обстоятельствах, в дефолтном 
использовании `redirect()` пользует перенаправление с кодом `302`

```python
from django.shortcuts import render, redirect

def archive(request, year):
    if int(year) > 2021:
        return redirect('/')

    return HttpResponse(f"<h1>Архив по годам {year}</h1>")

    # Вывод в терминале
    # "GET /archive/2025 HTTP/1.1" 302 0
```

Если передать в функцию именной параметр, `permanent=True` то 
перенаправление будет постоянным.

```python
    return redirect('/', permanent=True)

    # Вывод в терминале
    # "GET /archive/2025 HTTP/1.1" 301 0
```

