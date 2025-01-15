#  --------------------------------------------------------------------------------------------------------------------
# MÓDULOS Y LIBRERÍAS IMPORTADAS

from fractions import Fraction
#  --------------------------------------------------------------------------------------------------------------------
# FUNCIONES


# Función que convierte una fila de números string a flotantes ---
def convierte_string_array(string_num):
    array_num = []
    array_str = string_num.split(" ")
    for numero in array_str:
        array_num.append(float(numero))
    return array_num


# Función que obtiene la multiplicación de dos matrices ---
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


# Función que hace unos la diagonal ----
def diagonal_uno(matriz, filas, columnas):
    fraccion = 1
    r = 0
    t = 0
    while r < filas:
        constante = matriz[r][r]
        fraccion *= constante
        while t < columnas:
            matriz[r][t] = round(matriz[r][t]/constante, 25)
            t = t + 1
        t = 0
        r = r + 1
    return fraccion


# Función que verifica que el pivote no sea cero y si lo es, cambia de lugar la fila -----
def pivote_distinto_cero(matrix1, filas, columnas, elemento):
    ciclos = 0
    change = 0
    while matrix1[columnas][elemento] == 0:
        aux = matrix1[columnas]
        matrix1.pop(columnas)
        matrix1.insert(filas, aux)
        if ciclos == columnas:
            break
        ciclos = ciclos + 1
        change = len(matrix1) - columnas + 1
    return change


# Función que realiza las operaciones elementales en una matriz ----
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


# Función que hace ceros abajo de la diagonal -----
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
        j = pos_pivote + 1

        while j < filas:
            cte_sig_fila = matrix[j][pos_pivote]
            if cte_sig_fila != 0:
                matrix[j] = multiplica_resta_filas(matrix[pos_pivote][:], matrix[j][:], valor_pivote, cte_sig_fila)
                f_piv *= valor_pivote
                conta += 1
            j = j + 1
        pos_pivote = pos_pivote + 1
        if bandera:
            f_piv *= 1/diagonal_uno(matrix, filas, columnas)
    return f_piv


# Función que obtiene la matriz transpuesta ----------
def transpone_matrix(matriz):
    transpuesta = []
    for i in range(len(matriz[0])):
        transpuesta.append([])
        for j in range(len(matriz)):
            transpuesta[i].append(matriz[j][i])
    return transpuesta


# Función que obtiene el determinante de la matriz triangular superior -----
def calcula_determinante(matrix):
    multiplica_diagonal = 1
    for k in range(len(matrix)):
        multiplica_diagonal *= matrix[k][k]
    return multiplica_diagonal


# Función que imprime una matriz --------
def imprime_matrix(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]}\t\t", end="")
        print("")


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
            cte *= 1 / diagonaliza_abajo(m_det, len(m_det), len(m_det[0]))
            determinante_mdet = cte * calcula_determinante(m_det)
            m_cofactores[i][j] = (-1)**(i+j+2) * determinante_mdet
            cte = 1
    return m_cofactores

#  --------------------------------------------------------------------------------------------------------------------
# PROGRAMA PRINCIPAL


bandera = False

A = [[-1, 4, 2], [2, 1, 3], [-1, 2, 2]]
A_cpy = [[-1, 4, 2], [2, 1, 3], [-1, 2, 2]]

fraccion = 1 / diagonaliza_abajo(A, 3, 3)
determinante = fraccion * calcula_determinante(A)

matrix_cofactores = matriz_cofactores(A_cpy)
matrix_transpuesta = transpone_matrix(matrix_cofactores)
for i in range(0, len(matrix_transpuesta)):
    for j in range(0, len(matrix_transpuesta[i])):
        matrix_transpuesta[j][i] = Fraction(matrix_transpuesta[j][i]/determinante).limit_denominator(1000)
imprime_matrix(matrix_transpuesta)


"""
s = []
fila = 1
col = 1
for i, j in enumerate(A):
    if i == fila:
        continue
    else:
        s.append([])
    for k, l in enumerate(A[i]):
        if k == col:
            continue
        else:
            s[len(s)-1].append(l)
print(s)
"""



# matriz_cofactores(A)