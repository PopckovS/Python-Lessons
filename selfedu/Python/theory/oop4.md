## Python и ООП 4
### Множественное наследование 
Этот механизм я встречал только в 2 языках, `C++` и `Python`.

Суть в том что мы можем наследоваться сразу от 2 классов.

Указание происходит также в скобках, первым вызывается методы класса
который указан первым, есть в данном случае первый будет вызван `One`:

    class My(One, Two):

При вызове конструктора, будет вызван конструктор класса `One` если
конечно нету конструктора в классе `My`

Для корректной работы множ наследования используется функция `super()`
суть этой функции заключается в том чтобы обходить родительские классы
только по одному разу и не повторяться.

### Реализация без super()

    class Poss:
        def __init__(self, x, y, *args):
            self._x = x
            self._y = y
            Style.__init__(self, *args)

    class Style:
        def __init__(self, name, style):
            self._name = name
            self._style = style

    class Point(Poss, Style):
        def draw(self):
            return f"x={self._x} y={self._y} name={self._name} style={self._style}"

    pt = Point(10, 20, 'Название', 'Стили')
    print(pt.draw())

    // Вывод
    x=10 y=20 name=Название style=Стили

Тут проблема заключается в том что указывая в явном виде эту строчку
`Style.__init__(self, *args)` мы жестко задаем класс конструктор которого 
будет вызван.

А если в классе `Style` указать чтото тиипа `Poss.__init__(self, *args)` то
это приведет нас к рекурсии, вобщем лучше так не делать.

### Реализация с super()

Мы моглибы сделать такую реализацию:

    class Styles:
        def __init__(self, color="red", width=1, *args):
            print("Конструктор Styles")
            self._color = color
            self._width = width
            super().__init__(*args)

    class Pos:
        def __init__(self, sp:Point, ep:Point, *args):
            print("Конструктор Pos")
            self._sp = sp
            self._ep = ep
            super().__init__(*args)

    class Line(Pos, Styles):
        def draw(self):
            print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")

Тоесть просто определять в каждом конструкторе `super().__init__(*args)`
который бы устанавливал нужные атрибуты а другие передавал бы далее по 
цепочке родителей.

Но в атком случае есть другая проблема, нам бы потребовалось четко 
контралировать порядок передачи аргументов, и мы бы не могли менять 
порядок наследования.

Правильная реализация выглядит следующим образом:

    class Styles:
        def __init__(self):
            print("Конструктор Styles")
            super().__init__()

    class Pos:
        def __init__(self):
            print("Конструктор Pos")
            super().__init__()

    class Line(Pos, Styles):
    # class Line(Styles, Pos):
        def __init__(self, sp:Point, ep:Point,color="red", width=1,):
            self._sp = sp
            self._ep = ep
            self._color = color
            self._width = width

        def draw(self):
            print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")

    ln = Line(Point(10, 10), Point(100, 100), "green", 5)
    ln.draw()

Как можно увидеть тут вся инициализация происходит только в непосредственном 
родительском классе, а не в его родителях, родитель только вызывают 
`super().__init__()` более верхнего класса.

При такой реализации нпм уже не важно какой порядок наследования, он может
быть любым.

### C3 алгоритм наследования MRO
Порядок наследования называется `MRO` он указывает порядок наследования классов
с начала Line -> Pos -> Style -> object

Это можно увидеть при помощи спец атрибута класса `__mro__`

    print(Line.__mro__)

    // Вывод
    (
        <class '__main__.func5.<locals>.Line'>,
        <class '__main__.func5.<locals>.Pos'>, 
        <class '__main__.func5.<locals>.Styles'>, 
        <class 'object'>
    )

### Функторы
Функторы - это класс в котором определили метод `__call__(self, *args, **kargs)`
этот метод будет срабатывать когда обькт класс пытаются вызвать как метод.


    class StripChars:
        """Класс функтор, удаляет из строки все не нужные символы"""
        def __init__(self, chars):
            self.__chars = chars

        def __call__(self, *args, **kwargs):
            if not isinstance(args[0], str):
                raise ValueError("Аргумент должен быть строкой")
            return args[0].strip(self.__chars)

    sc = StripChars('!')
    print(sc('Hello World!'))
    
    // Вывод
    Hello World

### Замыкания
Замыкания, полнение функции с той обл видимости не в которой она вызывается
а в которой она определена.

Создаем функцию `strip_string(chars)` которая принимает строчку, и в нутри 
функции определяем еще одну функцию `inner_function(string)` которая тоже 
принимает строчку, из функции верх уровня мы возвращаем функцию нижнего 
уровня, тоетсь ссылку на нее:


    def strip_string(chars):
        def inner_function(string:str):
            return string.strip(chars)
        return inner_function

    x1 = strip_string('!')
    print('Работа с замыканиями 1:', x1("!Hello World!"))


    x2 = strip_string('!')
    print('Работа с замыканиями 2:', x2("!Helorld!"))

    // Вывод
    Работа с замыканиями 1: Hello World
    Работа с замыканиями 2: Helorld

В дальнейшем каждый раз вызывая ее мы будем получать ссфлку на функцию 
нижнего уровня, и вызывая ее в работу она будет исполняться в контексте
тех данных что были переданы в функцию верхнего уровня.

И каждый из экземпляров будет работать в своем контексте.

### Менеджеры контекста
with ... as ...












