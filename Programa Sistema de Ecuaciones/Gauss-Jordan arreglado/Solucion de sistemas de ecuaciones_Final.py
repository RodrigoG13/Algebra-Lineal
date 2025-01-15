'''
INSTITUTO POLITÉCNICO NACIONAL
ESCUELA SUPERIOR DE CÓMPUTO

INGENIERÍA EN INTELIGENCIA ARTIFICIAL

ÁLGEBRA LINEAL
RESOLUCIÓN DE SISTEMAS DE ECUACIONES POR EL MÉTODO DE GAUSS-JORDAN

GRUPO: 2BM1
@author: Rodrigo Gerardo Trejo Arriaga

ESTE PROGRAMA RESUELVE UN SISTEMA DE ECUACIONES POR EL MÉTODO DE GAUSS-JORDAN INDICANDO SI:
i) TIENE SOLUCIÓN ÚNICA (PRESENTÁNDOLA)
ii) TIENE INFINIDAD DE SOLUCIONES, DÁNDOLAS EN TÉRMINOS DE PARÁMETROS LIBRES
iii) NO TIENE SOLUCIÓN

ÚLTIMA MODIFICACIÓN: 01/03/2022
'''
#  --------------------------------------------------------------------------------------------------------------------
# MÓDULOS Y LIBRERÍAS IMPORTADAS

from fractions import Fraction
#  ----------------------------------------------------------------------------------------------------------
# FUNCIONES


def almacena_variables(ecuacion_string):            # "-w+6x+2y=2"
    """
    Almacena las variables introducidas por el usuario de un string a un array
    :param ecuacion_string: (String) String con la ecuación introducida
    :return variables_array: (list) Lista con las variables que introdujo el usuario
    """
    guion = "-"
    newstring = ''.join([i for i in ecuacion_string if i.isalpha()])    # "wxy"
    var_string = guion.join(newstring)              # "w-x-y"
    variables_array = var_string.split("-")         # ["w", "x", "y"]
    return variables_array


def convierte_ecuacion_fila(ecuacion_string):      # "-w+6x+2y=2"
    """
    Convierte una ecuación a una fila de una matriz
    :param ecuacion_string: (String) String con la ecuación introducida
    :return fila: (list) Lista con los coeficientes (con signo) de la ecuacion
    """
    uno_string = "1"
    fila = []
    signo_mas = "+"
    signo_menos = "-"
    uno_positivo = "+1"
    uno_negativo = "-1"
    ecuacion_string = ecuacion_string.lower()
    ecuacion_string = ecuacion_string.replace("=", "x")     # "-w+6x+2yx2"
    for a in range(97, 123):
        signo_mas_letra = signo_mas + chr(a)        # "+w"
        signo_menos_letra = signo_menos + chr(a)    # "-w"

        if ecuacion_string.startswith(chr(a)):      # "w"
            ecuacion_string = uno_string + ecuacion_string
            ecuacion_string = ecuacion_string.replace(chr(a), "x")

        elif signo_mas_letra in ecuacion_string:    # "+w"
            uno_mas_letra = uno_positivo+"x"        # "+1x"
            ecuacion_string = ecuacion_string.replace(signo_mas_letra, uno_mas_letra)

        elif signo_menos_letra in ecuacion_string:  # "-w"
            uno_menos_letra = uno_negativo+"x"      # "-1x"
            ecuacion_string = ecuacion_string.replace(signo_menos_letra, uno_menos_letra)
            # "-w+6x+2y=2" -> "-1x+6x+2y=2"

        elif chr(a) in ecuacion_string:             # "w"
            ecuacion_string = ecuacion_string.replace(chr(a), "x")

            # "-1x+6x+2xx2"

    ecuacion_string = ecuacion_string.split("x")   # ["-1","+6","+2","","2"]
    ecuacion_string.remove("")                     # ["-1","+6","+2","2"]
    for numero in ecuacion_string:
        fila.append(float(numero))
    return fila                                    # [-1, 6, 2 , 2]


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


def intercambia_columnas(matriz, pos_pivote):
    """
    Intercambia columnas en la matriz Gauss-Jordan para obtener un pivote diferente de cero
    :param matriz: (list) Matriz Gauss-Jordan
    :param pos_pivote: (int) posicion del pivote que nos interesa que no sea cero
    :param dict_var: (dict) Diccionario con las variables del sistema y su posicion en la matriz
    :return matriz_intercambio: (list) Matriz con las columnas intercambiadas
    """
    global variables
    transpuesta = transpone_matrix(matriz)
    for i in range(len(transpuesta)-pos_pivote-1):
        if transpuesta[pos_pivote+i][pos_pivote] != 0:
            aux1 = transpuesta[pos_pivote]
            aux2 = transpuesta[pos_pivote + i]
            pos1 = variables[pos_pivote]
            pos2 = variables[pos_pivote+i]
            variables[pos_pivote] = pos2
            variables[pos_pivote+i] = pos1
            transpuesta[pos_pivote] = aux2
            transpuesta[pos_pivote+i] = aux1
            matriz_intercambio = transpone_matrix(transpuesta)
            break
    return matriz_intercambio


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
        if valor_pivote == 0:
            pivote_distinto_cero(matrix, ecuaciones, pos_pivote, pos_pivote)
            if fila_cero in matrix:
                break
            valor_pivote = matrix[pos_pivote][pos_pivote]
            if valor_pivote == 0:
                matrix = intercambia_columnas(matrix, pos_pivote)
                valor_pivote = matrix[pos_pivote][pos_pivote]
            if valor_pivote == 0:
                pivote_distinto_cero(matrix, ecuaciones, pos_pivote, pos_pivote)
                valor_pivote = matrix[pos_pivote][pos_pivote]
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


def diagonaliza_arriba(matrix, ecuaciones, variables):
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
            matrix = intercambia_columnas(matrix, pos_pivote)
            valor_pivote = matrix[pos_pivote][pos_pivote]
        if valor_pivote == 0:
            pivote_distinto_cero(matrix, ecuaciones, pos_pivote, pos_pivote)
            valor_pivote = matrix[pos_pivote][pos_pivote]
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


def imprime_soluciones_infinitas(matrix, literales, num_param, param):
    """
    Escribe las soluciones infinitas utilizando symbols en un arreglo
    :param matrix: (list) Matriz a la que se le aplicó Gauss-Jordan
    :param num_param: (int) Número de parámetros libres que saldrán en las soluciones infinitas
    :return literales: (list) Lista con los parámetros libres en symbols utilizados para las soluciones infinitas
    :return param: (list) Lista con los lambdas para imprimir soluciones infinitas
    """ 
    comienzo = len(matrix[0]) - num_param
    p_l = 0
    bucles = 0
    for indice, ecuacion in enumerate(matrix):
        if matrix[indice][-1] == 0:
            print(f"{literales[indice]} = ", end="")
        else:
            print(f"{literales[indice]} = {matrix[indice][-1]}", end="")
        for p in range(comienzo, len(matrix[0])):
            if matrix[indice][p - 1] < 0:
                print("+", end="")
            print(f"{-matrix[indice][p - 1]}{param[p_l]}", end="")
            p_l = p_l + 1
        print("\n")
        p_l = 0

    p_l = 0
    print("O, en términos fraccionarios: ")
    for indice, ecuacion in enumerate(matrix):
        if matrix[indice][-1] == 0:
            print(f"{literales[indice]} ≈ ", end="")
        else:
            print(f"{literales[indice]} ≈ {Fraction(matrix[indice][-1]).limit_denominator(1000)}", end="")
        for p in range(comienzo, len(matrix[0])):
            if matrix[indice][p - 1] < 0:
                print("+", end="")
            print(f"{-Fraction(matrix[indice][p - 1]).limit_denominator(1000)}{param[p_l]}", end="")
            p_l = p_l + 1
        print("\n")
        bucles = bucles + 1
        p_l = 0

    for g in range(0, bucles):
        literales.pop(0)
#  --------------------------------------------------------------------------------------------------------------------
# PROGRAMA PRINCIPAL

if __name__ == "__main__":
    matrix_aumentada = []
    matrix_coeficientes = []
    variables = []
    filas_ceros = []
    parametros = ["λ\u2081", "λ\u2082", "λ\u2083", "λ\u2084", "λ\u2085", "λ\u2086", "λ\u2087", "λ\u2088", "λ\u2089"]

    print("                             ***SOLUCIÓN DE SISTEMAS DE ECUACIONES POR GAUSS-JORDAN***\n")
    print("Instrucciones: Ingresa el sistema de ecuaciones con diferentes literales (...x,y,z), sin espacios"
        " y en un mismo orden.\n"
        "Por ejemplo: ax+by+cz=d\n"
        "             ex+fy+gz=h          Donde a,b,c,d,e,f,g,h,i,j,k,l ∈ ℝ\n"
        "             ix+jy+kz=l\n")
    print("NOTA: Incluye todas las variables incluso si su coeficiente es 0 (cero).")
    numero_ecs = int(input("¿Cuántas ecuaciones deseas ingresar?: "))
    numero_incognitas = int(input("¿De cuántas variables?: "))

    for cero in range(0, numero_incognitas + 1):
        filas_ceros.append(0)

    dict_posicional = {}
    for i in range(0, numero_incognitas):
                    # variable, posicion
        dict_posicional[i] = i

    # Recibe datos
    s = 0
    while s < numero_ecs:
        ecuacion_str = input(f"Ec{s+1})     ")
        ecuacion_array = convierte_ecuacion_fila(ecuacion_str)
        while len(ecuacion_array) < numero_incognitas + 1:
            print(f'La ecuación no tiene el numero correcto de variables, inténtalo nuevamente \U0001F61E.')
            ecuacion_str = input(f"Ec{s + 1})     ")
            ecuacion_array = convierte_ecuacion_fila(ecuacion_str)
        matrix_aumentada.append(ecuacion_array)
        matrix_coeficientes.append(ecuacion_array)
        if s == 0:
            variables = almacena_variables(ecuacion_str)
        s = s+1

    # Calcula el rango de la matriz aumentada y de coeficientes
    matrix_coeficientes = pivote_distinto_cero(matrix_coeficientes, numero_ecs, 0, 0)
    matrix_aumentada = pivote_distinto_cero(matrix_aumentada, numero_ecs, 0, 0)
    matrix_aumentada = diagonaliza_abajo(matrix_aumentada, numero_ecs, numero_incognitas)

    for ind in range(0, len(matrix_coeficientes)):
        matrix_coeficientes[ind] = matrix_aumentada[ind][0:numero_incognitas]
    rango_aumentada = calcular_range(matrix_aumentada)
    rango_coeficientes = calcular_range(matrix_coeficientes)

    # Clasifica al sistema
    if rango_aumentada == rango_coeficientes and rango_aumentada == numero_incognitas:
        if (matrix_aumentada[-2][0:-2] == matrix_aumentada[-1][0:-2]) and (
            matrix_aumentada[-2][-2:] != matrix_aumentada[-1][-2:]) and not(filas_ceros in matrix_aumentada) :
            print('\nEl sistema no tiene solución, observa la matriz \U0001F910!!!')
            print(matrix_aumentada)

        else:    
            if filas_ceros in matrix_aumentada:
                numero_fceros = matrix_aumentada.count(filas_ceros)
                for n in range(0, numero_fceros):
                    matrix_aumentada.remove(filas_ceros)
                numero_ecs = numero_ecs - numero_fceros
            matrix_aumentada = diagonaliza_arriba(matrix_aumentada, numero_ecs, numero_incognitas)
            diagonal_uno(matrix_aumentada, numero_ecs, numero_incognitas)
            print('\nEl sistema tiene una única solución \U0001F642')
            print("Solución del sistema:")
            v = 0
            while v < len(matrix_aumentada):
                print(f"\t{variables[v]} = {matrix_aumentada[v][-1]} ≈ ", end="")
                print(f"{Fraction(matrix_aumentada[v][-1]).limit_denominator(1000)}")
                v = v + 1

    elif rango_aumentada == rango_coeficientes and rango_aumentada < numero_incognitas:
        print('\nEl sistema tiene infinidad de soluciones \U0001F914')
        numero_parametros = numero_incognitas - rango_aumentada
        f_eliminadas = elimina_fila_cero(matrix_aumentada, numero_incognitas + 1)
        numero_ecs = numero_ecs - f_eliminadas
        matrix_aumentada = diagonaliza_arriba(matrix_aumentada, numero_ecs, numero_incognitas)
        diagonal_uno(matrix_aumentada, numero_ecs, numero_incognitas)
        print(f"En términos de parámetros libres la solución es: ")
        imprime_soluciones_infinitas(matrix_aumentada, variables, numero_parametros, parametros)

        print("Donde: ")
        for ind, variable in enumerate(variables):
            print(f"{variable} = {parametros[ind]}")

    elif rango_aumentada != rango_coeficientes:
        print('\nEl sistema no tiene solución, observa la matriz \U0001F910!!!')
        print(matrix_aumentada)