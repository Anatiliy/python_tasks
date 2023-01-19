# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом



def print_matrix(matrix):
    for row in matrix:
        for item in row:
            print(str(item).rjust(2), end='')
        print()


def create_matrix(n, m):
    matrix = []
    for i in range(n):
        matrix.append(['*' for _ in range(m)])
    return matrix


def matrix_rotation(matrix):
    result = create_matrix(len(matrix[0]), len(matrix))
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            result[j][i] = matrix[i][j]
    return result


def matrix_diagonal(matrix):
    diagonal1 = []
    diagonal2 = []
    for i in range(len(matrix)):
        diagonal1.append(matrix[i][i])
        diagonal1.append(matrix[i][-i - 1])
    return diagonal1, diagonal2


def check_matrix(matrix, key):
    if key in matrix:
        return True
    elif key in matrix_diagonal(matrix):
        return True
    elif key in matrix_rotation(matrix):
        return True
    else:
        return False   


def create_x_0_matrix():
    matrix = create_matrix(4, 4)
    for i in range(1, 4):
        matrix[0][i] = i
        matrix[i][0] = i

    return matrix


def trim_matrix(matrix):
    result = []
    for i in range(1, len(matrix)):
        result.append([])
        for j in range(1, len(matrix[0])):
            result[i - 1].append(matrix[i][j])
    return result


def game(gamer, x_0_matrix, symbol):
    print(f'{gamer} ставьте {symbol}')
    motion = tuple(map(int, input('введите координаты в формате: "номер строки" "пробел" "номер столбца" ').split()))
    x_0_matrix[motion[0]][motion[1]] = symbol
    print_matrix(x_0_matrix)
    return x_0_matrix    

x_0_matrix = create_x_0_matrix()
print_matrix(x_0_matrix)
if input('если хотите играть с ботом, введите "b", если хотите играть с живым игроком, нажмите enter ') == 'b':
    
    name_of_gamer = input('введите своё имя ')
#    while numbers_of_candies:
 #       x_0_matrix = game(name_of_gamer, numbers_of_candies)
  #      if not numbers_of_candies:
   #         print(name_of_gamer,'победил!!!')
#            break
#        numbers_of_candies = gamer_bot(numbers_of_candies)
#        if not numbers_of_candies:
#            print('bot победил!!!')
#            break

else:
    
    name_of_gamers = tuple(zip(input('введите имена игроков через пробел ').split(), ('X', '0'), (['X', 'X', 'X'], ['0', '0', '0'])))
    flag = True
    count = 0
    while count < 10:
        for gamer, symbol, key in name_of_gamers:
            count += 1
            if check_matrix(trim_matrix(game(gamer, x_0_matrix, symbol)), key):
                print(gamer,'победил!!!')
                flag = False
                break
        if not flag:
            break
    else:
        print('ничья!')

    
