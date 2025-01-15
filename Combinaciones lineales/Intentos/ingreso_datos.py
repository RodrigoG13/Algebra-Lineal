'''
INSTITUTO POLITÉCNICO NACIONAL
ESCUELA SUPERIOR DE CÓMPUTO

INGENIERÍA EN INTELIGENCIA ARTIFICIAL

ÁLGEBRA LINEAL
COMBINACION LINEAL, ESPACIOS GENERADORES

GRUPO: 2BM1
ALUMNO: TREJO ARRIAGA RODRIGO GERARDO

ESTE PROGRAMA RECIBE UNA COMBINACIÓN LINEAL 'V' Y UN VECTOR 'u' E INDICA:
i) SI V ES UNA COMBINACIÓN LINEAL DE 'u'
ii) SI V es un espacio generador de ℝ^n
iii) 
iv) 

ÚLTIMA MODIFICACIÓN: 11/04/2022
'''
#  ---------------------------------------------------------------------------------------------------
# MÓDULOS Y LIBRERÍAS IMPORTADAS

from fractions import Fraction
from sympy import symbols
from gauss_jordan import *
#  ---------------------------------------------------------------------------------------------------
# FUNCIONES

def transpone_matrix(matriz):
    transpuesta = []
    for i in range(len(matriz[0])):
        transpuesta.append([])
        for j in range(len(matriz)):
            transpuesta[i].append(matriz[j][i])
    return transpuesta

def convierte_string_array(string_num):
    array_num = []
    array_str = string_num.split(",")
    for numero in array_str:
        array_num.append(float(numero))
    return array_num

subindices = ["\u2081", "\u2082", "\u2083", "\u2084", "\u2085", "\u2086", "\u2087", "\u2088",
            "\u2089", "\u2081\u2080", "\u2081\u2081", "\u2081\u2082", "\u2081\u2083",
            "\u2081\u2084", "\u2081\u2085", "\u2081\u2086", "\u2081\u2087", "\u2081\u2088",
            "\u2081\u2089", "\u2082\u2080", "\u2082\u2081", "\u2082\u2082", "\u2082\u2083",
            "\u2082\u2084", "\u2082\u2085", "\u2082\u2086", "\u2082\u2087"]

superindices = ["\u00b9", "\u00b2", "\u00b3", "\u2074", "\u2075", "\u2076", "\u2077", "\u2078",
            "\u2079", "\u00b9\u2070", "\u00b9\u00b9", "\u00b9\u00b2", "\u00b9\u00b3",
            "\u00b9\u2084", "\u00b9\u2075", "\u00b9\u2076", "\u00b9\u2077", "\u00b9\u2078",
            "\u00b9\u2079", "\u00b2\u2070", "\u00b2\u00b9", "\u00b2\u00b2", "\u00b2\u00b3",
            "\u00b2\u2074", "\u00b2\u2075", "\u00b2\u2076", "\u00b2\u2077"]

print("\t\t\t\t***COMBINACIONES LINEALES Y ESPACIOS GENERADORES***\n")
print("""Instrucciones: Este programa recibe una combinación lineal de vectores <v\u2081, v\u2082, ... , v\u2099>, y un vector
            'u', indicando si es una combinación lineal de u, un espacio generador de ℝ\u207F""")
num_vectores = int(input("¿De cuántos vectores será la combinación lineal <v\u2081, v\u2082, ... , v\u2099>: "))
num_elementos = int(input("¿De cuántos elementos será cada vector v?: "))

simbolos = []
for i in range(97, 123):
    simbolos.append(symbols(chr(i)))
simbolos_uso = simbolos[len(simbolos)-num_elementos:]

s = 0

combinacion = []

while s < num_vectores:
    string_vector = input(f"v{subindices[s]} =\t")
    vector_array = convierte_string_array(string_vector)
    while len(vector_array) != num_elementos:
        print(f'La fila no tiene el numero correcto de elementos, inténtalo nuevamente \U0001F61E.')
        string_vector = input(f"Fila{s + 1} =\t")
        vector_array = convierte_string_array(string_vector)
    s += 1
    combinacion.append(vector_array)
    
u_vector = input("Ingresa el vector u: ")
u_vector = convierte_string_array(u_vector)
while len(u_vector) != num_elementos:
        print(f"{len(u_vector)} == {num_elementos}")
        print(f'El vector no tiene el numero correcto de elementos, inténtalo nuevamente \U0001F61E.')
        u_vector = input("Ingresa el vector u: ")
        u_vector = convierte_string_array(u_vector)

combinacion_coef = [n[:] for n in combinacion]
combinacion_coef = transpone_matrix(combinacion_coef)
combinacion_lineal = [n[:] for n in combinacion_coef]
espacio_generador = [n[:] for n in combinacion_coef]

for indice, lista in enumerate(combinacion_lineal):
    lista.append(u_vector[indice])

for indice, lista in enumerate(espacio_generador):
    lista.append(simbolos_uso[indice])

solucion_sistema, bandera = sistema_ecs(combinacion_lineal, combinacion_coef, num_elementos, num_vectores)

if len(solucion_sistema) != 0 and bandera == 0:
    print("Sí es combinación lineal, una de ellas es:")
    print(f"{tuple(u_vector)} =",end=" ")
    for constante, vector in enumerate(combinacion):
        if solucion_sistema[constante] < 0:
            print(f"{solucion_sistema[constante]}{tuple(vector)}",end=" ")

        elif solucion_sistema[constante] == 1:
            print(f"+ {tuple(vector)}",end=" ")

        else:
            print(f"+ {solucion_sistema[constante]}{tuple(vector)}",end=" ")
    print("\n")

elif len(solucion_sistema) != 0 and bandera == 1:
    print("Sí es combinación lineal \U0001F642, una de ellas es:")
    print(f"{tuple(u_vector)} =",end=" ")
    for constante, vector in enumerate(combinacion):
        if solucion_sistema[constante] < 0:
            print(f"{solucion_sistema[constante]}{tuple(vector)}",end=" ")

        elif solucion_sistema[constante] == 1:
            print(f"+ {tuple(vector)}",end=" ")

        else:
            print(f"+ {solucion_sistema[constante]}{tuple(vector)}",end=" ")
    print("\n")

else:
    print("'u' no es combinación lineal <v\u2081, v\u2082, ... , v\u2099> \U0001F910!")


