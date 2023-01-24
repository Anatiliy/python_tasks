# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов, отличной от 0.

# Пример:

# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# numbers = ['1.1', '1.2', '3.1', '5', '10.01']

from math import *

lst = [1.1, 1.2, 3.1, 5, 10.01]
print(round(max(filter(None, map(lambda item: item - floor(item), lst))) - min(filter(None, map(lambda item: item - floor(item), lst))), 2))