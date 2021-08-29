None
---
---

None - это класс у которого реализован паттерн `singlton`, так что 
есть только один `None` все программы, и его проверка на самого
себя вернет `True` 
 
```python
    print('Проверка по значнеию None == None', None == None)
    print('Проверка по ссылке None == None', None is None)

    # Вывод
    # True
    # True
```

Тип данных `None` занимает `16 байт`, является классом и реализует 
паттерн `singlton`

```python
    import sys
    
    var = None
    
    memory = sys.getsizeof(var)
    
    print(var.__sizeof__())
    print(memory)
    
    # Вывод
    # 16
    # 16
```
