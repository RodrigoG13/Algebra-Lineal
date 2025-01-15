'''
INSTITUTO POLITÉCNICO NACIONAL
ESCUELA SUPERIOR DE CÓMPUTO

INGENIERÍA EN INTELIGENCIA ARTIFICIAL

ÁLGEBRA LINEAL
CAMBIO DE BASES

GRUPO: 2BM1
@author: Rodrigo Gerardo Trejo Arriaga

ESTE PROGRAMA RECIBE DOS BASES DE ℝ^n Y UN VECTOR 'u' en ℝ^n E INDICA:
i) SI B1 Y B2 SON BASES
ii) CALCULA LA MATRIZ DE TRANSICIÓN DE B1 A B2
iii) CALCULA LA MATRIZ DE TRANSICIÓN DE B2 A B1
iv) REALIZA EL CAMBIO DE BASE DEL VECTOR 'u' DE LA BASE CANÓNICA A B1 Y B2
v) REALIZA EL CAMBIO DE BASE DEL VECTOR (1,1,1,...,1) DE LA BASE CANÓNICA A B1 Y B2

FECHA DE INICIO DE PROYECTO: 07/05/2022
ÚLTIMA MODIFICACIÓN: 09/05/2022
'''
#  ---------------------------------------------------------------------------------------------------
# MÓDULOS Y LIBRERÍAS IMPORTADAS


import os
from sub_super import *
from bases import *
from tabulate import tabulate
#  ---------------------------------------------------------------------------------------------------
# FUNCIONES


def imprime_matrix(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]}\t\t", end="")
        print("")


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


def matriz_transicion(base_a, base_b, num_el, num_vect):
    """
    Calcula la matriz de transicion de una base Ba a una base Bb
    :param base_a: (list) Base de la que partiremos
    :param base_b: (list) Base a la que queremos llegar
    :param num_elementos: (int) Número de componentes de los vectores
    :param num_vectores: (int) Número de vectores del conjunto
    :return transicion_babb: (list) Matriz de transición de Ba a Bb
    """
    transicion_babb = []
    for vector in base_a:
        combinacion = combinacion_lineal(base_b, vector, num_el, num_vect)
        if combinacion:
            transicion_babb.append(combinacion)
        else:
            print("No fue posible realizar la combinacion lineal")
            break
    return transicion_babb


def multiplica_matrix(m1, m2):
    """
    Multiplica dos matrices compatibles entre sí
    :param m1: (list) Matriz m1 que se multiplicará por m2
    :param m2: (list) Matriz m2 que será multiplicada por m1
    :return m_pultiplicada: (list) Multiplicación de m1 x m2
    """
    m_pultiplicada = []
    for i in range(len(m1)):
        m_pultiplicada.append([])
        for j in range(len(m2[0])):
            m_pultiplicada[i].append(0)
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m1[0])):
                m_pultiplicada[i][j] += m1[i][k] * m2[k][j]
    return m_pultiplicada


def imprimir_vector(vector):
    """
    Imprime un vector
    :param vect: (list) Vector que se imprimirá
    :return: (None) La impresión se realiza de manera interna
    """
    for i in range(len(vector)):
        if i == 0:
            print(f"({vector[i]}", end="")
        elif i == len(vector) - 1:
            print(f",{vector[i]})", end="")
        else:
            print(f",{vector[i]}", end="")
    print("\n")

#  ---------------------------------------------------------------------------------------------------
# PROGRAMA PRINCIPAL
repetir = "si"
while repetir == "si":
    os.system("cls")
    print("\t\t\t\t\t\t***CAMBIO DE BASE***\n")
    print(f"""Instrucciones: Ingresa dos bases (\u03B2{subindices[0]}, \u03B2{subindices[1]}) cuyos elementos estén separados por comas (,) y sin espacios.
               Ejemplo: v\u2099 - \u03B2\u2099 = 1,0,0,...,0\n""")
    num_vectores = int(input("¿De cuántos vectores serán las bases?: "))
    num_elementos = int(input("¿De cuántos elementos será cada vector?: "))

# Ingreso de datos
    k = 1
    base_1 = []
    base_2 = []
    bandera_b1 = True
    while k < num_vectores * 2 + 1:
        if k == 1:
            print(f"\n-------- BASE \u03B2{subindices[0]} --------")
        elif k == num_vectores + 1:
            print(f"\n-------- BASE \u03B2{subindices[1]} --------")
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

    u_vectorpr = input("Ingresa el vector u en base canónica: ")
    u_vectorpr = convierte_string_array(u_vectorpr)
    while len(u_vectorpr) != num_elementos:
        print(f"{len(u_vectorpr)} == {num_elementos}")
        print(f'El vector no tiene la longitud indicada, inténtalo nuevamente \U0001F61E.')
        u_vectorpr = input("Ingresa el vector u: ")
        u_vectorpr = convierte_string_array(u_vectorpr)

    # Verifica si son bases
    bandera_b1 = base(base_1, num_elementos, num_vectores)
    bandera_b2 = base(base_2, num_elementos, num_vectores)
    print(f"\n-------- COMPROBACIÓN DE BASES --------")
    if bandera_b1:
        print(f"\u03B2{subindices[0]} si es base \U0001F642", end="\t\t")
    else:
        print(f"\u03B2{subindices[0]} no es base \U0001F97A", end="\t\t")
    if bandera_b2:
        print(f"\u03B2{subindices[1]} si es base \U0001F642")
    else:
        print(f"\u03B2{subindices[1]} no es base \U0001F97A")

    if bandera_b1 and bandera_b2:
        transicion_b1b2 = matriz_transicion(base_1, base_2, num_elementos, num_vectores)
        transicion_b2b1 = matriz_transicion(base_2, base_1, num_elementos, num_vectores)
        print(f"\n-------- MATRICES DE TRANSICIÓN --------")
        print(f"De \u03B2{subindices[0]} a \u03B2{subindices[1]} es:")
        #print(tabulate(transicion_b1b2))
        imprime_matrix(transicion_b1b2)
        print("\n")
        print(f"De \u03B2{subindices[1]} a \u03B2{subindices[0]} es TOMAR ESTA:")
        #print(tabulate(transicion_b2b1))
        imprime_matrix(transicion_b2b1)
        print("\n")
        fila_cero = [0 for i in range(0, num_elementos)]
        v_canonicos = [fila_cero[:] for i in range(0, num_vectores)]
        for indice, vector in enumerate(v_canonicos):
            vector[indice] = 1
        transicion_canb1 = matriz_transicion(v_canonicos, base_1, num_elementos, num_vectores)
        transicion_canb2 = matriz_transicion(v_canonicos, base_2, num_elementos, num_vectores)
        print(f"De \u03B2{subindices[0]} a canónica es:")
        #print(tabulate(transicion_canb1))
        imprime_matrix(transicion_canb1)
        print("\n")
        print(f"De \u03B2{subindices[1]} a a canónica es:")
        #print(tabulate(transicion_canb2))
        imprime_matrix(transicion_canb2)
        print("\n")
        vector_1 = [[1] for i in range(0, num_elementos) ]
        vector1_print = [1 for i in range(0, num_elementos) ]
        vector1_b1 = multiplica_matrix(transicion_canb1, vector_1)
        vector1_b2 = multiplica_matrix(transicion_canb2, vector_1)
        vector1b1_print = [(Fraction(i[0]).limit_denominator(1000)) for i in vector1_b1]
        vector1b2_print = [(Fraction(i[0]).limit_denominator(1000)) for i in vector1_b2]
        u_vector = [[n] for n in u_vectorpr]
        u_b1 = multiplica_matrix(transicion_canb1, u_vector)
        u_b2 = multiplica_matrix(transicion_canb2, u_vector)
        ub1_print = [(Fraction(i[0]).limit_denominator(1000)) for i in u_b1]
        ub2_print = [(Fraction(i[0]).limit_denominator(1000)) for i in u_b2]

        print(f"\n-------- EXPRESIÓN DEL VECTOR {tuple(vector1_print)} EN BASE CANÓNICA --------")
        print(f"En la \u03B2{subindices[0]} es \U0001F632:")
        imprimir_vector(vector1b1_print)
        print(f"En la \u03B2{subindices[1]} es \U0001F60E:")
        imprimir_vector(vector1b2_print)

        print(f"\n-------- EXPRESIÓN DEL VECTOR 'u' {tuple(u_vectorpr)} EN BASE CANÓNICA --------")
        print(f"En la \u03B2{subindices[0]} es \U0001F632:")
        #print(tabulate(transicion_canb1))
        imprimir_vector(ub1_print)
        print(f"En la \u03B2{subindices[1]} es \U0001F60E:")
        imprimir_vector(ub2_print)
        #print(tabulate(transicion_canb2))

    else:
        print(f"\nEs necesario que tanto \u03B2{subindices[0]} como \u03B2{subindices[1]} sean bases para efectuar el cambio \U0001F61E\n")
    
    repetir = input("Desea ejecutar nuevamente el programa \U0001F914? si/no: ")
    repetir = repetir.lower()