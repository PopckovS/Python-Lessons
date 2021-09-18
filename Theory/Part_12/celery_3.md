Celery
---
Когда чам сервер Django запущен, для того чтобы Celery мог 
запускать задачи асинхронно, мы должны запустить его сервер,
сделать это можно следующей командой:

    # Обычный запуск
    celery -A project-name worker -l INFO

    # Запуск с просмотром логов
    celery -A project-name worker -l debug

При указании `project-name` мы указываем тот пакет, в котором 
находится наше Celery приложение, тот модуль где находится
`__init__` и файл `celery.py` в котором обьявляется наше 
приложение `Celery`

---

При запуске мы получим сообщение следующего вида:

```
 -------------- celery@serg-pk v5.1.2 (sun-harmonics)
--- ***** ----- 
-- ******* ---- Linux-5.4.0-84-generic-x86_64-with-glibc2.27 2021-09-18 19:58:03
- *** --- * --- 
- ** ---------- [config]
- ** ---------- .> app:         main:0x7f48f6903550
- ** ---------- .> transport:   redis://127.0.0.1:6379/0
- ** ---------- .> results:     redis://127.0.0.1:6379/0
- *** --- * --- .> concurrency: 4 (prefork)
-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
--- ***** ----- 
 -------------- [queues]
                .> celery           exchange=celery(direct) key=celery
```
Тут указано `transport` это наш брокер сообщений, `results` это
наш бэкэнд результатов.
