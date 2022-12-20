Логирование
---

[Документация логирования](https://djangodoc.ru/3.2/topics/logging/)

У самого языка `Python` есть свой собственный встроенный модуль для
логирования `logging`

Пример работы
```python
import logging

logger = logging.getLogger('logger_for_debug')

def some_function():
    if False:
        logger.error('Ошибка ...')
```

`logging.getLogger()` - получает или если не существовало ранее, создает 
экземпляр регистратора для логирования сообщений, имя регистратора будет 
его уникальным идентификатором.

Виды логирования:

- `logger.debug()`
- `logger.info()`
- `logger.warning()`
- `logger.error()`
- `logger.critical()`

---
Ведение журнала для логирования.

Настроить журнал ведения логирования можно по разному, чаще используют
способ через словарь `LOGGING`. 

`LOGGING` - словарь с параметрами который будет описывать как вести журнал
логирования, фильтры и средства форматирования для ведения логов.

Настройки `settings.py` с параметрами `LOGGING` для ведения журнала:
```python
import os

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
    },
}
```

---
Запись логов в файл
---

Записываем результаты логирования в файл, с очищением перед каждым сеансом.

```python
import logging

logging.basicConfig(filemode='w',
                    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
                    level=logging.INFO,
                    filename='logging.log'
                    )
