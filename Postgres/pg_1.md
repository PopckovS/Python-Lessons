Смена пароля пользователя для Postgres
---

Входим в postgres как суперпользователь

    sudo -u postgres psql

Меняем пароль для пользователя

    ALTER USER postgres PASSWORD '<new-password>';

Меняем настройки доступа в файле с настройками для постгресса, он 
находится по пути
`/etc/postgresql/<postgres_version>/main/pg_hba.conf`

Меняем доступ с `peer`

    local   all         all                  peer

на доступ типа `md5`

    local   all         all                  md5

Перезагружаем сервис постгресса

     sudo service postgresql restart
