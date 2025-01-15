'''
                            LIBRERÍA DE BASES PARA LA NULIDAD DE UNA MATRIZ
@author: Rodrigo Gerardo Trejo Arriaga
'''
#  -------------------------------------------------------------------------------------------------
# MÓDULOS Y LIBRERÍAS IMPORTADAS

from fractions import Fraction
from gj_nulidad_i2 import *

#  -------------------------------------------------------------------------------------------------
# FUNCIONES


def genera_vectores(num_pl, pl,expresiones):
    """
    Genera los vectores que conforman la base del espacio nulo
    :param num_pl: (int) Numero de parámetros libres que resultaron del sistema de ecs
    :param pl: (list) Lista con los parametros libres en formato symbol
    :param expresiones: (lista) Lista con las expresiones en terminos de parámetros libres
    :retur vect: (list) Lista con los vectores numéricos de la base del espacio nulo
    """
    vect = []
    for j in range (0, num_pl):
        diccionario = {}
        for i in range(0, num_pl):
            if i == j:
                diccionario [pl[i]] = 1
            else:
                diccionario [pl[i]] = 0
        aux = []
        for exp in expresiones:
            if type(exp) == int:
                aux.append(exp)
            else:
                aux.append(Fraction(float(exp.subs(diccionario))).limit_denominator(1000))
        vect.append(aux)
        aux = []
    return vect


def imprimir_vectores(vect):
    """
    Imprime los vectores resultantes de la base del espcio nulo
    :param vect: (list) Vectores a imprimir
    :return: (None) La impresión se realiza de manera interna
    """
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
    array_str = string_num.split(" ")
    for numero in array_str:
        array_num.append(float(numero))
    return array_num


def nulidad(matrix_vect):
    numero_fil = len(matrix_vect)
    numero_col = len(matrix_vect[0])
    cero_vector = []
    matrix_copy = [n[:] for n in matrix_vect]
    for i in matrix_vect:
        i.append(0)
    for i in range(0, numero_col):
        cero_vector.append(0)
    soluciones = sistema_ecs(matrix_vect, matrix_copy, numero_fil, numero_col)
    if type(soluciones) == tuple:
        numero_parametros, simb, exp = soluciones
        vectores = genera_vectores(numero_parametros, simb, exp)
        return vectores
    else:
        return list(soluciones)
