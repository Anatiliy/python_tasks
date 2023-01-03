# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи


def fibonachi(num, begin_list = [0, 1]):
    if len(begin_list) <= num:
        begin_list.append(begin_list[-1] + begin_list[-2])
        return fibonachi(num, begin_list)
    else:
        return begin_list


def negofibonachi(num):
    result_list = fibonachi(num)[1:]
    for i in range(len(result_list)):
        result_list[i] *=(-1) ** i
    return result_list[::-1]


def task_funk(num):
    return negofibonachi(num) + fibonachi(num)


print(task_funk(int(input('введите натуральное число '))))

