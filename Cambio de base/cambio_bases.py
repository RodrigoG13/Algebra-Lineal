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
ÚLTIMA MODIFICACIÓN: 08/05/2022
'''
#  ---------------------------------------------------------------------------------------------------
# MÓDULOS Y LIBRERÍAS IMPORTADAS

from bases import *
#  ---------------------------------------------------------------------------------------------------
# FUNCIONES


def convierte_string_array(string_num):
    array_num = []
    array_str = string_num.split(",")
    for numero in array_str:
        array_num.append(float(numero))
    return array_num

def matriz_transicion(base_a, base_b, num_el, num_vect):
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

#  ---------------------------------------------------------------------------------------------------
# PROGRAMA PRINCIPAL
repetir = "si"
while repetir == "si":
    print("\t\t\t\t\t\t***CAMBIO DE BASE***\n")
    num_vectores = int(input("¿De cuántos vectores serán las bases?: "))
    num_elementos = int(input("¿De cuántos elementos será cada vector?: "))

# Ingreso de datos
    k = 1
    base_1 = []
    base_2 = []
    bandera_b1 = True
    while k < num_vectores * 2 + 1:
        if k == 1:
            print(f"\n-------- BASE B1 --------")
        elif k == num_vectores + 1:
            print(f"\n-------- BASE B2 --------")
        if k > num_vectores:
            bandera_b1 = False
        if bandera_b1:
            string_vector = input(f"v{k} - B1: ")
        else:
            string_vector = input(f"v{k-num_vectores-1} - B2: ")
        vector_array = convierte_string_array(string_vector)
        k += 1
        if bandera_b1:
            base_1.append(vector_array)
        else:
            base_2.append(vector_array)

    # Verifica si son bases
    bandera_b1 = base(base_1, num_elementos, num_vectores)
    bandera_b2 = base(base_2, num_elementos, num_vectores)
    print(f"\n-------- COMPROBACIÓN DE BASES --------")
    if bandera_b1:
        print(f"B1 si es base", end="\t\t")
    else:
        print(f"B1 no es base", end="\t\t")
    if bandera_b2:
        print(f"B2 si es base")
    else:
        print(f"2B no es base")

    if bandera_b1 and bandera_b2:
        transicion_b1b2 = matriz_transicion(base_1, base_2, num_elementos, num_vectores)
        transicion_b2b1 = matriz_transicion(base_2, base_1, num_elementos, num_vectores)
        print(f"\n-------- MATRICES DE TRANSICIÓN --------")
        print(f"De B1 a B2 es:")
        print(transicion_b1b2)
        print(f"De B2 a B1 es:")
        print(transicion_b2b1)
        fila_cero = [0 for i in range(0, num_elementos)]
        v_canonicos = [fila_cero[:] for i in range(0, num_vectores)]
        for indice, vector in enumerate(v_canonicos):
            vector[indice] = 1
        transicion_canb1 = matriz_transicion(v_canonicos, base_1, num_elementos, num_vectores)
        transicion_canb2 = matriz_transicion(v_canonicos, base_2, num_elementos, num_vectores)
        vector_1 = [[1] for i in range(0, num_elementos) ]
        vector1_print = [1 for i in range(0, num_elementos) ]
        vector1_b1 = multiplica_matrix(transicion_canb1, vector_1)
        vector1_b2 = multiplica_matrix(transicion_canb2, vector_1)
        vector1b1_print = [i[0] for i in vector1_b1]
        vector1b2_print = [i[0] for i in vector1_b2]
        print(f"\n-------- EXPRESIÓN DEL VECTOR {vector1_print} EN BASE CANÓNICA --------")
        print(f"En la B1 es:")
        print(vector1b1_print)
        print(f"En la B2 es:")
        print(vector1b2_print)

    else:
        pass
    
    repetir = input("Desea ejecutar nuevamente el programa? si/no: ")
    repetir = repetir.lower()