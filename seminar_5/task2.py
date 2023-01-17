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


def create_x_0_matrix():
    matrix = create_matrix(4, 4)
    for i in range(1, 4):
        matrix[0][i] = i
        matrix[i][0] = i

    print_matrix(matrix)


create_x_0_matrix()
