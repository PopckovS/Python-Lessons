Модуль `pyperclip` 
---
---

`pyperclip` - управляет буфером обмена, теми данными что 
сохраняются в момент копирования `Ctrl+C`

Данный модуль предназначен для работы со строчками, если
в буфер обмен будет скопирован файл, то `pyperclip` вернет 
полный путь к этому файлу от корня файловой системы.

Для установки, потребуется установить ряд 
дополнительных пакетов.

    sudo apt-get install xsel
    sudo apt-get install xclip
    pip3 install gtk
    pip3 install pyperclip

Имеется 2 метода:

1) `paste()` - получает данные из буфера. 
2) `copy()` - вносит данные в буфер.

Пример использования, при условии, что перед запуском мы
скопировали файл по пути `/var/www/python-script/main.py`

```python
    import pyperclip

    buffer_data = pyperclip.paste()
    
    print('pyperclip.paste() = ', buffer_data)

    print('С помощью метода pyperclip.copy() вносим данные')
    
    buffer_data = "Эти данные внесены в Буфер обмена."

    pyperclip.copy(buffer_data)

    # Вывод
    # pyperclip.paste() =  /var/www/python-script/main.py
    # С помощью метода pyperclip.copy() вносим данные
```