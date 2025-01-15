'''
INSTITUTO POLITÉCNICO NACIONAL
ESCUELA SUPERIOR DE CÓMPUTO

ALGEBRA LINEAL
RESOLUCION DE SISTEMAS DE ECUACIONES POR EL METODO DE GAUSS JORDAN

GRUPO: 2BM1
ALUMNO: TREJO ARRIAGA RODRIGO GERARDO

ESTE PROGRAMA RESUELVE UN SISTEMA DE ECUACIONES POR EL METODO DE GAUSS JORDAN INDICANDO SI:
i) TIENE UNA ÚNICA SOLUCION (PRESENTÁNDOLA)
ii) TIENE INFINIDAD DE SOLUCIONES
iii) NO TIENE SOLUCION
'''
#  --------------------------------------------------------------------------------------------------------------------
# FUNCIONES


def ingresa_convierte_sistema(ecuacion_string):
    uno = "1"
    fila = []
    sin_unomas = "+"
    sin_unomenos = "-"
    uno_mas = "+1"
    uno_menos = "-1"
    ecuacion_string = ecuacion_string.lower()
    ecuacion_string = ecuacion_string.replace("=", "x")
    for a in range(97, 123):
        sin_unomas_letra = sin_unomas + chr(a)
        sin_unomenos_letra = sin_unomenos + chr(a)

        if sin_unomas_letra in ecuacion_string:
            uno_mas_letra = uno_mas+"x"
            ecuacion_string = ecuacion_string.replace(sin_unomas_letra, uno_mas_letra)

        elif sin_unomenos_letra in ecuacion_string:
            uno_menos_letra = uno_menos+"x"
            ecuacion_string = ecuacion_string.replace(sin_unomenos_letra, uno_menos_letra)

        elif chr(a) in ecuacion_string:
            ecuacion_string = ecuacion_string.replace(chr(a), "x")

    ecuacion_string = ecuacion_string.split("x")
    ecuacion_string.remove("")
    for numero in ecuacion_string:
        fila.append(float(numero))
    return fila
#  --------------------------------------------------------------------------------------------------------------------
# PROGRAMA PRINCIPAL

matrix = []
print("                                  ***SISTEMAS DE ECUACIONES POR GAUSS JORDAN**\n")
print("Instrucciones: Ingresa el sistema de ecuaciones con diferentes variables (x,y,z...), sin espacios"
      " y en un mismo orden\n"
                 "Por ejemplo: ax+by+cz=d\n"
                 "             ex+fy+gz=h\n"
                 "             ix+jy+kz=l\n")
numero_ecs = int(input("¿Cuantas ecuaciones deseas ingresar?: "))
k = 0
while k < numero_ecs:
    ecuacion = input(f"Ec{k+1})     ")
    matrix.append(ingresa_convierte_sistema(ecuacion))
    k = k+1
print(matrix)
