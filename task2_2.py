# Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, 
# а так же сумму элементов списка.

# Пример:

# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

# решение 1

from math import *

result = 0
result_list = []
for i in range(1, int(input('введите число элементов последовательности ')) + 1):
    result += (1 + 1/i)**i
    result_list.append(round((1 + 1/i)**i, 2))
print(result_list)
print(round(result, 2))


# решение 2

result_list = list(round((1 + 1/i)**i, 2) for i in range(1, int(input('введите число элементов последовательности ')) + 1))
print(result_list)
print(sum(result_list))


