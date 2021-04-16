#! /usr/bin/python3

import re


def func1():
    """Работа с регулярными выражениями"""

    text = "Карта map и обьект bitmap - это разные вещи."

    search1 = "map"
    search2 = " map "
    search3 = "\\bmap\\b"
    search4 = r"\bmap\b"

    result = re.findall(search4, text)

    print(result)















func1()
