## Урок 3

### Генерация списков
Обычная система создания списков выглядит так:

    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Но в Питоне можно генерировать списки при помощи спеуиальной 
системы записи в одну строчку, к примеру так:

    my_list = [number for number in range(1, 11)]
    print(my_list)

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

При помощи функции `range(1, 11)` генерируем 10 значений от 1 до 10.
При каждой итерации цикла `for` каждое из генерируемых чисел, попадает
в переменную `number` и заносится в список, таким образом список 
генерируется из тех значений что генерируются ы функции `range()`.

При обычном обходе циклом `for` мы с начала аписываем условие а потом
то что хотим получить, при генерации списка, с начала зписываем то что
хотим получить, а уже потом условие `for`.


### Генерация списка из рандомных значений
Можно сгенерировать список из рандомных значений, след образом.

    my_list = [ randint(0, 10) for i in range(3) ]
    print(my_list)

    [6, 9, 0]

Используем тот же цикл `for` чтобы сгенерировать количество элементов
при помощи range() но теперь в место итерации цикла, зановим в список
рандомное значение в неком диапозоне.

### Генерация матрицы при помощи генерации списков

      # matrix_two = [[randint(0,10) for c in range(3)] for r in range(3)]

      # Тоже самое
      matrix_two = [ 
            [randint(0, 10) for c in range(3)] 
            for r in range(3) 
      ]

      [ [10, 1, 8], [3, 3, 2], [10, 0, 3] ]

С начала мы генерируем 3 цикла при помощи этой строчки `for r in range(3)`
и в нутри каждого их этих циклов мы генерируем список, и каждый из этих
циклов будет содержать рандомное значение, эту работу выполняет след 
строчка кода: `[ randint(0, 10) for c in range(3) ]` в результате мы
получаем список с тремя списками.

### Генерация списков с условиями
По мимо генерации списков с использованием `for` мы можем еще и добавить 
условие в генерацию, и тогда в финальный список войдет не прсото все что 
будет сгенерировано, но и еще то что будет удовлетворять условию. 

При генесрации списков, двоеточие не ставится, оно не ставится как 
после `for` так и после `if`

    odd = [ number for number in range(0, 11) if number%2==0]
    print(odd)

    [0, 2, 4, 6, 8, 10]

В этом списке мы заносим значения что являются четными, тоесть делятся 
на 2 без остатка, мы просто дабавляем условие проверки на четность 
после цикла `if number%2==0` при чем двоеточия мы не ставим.

### Генерация с циклом
Тут все очень просто, мы в генерации цикла вставляем еще один цикл,
таким образом в каждом цикле есть свой цикл.

К примеру, генерируем цикл который генерирует цикл, и вносимые элементы
будут представлять из себя произведение, каждого элемента внешнего цикла 
на каждый элемент внутренного цикла:

    for_for = [ i*j for j in range(0, 3) for i in range(0, 3) ]
    print("Генерация с вложенным циклом 'for' : %s"%for_for)

    Генерация с вложенным циклом 'for' : [0, 0, 0, 0, 1, 2, 0, 2, 4]

Тоесть по сути, происходит вот что:

    0 * 0 = 0
    1 * 0 = 0
    2 * 0 = 0
    0 * 1 = 0
    1 * 1 = 1
    2 * 1 = 2
    0 * 2 = 0
    1 * 2 = 2
    2 * 2 = 4

### Важное Замечание
При генерации списка есть 2 важных момента, это либо фильтр по 
которому мы хотим отфильтровать включаемое в список значение, и 
некое изменение которое мы хотим произвести с уже включенном в список
значением.

Если мы хоти отфильтровать значение по какомуто признаку, то его мы 
включаем в конец генерации списка, к примеру включение в список
только четные значения:

    odd_list = [num for num in range(0, 10) if num % 2 == 0]
    print("Четными элементами %s"%odd_list)

    Список с только четными элементами [0, 2, 4, 6, 8]

Если мы хоти произвести некое изменение с уже включенным в список 
значением, то добавляем его с левой стороны, тоесть мы с начала внесли
значение а потом его изменяем, к примеру добавим ко всем уже включенным 
в список значениям +2 выглядеть это будет так:

    odd_list_2 = [num+2 for num in range(0, 10) if num%2==0]
    print("Четными элементами сложенными с '+2' %s"%odd_list_2)    

    Список с только четными элементами сложенными с '+2' [2, 4, 6, 8, 10]

### Вложенный генератор списков
Мы можем генерировать цикл, и в нутри этой генерации, генерируем еще
один список:

Генерация списка:
    
    for_list = [x**2 for x in range(0, 11)]
    print(for_list)    

    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

Генерация списка в списке:

    for_for_list = [ x**2 for x in [x**2 for x in range(0, 11)] ]
    print(for_for_list)

    [0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561, 10000]

### Примеры генерации списков
Список из слова:

    l = [letter for letter in "word"]
    print(l)

    ['w', 'o', 'r', 'd']

Проверка на четность в генерируемом диапозоне:

    odd = [ number for number in range(0, 11) if number%2==0]
    print(odd)

    [0, 2, 4, 6, 8, 10]

Выводим список с градусами Цельсия, и расчитываем их аналоги 
по Фаренгейту:

    celsius = [0, 10, 20.1, 34.5]
    farenhait = [ (temp*9/5)+32 for temp in celsius]

    print("Расчет градусов по Цельсию и Фаренгейту")
    print("Цельсия : %s"%celsius)
    print("Фаренгейт : %s"%farenhait)

    Расчет градусов по Цельсию и Фаренгейту
    Цельсия : [0, 10, 20.1, 34.5]
    Фаренгейт : [32.0, 50.0, 68.18, 94.1]






