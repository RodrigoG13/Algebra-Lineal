def calcula_range(matrix):
    cuenta_ceros = 0
    filas_cero = 0
    for fila in range(0, len(matrix)):
        for elemento in range(0, len(matrix[fila])):
            if matrix[fila][elemento] == 0:
                cuenta_ceros = cuenta_ceros + 1
        if cuenta_ceros == len(matrix[fila]):
            filas_cero = filas_cero + 1
        cuenta_ceros = 0
    range_matrix = len(matrix) - filas_cero
    return range_matrix


matriz_test = [[0, 0, 0, 0], [0, 7, 9, 4], [0, 0, 7, 8], [0, 0, 0, 12], [9, 10, 11, 12], [9, 10, 11, 12]]
print(calcula_range(matriz_test))