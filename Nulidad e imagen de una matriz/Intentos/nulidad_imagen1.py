'''
INSTITUTO POLITÉCNICO NACIONAL
ESCUELA SUPERIOR DE CÓMPUTO

INGENIERÍA EN INTELIGENCIA ARTIFICIAL

ÁLGEBRA LINEAL
BASES DEL ESPACIO NULO E IMAGEN DE UNA MATRIZ MXN

GRUPO: 2BM1
@author: Rodrigo Gerardo Trejo Arriaga

ESTE PROGRAMA RECIBE UNA MATRIZ MXN Y CALCULA LO SIGUIENTE:
i) UNA BASE PARA EL ESPACIO NULO DE DICHA MATRIZ
ii) UNA BASE PARA LA IMAGEN DE LA MATRIZ

FECHA DE INICIO DE PROYECTO: 05/05/2022
ÚLTIMA MODIFICACIÓN: 07/05/2022
'''
#  -------------------------------------------------------------------------------------------------
# MÓDULOS Y LIBRERÍAS IMPORTADAS

from itertools import combinations
from fractions import Fraction
from sympy import symbols
from gj_indlineal import *
import os
from sub_super import *
from gj_nulidad import *
#  -------------------------------------------------------------------------------------------------
# FUNCIONES


def independencia_lineal(vectores):
    """
    Verifica si un conjunto de vectores son linealmente independientes
    :param vectores: (list) Lista de vectores que pueden ser li
    :retur bandera_li: (int) 1 -> Son Li / 0 -> No son Li
    """
    vectores_copy = [n[:] for n in vectores]
    for vector in vectores:
        vector.append(0)
    bandera_li = sistema_ecs_li(vectores, vectores_copy, len(vectores), len(vectores[0])-1, 2)
    return bandera_li


def verificar_li(vect, cant_vect):
    """
    Genera todas las combinaciones posibles de vectores que pueden ser Li
    :param vect: (list) Lista de vectores a combinar
    :param cant_vect: (int) Cantidad de vectores que tendrá la combinatoria
    :retur vectores_comb: (list) Lista de vectores que son Li
    """
    for combinacion in combinations(vect, cant_vect):
        vectores_comb = list(combinacion)
        vc_copy = [n[:] for n in vectores_comb]
        es_li = independencia_lineal(vc_copy)
        if es_li == 1:
            return vectores_comb


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

#  ---------------------------------------------------------------------------------------------------
# PROGRAMA PRINCIPAL

repetir = "si"
while repetir == "si":
    os.system("cls")
    print("\t\t\t\t***NULIDAD E IMAGEN DE UNA MATRIZ***\n")
    print("Instrucciones: Ingresa los elementos de las filas de la matriz separados por un solo espacio")
    numero_fil = int(input("¿Cuántas filas tendrá la matriz?: "))
    numero_col = int(input("¿Cuántas columnas tendrá la matriz?: "))

    # Recibe datos
    s = 0
    matrix_vect = []
    matrix_copy = []
    cero_vector = []
    while s < numero_fil:
        string_fila = input(f"Fila{s+1})\t")
        array_fila = convierte_string_array(string_fila)
        while len(array_fila) != numero_col:
            print(f'La fila no tiene el numero correcto de elementos, inténtalo nuevamente \U0001F61E.')
            string_fila = input(f"Fila{s + 1})\t")
            array_fila = convierte_string_array(string_fila)
        s += 1
        matrix_vect.append(array_fila)
    vectores_columna = transpone_matrix(matrix_vect)
    matrix_copy = [n[:] for n in matrix_vect]

    for i in matrix_vect:
        i.append(0)
    for i in range(0, numero_col):
        cero_vector.append(0)

    print("La base del espacio nulo es \U0001F609: ")
    soluciones = sistema_ecs(matrix_vect, matrix_copy, numero_fil, numero_col)
    print(f"Soluciones {soluciones}")
    if type(soluciones) == tuple:
        numero_parametros, simb, exp, bandera_colcero, filas_ceros, indices_colsceros = soluciones
        vectores = genera_vectores(numero_parametros, simb, exp)
        if bandera_colcero:
            vectores_colcero = []
            filas_ceros.pop()
            for j, i in enumerate(indices_colsceros):
                vectores[j].insert(i,0)
            for j in indices_colsceros:
                aux_fc = filas_ceros[:]
                aux_fc[j] = 1
                vectores.append(aux_fc)
        dimension_nulidad = len(vectores)
        imprimir_vectores(vectores)

    else:
        if soluciones == cero_vector:
            dimension_nulidad = 0
        else:
            dimension_nulidad = 1
        print(tuple(soluciones))
    print("\n")
    dimension_imagen = numero_col - dimension_nulidad
    vectores_li = verificar_li(vectores_columna, dimension_imagen)

    print("Una base de la imagen de la matriz es \U0001F60E:")
    if vectores_li is not None:
        vectores_li = [tuple(n) for n in vectores_li]
        vectores_li = tuple(vectores_li)
        print(vectores_li)
    else:
        print("No fue posible encontrar una base para la imagen \U0001F633")

    print("\n")
    repetir = input("Desea ejecutar nuevamente el programa \U0001F914? si/no: ")
    repetir = repetir.lower()