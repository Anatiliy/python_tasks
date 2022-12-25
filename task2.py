# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.


a = [False, True]

for x in a:
    for y in a:
        for z in a:
            print(f'X = {x}, Y = {y}, Z = {z}')
            print('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
            print(not(x or y or z) == ((not x) and (not y) and (not z)))
            print()