Модуль pyshorteners
---
---

`pyshorteners` - модуль создает короткие ссылки на ресурс.

Установка :
    
    pip3 install pyshorteners

Пример :
```python
    import pyshorteners

    # Создали обьет
    pyshort = pyshorteners.Shortener()
    
    # Полная сылка и коротка 
    full_url = 'https://www.youtube.com/watch?v=pbMLW0nRvZY&list=RDMMpbMLW0nRvZY&start_radio=1'
    short_url = pyshort.tinyurl.short(full_url)
    
    print('Полная ссылка = ', full_url)
    print("Сокращенная ссылка - ", short_url)

    # Вывод
    # Полная ссылка =  https://www.youtube.com/watch?v=pbMLW0nRvZY&list=RDMMpbMLW0nRvZY&start_radio=1
    # Сокращенная ссылка -  https://tinyurl.com/yjzz49rt
```