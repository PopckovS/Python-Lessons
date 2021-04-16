## Регулярные выражения
Модуль `re` и его методы по поиску в тексте написаны на языке C что 
делает его очень быстрым.

Импортируем модуль для регулярных выражений:

    import re

Найти слово можно так `"map"` но в таком случае будут извлечены даже те 
слова что выглядят так `"bitmap"` для того чтобы найти именно отдельно 
стоящие слова, можно использовать такие способы:

" map " - Найдет отдельно стоящее слово

"\\bmap\\b" - Обрамив искомое слово символами \\b с двух сторон, мы 
указываем что должны найти именно отдельно стоящее слово. Здесь два слеша
нужны для экранирования.

r"\bmap\b" - Поставив указатель r перед строчкой, мы указываем что эта строка
будет использована как регулярное выражение, и в нутри можно уже не 
экранирвоать при помощи 2 слешей а писать только так \b

### Специальные символы
В регу выражениях есть спец символы, эти символы используются для спеу 
функционала, вот они `\.^$&+*{}[]()`

### Метод findall
Метод находит все вхождения подстроки в строке.

    re.findall(search, text)


















