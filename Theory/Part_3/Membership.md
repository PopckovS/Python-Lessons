Операторы принадлежности `in`, `not in`
---
---

Эти операторы проверяют, является ли значение частью 
последовательности, возвращает True / False. 

```python
    list_str = ['ferret', 'cat', 'dog']

    print('list_str = ', list_str)
    print('"fox" in list_str = ', 'fox' in list_str)
    print('"dog" in list_str = ', 'dog' in list_str)

    # Вывод
    # list_str =  ['ferret', 'cat', 'dog']
    # "fox" in list_str =  False
    # "dog" in list_str =  True
```

В python строки это последовательности элементов, как и
списки, так что можно проверять наличие подстроки в строке,
при помощи оператора `in`

```python
    print('me' in 'disappointment')
    
    # Вывод
    # True
```



