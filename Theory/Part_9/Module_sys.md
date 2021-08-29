Модуль sys
---
---

Параметр `sys.executable`
---
Параметр `sys.executable` выводит полный путь к интерпретатору Python

```python
    import sys

    print('sys.executable = ', sys.executable)

    # Вывод
    
    # Через обынчный локальный интерпретатор
    # python3 2.py
    # sys.executable =  /var/www/Python-programm/venv/bin/python3

    # Через сшибанг в начале файла
    # ./2.py
    # sys.executable = /usr/bin/python3
```

---

Метод `sys.exit()`
---
Используется для выхода из программы, имеет необязательный атрибут 
в виде числа, где 0 это успешный выход, при его использовании вызывается
исключение типа `SystemExit` которое можно перехватывать.

[comment]: <> (`sys.getsizeof&#40;&#41;`)

[comment]: <> (Если требуется получить)

[comment]: <> (параметры из терминала sys.argv[1] это массив с параметрами)