# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов 
# списка, стоящих на позиции с нечетным индексом.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


# решение 1

def sum_negativ_item(list1):
    total = 0
    for i in range(1,len(list1),2):
        total += list1[i]

    return total


def my_map(func, list1):
    result_list = []
    for i in list1:
        result_list.append(func(i))
    return result_list

my_list = input('введите натуральные числа через пробел ').split()

print(sum_negativ_item(my_map(int, my_list)))


# решение 2

my_list = input('введите натуральные числа через пробел ').split()
print(sum(int(my_list[i]) for i in range(len(my_list)) if i % 2 != 0))

