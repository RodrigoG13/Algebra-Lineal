"""
Verifica que el primer arreglo tenga térimo inicial distinto de cero
"""


def pivote_distinto_cero(matrix1, ecuaciones, arrayde_arrays, elemento):
    while matrix1[arrayde_arrays][elemento] == 0:
        aux = matrix1[0]
        matrix1.pop(0)
        matrix1.insert(ecuaciones, aux)
    return matrix1


num_ecs = 3
matrix = [[0, 5, 3, 2, 5], [0, 9, 4, 5, 6, 6], [0, 8, 9, 1, 2, 3, 4], [3, 4, 5, 6, 7, 8]]
matrix = pivote_distinto_cero(matrix, num_ecs)
print(matrix, 0, 0)