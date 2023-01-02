# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10



def decimal_to_binary(num):
    result = ''
    while num != 0:
        result += str(num % 2)
        num //= 2
    return result[::-1]


num = int(input('введите целое чтсло '))

print(decimal_to_binary(num))   