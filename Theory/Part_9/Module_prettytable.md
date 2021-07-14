Модуль prettytable
---
---
Данный модуль создает красивые таблицы в терминале.

Установка:

    pip3 install prettytable

Использование:

```python
    from prettytable import PrettyTable

    # Создаем экземпляр таблицы
    table = PrettyTable()
    
    # Задаем колонки
    table.field_names = ['Names', 'Age', 'City']
    
    # Создаем строчки
    table.add_row(["Алекс", 20, "Москва"])
    table.add_row(["Боб", 25, "Москва"])
    table.add_row(["Саша", 30, "Минск"])
    table.add_row(["Петя", 23, "Киев"])
    table.add_row(["Вася", 67, "Москва"])

    # Выравнивание по краю
    table.align = 'l'
    
    # Сортировка схожая с ORDER BY в SQL
    table.sortby = "Age"
    
    # Вывод на экран
    print(table)

    # Вывод таблицы в терминале
    # 
    # +-------+-----+--------+
    # | Names | Age | City   |
    # +-------+-----+--------+
    # | Алекс | 20  | Москва |
    # | Петя  | 23  | Киев   |
    # | Боб   | 25  | Москва |
    # | Саша  | 30  | Минск  |
    # | Вася  | 67  | Москва |
    # +-------+-----+--------+
```

