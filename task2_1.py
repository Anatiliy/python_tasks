# Напишите программу, которая принимает на вход вещественное число и показывает
# сумму его цифр.


# Пример:
# 6782 -> 23
# 0,56 -> 11


result = 0

for d in list(input('введите вещественное число ')):
    if d.isdigit():
        result += int(d)
print(result)

print(sum(int(d) for d in list(input('введите вещественное число ')) if d.isdigit()))
