# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов, отличной от 0.

# Пример:

# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# numbers = ['1.1', '1.2', '3.1', '5', '10.01']

from decimal import *


def check_numbers(numbers):
    import re
    for num in numbers:
        return num in re.findall(r'[0-9]+\.?[0-9]*', num)


def my_map(func, list1):
    result_list = []
    for i in list1:
        result_list.append(func(i))
    return result_list


def task_func(numbers):
    
    result_list = []
    for i in numbers:
        result_list.append(Decimal(i) - (int(float(i))))
    return result_list    

def my_filter(numbers):
    result_list = []
    for i in numbers:
        if i != 0:
            result_list.append(i)
    return result_list

numbers = input('введите вещественные числа через прбел ').split()

while not check_numbers(numbers):
    print('не коректно заданы числа')
    numbers = input('введите вещественные числа через прбел ').split()

print(max(my_filter(task_func(numbers))) - min(my_filter(task_func(numbers))))



