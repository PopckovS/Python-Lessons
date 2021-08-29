Функция это все еще объект !
---

По скольку функция это все еще объект, мы можем присвоить этой
функции атрибуты класса, и по скольку класс этого объекта-функции
существует в не зависимости от объектов, тем самым мы создаем
статическое значение принадлежащее этой функции:

```python
def func(x):
    intermediate_var = x ** 2 + x + 1

    if intermediate_var % 2:
        y = intermediate_var ** 3
    else:
        y = intermediate_var ** 3 + 1

    # setting attributes here
    func.optional_return = intermediate_var
    func.is_awesome = 'Yes, my function is awesome.'

    return y

y = func(3)
print('Final answer is', y)

# Accessing function attributes
print('Show calculations -->', func.optional_return)
print('Is my function awesome? -->', func.is_awesome)

# Final answer is 2197
# Show calculations --> 13
# Is my function awesome? --> Yes, my function is awesome.
```
    
По началу функция не имеет атрибутов класса, но в процессе работы
мы устанавливаем этой функции атрибут класса, и теперь можем
обращаться к ней, устанавливать их можно как внутри функции, так
и с наружи.

Так образ можно к примеру сохранять предыдущие значения вычисления.

---

Возвращаемое Функцией значение
---
Если вывести что то в функции `print()` то оно будет напечатано, но 
если вывести `print()` в `print()` то ошибки не будет, а напечатано 
будет `None`

```python
print(print("123"))

# Вывод
# None
```

Это происходит по причини того что любая функция всегда возвращает 
какое либо значение, и если мы не определили это поведение при помощи
оператора `return` то функция всегда по стандарту возвращает `None`

---

Хорошая практика
---

Представим что создаем функцию которая должна сортировать приходящие
аргументы.

По скольку нам требуется чтобы было что сортировать, то нам
необходимо чтобы в функцию приходил хотя бы один аргумент, для
этого реализуем сразу `2` аргумента в функцию 
`def find_min(first, *args)` аргумент `first` обязательный аргумент
так что мы точно получим хотя бы `1` аргумент для сортировки, а
потом просто в условии цикла объединяем их в кортеж по которому
будем идти `(first, ) + args`

Таким образом мы обязуем передавать хотя бы `1` аргумент, и в то
же время работаем с ними как с единым кортежем. 

```python
import math

def find_min(first, *args, min_inf=-math.inf, max_inf=math.inf):
    result = max_inf
    for element in (first, ) + args:
        if element < result and min_inf < element < max_inf:
            result = element
    return max(result, min_inf)

print(find_min(88, 12, 13, -5, min_inf=0, max_inf=255))
print(find_min(12, 13, -5))

# Вывод
# 12
# -5
```