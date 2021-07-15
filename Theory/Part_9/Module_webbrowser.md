Модуль webbrowser
---
---
Стандартный модуль, открывает в браузере url ссылку.

Данный пример, открывает дефолтный в системе браузер, и 
идет на стр https://yandex.ru/maps куда передает адрес,
что передан из терминала или буфер обмена, и мы получаем 
этот адрес.
Данный пример, открывает дефолтный браузер системы, и идет 
на ресурс `https://yandex.ru/maps` гугл карт, если при 
запуске был передан адрес для поиска то по нему и будет 
идти поиск местоположения, если параметра для поиска при 
запуске не передано, то адрес будет взят из буфера обмена.  

```python
    import webbrowser
    import sys
    import pyperclip
    from urllib import parse

    if len(sys.argv) > 1:
        address = ' '.join(sys.argv[1:])
    else:
        address = pyperclip.paste()

    address = parse.urlencode({'text': address})
    webbrowser.open('https://yandex.ru/maps/?' + address)
```

Можно самому выбирать в каком браузере открывать ресурс.

Данный пример открывает в chrome песню с youtube "сердце хана".
```python
    import webbrowser

    khan_heart_url = "https://www.youtube.com/watch?v=BhbsaGmd3EM&list=PLJwYC3yCHjKsqDQkLKb1yPQ96OX9PBYg6&index=14"
    webbrowser.get(using='google-chrome').open_new_tab(khan_heart_url)
```