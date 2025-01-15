def multiplica_resta_filas(array1, array2, constante1, constante2):
    i = 0
    j = 0
    k = 0
    while i < len(array1):
        array1[i] = array1[i] * constante2
        i = i + 1
 #   print(array1)

    while j < len(array2):
        array2[j] = array2[j] * -constante1
        j = j + 1
  #  print(array2)

    while k < len(array1):
        array2[k] = array2[k] + array1[k]
        k = k + 1
    print(f"array2 es : {array2}")
    return array2


def pivote_distinto_cero(matrix1, ecuaciones, arrayde_arrays, elemento):
    while matrix1[arrayde_arrays][elemento] == 0:
        print(f"matrix1[arrayde_arrays][elemento] es = {matrix1[arrayde_arrays][elemento]}")
        aux = matrix1[arrayde_arrays]
        print(f"aux = matrix1[arrayde_arrays] es: {aux}")
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
        print(f"pos_pivote es: {pos_pivote}")
        valor_pivote = matrix[pos_pivote][pos_pivote]
        print(f"Valor_piv antes del if es {valor_pivote}")
        if valor_pivote == 0:
            pivote_distinto_cero(matrix, ecuaciones, pos_pivote, pos_pivote)
            valor_pivote = matrix[pos_pivote][pos_pivote]
            print(f"Matrix despues del if es {matrix}")
        print(f"Valor pivote en {pos_pivote} es: {valor_pivote}")
        j = pos_pivote + 1
        print(f" j en pos_piv = {pos_pivote} es: {j}")
        while j < ecuaciones:
            cte_sig_fila = matrix[j][pos_pivote]
            print(f"cte_sig_fila en pos_piv={pos_pivote} y j={j} es: {cte_sig_fila}")
            print(f"La matriz antes de llamar a muktiplicar es: {matrix}")
            print(f"Valor pivote es = {valor_pivote}")
            if cte_sig_fila != 0:
                matrix[j] = multiplica_resta_filas(matrix[pos_pivote][:], matrix[j][:], valor_pivote, cte_sig_fila)
                print(f"La matrix es: {matrix}")
            j = j + 1
            print(f"J es {j}")
        pos_pivote = pos_pivote + 1
    return matrix





matriz1 = [[1, 1, 4, -1, 0, 5, 9], [4, -1, 1, -1, 6, 1, 20], [1, 0, 1, -1, 0, 1, 12], [-1, 1, 0, 0, 1, -10, -14], [6, -3, 6, -4, 5, -1, 19] , [1, 0, -1, 0, -1, -1, 25]]
num_ecs1 = 6
num_var1 = 6
matriz2 = [[1, 1, -1, 7], [2, -3, 2, 6], [3, -2, 3, 13]]
num_ecs2 = 3
num_var2 = 3
matrix3 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
num_ecs3 = 5
num_var3 = 3

print(diagonaliza_abajo(matriz1, num_ecs1, num_var1))

#print(multiplica_resta_filas(matriz[0], matriz[1], 1, 4))

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

