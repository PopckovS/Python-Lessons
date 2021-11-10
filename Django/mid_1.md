Промежуточное ПО `middleware`
---
---
Промежуточное ПО - это специальная структура для перехвата запросов/ответов в
Django, это глобальная система которая перехватывает и обрабатывает, изменяет 
и передает его дальше по стандартному ходу.

`middleware` -  работает функционально, где каждый компонент 
обрабатывает определенное поведение. К примеру `AuthenticationMiddleware`
производит связываение пользователя с запросом, таким образом мы можем иметь
доступ к `request.user` в видах.

`middleware` обрабатывается перед и после работы запроса, подобно тому как
сигналы обрабатываются для модели.

---

Модули `middleware` подключается в `settings.py` в списке настроек `MIDDLEWARE`

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    
    # Управление сессиями между запросами
    'django.contrib.sessions.middleware.SessionMiddleware',
    
    # Запрет user-agent, нормализация url, назначение длины запроса
    'django.middleware.common.CommonMiddleware',

    # Обработка Csrf для работы с формами 
    'django.middleware.csrf.CsrfViewMiddleware',
    
    # Связывание пользователей с запросами используя сессии
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```









