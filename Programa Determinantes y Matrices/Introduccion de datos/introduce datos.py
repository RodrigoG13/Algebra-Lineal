'''
INSTITUTO POLITÉCNICO NACIONAL
ESCUELA SUPERIOR DE CÓMPUTO

INGENIERÍA EN INTELIGENCIA ARTIFICIAL

ÁLGEBRA LINEAL
DETERMINANTES Y MATRICES

GRUPO: 2BM1
ALUMNO: TREJO ARRIAGA RODRIGO GERARDO

ESTE PROGRAMA RECIBE UNA MATRIZ A Y CALCULA LO SIGUIENTE:
i) EL DETERMINANTE DE A
ii) LA MATRIZ A^2
iii) EL DETERMINANTE DE A^2
iv) LA MATRIZ INVERSA DE A

ÚLTIMA MODIFICACIÓN: 01/03/2022
'''
#  ----------------------------------------------------------------------------------------------------------
# FUNCIONES


def convierte_string_array(string_num):
    array_num = []
    array_str = string_num.split(" ")
    for numero in array_str:
        array_num.append(float(numero))
    return array_num

#  --------------------------------------------------------------------------------------------------------------------
# PROGRAMA PRINCIPAL


print("\t\t\t\t\t\t\t\t\t***DETERMINANTES Y MATRICES***\n")
print("Instrucciones: Ingresa los elementos de las filas de la matriz separados por un sólo espacio")
numero_fil_col = int(input("¿Cuántas filas=columnas tendrá la matriz?: "))

# Recibe datos
s = 0
matrix_A = []
while s < numero_fil_col:
    string_fila = input(f"Fila{s+1})\t")
    array_fila = convierte_string_array(string_fila)
    while len(array_fila) != numero_fil_col:
        print(f'La fila no tiene el numero correcto de elementos, inténtalo nuevamente \U0001F61E.')
        string_fila = input(f"Fila{s + 1})\t")
        array_fila = convierte_string_array(string_fila)
        print(f"{s}")
    s += 1
    matrix_A.append(array_fila)

print(matrix_A)
