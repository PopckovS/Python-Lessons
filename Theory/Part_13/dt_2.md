Библиотека `arrow`
---
---

[Репозиторий библиотеки `arrow`](https://github.com/arrow-py/arrow)

Это удобная библиотека для работы с датой/временем.

Установка:

    pip install arrow

Создать дату/время можно стандартным методом `arrow.get()` можно создавать
дату/время как из строки, так и из обьекта дата/время стандартной библиотеки
`python`

Создав дату/время можем удобно привести ее к временной зоне методом `to()`

Получить дату, время, дату/время обьекта `arrow` можно с помощью специальных
методов `time()`, `date()`, `datetime()`

Создаем дату/время и приводим ее к временным зонам, и получаем их `время`, 
`дату` и `дату/время`
```python
import arrow
import datetime

# временные зоны
TIME_ZONE_1 = 'Europe/Moscow'
TIME_ZONE_2 = 'Asia/Kolkata'

# создание обьектов даты/время
dt_1 = arrow.get('2013-05-11T21:23:58.970460+07:00')

dt_2 = arrow.get(
    datetime.datetime(2021, 10, 10, 7, 7, 7)
)

# задаем временную зону для обьектов даты/время
dt_1.to(TIME_ZONE_1)
dt_2.to(TIME_ZONE_2)

dt_1.time()
dt_1.date()
dt_1.datetime()
```

