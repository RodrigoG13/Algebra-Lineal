def fila_cero(array):
    conta_ceros = 0
    toda_fila_ceros = False
    for elemento in array:
        if elemento == 0:
            conta_ceros = conta_ceros + 1
    if conta_ceros == len(array):
        toda_fila_ceros = True
    return toda_fila_ceros


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


def pivote_distinto_cero(matrix1, ecuaciones, arrayde_arrays, elemento):
    while matrix1[arrayde_arrays][elemento] == 0:
        aux = matrix1[arrayde_arrays]
        matrix1.pop(arrayde_arrays)
        matrix1.insert(ecuaciones, aux)
    return matrix1


def diagonaliza_abajo(matrix, ecuaciones, variables):
    limite_pivote = 0
    if ecuaciones < variables:
        limite_pivote = ecuaciones

    elif variables < ecuaciones or variables == ecuaciones:
        limite_pivote = variables

    pos_pivote = 0

    while pos_pivote < limite_pivote:
        valor_pivote = matrix[pos_pivote][pos_pivote]
        print(f"pos_pivote es: {pos_pivote}")
        print(f"lim_pivote es: {limite_pivote}")
        print(f"valor_piv es {valor_pivote}")
        print(matrix)
        print(f"funcion es: {fila_cero(matrix[pos_pivote])}")


        if pos_pivote + 1 == limite_pivote and valor_pivote == 0 and fila_cero(matrix[pos_pivote]) == True:
            print("Cayó en el if")
            break

        elif valor_pivote == 0:
            pivote_distinto_cero(matrix, ecuaciones, pos_pivote, pos_pivote)
            valor_pivote = matrix[pos_pivote][pos_pivote]
        j = pos_pivote + 1



        while j < ecuaciones:
            cte_sig_fila = matrix[j][pos_pivote]
            if cte_sig_fila != 0:
                matrix[j] = multiplica_resta_filas(matrix[pos_pivote][:], matrix[j][:], valor_pivote, cte_sig_fila)
            j = j + 1
        pos_pivote = pos_pivote + 1
    return matrix


matriz1 = [[1, 1, 4, -1, 0, 5, 9], [4, -1, 1, -1, 6, 1, 20], [1, 0, 1, -1, 0, 1, 12], [-1, 1, 0, 0, 1, -10, -14], [6, -3, 6, -4, 5, -1, 19] , [1, 0, -1, 0, -1, -1, 25]]
num_ecs1 = 6
num_var1 = 6
matriz2 = [[1, 2, 3, 9], [4, 5, 6, 24], [2, 7, 12, 30]]
num_ecs2 = 3
num_var2 = 3
matrix3 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
num_ecs3 = 5
num_var3 = 3
print(diagonaliza_abajo(matriz2, num_ecs2, num_var2))