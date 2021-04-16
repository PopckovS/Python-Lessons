#! /usr/bin/python3

# Функция для удобного вывода содержимого
from custom_functions import trace
import os
import sys

my_set1 = (1,2,'sfd')
hash1 = hash(my_set1)

print(my_set1)
print(hash1)

my_set2 = (1,2, [1,2,3])
hash2 = hash(my_set2)

print(my_set2)
print(hash2)


