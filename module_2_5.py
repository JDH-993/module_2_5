def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for g in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix


get_matrix(int(input()), int(input()), int(input()))
