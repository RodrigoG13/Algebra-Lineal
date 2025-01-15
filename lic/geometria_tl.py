'''
INSTITUTO POLITÉCNICO NACIONAL
ESCUELA SUPERIOR DE CÓMPUTO

INGENIERÍA EN INTELIGENCIA ARTIFICIAL

ÁLGEBRA LINEAL
GEOMETRÍA DE LAS TRANSFORMACIONES LINEALES

GRUPO: 2BM1
@author: Rodrigo Gerardo Trejo Arriaga

ESTE PROGRAMA RECIBE UN POLÍGONO O EL NOMBRE DE UNA FIGURA PREESTABLECIDA Y:
--- GRAFICA LA FIGURA ORIGINAL ---
i) PERMITE LA REFLEXIÓN EN EL EJE X DE LA FIGURA
ii) PERMITE LA REFLEXIÓN EN EL EJE Y DE LA FIGURA
iii) PERMITE LA EXPANCIÓN EN EL EJE X DE LA FIGURA
iv) PERMITE LA EXPANCIÓN EN EL EJE Y DE LA FIGURA
v) PERMITE REALIZAR UN CORTE EN EL EJE X DE LA FIGURA
vi) PERMITE REALIZAR UN CORTE EN EL EJE X DE LA FIGURA
vii) PERMITE REALIZAR UN CORTE EN EL EJE Y DE LA FIGURA
viii) PERMITE ROTAR EN CIERTO ÁNGULO LA FIGURA
--- GRAFICA LA TRANSFORMACIÓn ---

FECHA DE INICIO DE PROYECTO: 27/05/2022
ÚLTIMA MODIFICACIÓN: 31/05/2022
'''
#  ---------------------------------------------------------------------------------------------------
# MÓDULOS Y LIBRERÍAS IMPORTADAS
from graficador import *
from transf_lineales import *
import os
from fg_pred import *

#  ---------------------------------------------------------------------------------------------------
# FUNCIONES


def convierte_string_array(string_num):
    """
    Convierte el string-punto ingresado por el usuario en una lista con las coordenadas del punto
    :param string_num: (string) String ingresado por el usuario
    :return array_num: (list) Vector ingresado por el usuario en una lista
    """
    array_num = []
    array_str = string_num.split(",")
    for numero in array_str:
        array_num.append(float(numero))
    return array_num


def menu():
    """
    Imprime el menú de instrucciones y retorna la figura seleccionada por el usuario
    :return1 figuras_pred[opcion_predeterminada.upper()]: (list) Lista con los puntos de la figura
    preestablecida y con las banderas de único trazo y reordenamiento de puntos
    :return2 [puntos], 1, 1: (tuple) Tupla con los puntos ingresados por el usuario y con las
                            banderas de único trazo y reordenamiento de puntos en True
    """
    print(f"""Instrucciones: Ingresa la opcion que desees ejecutar.""")
    print(  "\t i) Figura predeterminada\n"
            "\t ii) Ingresar polígono")
    opcion_figura = input("Ingresa el número romano de la opcion deseada: ")
    if opcion_figura == "i" or opcion_figura == "i)" or opcion_figura== "I" or opcion_figura=="I)":
        print(  "\n\t A. Fig 1\n"
                "\t B. Fig 2\n"
                "\t C. Fig 3\n"
                "\t D. Fig 4\n"
                "\t E. Fig 5\n")
        opcion_predeterminada = input("Ingresa la letra que corresponde a la figura deseada: ")
        return figuras_pred[opcion_predeterminada.upper()]
    else:
        puntos = []
        print("\nIngresa los puntos del polígono de la forma: a,b")
        num_puntos = int(input("¿De cuántos puntos será el polígono?: "))
        for i in range(0, num_puntos):
            punto_string = input(f"P{i+1})\t")
            puntos.append(convierte_string_array(punto_string))
        print("\n")
        return [puntos], 1, 1


def menu_transf(opciones_seleccionadas):
    """
    Menú que solicita los datos de las transformaciones lineales requeridas
    :param opciones_seleccionadas: (list) Lista de puntos de la figura y banderas de  reordenamiento 
                                        de puntos y único trazo
                                    
    :return opciones_transf[transf]: (str) Nombre de la transformación seleccionada por el usuario
    """
    cte = None
    print(  "\t 1. Reflexión en el eje X\n"
            "\t 2. Reflexión en el eje Y\n"
            "\t 3. Expanxión en el eje X\n"
            "\t 4. Expanxión en el eje Y\n"
            "\t 5. Corte en el eje X\n"
            "\t 6. Corte en el eje Y\n"
            "\t 7. Rotación\n")
    transf = int(input("Ingresa la transformación que desees que se realice a la figura: "))
    if transf == 3 or transf == 4 or transf == 5 or transf == 6:
        cte = float(input(f"Ingresa la constante de {opciones_transf[transf]}: " ))
    elif transf == 7:
        cte = float(input(f"Ingresa el ángulo de {opciones_transf[transf]}: " ))
    if opciones_seleccionadas[2]:
        stop = 1
    else:
        stop = len(opciones_seleccionadas[0])
    for k in range(0, stop):
        if transf == 1:
            opciones_seleccionadas[0][k] = reflejar(opciones_seleccionadas[0][k], False)
        elif transf == 2:
            opciones_seleccionadas[0][k] = reflejar(opciones_seleccionadas[0][k], True)
        elif transf == 3:
            opciones_seleccionadas[0][k] = expandir(opciones_seleccionadas[0][k], cte, True)
        elif transf == 4:
            opciones_seleccionadas[0][k] = expandir(opciones_seleccionadas[0][k], cte, False)
        elif transf == 5:
            opciones_seleccionadas[0][k] = cortar(opciones_seleccionadas[0][k], cte, True)
        elif transf == 6:
            opciones_seleccionadas[0][k] = cortar(opciones_seleccionadas[0][k], cte, False)
        elif transf == 7:
            opciones_seleccionadas[0][k] = rotar(opciones_seleccionadas[0][k], cte)
    return opciones_transf[transf]


def graficar(opciones_seleccion, num_graf, titulo):
    """
    Grafica en R2 una lista de puntos establecida por el usuario
    :param opciones_seleccion: (list) Lista de puntos de la figura y banderas de único trazo
                                    y reordenamiento de puntos
    :param num_graf: (int) Número de transformacion lineal realizada
    :param titulo: (string) Nombre de la transformación lineal (título del gráfico)
    :return None: (None) El gráfico se realiza de manera interna
    """
    if lista_seleccion[2]:
        stop = 1
    else:
        stop = len(opciones_seleccion[0])
    for k in range(0, stop):
        if k == stop -1:
            opciones_seleccion[0][k] = graficar_poligono(opciones_seleccion[0][k], num_graf, titulo, 
                        opciones_seleccion[1], True)
        else:
            opciones_seleccion[0][k] = graficar_poligono(opciones_seleccion[0][k], num_graf, titulo, 
                        opciones_seleccion[1], opciones_seleccion[2])

#  ---------------------------------------------------------------------------------------------------
# PROGRAMA PRINCIPAL 
contador = 0
repetir = "si"
while repetir == "si":
    os.system("cls")
    print("\t\t\t***GEOMETRÍA DE LAS TRANSFORMACIONES LINEALES***\n")
    if contador == 0:
        lista_seleccion = menu()
        graficar(lista_seleccion, contador, "Figura Original")
    contador += 1
    titulo_graf = menu_transf(lista_seleccion)
    graficar(lista_seleccion, contador, titulo_graf)
    repetir = input("Deseas realizar otra transformación si/no: ")
    repetir = repetir.lower()