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

TODO
- Hacer el gauss jordan funcion
- Que retorne la expresion de infinidad de soluciones
- Hacer propiamente el programa solicitado

'''
#  --------------------------------------------------------------------------------------------------------------------
# MÓDULOS Y LIBRERÍAS IMPORTADAS

from fractions import Fraction
from sympy import symbols
#  ----------------------------------------------------------------------------------------------------------
# FUNCIONES



def transpone_matrix(matriz):
    transpuesta = []
    for i in range(len(matriz[0])):
        transpuesta.append([])
        for j in range(len(matriz)):
            transpuesta[i].append(matriz[j][i])
    return transpuesta


def genera_vectores(num_pl, pl,expresion):
    vect = []
    for j in range (0, num_pl):
        diccionario = {}
        for i in range(0, num_pl):
            if i == j:
                diccionario [pl[i]] = 1
            else:
                diccionario [pl[i]] = 0
        aux = []
        for exp in expresion:
            aux.append(Fraction(float(exp.subs(diccionario))).limit_denominator(1000))
        vect.append(aux)
        aux = []
    return vect

def imprimir_vectores(vect):
    for i in range(len(vect)):
        for j in range(len(vect[i])):
            if j == 0:
                print(f"({vect[i][j]}", end="")
            elif j == len(vect[i]) - 1:
                print(f",{vect[i][j]})", end="")
            else:
                print(f",{vect[i][j]}", end="")
        if i != len(vect) -1:
            print(",", end="")
    print("\n")



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


# Función que imprime la infinidad de soluciones en términos de sus parámetros libres
def definir_expresiones(matrix, num_param):
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
#  --------------------------------------------------------------------------------------------------------------------
# PROGRAMA PRINCIPAL

def sistema_ecs(matrix_aumentada, matrix_coeficientes, numero_ecs, numero_incognitas):
    filas_ceros = []
    indices_colsceros = []
    bandera_colcero = False
    for cero in range(0, numero_incognitas + 1):
        filas_ceros.append(0)

    cols_cero = []
    for cero in range(0, numero_ecs):
        cols_cero.append(0)


    #transpuesta = [n[:] for n in matrix_aumentada]
    transpuesta = transpone_matrix(matrix_aumentada)
    #print(matrix_aumentada)
    #print(transpuesta)
    if transpuesta.count(cols_cero) > 1:
        while transpuesta.count(cols_cero) > 1:
            indices_colsceros.append(transpuesta.index(cols_cero))
            transpuesta.remove(cols_cero)
        #print(transpuesta)
        matrix_aumentada = transpone_matrix(transpuesta)
        numero_incognitas -= 1
        bandera_colcero = True
    
    """
    print(transpuesta)
    print(indices_colsceros)
    """

    # Calcula el rango de la matriz aumentada y de coeficientes
    matrix_aumentada = pivote_distinto_cero(matrix_aumentada, numero_ecs, 0, 0)
    diagonaliza_abajo(matrix_aumentada, numero_ecs, numero_incognitas)
    diagonaliza_abajo(matrix_coeficientes, numero_ecs, numero_incognitas)
    """
    print(f"aumentada {matrix_aumentada}")
    print(f"num_inc = {numero_incognitas}")
    """
    for ind in range(0, len(matrix_coeficientes)):
        matrix_coeficientes[ind] = matrix_aumentada[ind][0:numero_incognitas]
    rango_aumentada = calcula_range(matrix_aumentada)
    rango_coeficientes = calcula_range(matrix_coeficientes)
    """
    print(f"aumentada {matrix_aumentada}")
    print(f"coef {matrix_coeficientes}")
    print(f"rango_aumentada = {rango_aumentada}")
    print(f"rango_coeficientes = {rango_coeficientes}")
    """

    # Clasifica al sistema
    if rango_aumentada == rango_coeficientes and rango_aumentada == numero_incognitas:
        if (matrix_aumentada[-2][0:-2] == matrix_aumentada[-1][0:-2]) and (
            matrix_aumentada[-2][-2:] != matrix_aumentada[-1][-2:]) and not(filas_ceros in matrix_aumentada) :
            return False

        else:
            filas_ceros.pop()
            if bandera_colcero:
                for i in indices_colsceros:
                    filas_ceros.insert(i,1)
            print(filas_ceros)
            return list(filas_ceros)

    elif rango_aumentada == rango_coeficientes and rango_aumentada < numero_incognitas:
        numero_parametros = numero_incognitas - rango_aumentada
        f_eliminadas = elimina_fila_cero(matrix_aumentada, numero_incognitas + 1)
        numero_ecsact = numero_ecs - f_eliminadas
        diagonal_uno(matrix_aumentada, numero_ecsact, numero_incognitas)
        diagonaliza_arriba(matrix_aumentada, numero_ecsact, numero_incognitas)
        diagonal_uno(matrix_aumentada, numero_ecsact, numero_incognitas)
        simb, exp = definir_expresiones(matrix_aumentada, numero_parametros)
        vectores = genera_vectores(numero_parametros, simb, exp)

        if bandera_colcero:
            #vectores_colcero = []
            filas_ceros.pop()
            for j, i in enumerate(indices_colsceros):
                vectores[j].insert(i,0)
            for j in indices_colsceros:
                aux_fc = filas_ceros[:]
                aux_fc[j] = 1
                vectores.append(aux_fc)

        imprimir_vectores(vectores)
        return numero_parametros, simb, exp, bandera_colcero

    elif rango_aumentada != rango_coeficientes:
        print("sin sol")
        return False

"""
matrix_aumentada = [[1,-1,1,1,1,0], [-2,4,3,-1,2,0], [-1,3,4,0,3,0]]
matrix_coeficientes = [[1,-1,1,1,1], [-2,4,3,-1,2], [-1,3,4,0,3]]
numero_ecs = 3
numero_inco = 5
"""

"""
matrix_aumentada = [[1,-1,2,0,1,0], [3,-1,3,0,0,0], [2,4,0,0,0,0], [-1,0,0,0,0,0]]
matrix_coeficientes = [[1,-1,2,0,1], [3,-1,3,0,0], [2,4,0,0,0], [-1,0,0,0,0]]
numero_ecs = 4
numero_inco = 5
"""
matrix_aumentada = [[2,-1,0,3,0], [4,-2,0,6,0], [-6,-3,0,-9,0]]
matrix_coeficientes = [[2,-1,0,3], [4,-2,0,6], [-6,-3,0,-9]]
numero_ecs = 3
numero_inco = 4
print(matrix_aumentada)
sistema_ecs(matrix_aumentada, matrix_coeficientes, numero_ecs, numero_inco)