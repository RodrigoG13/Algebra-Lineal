#  --------------------------------------------------------------------------------------------------------------------
# MÓDULOS Y LIBRERÍAS IMPORTADAS

from fractions import Fraction
#  --------------------------------------------------------------------------------------------------------------------


# Función que verifica que el pivote no sea cero y si lo es, cambia de lugar la fila
def pivote_distinto_cero(matrix1, ecuaciones, arrayde_arrays, elemento):
    ciclos = 0
    while matrix1[arrayde_arrays][elemento] == 0:
        aux = matrix1[arrayde_arrays]
        matrix1.pop(arrayde_arrays)
        matrix1.insert(ecuaciones, aux)
        if ciclos == arrayde_arrays:
            break
        ciclos = ciclos + 1
    return matrix1


# Función que realiza las operaciones elementales en una matriz
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


# Función que hace ceros abajo de la diagonal
def diagonaliza_abajo(matrix, ecuaciones, variables):
    f_piv = 1
    f_sig_fila = 1
    limite_pivote = 0
    fila_cero = []
    for cero in range(0, variables):
        fila_cero.append(0)

    if ecuaciones < variables:
        limite_pivote = ecuaciones
    elif variables < ecuaciones or variables == ecuaciones:
        limite_pivote = variables

    pos_pivote = 0
    while pos_pivote < limite_pivote:
        valor_pivote = matrix[pos_pivote][pos_pivote]
        if pos_pivote + 1 == limite_pivote and valor_pivote == 0:
            break
        elif valor_pivote == 0:
            pivote_distinto_cero(matrix, ecuaciones, pos_pivote, pos_pivote)
            if fila_cero in matrix:
                break
            valor_pivote = matrix[pos_pivote][pos_pivote]
        j = pos_pivote + 1

        while j < ecuaciones:
            cte_sig_fila = matrix[j][pos_pivote]
            if cte_sig_fila != 0:
                matrix[j] = multiplica_resta_filas(matrix[pos_pivote][:], matrix[j][:], valor_pivote, cte_sig_fila)
                f_piv *= valor_pivote
            j = j + 1
        pos_pivote = pos_pivote + 1
    return f_piv


def imprime_matrix(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]}\t\t", end="")
        print("\n")


def calcula_determinante(matrix):
    multiplica_diagonal = 1
    for k in range(len(matrix)):
        multiplica_diagonal *= matrix[k][k]
    return multiplica_diagonal


matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, -7, 12], [13, -3, 15, 2]]
fraccion_pivote = 1/diagonaliza_abajo(matriz, len(matriz), len(matriz[0]))
imprime_matrix(matriz)
determinante_matrix = fraccion_pivote * calcula_determinante(matriz)
print(f"El determinante es {determinante_matrix}")
print(f"Y en fracción: {Fraction(determinante_matrix).limit_denominator(1000)}")
