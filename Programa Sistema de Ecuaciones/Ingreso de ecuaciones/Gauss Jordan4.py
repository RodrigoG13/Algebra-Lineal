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

        if ecuacion_string.startswith(chr(a)):
            ecuacion_string = uno + ecuacion_string
            ecuacion_string = ecuacion_string.replace(chr(a), "x")
            if k == (numero_ecs -1): variables.append(chr(a))

        elif sin_unomas_letra in ecuacion_string:
            uno_mas_letra = uno_mas+"x"
            ecuacion_string = ecuacion_string.replace(sin_unomas_letra, uno_mas_letra)
            if k == (numero_ecs -1): variables.append(chr(a))

        elif sin_unomenos_letra in ecuacion_string:
            uno_menos_letra = uno_menos+"x"
            ecuacion_string = ecuacion_string.replace(sin_unomenos_letra, uno_menos_letra)
            if k == (numero_ecs - 1): variables.append(chr(a))

        elif chr(a) in ecuacion_string:
            ecuacion_string = ecuacion_string.replace(chr(a), "x")
            if k == (numero_ecs - 1): variables.append(chr(a))

    ecuacion_string = ecuacion_string.split("x")
    ecuacion_string.remove("")
    for numero in ecuacion_string:
        fila.append(float(numero))
    return fila
#  --------------------------------------------------------------------------------------------------------------------
# PROGRAMA PRINCIPAL

matrix_aumentada = []
matrix_coeficientes = []
variables = []
print("                                  ***SISTEMAS DE ECUACIONES POR GAUSS JORDAN**\n")
print("Instrucciones: Ingresa el sistema de ecuaciones con diferentes variables (x,y,z...), sin espacios"
      " y en un mismo orden\n"
                 "Por ejemplo: ax+by+cz=d\n"
                 "             ex+fy+gz=h\n"
                 "             ix+jy+kz=l\n")
numero_ecs = int(input("¿Cuántas ecuaciones deseas ingresar?: "))
numero_incognitas = int(input("¿De cuántas ecuaciones?: "))
k = 0
while k < numero_ecs:
    ecuacion_str = input(f"Ec{k+1})     ")
    ecuacion_array = ingresa_convierte_sistema(ecuacion_str)
    matrix_aumentada.append(ecuacion_array)
    matrix_coeficientes.append(ecuacion_array[0:len(ecuacion_array)-1])
    k = k+1
print(matrix_aumentada)
print(matrix_coeficientes)
print(variables)

