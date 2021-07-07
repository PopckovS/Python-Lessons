Модуль os
---
---

os.path()
---
`os.path.basename` - вернет названия файла в этом пути, последнний файл:

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

`os.path.exists` - ворит о существовании файла или нет.

`os.path.isdir / os.path.isfile` - аналогичная проверка на существование.

`os.path.join` - совмещает пути при помощи разделителя в текущей операционной 
системе:

```python
    print(os.path.join(r'C:\Python27\Tools\pynche', 'ChipViewer.py'))

    # Вывод
    # C:\\Python27\\Tools\\pynche\\ChipViewer.py
```
---

Метод os.walk(dir)
---
Этот метод получает аргумент строку пути, сканирует все содержимое, и 
возвращает обьект генератор со всем содержимым, содержимое генератора
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
Если использовать символ `/` то получим списки всех путей на пк

---

`os.getcwd()` - Показать путь до текущей директории в которой запущен файл.

