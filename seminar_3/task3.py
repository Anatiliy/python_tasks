# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов, отличной от 0.

# Пример:

# [1.1, 1.2, 3.1, 5, 10.01] => 0.19




def check_numbers(numbers):
    import re
    for num in numbers:
        return num in re.findall(r'[0-9]+\.?[0-9]*', num)


def my_map(func, list1):
    result_list = []
    for i in list1:
        result_list.append(func(i))
    return result_list


numbers = input('введите вещественные числа через прбел ').split()

while not check_numbers(numbers):
    print('не коректно заданы числа')
    numbers = input('введите вещественные числа через прбел ').split()

#временный вывод для проверки
print(list(map(float, numbers)))



