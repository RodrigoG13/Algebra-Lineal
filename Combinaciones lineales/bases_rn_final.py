'''
INSTITUTO POLITÉCNICO NACIONAL
ESCUELA SUPERIOR DE CÓMPUTO

INGENIERÍA EN INTELIGENCIA ARTIFICIAL

ÁLGEBRA LINEAL
COMBINACION LINEAL, ESPACIOS GENERADORES, INDEPENDENCIA LINEAL Y BASES

GRUPO: 2BM1
@author: Rodrigo Gerardo Trejo Arriaga

ESTE PROGRAMA RECIBE UN CONJUNTO DE VECTORES 'v' Y UN VECTOR 'u' E INDICA:
i) SI v ES UNA COMBINACIÓN LINEAL DE 'u'
ii) SI v ES UN ESPACIO GENERADOR DE ℝ^n
iii) SI v ES LINEALMENTE INDEPENDIENTE 
iv) SI v ES UNA BASE

FECHA DE INICIO DE PROYECTO: 10/04/2022
ÚLTIMA MODIFICACIÓN: 13/04/2022
'''
#  ---------------------------------------------------------------------------------------------------
# MÓDULOS Y LIBRERÍAS IMPORTADAS


from fractions import Fraction
from sympy import symbols
from gauss_jordan2 import *
import os
from sub_super import *
#  ---------------------------------------------------------------------------------------------------
# FUNCIONES


# Función que genera la matriz para el sistema de ecuaciones
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


# Función de ingreso de datos
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

#  ---------------------------------------------------------------------------------------------------
# PROGRAMA PRINCIPAL


repetir = "si"
while repetir == "si":
    os.system("cls")
    print("\t\t***COMBINACIONES LINEALES, ESPACIOS GENERADORES, INDEPENDENCIA LINEAL Y BASES***\n")
    print("""Instrucciones: Ingresa un conjunto de vectores <v\u2081, v\u2082, ... , v\u2099>, y un vector
            'u', cuyos elementos estén separados por comas (,) y sin espacios. Ejemplo: v\u2099 = 1,0,0""")
    num_vectores = int(input("¿De cuántos vectores será el conjunto <v\u2081, v\u2082, ... , v\u2099>?: "))
    num_elementos = int(input("¿De cuántos elementos será cada vector v?: "))

    # Crea las literales para trabajar el espacio generador
    simbolos = []
    for i in range(97, 123):
        simbolos.append(symbols(chr(i)))

    simbolos_uso = simbolos[len(simbolos)-num_elementos:]

    # Introducción de datos
    s = 0
    combinacion = []
    while s < num_vectores:
        string_vector = input(f"v{subindices[s]} =\t")
        vector_array = convierte_string_array(string_vector)
        while len(vector_array) != num_elementos:
            print(f'El vector no tiene la longitud indicada, inténtalo nuevamente  \U0001F61E.')
            string_vector = input(f"Fila{s + 1} =\t")
            vector_array = convierte_string_array(string_vector)
        s += 1
        combinacion.append(vector_array)
    
    u_vector = input("Ingresa el vector u: ")
    u_vector = convierte_string_array(u_vector)
    while len(u_vector) != num_elementos:
        print(f"{len(u_vector)} == {num_elementos}")
        print(f'El vector no tiene la longitud indicada, inténtalo nuevamente \U0001F61E.')
        u_vector = input("Ingresa el vector u: ")
        u_vector = convierte_string_array(u_vector)

    # Crea copias de la matriz base para resolver los sistemas de ecuaciones según el caso
    combinacion_coef = [n[:] for n in combinacion]
    combinacion_coef = transpone_matrix(combinacion_coef)
    combinacion_lineal = [n[:] for n in combinacion_coef]
    espacio_generador = [n[:] for n in combinacion_coef]
    independencia_lineal = [n[:] for n in combinacion_coef]

    # Crea el sistema de ecuaciones para la combinación lineal
    for indice, lista in enumerate(combinacion_lineal):
        lista.append(u_vector[indice])
    solucion_sistema, bandera = sistema_ecs(combinacion_lineal, combinacion_coef, num_elementos, num_vectores, 1)

    # Opciones para la combinación lineal
    print("\n>>>> COMBINACIÓN LINEAL:")
    if len(solucion_sistema) != 0:
        if bandera == 0:
            print("\tSí, es combinación lineal \U0001F642. Esta es:")
        else:
            print("\tSí, es combinación lineal \U0001F642. Una de ellas es:")
        print(f"{tuple(u_vector)} =", end=" ")
        for constante, vector in enumerate(combinacion):
            if solucion_sistema[constante] < 0:
                print(f"{solucion_sistema[constante]}{tuple(vector)}", end=" ")

            elif solucion_sistema[constante] == 1:
                print(f"+ {tuple(vector)}", end=" ")

            else:
                print(f"+ {solucion_sistema[constante]}{tuple(vector)}", end=" ")
        print("\n")
    else:
        print("\t'u' no es combinación lineal <v\u2081, v\u2082, ... , v\u2099> \U0001F910!")

    # Crea el sistema de ecuaciones para el espacio generador
    for indice, lista in enumerate(espacio_generador):
        lista.append(simbolos_uso[indice])
    bandera_esp_gen = sistema_ecs(espacio_generador, combinacion_coef, num_elementos, num_vectores, 2)

    # Opciones para el espacio generador
    print("\n>>>> ESPACIO GENERADOR")
    if bandera_esp_gen:
        print(f"\tSi es un espacio generador de ℝ{superindices[num_elementos-1]}\U0001F920!")
    else:
        print(f"\tNo es un espacio generador  de ℝ{superindices[num_elementos-1]}\U0001F97A!")

    # Crea el sistema de ecuaciones para la combinación lineal
    for lista in independencia_lineal:
        lista.append(0)
    bandera_li = sistema_ecs(independencia_lineal, combinacion_coef, num_elementos, num_vectores, 2)

    # Opciones para la independencia lineal
    print("\n>>>> INDEPENDENCIA LINEAL")
    if bandera_li == 1:
        print("\tEl conjunto de vectores es linealmente independiente \U0001F609")
    else:
        print("\tEl conjunto de vectores es linealmente dependiente \U0001F633")

    # Opciones para la base
    print("\n>>>> BASE DE ℝ\u207F")
    if bandera_esp_gen and bandera_li == 1:
        print(f"\tEl conjunto de vectores es una base de ℝ{superindices[num_elementos-1]} \U0001F60E")
    else:
        print(f"\tEl conjunto de vectores no es una base de ℝ{superindices[num_elementos-1]} \U0001F632")
    
    print("\n")
    repetir = input("Desea ejecutar nuevamente el programa \U0001F914? si/no: ")
    repetir = repetir.lower()