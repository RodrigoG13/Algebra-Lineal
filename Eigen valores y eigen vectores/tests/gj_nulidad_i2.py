'''
            LIBRERÍA DE SOLUCIÓN DE SISTEMAS DE ECUACIONES POR GAUSS JORDAN - NULIDAD
@author: Rodrigo Gerardo Trejo Arriaga
'''
#  --------------------------------------------------------------------------------------------------------------------
# MÓDULOS Y LIBRERÍAS IMPORTADAS

from sympy import symbols
#  ----------------------------------------------------------------------------------------------------------
# FUNCIONES


def intercambia_columnas(matriz, pos_pivote, dict_var):
    """
    Intercambia columnas en la matriz Gauss-Jordan para obtener un pivote diferente de cero
    :param matriz: (list) Matriz Gauss-Jordan
    :param pos_pivote: (int) posicion del pivote que nos interesa que no sea cero
    :param dict_var: (dict) Diccionario con las variables del sistema y su posicion en la matriz
    :return matriz_intercambio: (list) Matriz con las columnas intercambiadas
    """
    transpuesta = transpone_matrix(matriz)
    matriz_intercambio = matriz
    for i in range(len(transpuesta)-pos_pivote-1):
        if transpuesta[pos_pivote+i][pos_pivote] != 0:
            aux1 = transpuesta[pos_pivote]
            aux2 = transpuesta[pos_pivote + i]
            var1 = dict_var[pos_pivote]
            var2 = dict_var[pos_pivote+i]
            dict_var[pos_pivote] = var2
            dict_var[pos_pivote+i] = var1
            transpuesta[pos_pivote] = aux2
            transpuesta[pos_pivote+i] = aux1
            matriz_intercambio = transpone_matrix(transpuesta)
            break
    return matriz_intercambio


def transpone_matrix(matriz):
    """
    Genera la matriz para el sistema de ecuaciones a partir de los vectores dados
    :param matriz: (list) Matriz de vectores ingresados por el usuario
    :return transpuesta: (list) Matriz de coeficientes para el sistema de ecuaciones
    """
    transpuesta = []
    for i in range(len(matriz[0])):
        transpuesta.append([])
        for j in range(len(matriz)):
            transpuesta[i].append(matriz[j][i])
    return transpuesta


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


def diagonaliza_abajo(matrix, ecuaciones, variables, dict_var):
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
        if valor_pivote == 0:
            pivote_distinto_cero(matrix, ecuaciones, pos_pivote, pos_pivote)
            if fila_cero in matrix:
                break
            valor_pivote = matrix[pos_pivote][pos_pivote]
            if valor_pivote == 0:
                matrix = intercambia_columnas(matrix, pos_pivote, dict_var)
                valor_pivote = matrix[pos_pivote][pos_pivote]
            if valor_pivote == 0:
                pivote_distinto_cero(matrix, ecuaciones, pos_pivote, pos_pivote)
            if valor_pivote == 0:
                break
        j = pos_pivote + 1

        while j < ecuaciones:
            cte_sig_fila = matrix[j][pos_pivote]
            if cte_sig_fila != 0:
                matrix[j] = multiplica_resta_filas(matrix[pos_pivote][:], matrix[j][:], valor_pivote, cte_sig_fila)
            j = j + 1
        pos_pivote = pos_pivote + 1
    return matrix


def calcular_range(matrix):
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


def diagonaliza_arriba(matrix, ecuaciones, variables, dict_var):
    """
    Convierte una matriz dada por el usuario en una matriz triangular superior
    :param matrix: (list) Matriz con ceros debajo de la diagonal
    :param ecuaciones: (int) Número de ecuaciones del sistema
    :param variables: (int) Número de variables del sistema
    :return matrix: (list) Matriz diagonalizada hacia arriba
    """
    limite_pivote = 0
    if ecuaciones < variables:
        limite_pivote = ecuaciones
    elif variables < ecuaciones or variables == ecuaciones:
        limite_pivote = variables
    pos_pivote = limite_pivote - 1
    while pos_pivote >= 0:
        valor_pivote = matrix[pos_pivote][pos_pivote]
        if valor_pivote == 0:
            matrix = intercambia_columnas(matrix, pos_pivote, dict_var)
            valor_pivote = matrix[pos_pivote][pos_pivote]
        if valor_pivote == 0:
            matrix = intercambia_columnas(matrix, pos_pivote, dict_var)
            valor_pivote = matrix[pos_pivote][pos_pivote]
            if valor_pivote == 0:
                break
        j = pos_pivote - 1
        while j >= 0:
            cte_sig_fila = matrix[j][pos_pivote]
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


def definir_expresiones(matrix, num_param, dict_var):
    """
    Escribe las soluciones infinitas utilizando symbols en un arreglo
    :param matrix: (list) Matriz a la que se le aplicó Gauss-Jordan
    :param num_param: (int) Número de parámetros libres que saldrán en las soluciones infinitas
    :return simbolos: (list) Lista con los parámetros libres en symbols utilizados para las soluciones infinitas
    :return expresiones: (list) Lista con las soluciones infinitas escritas com symbols
    """  
    simbolos = []
    expresion = 0
    dict_pl = {}
    encontrados = 0
    try:
        expresiones = [0 for i in range(0, len(matrix[0])-1)]
    except:
        expresiones = [0 for i in range(0, num_param)]

    for i in range(97, 123):
        simbolos.append(symbols(chr(i)))
        if len(simbolos) == num_param:
            break
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if i != j and matrix[i][j] != 0 and j not in dict_pl:
                dict_pl[j] = simbolos[encontrados]
                encontrados += 1
        if encontrados == num_param:
            break
    for i in range(0, len(matrix)):
        expresion = 0
        for j in range(0, len(matrix[0])-1):
            if i!=j and j in dict_pl.keys():
                expresion += -matrix[i][j] * dict_pl[j]
        expresiones[dict_var[i]] = expresion
        expresion = 0
    for pos, var in dict_pl.items():
        expresiones[dict_var[pos]] = var
    tranpuesta = transpone_matrix(matrix)
    col_ceros = [0 for i in range(0, len(tranpuesta[0]))]
    if tranpuesta.count(col_ceros) > 1:
        posiciones = [dict_var[i]  for i in range(0, len(tranpuesta)-1) if tranpuesta[i] == col_ceros]
        k = 0
        for i in range(encontrados, num_param):
            expresiones[posiciones[k]] = simbolos[i]
            k += 1
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
    dict_var = {}
    for i in range(0, numero_incognitas):
        # Variable, pos
        dict_var[i] = i
    filas_ceros = []
    for cero in range(0, numero_ecs+1):
        filas_ceros.append(0)
    
    # Calcula el rango de la matriz aumentada y de coeficientes
    matrix_aumentada = pivote_distinto_cero(matrix_aumentada, numero_ecs, 0, 0)
    if matrix_aumentada[0][0] == 0:
        matrix_aumentada = intercambia_columnas(matrix_aumentada, 0, dict_var)
    matrix_aumentada = diagonaliza_abajo(matrix_aumentada, numero_ecs, numero_incognitas, dict_var)
    for ind in range(0, len(matrix_coeficientes)):
        matrix_coeficientes[ind] = matrix_aumentada[ind][0:numero_incognitas]
    rango_aumentada = calcular_range(matrix_aumentada)
    rango_coeficientes = calcular_range(matrix_coeficientes)

    # Clasifica al sistema
    if rango_aumentada == rango_coeficientes and rango_aumentada == numero_incognitas:
        filas_ceros.pop()

    elif rango_aumentada == rango_coeficientes and rango_aumentada < numero_incognitas:
        numero_parametros = numero_incognitas - rango_aumentada
        f_eliminadas = elimina_fila_cero(matrix_aumentada, numero_incognitas + 1)
        numero_ecsact = numero_ecs - f_eliminadas
        matrix_aumentada = diagonaliza_arriba(matrix_aumentada, numero_ecsact, numero_incognitas, dict_var)
        diagonal_uno(matrix_aumentada, numero_ecsact, numero_incognitas)
        simb, exp = definir_expresiones(matrix_aumentada, numero_parametros, dict_var)
        return numero_parametros, simb, exp