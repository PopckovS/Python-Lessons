Метод range(start, end, step)
---
---

Метод `range()` создает не список а особый обьект, по которому можно 
итерироваться при помощи цикла `for` но списком не является, и
для преврващение в список требуется указать это явно:

```python
    some = range(1, 11)
    print(some)
    print(type(some))

    my_list = list(some)
    print(my_list)
    print(type(my_list))

    # Вывод
    # range(1, 11)
    # <class 'range'>
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # <class 'list'>
```
