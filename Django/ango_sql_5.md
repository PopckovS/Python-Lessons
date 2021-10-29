Приставки в выборке данных из Модели
---

[Почитать про приставки тут](https://djangodoc.ru/3.1/ref/models/querysets/#field-lookups)

Используя метод `objects.filter()` жно проводить поиск набора
объектов, для использования фильтра существуют специальные
приставки к полям по которым будет вестись поиск.

Приставки к полям, по которым ведется поиск записей в 
таблице, используются для уточнения запроса, у таких приставок
используется `__` двойное подчеркивание перед приставкой. 

Приставка `__lt`
---

`__lt` - приставка эквивалентная применению `<` (меньше)

```python
Entry.objects.filter(pub_date__lt='2006-01-01')
```
Превращается в следующий SQL запрос
```sql
SELECT * FROM blog_entry WHERE pub_date < '2006-01-01';
```

---

Приставка `__lte`
---
`__lte` - приставка эквивалентная применению `<=` 
(меньше, равно)

```python
Entry.objects.filter(pub_date__lte='2006-01-01')
```
Превращается в следующий SQL запрос
```sql
SELECT * FROM blog_entry WHERE pub_date <= '2006-01-01';
```

---

Приставка `__exact`
---
`__exact` - поиск с точным совпадение

```python
Entry.objects.get(headline__exact="Cat bites dog")
```
Превратится в 
```sql
SELECT ... WHERE headline = 'Cat bites dog';
```

Если вы не указали тип поиска, то есть если ваш аргумент
ключевого слова не содержит двойного подчеркивания, 
предполагается, что это тип поиска exact

Например, следующие два оператора эквивалентны:

```python
Blog.objects.get(id__exact=14)  # Explicit form
Blog.objects.get(id=14)         # __exact is implied
```

---

Приставка `__iexact`
---

`__iexact` - Соответствие без учета регистра. Итак, запрос:

```python
Blog.objects.get(name__iexact="beatles blog")
```

То есть подойдут все следующие записи:

    "Beatles Blog"
    "beatles blog" 
    "BeAtlES blOG"

---

Приставка `contains`
---

`contains` - Проверка на сдерживание с учетом регистра. 

Например:

```python
Entry.objects.get(headline__contains='Lennon')
```

Примерно переводится на этот SQL:

```sql
SELECT ... WHERE headline LIKE '%Lennon%';
```

Найдет `Today Lennon honored` но не найдет `today lennon honored`

---

Приставка `__icontains`
---

`__icontains` - тоже что и `contains` но не чувствительный к 
регистру

---

Приставка `__gt`
---

`__gt` - Больше чем, эквивалентно `>`

```python
Entry.objects.filter(id__gt=4)
```
Эквивалент SQL:
```sql
SELECT ... WHERE id > 4;
```

---

Приставка `__gte`
---

`__gte` - Больше чем равно, эквивалентно `>=`

```python
Entry.objects.filter(id__gte=4)
```
Эквивалент SQL:
```sql
SELECT ... WHERE id >= 4;
```

---

Приставка `__startswith`
---

`__startswith` - Начинается с (с учетом регистра).

```python
Entry.objects.filter(headline__startswith='Lennon')
```

Эквивалент SQL:

```sql
SELECT ... WHERE headline LIKE 'Lennon%';
```

---

Приставка __istartswith`
---

`__istartswith` - Тоже самое что и `__istartswith` но 
(без учета регистра).

---

Приставка `__endswith`
---

`__endswith` - Заканчивается на (с учетом регистра)

---

Приставка `__iendswith`

`__iendswith` - Заканчивается на (без учета регистра).
