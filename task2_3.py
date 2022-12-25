# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для и получения случайного int

import random

result_list = input('введите данные через пробел ').split()

print(result_list)

for i in result_list:
    result_list.append(result_list.pop(random.randint(0, len(result_list) - 1)))


print(result_list)
