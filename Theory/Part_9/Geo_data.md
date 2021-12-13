API для получения Гео-данных
---
---
Существует несколько специальных сервисов для получения гео-данных
по адресу или координатам долготы и широты.

---
Yandex geocoder API
---
Для работы требуется зарегистрировать почту на `Yandex`, после в 
разделе для разработчиков по адресу 
[Yandex Services](https://developer.tech.yandex.ru/services/)
потребуется подключить сервис **JavaScript API и HTTP Геокодер**
после процесса регистрации, будет сгенерирован ключ API

Библиотека на PyPi

    https://pypi.org/project/yandex-geocoder/

Yandex geocoder API хорошо парсит адреса но дает только `1000` запросов
в день, больше только платно.

---
OSM OpenStreetMap API
---

Сам OSM это открытый API, не требует регистрации и секретных ключей. 

Для работы с ним можно использовать библиотеку `geocoder` которую
можно найти на [PyPi](https://pypi.org/project/geocoder/)

```python
import geocoder

geo = geocoder.osm('Адресс тут')

print('lat = ', geo.json['lat'])
print('lng = ', geo.json['lng'])
```

OSM позволяет делать сколь угодно много запросов, но плохо парсит адреса.

---
DaData API
---
Сервис [DaData](https://dadata.ru/) дает услуги по геокодированию, 
и многое другое, для работы потребуется регистрация, предоставляет
2 секретных ключа, для работы потребуются оба.

Установка модуля для работы с [DaData](https://github.com/hflabs/dadata-py)

ример работы с сервисом
```python
from dadata import Dadata

api_key = "api ключ"
secret_key = "секретный ключ"

dadata = Dadata(api_key, secret_key)
result = dadata.clean(name="address", source="москва сухонская 11")

print('lat = ', result['geo_lat'])
print('lng = ', result['geo_lon'])
```

Позволяет использовать `10 000` бесплатных запросов в день, под ккапотом
использует тот же сервис OSM, но берет на себя нагрузу по парсингу адреса 
из строки, определяет адреса так же хорошо как и `Yandex geocoder API`
