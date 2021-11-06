PostgreSQL, утилита pg_dump
---
---

Утилита `pg_dump` находится по пути `/usr/bin/pg_dump` и используется для 
создания дампов баз данных.


```
 pg_dump --host {HOST} --port {PORT} --username {UserName}
  --blobs --verbose --encoding utf-8 --schema-only 
  --file "{КудаВыгрузитьБД}.sql" "{ДатьНазвание}"
```
