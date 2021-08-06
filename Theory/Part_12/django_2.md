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


