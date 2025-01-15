'''
INSTITUTO POLITÉCNICO NACIONAL
ESCUELA SUPERIOR DE CÓMPUTO

INGENIERÍA EN INTELIGENCIA ARTIFICIAL

ÁLGEBRA LINEAL
EIGEN VALORES Y EIGEN VECTORES

GRUPO: 2BM1
@author: Rodrigo Gerardo Trejo Arriaga

ESTE PROGRAMA RECIBE UNA TRANSFORMACIÓN LINEAL Y CALCULA:
i) EL POLINOMIO CARACTERÍSTICO DE LA TRANSFORMACIÓN
ii) LOS EIGEN VALORES DE LA TRANSFORMACIÓN
iii) LOS EIGEN VECTORES ASOCIADOS A CADA EIGEN VALOR

ÚLTIMA MODIFICACIÓN: 11/06/2022
'''

#  -------------------------------------------------------------------------------------------------
# MÓDULOS Y LIBRERÍAS IMPORTADAS


from os import system
import sympy as sp
from nulidad import *
#  -------------------------------------------------------------------------------------------------
# FUNCIONES


def imprimir_vectores(vect):
    """
    Imprime los vectores resultantes de la base del espcio nulo
    :param vect: (list) Vectores a imprimir
    :return: (None) La impresión se realiza de manera interna
    """
    print("<", end="")
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
    print(">", end="")
    print("\n")


def convierte_expresion_lista(expresion_string):
    """
    Convierte una expresion dada con variables en una lista que almacena solo los coeficientes
    con signo de dicha expresion
    :param expresion_string: (str) Expresion algebraica con variables y coeficientes
    :return fila: (list) Coeficientes con signo de cada variable de la expresion
    """      
    uno_string = "1"
    fila = []
    signo_mas = "+"
    signo_menos = "-"
    uno_positivo = "+1"
    uno_negativo = "-1"
    expresion_string = expresion_string.lower()
    expresion_string = expresion_string.replace("=", "x")     
    for a in range(97, 123):
        signo_mas_letra = signo_mas + chr(a)        
        signo_menos_letra = signo_menos + chr(a)    

        if expresion_string.startswith(chr(a)):      
            expresion_string = uno_string + expresion_string
            expresion_string = expresion_string.replace(chr(a), "x")

        elif signo_mas_letra in expresion_string:   
            uno_mas_letra = uno_positivo+"x"       
            expresion_string = expresion_string.replace(signo_mas_letra, uno_mas_letra)

        elif signo_menos_letra in expresion_string:  
            uno_menos_letra = uno_negativo+"x"     
            expresion_string = expresion_string.replace(signo_menos_letra, uno_menos_letra)

        elif chr(a) in expresion_string:            
            expresion_string = expresion_string.replace(chr(a), "x")

    expresion_string = expresion_string.split("x")  
    expresion_string.remove("")                   
    for numero in expresion_string:
        fila.append(float(numero))
    return fila                                


def menu_mtransf():
    """
    Imprime el menú de instrucciones y recibe los datos para crear la matriz de transformación
    :return dim_r: (int) Dimension de R en la que se harán los cálculos
    :return m_transformacion: Matriz A asociada a la transformación lineal introducida
    """
    print(f"""Instrucciones: Ingresa las filas de la transformación lineal con diferentes variables.
NOTA: Incluye también aquellas variables cuyo coeficiente sea 0 (cero)\n""")
    dim_r = int(input("¿En qué dimensión de R se realizará la transformación?: "))
    m_transformacion = []
    s = 0
    while s < dim_r:
        expresion_str = input(f"T - F{s+1})     ")
        ecuacion_array = convierte_expresion_lista(expresion_str)
        while len(ecuacion_array) < dim_r:
            print(f'La expresion no tiene el numero correcto de variables, inténtalo nuevamente \U0001F61E.')
            expresion_str = input(f"Ec{s + 1})     ")
            ecuacion_array = convierte_expresion_lista(expresion_str)
        m_transformacion.append(ecuacion_array)
        s = s+1
    return dim_r, m_transformacion


def crear_identidad(dim_r):
    """
    Crea la matriz identidad de acuerdo a la dimension de R introducida
    :param dim_r: (int) Dimension de R en la que se harán los cálculos
    :return fila: (identidad) Matriz identidad en la R seleccionada
    """     
    fila = [0 for i in range(0, dim_r)]
    identidad = [fila[:] for i in range(0, dim_r)]
    for i in range(0, dim_r):
        identidad[i][i] = 1
    return identidad


def multiplicar_identidad(identidad, cte):
    """
    Multiplica la matriz identidad por una constante dada
    :param identidad: (list) Matriz identidad
    :param cte: (int) Constante por la que se multiplicará la identidad
    :return copy_identidad: (list) Matriz identidad multiplicada por la constante
    """  
    copy_identidad = [i[:] for i in identidad]
    for i in range(0, len(copy_identidad)):
        copy_identidad[i][i] *= cte
    return copy_identidad


def restar_matrices(m1, m2):
    """
    Resta dos matrices dadas
    :param m1: (list) Matriz 1
    :param m2: (list) Matriz 2 que se le restará a la 1 
    :return resta: (list) Matriz resta de m1 - m2
    """
    fila_r = [0 for i in range(0, len(m1))]
    resta = [fila_r[:] for i in range(0, len(m1[0]))]
    for i in range(0, len(m1)):
        for j in range(0, len(m1[0])):
            resta[i][j] = m1[i][j] - m2[i][j]
    return resta


def validar_valores(valores):
    """
    Selecciona los valores propios que pertenecen a los reales y los guarda en un diccionario
    :param valores: (list) Valores propios obtenidos del polinomio característico
    :return valvect_propios: (dict) Diccionario con los valores propios en los reales
    """
    valvect_propios = {}
    for i in range(0, len(valores)):
        try:
            valvect_propios[Fraction(float(valores[i])).limit_denominator(1000)] = None
        except:
            pass
    return valvect_propios


def imprimir_valores(valvect_propios):
    """
    Imprime un conjunto de vectores
    :param valvect_propios: (dict) Valores y vectores propios de la transformación
    :return None: (None) La impresión se realiza de manera interna
    """
    conta = 0
    for i in valvect_propios.keys():
        if conta < len(valvect_propios.keys()) - 1:
            print(f"{i}, ", end="")
        elif conta == len(valvect_propios.keys()) -1:
            print(f"{i}")
        conta += 1

def es_matriz_ceros(matriz):
    """
    Indica si la matriz dada es una matriz con puros ceros en sus entradas
    :param matriz: (list) Matriz a analizar
    :return matriz == matriz_cero: (Bool) True/False
    """
    dimension = len(matriz)
    fila_cero = [0 for i in range(0, dimension)]
    matriz_cero = [fila_cero[:] for i in range(0, dimension) ]
    return matriz == matriz_cero


def calcular_vectores_propios(valvect_propios):
    """
    Calcula los vectores propios asociados a cada valor propio
    :param valvect_propios: (dict) Valores y vectores propios de la transformación
    :return None: (None) El almacenamiento de los vectores obtenidos se realiza internamente
    """

    for i in valvect_propios.keys():
        m_valorpropio = multiplicar_identidad(m_identidad, i)
        matriz_nulidad = restar_matrices(matrix_transformacion, m_valorpropio)
        try:
            if not es_matriz_ceros(matriz_nulidad):
                vectores = nulidad(matriz_nulidad)
                valvect_propios[i] = vectores
            else:
                valvect_propios[i] = m_identidad
        except:
            pass
            cero_gordo = [0 for i in range(0, len(matriz_nulidad))]
            valvect_propios[i] = [cero_gordo]


def imprimir_vectpropios(valvect_propios):
    """
    Imprime los vectores propios asociados a cada valor propio
    :param valvect_propios: (dict) Valores y vectores propios de la transformación
    :return None: (None) La impresión de los vectores se realiza internamente
    """
    for valor, vector in valvect_propios.items():
        print(f"\nLos vectores para el valor propio {Fraction(valor).limit_denominator(1000)} son:")
        print("\t", end="")
        imprimir_vectores(vector)

#  --------------------------------------------------------------------------------------------------------------------
# PROGRAMA PRINCIPAL

repetir = "si"
while repetir == "si":
    system("cls")
    print("\t\t\t***EIGEN VALORES Y EIGEN VECTORES***")
    dimension_r, matrix_transformacion = menu_mtransf()
    lamb = sp.Symbol('λ')
    m_identidad = crear_identidad(dimension_r)
    lamb_identidad = multiplicar_identidad(m_identidad, lamb)
    m_resta = restar_matrices(matrix_transformacion, lamb_identidad)
    mr_simb = sp.Matrix(m_resta)
    polinomio = mr_simb.det()
    valores_propios = sp.solve(polinomio)
    valores_vectores = validar_valores(valores_propios)
    if valores_vectores != {}:
        calcular_vectores_propios(valores_vectores)
        print("\n>>>Polinomio característico: ")
        print(f"\t{polinomio}")
        print("\n>>>Valores propios:")
        print("\t",end="")
        imprimir_valores(valores_vectores)
        print("\n>>>Vectores propios: ")
        imprimir_vectpropios(valores_vectores)
    else:
        print("Todas las raices del polinomio característico son complejas")
    repetir = input("Desea hacer otra operación? si/no: ")
    repetir = repetir.lower()