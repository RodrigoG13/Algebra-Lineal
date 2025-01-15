'''
INSTITUTO POLITÉCNICO NACIONAL
ESCUELA SUPERIOR DE CÓMPUTO

INGENIERÍA EN INTELIGENCIA ARTIFICIAL

ÁLGEBRA LINEAL
CAMBIO DE BASES

GRUPO: 2BM1
@author: Rodrigo Gerardo Trejo Arriaga

ESTE PROGRAMA RECIBE DOS BASES DE ℝ^n E INDICA:
i) SI B1 Y B2 SON BASES
ii) CALCULA LA MATRIZ DE TRANSICIÓN DE B1 A B2
iii) CALCULA LA MATRIZ DE TRANSICIÓN DE B2 A B1
iv) CALCULA LA TRANSICIÓN DEL VECTOR (1,1,1,...,1) DE LA BASE CANÓNICA A B1 Y B2

FECHA DE INICIO DE PROYECTO: 07/05/2022
ÚLTIMA MODIFICACIÓN: 07/05/2022
'''
#  ---------------------------------------------------------------------------------------------------
# MÓDULOS Y LIBRERÍAS IMPORTADAS

import os
from sub_super import *
#  ---------------------------------------------------------------------------------------------------
# FUNCIONES

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
    print("\t\t\t\t\t\t***CAMBIO DE BASE***\n")
    print(f"""Instrucciones: Ingresa dos bases (\u03B2{subindices[0]}, \u03B2{subindices[1]}) cuyos elementos estén separados por comas (,) y sin espacios.
               Ejemplo: v\u2099 - \u03B2\u2099 = 1,0,0\n""")
    num_vectores = int(input("¿De cuántos vectores serán las bases?: "))
    num_elementos = int(input("¿De cuántos elementos será cada vector?: "))

    k = 1
    base_1 = []
    base_2 = []
    bandera_b1 = True
    while k < num_vectores * 2 + 1:
        if k == 1:
            print(f"\n----- BASE \u03B2{subindices[0]} -----")
        elif k == num_vectores + 1:
            print(f"\n----- BASE \u03B2{subindices[1]} -----")
        if k > num_vectores:
            bandera_b1 = False
        if bandera_b1:
            string_vector = input(f"v{subindices[k-1]} - \u03B2{subindices[0]} =\t")
        else:
            string_vector = input(f"v{subindices[k-num_vectores-1]} - \u03B2{subindices[1]} =\t")
        vector_array = convierte_string_array(string_vector)
        while len(vector_array) != num_elementos:
            print(f'El vector no tiene la longitud indicada, inténtalo nuevamente  \U0001F61E.')
            if bandera_b1:
                string_vector = input(f"v{subindices[k-1]} - \u03B2{subindices[0]} =\t")
            else:
                string_vector = input(f"v{subindices[k-num_vectores-1]} - \u03B2{subindices[1]} =\t")        
            vector_array = convierte_string_array(string_vector)
        k += 1
        if bandera_b1:
            base_1.append(vector_array)
        else:
            base_2.append(vector_array)

    print(f"\nbase 1 {base_1}")
    print(f"base 2 {base_2}")

    print("\n")
    repetir = input("Desea ejecutar nuevamente el programa \U0001F914? si/no: ")
    repetir = repetir.lower()
