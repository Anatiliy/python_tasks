# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов 
# списка, стоящих на позиции с нечетным индексом.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

lst = [2, 3, 5, 9, 3]
print(sum(map(lambda item: item[1], filter(lambda item: item[0] % 2 != 0, enumerate(lst)))))
