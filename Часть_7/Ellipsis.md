Ellipsis
---
Это спец константа в питоне, состоит из трех многоточий `...` она имеет 
несколько применений:

1) Плейсхолдер как замена оператора `pass`

```python
    def func1():
        print('Внутреняя функция func1')
        pass

    def func2():
        print('Внутреняя функция func2')
        ...

    func1()
    func2()   
```

2) Второй способ это отсутствие каких либо аргументов вабще, None это тоже аргумент.
   
```python
        def original_num(m=...):
            if m is ...:
                print('Было передано ...')
            if m is None:        
                print('Было передано None')
            if instance(m, int) :
                print('Было передано int')

        original_num()

        # Вывод
        # print('Было передано ...')
```