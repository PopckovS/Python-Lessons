Модуль requests
---
---
`requests` - модуль для работы с HTTP запросами, 
отправлять `GET` и `POST` запросы.

Установка :
    
    pip3 install requests 

Если используем виртуальную среду :

    pipenv install requests

Можно посмотреть на различные данные пришедшие с 
ответом, `encoding` - кодировка ответа, статус код
`status_code` (200 / 400 ...), `cookies` можно 
посмотреть куки `cookies`, был ли редирект с того 
ресурса, на который делали запрос `is_redirect`,
`elapsed` время прошедшее с момента отправки и 
получения ответа, `url` с которого пришел ответ,
может отличатся за счет редиректа, 

```python
    url = "http://xakep.ru"
    response = requests.get(url)

    print('encoding = ', response.encoding) 
    print('status_code = ', response.status_code)
    print('cookies = ', response.cookies)
    print('is_redirect = ', response.is_redirect)
    print('elapsed = ', response.elapsed)
    print('url = ', response.url)
    print('history = ', response.history)
    
    # Вывод
    # encoding =  UTF-8
    # status_code =  200
    # cookies =  <RequestsCookieJar[]>
    # is_redirect =  False
    # elapsed =  0:00:00.573094
    # url =  https://xakep.ru/
    # history =  [<Response [301]>]
```

 `headers` - Можно увидеть все заголовки пришедшие от 
сервера.

```python
    url = "http://xakep.ru"
    response = requests.get(url)

    print(response.headers)

    # Вывод
    # { 'Server': 'QRATOR', 
    #  'Date': 'Fri, 16 Jul 2021 02:34:37 GMT', 
    #  'Content-Type': 'text/html; charset=UTF-8',
    #  'Content-Length': '26772',
    #  'Connection': 'keep-alive',
    #  'Link': '<https://xakep.ru/wp-json/>;
    #  ...
    # }
```
