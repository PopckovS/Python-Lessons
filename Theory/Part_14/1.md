TimescaleDB в Ubuntu
---
---

[Почитать про это](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-timescaledb-on-ubuntu-18-04-ru)

`timescaledb` - база данных с открытым исходным кодом, 
оптимизированная для хранения данных временного ряда. 
Она реализуется как расширение PostgreSQL и сочетает в себе
удобство реляционных баз данных и быстродействие баз данных NoSQL. 
Таким образом, она позволяет использовать PostgreSQL 
для хранения бизнес-данных и данных временного ряда в одном месте.

С начала устанавливает репозиторий в саму ОС

```
sudo add-apt-repository ppa:timescale/timescaledb-ppa

sudo apt update

sudo apt install timescaledb-postgresql-10
```

---

Для того что бы `timescaledb` можно было установить в postgreSQL
как расширение, потребуется отредактировать файл с настройками 
`postgresql.conf`

Проходим по пути, где находится файл настроек для конкретной версии 
`postgresql`

```
/etc/postgresql/10/main/postgresql.conf
```

Редактируем файл

```
sudo nano postgresql.conf
```

Меняем настройки

```
# заменяем эту настройку
shared_preload_libraries = ''             # (change requires restart)

# указывая timescaledb
shared_preload_libraries = 'timescaledb'  # (change requires restart)
```

Далее перезагружаем сервис `postgresql`

```
sudo service postgresql restart
```

После этого `timescaledb` станет доступным в списке расширений постгресса
