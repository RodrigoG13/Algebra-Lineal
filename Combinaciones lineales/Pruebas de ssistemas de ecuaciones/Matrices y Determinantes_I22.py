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
ii) LA MATRIZ INVERSA DE A
iii) LA MATRIZ A^2
iv) EL DETERMINANTE DE A^2

ÚLTIMA MODIFICACIÓN: 16/03/2022
'''
#  --------------------------------------------------------------------------------------------------------------------
# MÓDULOS Y LIBRERÍAS IMPORTADAS

from fractions import Fraction
from tabulate import tabulate
#  --------------------------------------------------------------------------------------------------------------------
# FUNCIONES


# Función que convierte una fila de números string a flotantes
def convierte_string_array(string_num):
    array_num = []
    array_str = string_num.split(" ")
    for numero in array_str:
        array_num.append(float(numero))
    return array_num


# Función que imprime una matriz
def imprime_matrix(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]}\t\t", end="")
        print("")


# Función que obtiene la multiplicación de dos matrices
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


# Función que verifica que el pivote no sea cero y si lo es, cambia de lugar la fila
def pivote_distinto_cero(matrix1, filas, columnas, elemento):
    ciclos = 0
    change = 0
    while matrix1[columnas][elemento] == 0:
        aux = matrix1[columnas]
        matrix1.pop(columnas)
        matrix1.insert(filas, aux)
        if ciclos == filas:
            break
        ciclos = ciclos + 1
        change = change + len(matrix1) - columnas + 1
    return change


# Función que hace el pivote uno
def filapiv_uno(array, pospiv):
    cte = 1/array[pospiv]
    for iterador in range(0, len(array)):
        array[iterador] = array[iterador] * cte
    return array


# Función que realiza las operaciones elementales en una matriz
def multiplica_resta_filas(array1, array2, constante1, constante2):
    i = 0                 # piv
    j = 0
    k = 0
    while i < len(array1):
        array1[i] = array1[i] * - constante2
        i = i + 1
    while j < len(array2):
        array2[j] = array2[j] * constante1
        j = j + 1
    while k < len(array1):
        array2[k] = array2[k] + array1[k]
        k = k + 1
    return array2


# Función que hace ceros abajo de la diagonal
def diagonaliza_abajo(matrix, filas, columnas):
    conta = 0
    f_piv = 1
    limite_pivote = 0
    fila_cero = []
    for cero in range(0, columnas):
        fila_cero.append(0)
    if filas < columnas:
        limite_pivote = filas
    elif columnas < filas or columnas == filas:
        limite_pivote = columnas

    pos_pivote = 0
    while pos_pivote < limite_pivote:
        valor_pivote = matrix[pos_pivote][pos_pivote]
        if pos_pivote + 1 == limite_pivote and valor_pivote == 0:
            break
        elif valor_pivote == 0:
            cambios_filas = pivote_distinto_cero(matrix, filas, pos_pivote, pos_pivote)
            f_piv *= (-1)**cambios_filas
            if fila_cero in matrix:
                break
            valor_pivote = matrix[pos_pivote][pos_pivote]
        if valor_pivote != 0:
            matrix[pos_pivote] = filapiv_uno(matrix[pos_pivote][:], pos_pivote)
            f_piv *= 1/valor_pivote
            valor_pivote = matrix[pos_pivote][pos_pivote]
        j = pos_pivote + 1

        while j < filas:
            cte_sig_fila = matrix[j][pos_pivote]
            if cte_sig_fila != 0:
                matrix[j] = multiplica_resta_filas(matrix[pos_pivote][:], matrix[j][:], valor_pivote, cte_sig_fila)
                f_piv *= valor_pivote
                conta += 1
            j = j + 1
        pos_pivote = pos_pivote + 1
    return f_piv


# Función que obtiene el determinante de la matriz triangular superior
def calcula_determinante(matrix):
    multiplica_diagonal = 1
    for k in range(len(matrix)):
        multiplica_diagonal *= matrix[k][k]
    return multiplica_diagonal


# Función que obtiene las submatrices para la matriz de cofactores
def elimina_fil_col(matriz, fila, col):
    matriz_copy = []
    for i, j in enumerate(matriz):
        if i == fila:
            continue
        else:
            matriz_copy.append([])
        for k, l in enumerate(matriz[i]):
            if k == col:
                continue
            else:
                matriz_copy[len(matriz_copy) - 1].append(l)
    return matriz_copy


# Función que obtiene la matriz de cofactores
def matriz_cofactores(matrixf):
    m_cofactores = []
    cte = 1
    for i in range(len(matrixf)):
        m_cofactores.append([])
        for j in range(len(matrixf[0])):
            m_cofactores[i].append(0)
    for i, fila in enumerate(matrixf):
        for j, elemento in enumerate(matrixf[i]):
            m_det = elimina_fil_col(matrixf[:], i, j)
            cte *= 1/diagonaliza_abajo(m_det, len(m_det), len(m_det[0]))
            determinante_mdet = cte * calcula_determinante(m_det)
            m_cofactores[i][j] = (-1)**(i+j+2) * determinante_mdet
            cte = 1
    return m_cofactores


# Función que obtiene la matriz transpuesta
def transpone_matrix(matriz):
    transpuesta = []
    for i in range(len(matriz[0])):
        transpuesta.append([])
        for j in range(len(matriz)):
            transpuesta[i].append(matriz[j][i])
    return transpuesta
#  --------------------------------------------------------------------------------------------------------------------
# PROGRAMA PRINCIPAL


fraction_A = 1
fraction_A2 = 1
print("\t\t\t\t\t\t\t\t\t***DETERMINANTES Y MATRICES***\n")
print("Instrucciones: Ingresa los elementos de las filas de la matriz separados por un sólo espacio")
numero_fil_col = int(input("¿Cuántas filas=columnas tendrá la matriz?: "))

# Recibe datos
s = 0
matrix_A = []
matrixA_copy = []
while s < numero_fil_col:
    string_fila = input(f"Fila{s+1})\t")
    array_fila = convierte_string_array(string_fila)
    while len(array_fila) != numero_fil_col:
        print(f'La fila no tiene el numero correcto de elementos, inténtalo nuevamente \U0001F61E.')
        string_fila = input(f"Fila{s + 1})\t")
        array_fila = convierte_string_array(string_fila)
    s += 1
    matrix_A.append(array_fila)
    matrixA_copy.append(array_fila)
mA_cuadrada = multiplica_matrix(matrix_A[:], matrix_A[:])
mA_cuadrada_copy = multiplica_matrix(matrix_A[:], matrix_A[:])


print("\t\t\t <<<<<<<<<<<<<<<<< MATRIZ A >>>>>>>>>>>>>>>>>")
print(tabulate(matrix_A))
fraction_A *= 1/diagonaliza_abajo(matrixA_copy, len(matrixA_copy), len(matrixA_copy[0]))
determinante_A = fraction_A * calcula_determinante(matrixA_copy)
print(f"El determinate de la Matriz A es {determinante_A : .5f}")
print(f"Y en fracción: {Fraction(determinante_A).limit_denominator(1000)}\n")

if determinante_A != 0:
    print("\t\t\t <<<<<<<<<<<<<<<<< MATRIZ A\u02C9\u00b9  >>>>>>>>>>>>>>>>>")
    matrix_cofactores = matriz_cofactores(matrix_A)
    matrix_transpuesta = transpone_matrix(matrix_cofactores)
    for i in range(0, len(matrix_transpuesta)):
        for j in range(0, len(matrix_transpuesta[i])):
            matrix_transpuesta[j][i] = Fraction(matrix_transpuesta[j][i] / determinante_A).limit_denominator(1000000)
    print(tabulate(matrix_transpuesta))
    print("\n")
    imprime_matrix(matrix_transpuesta)
    print("\n")
else:
    print("Esta matriz no tiene inversa ):\n")

print("\t\t\t <<<<<<<<<<<<<<<<< MATRIZ A\u00b2  >>>>>>>>>>>>>>>>>")
print(tabulate(mA_cuadrada))
fraction_A2 *= 1/diagonaliza_abajo(mA_cuadrada_copy, len(mA_cuadrada_copy), len(mA_cuadrada_copy[0]))
determinante_A2 = fraction_A2 * calcula_determinante(mA_cuadrada_copy)
print(f"El determinate de la Matriz A\u00b2 es {determinante_A2 : .5f}")
print(f"Y en fracción: {Fraction(determinante_A2).limit_denominator(1000)}")