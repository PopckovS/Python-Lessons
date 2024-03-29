Условие `if`, `elif`, `else`
---

Когда выполняется инструкция `if`, проверяется условие,
если условие истинно, тогда все инструкции в блоке `if`
выполняются. Но если условие оказывается неверным, 
тогда все инструкции внутри этого блока пропускаются.

```python
    if True:
        print('Вы это видите')
    if 0:
        print('то вы не увидите')

    # Вывод
    # Вы это видите
```

---

Условие `else` исполняется если блок `if` не проходит проверку на
истинность.

```python
    var = int(input('Введите число: '))
    if var >= 10:
        print('Число {0} больше или равно 10'.format(var))
    else:
        print('Число {0} меньше чем 10'.format(var))

    # Вывод
    
    # Введите число: 1
    # Число 1 меньше чем 10
    
    # Введите число: 10
    # Число 10 больше или равно 10

    # Введите число: 123
    # Число 123 больше или равно 10
```

---

Оператор `if-elif-else` — это альтернативное представление 
оператора `if-else`, которое позволяет проверять несколько 
условий, вместо того чтобы писать вложенные `if-else`.

```python
    score = int(input("Введите вашу оценку: "))

    if score >= 90:
        print("Отлично! Ваша оценка А")
    elif score >= 80:
        print("Здорово! Ваша оценка - B")
    elif score >= 70:
        print("Хорошо! Ваша оценка - C")
    elif score >= 60:
        print("Ваша оценка - D. Стоит повторить материал.")
    else:
        print("Вы не сдали экзамен")

    # Вывод
    # Введите вашу оценку: 100 
    # Отлично! Ваша оценка А
```



