Публикация пакетов на PyPi
---
---

Для выпуска проекта на https://pypi.org/, следует на нем 
зарегистрироваться.

Все пакеты, что устанавливаются через `pip` или `pip3` хранятся на 
официальном сайте https://pypi.org/ там же можно выложить в открытый 
доступ и свои пакеты.

Создаем свой пакет с модулями по следующей структуре, сам проект имеет 
название `ProjectName` в нем находится пакет с таким же названием, в
котором хранятся все модули с файлом `__init__.py` на верхнем уровне
находятся еще 2 файла, `setup.py` и `LICENSE`
```
    ProjectName /
        |
        ----> ProjectName/
        |           ----> __init__.py
        |           ----> module_1.py
        |           ----> module_2.py
        |
        ----> setup.py
        ----> LICENSE
        ----> README.md
```

---

Добавляем лицензию
---

`LICENSE` - Создаем файл с лицензией распространения программы,
выбираем `MIT License` со следующим содержанием, только заменяем
`[YEAR]` и `[NAME]` на свои:

```
MIT License

Copyright (c) [YEAR] [NAME]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---
Модуль `setuptools` и файл с настройками `setup.py`
---

Устанавливаем модуль `setuptools`
```
pip3 install setuptools
```

Создаем файл `setup.py`

`setup.py` - специальный файл с настройками, для организации программы
в проект для загрузки на PyPi и наполняем его содержимым, тут будут 
настройки для описания программы, которая будет выложена на PyPi 

```python
# Импортируем установленный setuptools
import setuptools

# Открываем файл README.md и получаем из него все описание, это описание
# мы используем для титульной страницы проекта на сайте PyPi
with open("README.md", "r") as fh:
    long_description = fh.read()

# Устанавливаем настройки
setuptools.setup(
    name="ComputMath", # Название проекта
    version="1.0.1", # Версия проекта
    author="Name", # Имя автора
    author_email="some@yandex.ru", # Ваша почта что зарег-на на pypi
    description="Computational Mathematics Package", # Краткое описание
    
    # Полное описание, тут мы используем описание из README.md иначе
    # можно тут описать его заново
    long_description=long_description, 
    # Формат в котором будет восприниматься полное описание
    long_description_content_type="text/markdown",
    # адрес вашей программы на github
    url="https://github.com/<REPO>/<PROJECT>",

    packages=setuptools.find_packages(),
    # Версия питона, лицензия распространения, ОС на которой будет работать
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
    # Зависимости
    python_requires='>=3.6',
)
```

python3 setup.py sdist bdist_wheel

pip3 install twine

twine upload dist/*


