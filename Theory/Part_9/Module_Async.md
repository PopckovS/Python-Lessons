Python Асинхронность - Часть 1
---

Существует 3 способа делать что-либо асинхронно:

1) Отдельный процесс
2) Отдельный поток
3) Асинхронный код

---

Отдельный процесс
---
Это именно отдельный процесс выполнения программы, разные процессы
хорошо работают в Linux.

---

**Отдельный процесс - хорошо**

Он использует все ресурсы ОС, он изолирован от других процессов, и они
могут выполняться по-настоящему параллельно.

---

**Отдельный процесс - плохо**

У разных процессов нет разделяемых переменных, они полностью изолированы 
друг от друга, если мы делаем что то одно, то разным процессам требуется 
синхронизация друг с другом, и они очень затратны, по скольку это отдел 
программа для них берется свои собственные участки памяти, и для каждого 
отдел процесса берется свой интерпретатор, и зависят от количества ядер.

---

**Где использовать отдел процессы**

1) Обработка изображений
2) Обработка больших массивы данных в DS
3) Обработка матриц

Для работы используется модуль `multiprocessing` его класс `Pool`
для создания разных процессов.

---

Отдельный поток
---
Хорошо работают в винде, все потоки работают последовательно,
просто передают управление от потока в поток.

---

**Отдельный потоки - хорошо**

1) Имеют общую память за счет того что запускаются в одном процессе
2) Общие переменные
3) Не требуют много память
4) Хорошо подходят для операций с сетью, делать запросы к серверам.

---

**Отдельный потоки - плохо**
1) У отдела потоков есть GIL -
2) Нельзя использовать CPU-bound функции - то есть если есть какие-то
долгие сложные и вычисления, то из-за вмешательства GIL в разных
потоках они будут работать т дольше чем просто последовательно.
4) Код не тривиален.
5) В работе нескольких потоках сразу могут возникать конфликты потоков.

---

**Где использовать отдел потоки**
1) Работа с сетью

Для работы есть модуль `threading`

---

Асинхронность
---
Асинхронный код умеет работать в одном процессе и в одном потоке, для 
асинхронного кода требуется 2 вещи:

1) Функции, что умеют засыпать и просыпаться в нужное время по 
команде.
2) Также требуется диспетчер, в асинхронном коде он называется 
Event Loop. этот диспетчер принимает асинхронном функции, решает
какой из них исполнятся и передает управление следующей функции.

---

**Асинхронность - хорошо**
1) Выполняется в одном процессе и одном потоке
2) Малое потребление ресурсов
3) Независим от ОС

---

**Асинхронность - плохо**
1) Сложность отладки
2) Исключение можно поймать только в внутри асинхронной функции
3) Сложно понять в каком контексте происходит работа
4) Сложно читаемый код
5) Легко допустить ошибку

Есть 2 библиотеки для работы с асинхронностью `asyncIo` `gevent`

---

**Корутины (Сопрограммы)**

Корутина (специализированная функция-генератор) - является основой для 
асинхронного программирования

---

**Суть Асинхронности**

Многопроцессорность - означает распараллеливание работы между частями 
центрально вычислительной системой, между процессорами и ядрами.

Многопоточность - суть в том что задача разбивается на множество 
потоков, занимающихся её решением, один процесс может содержать в 
себе множество потоков. Она прекрасно решает задачи связанные с 
вводом/выводом (IO)

В интерпретатор Cpython введен новый тип работы, при помощи 2 ключевых 
слов async и await. Подобная асинхронность тоже есть в других языках
как Go, C# и Scala.

Модуль asyncio - поддерживает одновременное выполнение задачи, но он не 
использует ни многопроцессорность ни многопоточность. Он использует 
один процесс один поток, и называет это **кооперативная многозадачность.**

Асинхронность позволяет ставить работу части программы на паузу при
помощи диспетчера Event Loop и передавать работу другой части 
программы, в этом асинхронность похожа больше на многопоточность,
которая тоже работает с перерывами, так асинхронность и многопоточность
выражают философию борьбы между своими потоками/асинх.функциями в то
время как многопроцессорность именно параллели процесс работы.

---

**Кооперативная многозадачность** - можно объяснить так, это один 
цикл который работает со множеством заданий, давая им оптимальное
время на работу.

Асинхронность удобна когда есть периоды ожидания, которые бы тратили 
время в пустую при синхронном выполнении.

---

Python Асинхронность - Часть 2
---

Материал - https://realpython.com/python-concurrency/

---

**Корутины** 

Сердце асинхронного программирования - это корутины. Корутины - это 
специальная версия функций-генераторов в Python.

Корутина это функция которая перед возвращением значения может прервать 
свое выполнение и передать контроль другой корутине.

---

Модуль AsyncIO await/async

Библиотека asyncio пользует 2 ключ слова await/async. Вот пример реализации:

```python
    import asyncio, time

    async def counter():
        print('one')
        await asyncio.sleep(1)
        print('two')

    async def main():
        await asyncio.gather(counter(), counter(), counter())

    time_1 = time.perf_counter()
    asyncio.run(main())
    time_2 = time.perf_counter()
    time_final = time_2 - time_1
    print(f'Время выполнения программы: {time_final:0.5f}')

    # Вывод
    # one
    # one
    # one
    # two
    # two
    # two
    # Время выполнения программы: 1.00132
```

И так в чем тут суть, если мы используем обычный `time.sleep(1)` он просто 
заблокирует выполнение, как бы имитируя сложную долгую обработку сервиса, 
в то время как `asyncio.sleep(1)` тоже имитирует долгую обработку, но на 
момент этого ожидания программа не ожидает, а переходит к выполнению 
другой функции корутины.

В такие моменты программа только ожидает выполнение и ничего не делает, и 
в этот самый момент времени мы и экономим, так образ достигаем илюзии 
параллельной работы, действительности это своего рода простая оптимизация.

---

Правила работы с асинхронным кодом

`async def` - называется естественной корутиной или асинхронным генератором.
Также есть и другие механизмы этого спец слова `async with` и `async for`
и они тоже работают, для своих целей.

`await` - Ключевое слово указывает функции что она будет отдавать контроль 
обратно в главный цикл работы, этот главный цикл в свою очередь содержит 
порядок выполнения всех зарегистрированных корутин.

Функция помеченная как `async def` может использовать одно из 
`await return yield`. await можно использовать только в теле самой 
корутины.

Для того чтобы пометить как `await` этот обьект должен быть `awaitable`
для этого это должна быть либо просто функция или обьект реализующий 
метод `__await__`

---

Python Асинхронность - Часть 3
---
---

Socket в JS
---

WebSocket — протокол связи поверх TCP-соединения, предназначенный для обмена
сообщениями между браузером и веб-сервером в режиме реального времени.

**Говоря о JavaScript**

В js есть 2 механизма для работы в живом времени, это Веб-сокеты и Socket.IO.

**Веб-сокеты** - стандартный вариант, открывает TCP-соединение, держит его 
открытым передавая информацию в реальном времени, их стоит использовать 
в след случаях:

1) Чаты
2) Многопользовательские игры
3) Совместное редактирование
4) Социальные (новостные) ленты
5) Приложения, работающие на основе местоположения
6) Торговые площадки,

**Socket.IO** — библиотека JavaScript, основанная (написанная поверх) на 
веб-сокетах,  использует веб соккеты если они доступны, или другием методы 
типа: Flash Socket, AJAX Long Polling, AJAX Multipart Stream

Эта библиотека удобнее в использовании, к примеру может сразу отправлять 
сообщение всем участникам сразу, при использовании веб-сокетов, для реализации 
подобной задачи вам потребуется список подключенных клиентов и отправка 
сообщений по одному. 

---

Socket в Python

Модуль `socket` для общения между клиентом и сервером, в качестве
клиента может выступать и другой сервер, создаем класс для работы
с сокетами:

**Общее**

`socket.socket(socket.AF_INET, socket.SOCK_STREAM)` - Создание сокета.

**Для Сервера**

`sock.bind((HOST_ALL, PORT))` - Сервер принимает соединение от клиента.

`sock.listen(5)` - Количество клиентов для связи.

`connection, addres = sock.accept()` - создание соединения.

Цикл получения и ответа на сообщение от клиента.

```python
    while True:
        data = connection.recv(1024)
        if not data:
            break
        print(f'Получено от клиента: {data.decode()}')
        message = 'Ответ от сервера'
        connection.send(message.encode())
```

**Для Клиента**

Соединение клиента с сервером:

```python
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    
    message = input('Ваше сообщение серверу: ')
    sock.send(message.encode())
    
    data = sock.recv(1024)
    print(f'Пришло от сервера: {data.decode()}')
```

**Общее**

`connection.shutdown(1); connection.close()` - закрываем соединение
