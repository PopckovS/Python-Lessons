Модуль `datetime` самого `python`
---
---

---
Модуль `timedelta`. Складываем и отнимаем дату/время
---

Подмодуль `timedelta` модуля `datetime` можно использовать для сложения 
и вычитания даты и времени. 

```python
import datetime

# создаем дату/время
my_date = datetime.date(2021, 10, 10)

# отнимаем от нее один день
my_date = my_date + datetime.timedelta(days=1)
```


---
Временные зоны `UTC` и `DTC`
---


---
Задать временную зону
---

Задаем временную зону для даты/времени

```python
import datetime
import pytz

TIME_ZONE = 'Europe/Moscow'

# создаем временную зону
time_zone = pytz.timezone(TIME_ZONE)

# переводим дату/время в заданную временную зону
dt = datetime.datetime(2021, 1, 10, 10, 0, 0, tzinfo=time_zone)
```

---
Скомбинировать дата + время = дата/время
---

Создать обьект дата/время из разрозненных частей даты и времени можно
с помощью стандартного метода `combine` модуля `datetime`

```python
import datetime

# создаем дату и время по отдельности
my_date = datetime.date(2021, 10, 10)
my_time = datetime.time(10, 10, 10)

# создаем дату/время из разрозненных частей
datetime.datetime.combine(my_date, my_time)
```

