Тип данных `Boolean`
---
---
`Boolean` - класс, что наследуется от типа `int`

Принимает только 2 возможных значения `True / False` 

На удивление занимает больше места чем можно себе представить, 
занимает `28 байт`, из-за того что в питоне все является объектом,
и на каждый объект ведется подсчет ссылок, и для самих ссылок 
требуется место, да еще и каждый объект реализует массу магических
методов, да и наследуется от главного объекта `object`, по итогу
он занимает `28 байт`.

`Boolean` может использоваться как результат сравнения, даже без 
использования оператора `if`

```python
    a = 'qwe'
    b = 'qwe'
    d = 'fgs'
    
    c = a == b
    g = a == d 
    
    print(c)

    # Вывод 
    # True
    # False
```
