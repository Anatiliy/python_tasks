#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

#Пример:
#- 6 -> да
#- 7 -> да
#- 1 -> нет

q = ['не выходной', 'выходной']
print(q[input() in ('6', '7')])