'''
            LIBRERÍA DE SOLUCIÓN DE SISTEMAS DE ECUACIONES POR GAUSS JORDAN - NULIDAD
@author: Rodrigo Gerardo Trejo Arriaga
'''
#  --------------------------------------------------------------------------------------------------------------------
# MÓDULOS Y LIBRERÍAS IMPORTADAS

from fractions import Fraction
from sympy import symbols
bandera = 0
# bandera = 1 -> valor_piv = 0, pospiv +1 -> valor != 0
pospivote = []

#  ----------------------------------------------------------------------------------------------------------
# FUNCIONES


def transpone_matrix(matriz):
    """
    Genera la matriz para el sistema de ecuaciones a partir de los vectores dados
    :param matriz: (list) Matriz de vectores ingresados por el usuario
    :return: (list) Matriz de coeficientes para el sistema de ecuaciones
    """
    transpuesta = []
    for i in range(len(matriz[0])):
        transpuesta.append([])
        for j in range(len(matriz)):
            transpuesta[i].append(matriz[j][i])
    return transpuesta


def filapiv_uno(array, pospiv):
    """
    Divide una fila entre el valor del pivote para hacerlo 1 y facilitar el proceso de Gauss Jordan
    :param array: (string) Fila a la que se aplicará la operación elemental
    :param pospiv: (int) Posición del pivote
    :return array: (list) Fila con el pivote en valor = 1
    """
    cte = 1/array[pospiv]
    for iterador in range(0, len(array)):
        array[iterador] = array[iterador] * cte
    return array


def pivote_distinto_cero(matrix1, ecuaciones, arrayde_arrays, elemento):
    """
    Verifica que el pivote no sea cero y si lo es, cambia de lugar la fila
    :param matrix1: (list) Matriz en la que se harán los cambios de filas
    :param ecuaciones: (int) Número de ecuaciones del sistema
    :param arrayde_arrays: (int) Número de columnas en la matriz
    :param elemento: (int) Posición del pivote en la fila dada
    :return matrix1: (list) Matriz con las filas intercambiadas
    """
    ciclos = 0
    while matrix1[arrayde_arrays][elemento] == 0:
        aux = matrix1[arrayde_arrays]
        matrix1.pop(arrayde_arrays)
        matrix1.insert(ecuaciones, aux)
        if ciclos == ecuaciones:
            break
        ciclos = ciclos + 1
    return matrix1


def multiplica_resta_filas(array1, array2, constante1, constante2):
    """
    Realiza las operaciones elementales para una matriz
    :param array1: (list) Fila 1 con la que se efectuarán las operaciones
    :param array2: (list) Fila 2 con la que se efectuarán las operaciones
    :param constante1: (int) Valor del pivote para hacer ceros abajo de él
    :param constante1: (int) Valor de la fila necesaria para hacer cero sun elemento
    :return array2: (list) Fila que recibió los cambios de las operaciones
    """
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
    """
    Convierte una matriz dada por el usuario en una matriz triangular superior
    :param matrix: (list) Matriz dada por el usuario
    :param ecuaciones: (int) Número de ecuaciones del sistema
    :param variables: (int) Número de variables del sistema
    :return matrix: (list) Matriz Triangular superior
    """
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


def calcula_range(matrix):
    """
    Calcula el rango de una matriz
    :param matrix: (list) Matriz con ceros por debajo de la diagonal
    :return range_matrix: (int) Rango de la matriz ingresada
    """
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


def diagonaliza_arriba(matrix, ecuaciones, variables):
    """
    Convierte una matriz dada por el usuario en una matriz triangular superior
    :param matrix: (list) Matriz con ceros debajo de la diagonal
    :param ecuaciones: (int) Número de ecuaciones del sistema
    :param variables: (int) Número de variables del sistema
    :return matrix: (list) Matriz diagonalizada hacia arriba
    """
    global bandera
    global pospivote

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
        if valor_pivote == 0:
            bandera = 1
            pospivote.append(pos_pivote)
        if valor_pivote != 0:
            matrix[pos_pivote] = filapiv_uno(matrix[pos_pivote][:], pos_pivote)
            valor_pivote = matrix[pos_pivote][pos_pivote]
        if bandera == 1:
            matrix[pos_pivote] = filapiv_uno(matrix[pos_pivote][:], pos_pivote + 1)
            valor_pivote = matrix[pos_pivote][pos_pivote + 1]
        j = pos_pivote - 1
        while j >= 0:
            cte_sig_fila = matrix[j][pos_pivote]
            if bandera == 1:
                cte_sig_fila = matrix[j][pos_pivote+1]
            if cte_sig_fila != 0:
                matrix[j] = multiplica_resta_filas(matrix[pos_pivote][:], matrix[j][:], valor_pivote, cte_sig_fila)
            j = j - 1
        pos_pivote = pos_pivote - 1
    return matrix


def diagonal_uno(matriz, ecuaciones, variables3):
    """
    Convierte los elementos de la diagonal en unos, efectuando operaciones elementales
    :param matriz: (list) Matriz con elementos distintos de 1 en la diagonal
    :param ecuaciones: (int) Número de ecuaciones del sistema
    :param variable3: (int) Número de variables del sistema
    :return matrix: (list) Matriz con unos en la diagonal
    """
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


def elimina_fila_cero(matrix, elementos):
    """
    Elimina las filas cuyos elementos sean únicamente ceros de la matriz
    :param matriz: (list) Matriz a la que se le retirarán las filas de ceros
    :param elementos: (int) Número de columnas de la matriz
    :return matrix: (list) Matriz sin filas de "puros ceros"
    """
    filas_eliminadas = 0
    fila_cero = []
    for cero in range(0, elementos):
        fila_cero.append(0)
    filas_cero = matrix.count(fila_cero)
    for eliminador in range(0, filas_cero):
        matrix.remove(fila_cero)
        filas_eliminadas = filas_eliminadas + 1
    return filas_eliminadas


def definir_expresiones(matrix, num_param):
    """
    Escribe las soluciones infinitas utilizando symbols en un arreglo
    :param matrix: (list) Matriz a la que se le aplicó Gauss-Jordan
    :param num_param: (int) Número de parámetros libres que saldrán en las soluciones infinitas
    :return simbolos: (list) Lista con los parámetros libres en symbols utilizados para las soluciones infinitas
    :return expresiones: (list) Lista con las soluciones infinitas escritas com symbols
    """    
    bandera = True
    simbolos = []
    expresiones = []
    expresion = 0
    for i in range(97, 123):
        simbolos.append(symbols(chr(i)))
        if len(simbolos) == num_param:
            break
    comienzo = len(matrix[0]) - num_param
    p_l = 0
    for indice, ecuacion in enumerate(matrix):
        for p in range(comienzo, len(matrix[0])):
            expresion += -matrix[indice][p - 1] * simbolos[p_l]
            p_l = p_l + 1
        expresiones.append(expresion)
        expresion = 0
        p_l = 0
    for k in simbolos:
        expresiones.append(k)
    return simbolos, expresiones

def expresiones_b1(aumentada, num_param):
    """
    Escribe las soluciones infinitas utilizando symbols en un arreglo
    :param matrix: (list) Matriz a la que se le aplicó Gauss-Jordan
    :param num_param: (int) Número de parámetros libres que saldrán en las soluciones infinitas
    :return simbolos: (list) Lista con los parámetros libres en symbols utilizados para las soluciones infinitas
    :return expresiones: (list) Lista con las soluciones infinitas escritas com symbols
    """    
    simbolos = []
    simbolos_uso = []
    expresiones = []
    expresion = 0
    for i in range(97, 123):
        simbolos.append(symbols(chr(i)))
        simbolos_uso.append(symbols(chr(i)))
        if len(simbolos) == num_param:
            break
    for i in aumentada:
        for k in range(0, i.count(0)):
            i.remove(0)
        for k in range(0, i.count(1)):
            i.remove(1)
        
    for i in range(0, len(aumentada)):
        for j in range(0, len(aumentada[i])):
            if j == 0:
                expresion -= aumentada[i][j] * simbolos[j+i]
            else:
                expresion -= aumentada[i][j] * simbolos[j+i]
        expresiones.append(expresion)
        expresion = 0

    for i, v in enumerate(pospivote):
        expresiones.insert(v, simbolos_uso[i])
        simbolos_uso.pop(0)

    for k in simbolos_uso:
        expresiones.append(k)
    return simbolos, expresiones


def sistema_ecs(matrix_aumentada, matrix_coeficientes, numero_ecs, numero_incognitas):
    """
    Función que resolverá el sistema de ecuaciones deseado
    :param matrix_aumentada: (list) Matriz aumentada del sistema de ecuaciones
    :param matrix_coeficientes: (list) Matriz con los coeficientes del sistema de ecuaciones
    :param numero_ecs: (int) Número de ecuaciones del sistema
    :param numero_incognitas: (int) Número de variables del sistema
    :param opcion: (int) Opción para ejecutar sólo la clasificación del sistema o su resolución total
    :return soluciones: (list) Una solución al sistema de ecuaciones
    :return: (int) Opcion que sirve para indicar al programa en que categoría cayó el sistema:
                    Solución única/ Infinidad de soluciones/ Sin solución 
    """
    global bandera
    filas_ceros = []
    indices_colsceros = []
    bandera_colcero = False
    for cero in range(0, numero_incognitas + 1):
        filas_ceros.append(0)
    cols_cero = []
    for cero in range(0, numero_ecs):
        cols_cero.append(0)
    transpuesta = transpone_matrix(matrix_aumentada)
    if transpuesta.count(cols_cero) > 1:
        while transpuesta.count(cols_cero) > 1:
            indices_colsceros.append(transpuesta.index(cols_cero))
            transpuesta.remove(cols_cero)
            numero_incognitas -= 1
        matrix_aumentada = transpone_matrix(transpuesta)
        bandera_colcero = True
    
    # Calcula el rango de la matriz aumentada y de coeficientes
    matrix_aumentada = pivote_distinto_cero(matrix_aumentada, numero_ecs, 0, 0)
    diagonaliza_abajo(matrix_aumentada, numero_ecs, numero_incognitas)
    diagonaliza_abajo(matrix_coeficientes, numero_ecs, numero_incognitas)
    for ind in range(0, len(matrix_coeficientes)):
        matrix_coeficientes[ind] = matrix_aumentada[ind][0:numero_incognitas]
    rango_aumentada = calcula_range(matrix_aumentada)
    rango_coeficientes = calcula_range(matrix_coeficientes)

    # Clasifica al sistema
    if rango_aumentada == rango_coeficientes and rango_aumentada == numero_incognitas:
        filas_ceros.pop()
        if bandera_colcero:
            for i in indices_colsceros:
                filas_ceros.pop()
                filas_ceros.insert(i,1)
        return list(filas_ceros)

    elif rango_aumentada == rango_coeficientes and rango_aumentada < numero_incognitas:
        numero_parametros = numero_incognitas - rango_aumentada
        f_eliminadas = elimina_fila_cero(matrix_aumentada, numero_incognitas + 1)
        numero_ecsact = numero_ecs - f_eliminadas
        diagonaliza_arriba(matrix_aumentada, numero_ecsact, numero_incognitas)
        try:
            diagonal_uno(matrix_aumentada, numero_ecsact, numero_incognitas)
        except:
            pass
        if bandera != 1:
            simb, exp = definir_expresiones(matrix_aumentada, numero_parametros)
        else:
            simb, exp = expresiones_b1(matrix_aumentada, numero_parametros)
        return numero_parametros, simb, exp, bandera_colcero, filas_ceros, indices_colsceros

    elif rango_aumentada != rango_coeficientes:
        return False

    else:
        f_eliminadas = elimina_fila_cero(matrix_aumentada, numero_incognitas + 1)
        matrix_aumentada = pivote_distinto_cero(matrix_aumentada, numero_ecs, 0, 0)
        numero_ecsact = numero_ecs - f_eliminadas
        diagonaliza_abajo(matrix_aumentada, numero_ecsact, numero_incognitas)
        matrix_coeficientes = []
        for ind in range(0, len(matrix_aumentada)):
            matrix_coeficientes.append(matrix_aumentada[ind][0:numero_incognitas])
        rango_aumentada = calcula_range(matrix_aumentada)
        rango_coeficientes = calcula_range(matrix_coeficientes) 
        if rango_aumentada == rango_coeficientes and rango_aumentada == numero_incognitas:
            filas_ceros.pop()
            return list(filas_ceros)