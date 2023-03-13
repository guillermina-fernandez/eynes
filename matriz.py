import random


def random_matrix():
    new_matrix = []
    for num in range(5):
        new_row = []
        for w in range(5):
            new_row.append(random.randint(-10**10, 10**10))
        new_matrix.append(new_row)
    return new_matrix


def check_matrix():
    matrix = random_matrix()
    results = []
    for r in range(5):
        for i in range(2):
            if abs(matrix[r][i] - matrix[r][i+1]) == 1 and abs(matrix[r][i+1] - matrix[r][i+2]) == 1 and abs(matrix[r][i+2] - matrix[r][i+3]) == 1:
                results.append(f'Inicial: ({r}, {i}), Final: ({r}, {i+3})')

    for j in range(5):
        for i in range(2):
            if abs(matrix[i][j] - matrix[i+1][j]) == 1 and abs(matrix[i+1][j] - matrix[i+2][j]) == 1 and abs(matrix[i+2][j] - matrix[i+3][j]) == 1:
                results.append(f'Inicial: ({i}, {j}), Final: ({i+3}, {j})')

    if len(results) >= 1:
        print(f'Posicion Inicial y Final de 4 números consecutivos en {matrix}')
        for r in results:
            print(r)
    else:
        print(f'No hay números consecutivos en {matrix}')


check_matrix()
