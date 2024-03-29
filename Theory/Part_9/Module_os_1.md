Модуль os
---
`os` - Это модуль для работы с операционной системой, работа
с файловой структурой, директориями.  


---
Модуль `os.path()`
---
`os.path.basename` - вернет названия файла в этом пути, последний
файл:

```python
    print(os.path.basename(r'C:\Python27\Tools\pynche\ChipViewer.py'))
    
    # Вывод
    # ChipViewer.py
```
    
`os.path.dirname` - вернет все до последнего файла:

```python
    print( os.path.dirname(r'C:\Python27\Tools\pynche\ChipViewer.py') )
    
    # Вывод
    # C:\\Python27\\Tools\\pynche
```

`os.path.exists` - говорит о существовании файла или нет.

`os.path.isdir / os.path.isfile` - аналогичная проверка на
существование.

`os.path.join` - совмещает пути при помощи разделителя в 
текущей операционной системе:

```python
    print(os.path.join(r'C:\Python27\Tools\pynche', 'ChipViewer.py'))

    # Вывод
    # C:\\Python27\\Tools\\pynche\\ChipViewer.py
```
---

Метод `os.walk(dir)`
---
Этот метод получает аргумент, строку пути, сканирует все содержимое, и 
возвращает объект генератор со всем содержимым, содержимое генератора
имеет структуру:

    ('Корень директории', [Список со всеми под директориями], [список файлов])

Пройдемся по генератору циклом for: 


```python
    test_dir = 'test-dir'
    gener = os.walk(test_dir)

    for root, dirs, files in gener:
        print(root, dirs, files)

    # Вывод
    # test-dir ['test-dir-2'] ['test.txt']
    # test-dir/test-dir-2 [] ['test-2.txt']
```
Или методом `next()`:

```python
    test_dir = 'test-dir'
    gener = os.walk(test_dir)

    print(next(gener))
    print(next(gener))

    # Вывод
    # ('test-dir', ['test-dir-2'], ['test.txt'])
    # ('test-dir/test-dir-2', [], ['test-2.txt'])
```
Если использовать символ `/` то получим списки всех путей со всеми
файлами во всей системе, это займет много времени, и заняло бы много
памяти, если это была бы обычная структура, но это генератор и по
этому он ест меньше памяти.

---

`os.getcwd()` - Показать путь до текущей директории в которой 
запущен файл.

---

`os.pardir`

---

`os.listdir` - Она показывает все содержимое каталога, если команда
`os.walk()` возвращает все содержимое до дна рекурсивно, то данная
команда выводит список только одной директории.

---

Удалить файл можно 2 способами
---

1) `os.remove('try.py')`
   
2) `os.unlink('try.py')`

---

Получить директорию текущего пользователя 
---
Сделать это можно 2 путями:

```python
    os.getenv('HOME')
    os.path.expanduser('~')

    # Вывод для обычного пользователя:
    # /home/serg
    # /home/serg

    # Если речь идет о суперпользователе, то вывод будет таким:
    # /root
```

---
`os.fork()` - ???

---
`os.system("shutdown -s")` - Выключение компьютера.
