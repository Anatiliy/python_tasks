#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние 
#между ними в 2D пространстве.

#Пример:

#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21
from math import *

a = int(input()), int(input())
b = int(input()), int(input())
print(sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2))