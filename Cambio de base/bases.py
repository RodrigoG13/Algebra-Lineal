'''
                            LIBRERÍA DE COMBINACIÓN LINEAL Y BASES 
@author: Rodrigo Gerardo Trejo Arriaga
'''
#  ---------------------------------------------------------------------------------------------------
# MÓDULOS Y LIBRERÍAS IMPORTADAS


from sympy import symbols
from gauss_jordan import *
#  ---------------------------------------------------------------------------------------------------
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


def convierte_string_array(string_num):
    """
    Convierte el string-vector ingresado por el usuario en una lista con los números del vector
    :param string_num: (string) String ingresado por el usuario
    :return array_num: (list) Vector ingresado por el usuario en una lista
    """
    array_num = []
    array_str = string_num.split(",")
    for numero in array_str:
        array_num.append(float(numero))
    return array_num


def combinacion_lineal(vectores, u_vector, num_elementos, num_vectores):
    """
    Verifica si un vector 'u' es combinación lineal de otro conjunto de vectores 
    :param vectores: (list) Conjunto de vectores de la combinación lineal
    :param u_vector: (list) Vector que se probará si es combinación lineal
    :param num_elementos: (int) Número de componentes de los vectores
    :param num_vectores: (int) Número de vectores del conjunto
    :return array_num: (list/bool) Si es una combinación lineal devuelve los factores
                                Si no es una combinación lineal devuelve False
    """
    comb_lineal_coef = [n[:] for n in vectores]
    comb_lineal_coef = transpone_matrix(comb_lineal_coef)
    combinacion_lineal = [n[:] for n in comb_lineal_coef]
    for indice, lista in enumerate(combinacion_lineal):
        lista.append(u_vector[indice])
    solucion_sistema, bandera = sistema_ecs(combinacion_lineal, comb_lineal_coef, num_elementos, num_vectores, 1)
    if len(solucion_sistema) != 0:
        return solucion_sistema
    else:
        return False

def espacio_generado(vectores, num_elementos, num_vectores):
    """
    Verifica si un conjunto de vectores generan ℝ^n
    :param vectores: (list) Conjunto de vectores que se probará si generan o no
    :param num_elementos: (int) Número de componentes de los vectores
    :param num_vectores: (int) Número de vectores del conjunto
    :return array_num: (bool) True -> Genera / False -> No genera
    """
    simbolos = []
    for i in range(97, 123):
        simbolos.append(symbols(chr(i)))
    simbolos_uso = simbolos[len(simbolos)-num_elementos:]
    espgen_coef = [n[:] for n in vectores]
    espgen_coef = transpone_matrix(espgen_coef)
    espacio_generador = [n[:] for n in espgen_coef]
    for indice, lista in enumerate(espacio_generador):
        lista.append(simbolos_uso[indice])
    bandera_esp_gen = sistema_ecs(espacio_generador, espgen_coef, num_elementos, num_vectores, 2)
    if bandera_esp_gen:
        return True
    else:
        return False


def independencia_lineal(vectores, num_elementos, num_vectores):
    """
    Verifica si un conjunto de vectores son linealmente independientes
    :param vectores: (list) Conjunto de vectores que se probará si son li
    :param num_elementos: (int) Número de componentes de los vectores
    :param num_vectores: (int) Número de vectores del conjunto
    :return array_num: (bool) True -> Son li / False -> No son li
    """
    ind_lineal_coef = [n[:] for n in vectores]
    ind_lineal_coef = transpone_matrix(ind_lineal_coef)
    ind_lineal = [n[:] for n in ind_lineal_coef]
    for lista in ind_lineal:
        lista.append(0)
    bandera_li = sistema_ecs(ind_lineal, ind_lineal_coef, num_elementos, num_vectores, 2)
    if bandera_li == 1:
        return True
    else:
        return False

def base(vectores, num_elementos, num_vectores):
    """
    Verifica si un conjunto de vectores son base de ℝ^n
    :param vectores: (list) Conjunto de vectores que se probará si son base
    :param num_elementos: (int) Número de componentes de los vectores
    :param num_vectores: (int) Número de vectores del conjunto
    :return array_num: (bool) True -> Son base / False -> No son base
    """
    bandera_esp_gen = espacio_generado(vectores, num_elementos, num_vectores)
    bandera_li = independencia_lineal(vectores, num_elementos, num_vectores)
    if bandera_esp_gen and bandera_li:
        return True
    else:
        return False