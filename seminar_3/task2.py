# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый
# и последний элемент, второй и предпоследний и т.д.
# Пример:
#[2, 3, 4, 5, 6] => [12, 15, 16];
#[2, 3, 5, 6] => [12, 15]



def product_of_pairs_of_list_numbers(list1):
    result = []
    for i in range((len(list1)// 2) + (len(list1) % 2)):
        result.append(list1[i] * list1[-i - 1])

    return result

def my_map(func, list1):
    result_list = []
    for i in list1:
        result_list.append(func(i))
    return result_list



my_list = input('введите числа через пробел ').split()

print(product_of_pairs_of_list_numbers(my_map(int, my_list)))
