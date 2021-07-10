Python-programm
---

Сборник теории и решения практических упражнений по python-3.8.

[Ссылки на полезный материал.](links.md)

[Вопросики.](questions.md)

---

Теория :
---
 
1.  **Часть №1. Основное :**

    - [Основы Python](Part_1_1/Base.md )
    - [Разница версий и строки Unicod](Part_1/Version_difference.md )
    - [Области видимости LEGB](Part_1/Scopes_LEGB.md)
    - [Память в Си и память в Pyhton](Part_1/Memory_C_Python.md)
    - [Механизм управления памятью Pymalloc](Part_1/Memory_Pymalloc.md )
    - [Сборщик мусора](Part_1/Garbage_collector.md )
    - [Интерактивный режим REPL](Part_1/Interactive_mode_REPL.md )
    - [Аннотации методов аргументов](Part_1/Annotations.md )


2. **Часть №2. Типы данных в Python :**

    - [Типы данных](Part_2/Data_types.md)
    - [Boolean](Part_2/Boolean.md)
    - [Int и Float](Part_2/Integer_float.md)
    - [String](Part_2/String.md)
    - [None](Part_2/None.md)
    - [Списки - list](Part_2/List.md)
    - [Словарь - dict](Part_2/Dict.md)
    - [Множества - set, frozenset](Part_2/set.md )
    - [Кортеж - tuple](Part_2/Tuple.md)


3. **Часть №3. Операторы :**
    - [Арифметические операторы](Part_3/Arithmetic.py) (`+`, `-`, `*`, `/`, `//`, `%`, `**`)
    - [Побитовые Операторы](Part_3/Bitwise.py) (`&`, `|`, `^`, `>>`, `<<`, `~`)
    - [Операторы присваивания](Part_3/Assigment.py) (`=`, `+=`, `-=`, `/=`, `//=` etc.)
    - [Оператор сравнения](Part_3/Comparison.py) (`==`, `!=`, `>`, `<`, `>=`, `<=`)
    - [Логические операторы ](Part_3/Logical.py) (`and`, `or`, `not`)
    - [Операторы идентичности](Part_3/Identity.py) (`is`, `is not`)
    - [Операторы членства](Part_3/Membership.py) (`in`, `not in`)


4. **Часть №4. Потоки управления :**
    - [The `if` statement](Part_4/If_else.py)
    - [The `for` statement](Part_4/For.py) (and `range()` function)
    - [The `while` statement](Part_4/While.py)
    - [The `try` statements](Part_4/Try.py)
    - [The `break` statement](Part_4/Break.py)
    - [The `continue` statement](Part_4/Continue.py)

   
5. **Часть №5. Функции:**

    - [Хэширование, метод hash()](Part_5/)
    - [Функции](Part_5/Functions.md)
    - [Замыкания функций](Part_5/Function_closures.md)
    - [Функции - lambda](Part_5/Function_lambda.md)
    - [Аргументы функции упаковка/распаковка](Part_5/Packing_and_unpacking_function_arguments.md)
    - [Аргументы функции по умолчанию](Part_5/Default_function_arguments.md)
    - [Методы range xrange](Part_5/Method_range_xrange.md)

6. **Часть №6. Обьекты :**

    - [Обьекты 1](Part_6/Object_1.md )
    - [Обьекты 2](Part_6/Object_2.md )
    - [Обьекты - функторы, @classmethod и @staticmethod, абстрактный метод, перегрузка ](Part_6/Object_3.md )
    - [Дескрипторы обьектов](Part_6/Descriptors.md )
    - [Модификаторы доступа public, protected, private](Part_6/Access_modifiers.md)
    - [Приватности в обьектах](Part_6/Privacy.md)
    - [Атрибут __slots__](Part_6/Mechanism__slots__.md )
    - [Наследование обьектов](Part_6/Inheritance.md )
    - [Магические (dunder) методы](Part_6/Dunder_method.md )
    - [Паттерны программирования](Part_6/Pattern.md )
   
---
Дальше старое
---

4. **Часть №4. Различные конструкции :**

    - [Сравнения == против is](Часть_4/Сравнение.md)

    - [Тернарный оператор ( 3 переменных )](Часть_4/Тернарный_оператор.md )

    - [Цикл for](Часть_4/)

    - [Итераторы и Выражения-генераторы ](Часть_4/Итераторы_выражения_генераторы.md)

    - [Функции-генераторы yield](Часть_4/Функции_генераторы_yield.md)

    - [Генерация списков](Часть_4/Генерация_списков.md)
   
    - [Условия: if else finally](Часть_4/Условия.md)
   



6. **Часть №6. Разное - 1 :**

    - [Исключения - Exception](Часть_6/Исключения.md)

    - [Менеджеры контекста with](Часть_6/Исключения.md)
   
    - [Декораторы методов и классов](Часть_6/Декораторы.md)
   
    - [Аргументы методов/функций по умолчанию](Часть_6/)
   
    - [Копирование обьектов copy.copy() и copy.deepcopy() ](Часть_6/)
   
    - [Функции all() any() ](Часть_6/Функции_all_any.md)
   
    - [Проверка обьекта на True / False](Часть_6/Сравнение_обьектов.md)
   

7. **Часть №7 Разное - 2 :**

    - [Файлы Ввод/Вывод](Часть_7/Файлы_ввод_вывод.md )
   
    - [Получение информации о памяти обьекта __sizeof__() и sys.getsizeof()](Часть_7/Получение_информации_о_памяти_обьекта.md )

    - [Копирование copy() и deepcopy()](Часть_7/Копирование_обьектов.md )

    - [Визуальный разделитель для чисел](Часть_7/Визуальный_разделитель_для_чисел.md )

    - [Ellipsis ...](Часть_7/Ellipsis.md)
   
    - [Особая распаковка (не функции)](Часть_7/Распаковка.md)


8. **Часть №8. Разное - 3 :**

    - [enumerate](Часть_8/Функция_enumerate.md)
   
    - [Функции globals() locals() vars()](Часть_8/Функции_областей_видимости.md)
   
    - [Хэширование hash()](Часть_8/Хэширование_hash.md)
   

9. **Часть №9. Модули :**
   
    - [Модуль os и shutil ](Часть_9/Модуль_os.md)
   
    - [Модуль sys](Часть_9/Модуль_sys.md)
   
    - [Модуль functools](Часть_9/Модуль_functools.md)
   
    - [Модуль weakref](Часть_9/Модуль_weakref.md)
   
    - [Модуль re - регулярные выражения](Часть_9/Модуль_re.md)
   
    - [Модуль random](Часть_9/Модуль_random.md)
   
    - [Модуль time](Часть_9/Модуль_time.md)
   
    - [Модуль Async](Часть_9/Модуль_Async.md)
   
    - [Модуль crontab](Часть_9/Модуль_crontab.md)



10. **Часть №10. Интересные вопросы по Python :**

    - [Вопросы 1](Часть_10/Вопросы_1.md)
    
    - [Вопросы 2](Часть_10/Вопросы_2.md)
   

---

Практика :
---

1) **[Часть №1 :](Практика_1/)**

    1 [](Практика_1/)
   
    2 [](Практика_1/)
   
    3 [](Практика_1/)
   


