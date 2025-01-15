def multiplica_resta_filas(array1, array2, constante1, constante2):
    i = 0
    j = 0
    k = 0
    while i < len(array1):
        array1[i] = array1[i] * constante2
        i = i + 1

    while j < len(array2):
        array2[j] = array2[j] * -constante1
        j = j + 1

    while k < len(array1):
        array2[k] = array2[k] + array1[k]
        k = k + 1
    return array2


def diagonaliza_abajo(matrix, ecuaciones, variables):
    limite_pivote = 0
    if ecuaciones < variables:
        limite_pivote = ecuaciones

    elif variables < ecuaciones or variables == ecuaciones:
        limite_pivote = variables

    pos_pivote = 0

    while pos_pivote < limite_pivote:
        valor_pivote = matrix[pos_pivote][pos_pivote]
        j = pos_pivote + 1
        while j < ecuaciones:
            cte_sig_fila = matrix[j][pos_pivote]
            matrix[j] = multiplica_resta_filas(matrix[pos_pivote][:], matrix[j][:], valor_pivote, cte_sig_fila)
            # Para enviar una lista por referencia a una funcion: funcion(lista[:])
            j = j + 1
        pos_pivote = pos_pivote + 1
    return matrix


matriz1 = [[1, 2, 3, 9], [4, 5, 6, 24], [2, 7, 12, 30]]
num_ecs1 = 3
num_var1 = 3
matriz2 = [[1, 1, -1, 7], [2, -3, 2, 6], [3, -2, 3, 13]]
num_ecs2 = 3
num_var2 = 3
matriz3 = [[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13], [14, 15, 16]]
num_ecs3 = 5
num_var3 = 2

print(diagonaliza_abajo(matriz3, num_ecs3, num_var3))

# print(multiplica_resta_filas(matriz[0], matriz[1], 1, 4))

"""
        while pos_pivote < limite_pivote:
        valor_pivote = matrix[pos_pivote][pos_pivote]
        j = pos_pivote + 1
        while j < ecuaciones:
            cte_sig_fila = matrix[j][pos_pivote]
            matrix[j] = multiplica_resta_filas(matrix[pos_pivote], matrix[j], valor_pivote, cte_sig_fila)
            print(matrix)
            j = j + 1
        pos_pivote = pos_pivote + 1
"""