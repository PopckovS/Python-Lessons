Кортежи - `tuple` 
---

Кортежи по сути полностью идентичен спискам, тоже являются 
последовательностями, главное их отличие это неизменяемость.

Определение такое же как и у списков, но через круглые скобки:

```python
    my_tuple = (1, "hello", 3.14)
```
    
Доступ к элементам происходит по индексу как и у списков:

```python
    print(my_tuple[0])

    # Вывод
    # 1
```

Поддерживают 2 способа создания кортежей, как с обозначением 
скобок, так и без них.

```python
    my_tuple1 = (1, 3.14, "Hello World!")
    my_tuple2 = 1, 1, "one", "one", "one", "two", 3
```

---

Методы кортежей
---

1) `my_tuple.index()` - Принимает значение и возвращает индекс по 
   которому оно находится в кортеже. 

```python
    my_tuple = (1, 3.14, "Hello World!")
    
    print('index of 3.14 = ', my_tuple.index(3.14))
    print('index of "Hello World!" = ', my_tuple.index("Hello World!"))
    
    # index of 3.14 =  1
    # index of "Hello World!" =  2
```

2) `my_tuple.count()` - Принимает значение и возвращает количество
    раз которое это значение содержится в кортеже.

```python
    my_tuple = (1, 3.14, 1, 34, 1, "Hello World!")
    
    print('count of number 1 = ', my_tuple.count(1))
    
    # count of number 1 =  3
```