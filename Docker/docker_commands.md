Docker команды
---
---


`--no-trunc` - параметр выводит информацию об изображениях и 
контейнерах в полной версии

Посмотреть все изображения

    docker images -a 

Посмотреть все контейнеры запущенные и незапущенные

    docker ps -a


Посмотреть запущенные контейнеры

    docker ps --no-trunc
    docker ps --no-trunc


Удаление всех контейнеров и изображений

    docker system prune -a

Запуск контейнера с названием "hello-world" с параметрами по 
умолчанию заданными в описании файлов настроек.

    docker run hello-world