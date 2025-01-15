'''
                                LIBRERÍAS DE SISTEMAS DE ECUACIONES
@author: Rodrigo Trejo
'''
#  --------------------------------------------------------------------------------------------------------------------
# MÓDULOS Y LIBRERÍAS IMPORTADAS

from fractions import Fraction
#  ----------------------------------------------------------------------------------------------------------
# FUNCIONES

def filapiv_uno(array, pospiv):
    cte = 1/array[pospiv]
    for iterador in range(0, len(array)):
        array[iterador] = array[iterador] * cte
    return array

# Función que verifica que el pivote no sea cero y si lo es, cambia de lugar la fila
def pivote_distinto_cero(matrix1, ecuaciones, arrayde_arrays, elemento):
    ciclos = 0
    while matrix1[arrayde_arrays][elemento] == 0:
        aux = matrix1[arrayde_arrays]
        matrix1.pop(arrayde_arrays)
        matrix1.insert(ecuaciones, aux)
        if ciclos == ecuaciones:
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

        if valor_pivote != 0:
            matrix[pos_pivote] = filapiv_uno(matrix[pos_pivote][:], pos_pivote)
            valor_pivote = matrix[pos_pivote][pos_pivote]
        j = pos_pivote + 1

        while j < ecuaciones:
            cte_sig_fila = matrix[j][pos_pivote]
            if cte_sig_fila != 0:
                matrix[j] = multiplica_resta_filas(matrix[pos_pivote][:], matrix[j][:], valor_pivote, cte_sig_fila)
            j = j + 1
        pos_pivote = pos_pivote + 1
    return matrix


# Función que calcula el rango de una matriz
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


# Función que hace ceros arriba de la diagonal
def diagonaliza_arriba(matrix, ecuaciones, variables):
    limite_pivote = 0
    if ecuaciones < variables:
        limite_pivote = ecuaciones
    elif variables < ecuaciones or variables == ecuaciones:
        limite_pivote = variables

    pos_pivote = limite_pivote - 1
    while pos_pivote >= 0:
        valor_pivote = matrix[pos_pivote][pos_pivote]
        if valor_pivote == 0:
            pivote_distinto_cero(matrix, ecuaciones, pos_pivote, pos_pivote)
            valor_pivote = matrix[pos_pivote][pos_pivote]
        if valor_pivote != 0:
            matrix[pos_pivote] = filapiv_uno(matrix[pos_pivote][:], pos_pivote)
            valor_pivote = matrix[pos_pivote][pos_pivote]
        j = pos_pivote - 1
        while j >= 0:
            cte_sig_fila = matrix[j][pos_pivote]
            if cte_sig_fila != 0:
                matrix[j] = multiplica_resta_filas(matrix[pos_pivote][:], matrix[j][:], valor_pivote, cte_sig_fila)
            j = j - 1
        pos_pivote = pos_pivote - 1
    return matrix


# Función que hace unos la diagonal
def diagonal_uno(matriz, ecuaciones, variables3):
    r = 0
    t = 0
    while r < ecuaciones:
        constante = matriz[r][r]
        while t <= variables3:
            matriz[r][t] = round(matriz[r][t]/constante, 10)
            t = t + 1
        t = 0
        r = r + 1
    return matriz


# Función que elimina las filas de "puros ceros" en la matriz aumentada
def elimina_fila_cero(matrix, elementos):
    filas_eliminadas = 0
    fila_cero = []
    for cero in range(0, elementos):
        fila_cero.append(0)
    filas_cero = matrix.count(fila_cero)
    for eliminador in range(0, filas_cero):
        matrix.remove(fila_cero)
        filas_eliminadas = filas_eliminadas + 1
    return filas_eliminadas


def define_solucion(matrix):
    global numero_incognitas
    sols = []
    for linea in matrix:
        suma = 1
        for i, elemento in enumerate(linea):
            if i == len(linea) -1:
                suma += elemento
            else:
                suma -= elemento
        sols.append(Fraction(suma).limit_denominator(1000))
        numero_incognitas -= 1
    return sols

def sistema_ecs(matrix_aumentada, matrix_coeficientes, numero_ecs):
    global numero_incognitas
    # Calcula el rango de la matriz aumentada y de coeficientes
    matrix_aumentada = pivote_distinto_cero(matrix_aumentada, numero_ecs, 0, 0)
    diagonaliza_abajo(matrix_aumentada, numero_ecs, numero_incognitas)
    diagonaliza_abajo(matrix_coeficientes, numero_ecs, numero_incognitas)
    for ind in range(0, len(matrix_coeficientes)):
        matrix_coeficientes[ind] = matrix_coeficientes[ind][0:numero_incognitas]
    rango_aumentada = calcula_range(matrix_aumentada)
    rango_coeficientes = calcula_range(matrix_coeficientes)

    # Clasifica al sistema

    

    if rango_aumentada == rango_coeficientes and rango_aumentada < numero_incognitas:
        f_eliminadas = elimina_fila_cero(matrix_aumentada, numero_incognitas + 1)
        numero_ecs = numero_ecs - f_eliminadas
        diagonaliza_arriba(matrix_aumentada, numero_ecs, numero_incognitas)
        diagonal_uno(matrix_aumentada, numero_ecs, numero_incognitas)
        soluciones = define_solucion(matrix_aumentada)
        for i in range(0, numero_incognitas):
            soluciones.append(1)
        print(soluciones)

    elif rango_aumentada != rango_coeficientes:
        print('\nEl sistema no tiene solución, observa la matriz \U0001F910!!!')
        print(matrix_aumentada)
#  --------------------------------------------------------------------------------------------------------------------
# PROGRAMA PRINCIPAL

"""
#numero_ecs = 3
#numero_incognitas = 5
#matrix_aumentada = [[1,-1,1,1,1,7],[-2,4,3,-1,2,-2],[-1,3,4,0,3,5]]
#matrix_coeficientes = [[1,-1,1,1,1],[-2,4,3,-1,2],[-1,3,4,0,3]]
"""

numero_ecs = 3
numero_incognitas = 3
matrix_aumentada = [[1,2,3,9],[4,5,6,24],[2,7,12,30]]
matrix_coeficientes = [[1,2,3],[4,5,6],[2,7,12]]

"""
numero_ecs = 4
numero_incognitas = 4
matrix_aumentada = [[4,-5,3,-4,28],[3,2,-4,5,12],[8,-10,6,-8,56],[7,-3,-1,1,40]]
matrix_coeficientes = [[4,-5,3,-4],[3,2,-4,5],[8,-10,6,-8],[7,-3,-1,1]]
"""
sistema_ecs(matrix_aumentada, matrix_coeficientes, numero_ecs)