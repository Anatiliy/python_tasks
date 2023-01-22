# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом


import random


# функция вывода матрици на экран
def print_matrix(matrix):
    for row in matrix:
        for item in row:
            print(str(item).rjust(2), end='')
        print()


# функция, создающая матрицу размера n на  m
def create_matrix(n, m):
    matrix = []
    for i in range(n):
        matrix.append(['*' for _ in range(m)])
    return matrix


# функция, поворачивающая матрицу относительно диагонали
def matrix_rotation(matrix):
    result = create_matrix(len(matrix[0]), len(matrix))
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            result[j][i] = matrix[i][j]
    return result

# функция, возвращающая диагонали матрици
def matrix_diagonal(matrix):
    diagonal1 = []
    diagonal2 = []
    for i in range(len(matrix)):
        diagonal1.append(matrix[i][i])
        diagonal2.append(matrix[i][-i - 1])
    return diagonal1, diagonal2


# функция, возвращающая True, если один из столбцов, строк или диагоналей соответствует ключу
def check_matrix(matrix, key):
    if key in matrix:
        return True
    elif key in matrix_diagonal(matrix):
        return True
    elif key in matrix_rotation(matrix):
        return True
    else:
        return False   


# функция, создающая игровое поле
def create_x_0_matrix():
    matrix = create_matrix(4, 4)
    for i in range(1, 4):
        matrix[0][i] = i
        matrix[i][0] = i

    return matrix


# функция,обрезающая у игрового поля координатные строку и столбец
def trim_matrix(matrix):
    result = []
    for i in range(1, len(matrix)):
        result.append([])
        for j in range(1, len(matrix[0])):
            result[i - 1].append(matrix[i][j])
    return result


# функция, создающая список возможных ходов
def create_list_motions(n=4, m=4):
    result_list = []
    for i in range(1, n):
        for j in range(1, m):
            result_list.append((i, j))
            
    return result_list


# функция, создающая список возможных комбинаций
def create_list_combinations(n=4, m=4):
    matrix = []
    result_list = []
    for i in range(1, n):
        matrix.append([])
        result_list.append([])
        for j in range(1, m):
            result_list[i - 1].append((i, j))
            matrix[i - 1].append((i, j))
    for i in range(n - 1):
        result_list.append(matrix_rotation(matrix)[i])
    result_list.append(matrix_diagonal(matrix)[0])       
    result_list.append(matrix_diagonal(matrix)[1])
    return result_list


# функция, реализующая ход реального игрока
def motion_of_gamer(gamer, symbol_of_gamer, list_motions):
    print(f'{gamer} ставьте {symbol_of_gamer}')
    motion = tuple(map(int, input('введите координаты в формате: "номер строки" "пробел" "номер столбца" ').split()))
    if motion in list_motions:
        return motion  
    else:
        print('ход невозможен!')
        return motion_of_gamer(gamer, symbol_of_gamer, list_motions)


# функция, реализующая ход бота
def motion_of_bot(symbol_of_bot, symbol_of_gamer, list_combinations, list_motions):
    print('ходит bot')
    for combi in list_combinations:
        if symbol_of_bot in combi and not (symbol_of_gamer in combi) and combi.count(symbol_of_bot) == 2:
            return list(filter(lambda item: not 'X' in item and not '0' in item, combi))[0]
    for combi in list_combinations:        
        if symbol_of_gamer in combi and not (symbol_of_bot in combi) and combi.count(symbol_of_gamer) == 2:
            return list(filter(lambda item: not 'X' in item and not '0' in item, combi))[0]
    for combi in list_combinations:        
        if symbol_of_bot in combi and combi.count(symbol_of_bot) == 1:
            return random.choice(list(filter(lambda item: not 'X' in item and not '0' in item, combi)))
    return random.choice(list_motions)


# функция, фиксирующая ходы,сделанные игроками, в списке комбинаций
def changing_list_combinations(motion, symbol, list_combinations):
    for combi in list_combinations:
        if motion in combi:
            combi[combi.index(motion)] = symbol


# функция проверки листа комбинаций на наличие победной комбинации
def check_list_combinations(list_combinations):
    for combi in list_combinations:        
        if 'X' in combi and combi.count('X') == 3:
            return True
    for combi in list_combinations:        
        if '0' in combi and combi.count('0') == 3:
            return True


# функция, реализующая логику игры между реальными игроками
def game(gamer, x_0_matrix, symbol, list_motions, list_combinations):
    print(f'{gamer} ставьте {symbol}')
    motion = tuple(map(int, input('введите координаты в формате: "номер строки" "пробел" "номер столбца" ').split()))
    list_motions.pop(list_motions.index(motion))
    changing_list_combinations(motion, symbol, list_combinations)
    x_0_matrix[motion[0]][motion[1]] = symbol
    print_matrix(x_0_matrix)
    return x_0_matrix
    


# основная программа     

x_0_matrix = create_x_0_matrix()
print_matrix(x_0_matrix)
list_motions = create_list_motions()
list_combinations = create_list_combinations()
lot = random.randint(0, 1) # переменная, реализующая жребий

if input('если хотите играть с ботом, введите "b", если хотите играть с живым игроком, нажмите enter ') == 'b':
    # игра с ботом
    name_of_gamer = input('введите своё имя ')
    if lot:
        while list_motions:
            motion = motion_of_bot('X', '0', list_combinations, list_motions)
            list_motions.pop(list_motions.index(motion))
            changing_list_combinations(motion, 'X', list_combinations)
            x_0_matrix[motion[0]][motion[1]] = 'X'
            print_matrix(x_0_matrix)
            if check_list_combinations(list_combinations):
                print('bot победил!!!')
                break
            elif all(map(lambda combi: 'X' in combi and '0' in combi, list_combinations)):
                print('ничья!!!')
                break
            motion = motion_of_gamer(name_of_gamer, '0', list_motions)
            list_motions.pop(list_motions.index(motion))
            changing_list_combinations(motion, '0', list_combinations)
            x_0_matrix[motion[0]][motion[1]] = '0'
            print_matrix(x_0_matrix)
            if check_list_combinations(list_combinations):
                print(f'{name_of_gamer} победил!!!')
                break
            elif all(map(lambda combi: 'X' in combi and '0' in combi, list_combinations)):
                print('ничья!!!')
                break
        else:
            print('ничья!!!')
    else:
        while list_motions:
            motion = motion_of_gamer(name_of_gamer, 'X', list_motions)
            list_motions.pop(list_motions.index(motion))
            changing_list_combinations(motion, 'X', list_combinations)
            x_0_matrix[motion[0]][motion[1]] = 'X'
            print_matrix(x_0_matrix)
            if check_list_combinations(list_combinations):
                print(f'{name_of_gamer} победил!!!')
                break
            elif all(map(lambda combi: 'X' in combi and '0' in combi, list_combinations)):
                print('ничья!!!')
                break
            motion = motion_of_bot('0', 'X', list_combinations, list_motions)
            list_motions.pop(list_motions.index(motion))
            changing_list_combinations(motion, '0', list_combinations)
            x_0_matrix[motion[0]][motion[1]] = '0'
            print_matrix(x_0_matrix)
            if check_list_combinations(list_combinations):
                print('bot победил!!!')
                break
            elif all(map(lambda combi: 'X' in combi and '0' in combi, list_combinations)):
                print('ничья!!!')
                break
        else:
            print('ничья!!!')
        
else:
    # игра между реальными игроками
    list_names = input('введите имена игроков через пробел ').split()
    random.shuffle(list_names)
    name_of_gamers = tuple(zip(list_names, ('X', '0'), (['X', 'X', 'X'], ['0', '0', '0'])))
    flag = True
    while list_motions:
        for gamer, symbol, key in name_of_gamers:
            if check_matrix(trim_matrix(game(gamer, x_0_matrix, symbol, list_motions, list_combinations)), key):
                print(gamer,'победил!!!')
                flag = False
                break
            elif not list_motions:
                break
            elif all(map(lambda combi: 'X' in combi and '0' in combi, list_combinations)):
                print('ничья!')
                flag = False
                break
        if not flag:
            break
    else:
        print('ничья!')

    
