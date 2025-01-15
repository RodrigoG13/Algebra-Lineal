'''
INSTITUTO POLITÉCNICO NACIONAL
ESCUELA SUPERIOR DE CÓMPUTO

INGENIERÍA EN INTELIGENCIA ARTIFICIAL

ÁLGEBRA LINEAL
RESOLUCIÓN DE SISTEMAS DE ECUACIONES POR EL MÉTODO DE GAUSS-JORDAN

GRUPO: 2BM1
ALUMNO: TREJO ARRIAGA RODRIGO GERARDO

ESTE PROGRAMA RESUELVE UN SISTEMA DE ECUACIONES POR EL MÉTODO DE GAUSS-JORDAN INDICANDO SI:
i) TIENE SOLUCIÓN ÚNICA (PRESENTÁNDOLA)
ii) TIENE INFINIDAD DE SOLUCIONES, DÁNDOLAS EN TÉRMINOS DE PARÁMETROS LIBRES
iii) NO TIENE SOLUCIÓN

ÚLTIMA MODIFICACIÓN: 01/03/2022
'''
#  --------------------------------------------------------------------------------------------------------------------
# MÓDULOS Y LIBRERÍAS IMPORTADAS

from fractions import Fraction
#  ----------------------------------------------------------------------------------------------------------
# FUNCIONES


# Función que almacena en orden las variables de las ecuaciones
def almacena_variables(ecuacion_string):            # "-w+6x+2y=2"
    guion = "-"
    newstring = ''.join([i for i in ecuacion_string if i.isalpha()])    # "wxy"
    var_string = guion.join(newstring)              # "w-x-y"
    variables_array = var_string.split("-")         # ["w", "x", "y"]
    return variables_array


# Función que convierte una ecuación en una fila de la matriz
def convierte_sistema_matriz(ecuacion_string):      # "-w+6x+2y=2"
    uno_string = "1"
    fila = []
    signo_mas = "+"
    signo_menos = "-"
    uno_positivo = "+1"
    uno_negativo = "-1"
    ecuacion_string = ecuacion_string.lower()
    ecuacion_string = ecuacion_string.replace("=", "x")     # "-w+6x+2yx2"
    for a in range(97, 123):
        signo_mas_letra = signo_mas + chr(a)        # "+w"
        signo_menos_letra = signo_menos + chr(a)    # "-w"

        if ecuacion_string.startswith(chr(a)):      # "w"
            ecuacion_string = uno_string + ecuacion_string
            ecuacion_string = ecuacion_string.replace(chr(a), "x")

        elif signo_mas_letra in ecuacion_string:    # "+w"
            uno_mas_letra = uno_positivo+"x"        # "+1x"
            ecuacion_string = ecuacion_string.replace(signo_mas_letra, uno_mas_letra)

        elif signo_menos_letra in ecuacion_string:  # "-w"
            uno_menos_letra = uno_negativo+"x"      # "-1x"
            ecuacion_string = ecuacion_string.replace(signo_menos_letra, uno_menos_letra)
            # "-w+6x+2y=2" -> "-1x+6x+2y=2"

        elif chr(a) in ecuacion_string:             # "w"
            ecuacion_string = ecuacion_string.replace(chr(a), "x")

            # "-1x+6x+2xx2"

    ecuacion_string = ecuacion_string.split("x")   # ["-1","+6","+2","","2"]
    ecuacion_string.remove("")                     # ["-1","+6","+2","2"]
    for numero in ecuacion_string:
        fila.append(float(numero))
    return fila                                    # [-1, 6, 2 , 2]


# Función que verifica que el pivote no sea cero y si lo es, cambia de lugar la fila
def pivote_distinto_cero(matrix1, ecuaciones, arrayde_arrays, elemento):
    ciclos = 0
    while matrix1[arrayde_arrays][elemento] == 0:
        aux = matrix1[arrayde_arrays]
        matrix1.pop(arrayde_arrays)
        matrix1.insert(ecuaciones, aux)
        if ciclos == arrayde_arrays:
            break
        ciclos = ciclos + 1
    return matrix1


# Función que realiza las operaciones elementales en una matriz
def multiplica_resta_filas(array1, array2, constante1, constante2):
    i = 0
    j = 0
    k = 0
    while i < len(array1):
        array1[i] = array1[i] * constante2
        i = i + 1
    while j < len(array2):
        array2[j] = array2[j] * -constante1
        j = j + 1
    while k < len(array1):
        array2[k] = array2[k] + array1[k]
        k = k + 1
    return array2


# Función que hace ceros abajo de la diagonal
def diagonaliza_abajo(matrix, ecuaciones, variables):
    limite_pivote = 0
    fila_cero = []
    for cero in range(0, variables):
        fila_cero.append(0)

    if ecuaciones < variables:
        limite_pivote = ecuaciones
    elif variables < ecuaciones or variables == ecuaciones:
        limite_pivote = variables

    pos_pivote = 0
    while pos_pivote < limite_pivote:
        valor_pivote = matrix[pos_pivote][pos_pivote]
        if pos_pivote + 1 == limite_pivote and valor_pivote == 0:
            break
        elif valor_pivote == 0:
            pivote_distinto_cero(matrix, ecuaciones, pos_pivote, pos_pivote)
            if fila_cero in matrix:
                break
            valor_pivote = matrix[pos_pivote][pos_pivote]
        j = pos_pivote + 1

        while j < ecuaciones:
            cte_sig_fila = matrix[j][pos_pivote]
            if cte_sig_fila != 0:
                matrix[j] = multiplica_resta_filas(matrix[pos_pivote][:], matrix[j][:], valor_pivote, cte_sig_fila)
            j = j + 1
        pos_pivote = pos_pivote + 1
    return matrix


# Función que calcula el rango de una matriz
def calcula_range(matrix):
    cuenta_ceros = 0
    filas_cero = 0
    for fila in range(0, len(matrix)):
        for elemento in range(0, len(matrix[fila])):
            if matrix[fila][elemento] == 0:
                cuenta_ceros = cuenta_ceros + 1
        if cuenta_ceros == len(matrix[fila]):
            filas_cero = filas_cero + 1
        cuenta_ceros = 0
    range_matrix = len(matrix) - filas_cero
    return range_matrix


# Función que hace ceros arriba de la diagonal
def diagonaliza_arriba(matrix, ecuaciones, variables):
    limite_pivote = 0
    if ecuaciones < variables:
        limite_pivote = ecuaciones
    elif variables < ecuaciones or variables == ecuaciones:
        limite_pivote = variables

    pos_pivote = limite_pivote - 1
    while pos_pivote >= 0:
        valor_pivote = matrix[pos_pivote][pos_pivote]
        if valor_pivote == 0:
            pivote_distinto_cero(matrix, ecuaciones, pos_pivote, pos_pivote)
            valor_pivote = matrix[pos_pivote][pos_pivote]
        j = pos_pivote - 1
        while j >= 0:
            cte_sig_fila = matrix[j][pos_pivote]
            if cte_sig_fila != 0:
                matrix[j] = multiplica_resta_filas(matrix[pos_pivote][:], matrix[j][:], valor_pivote, cte_sig_fila)
            j = j - 1
        pos_pivote = pos_pivote - 1
    return matrix


# Función que hace unos la diagonal
def diagonal_uno(matriz, ecuaciones, variables3):
    r = 0
    t = 0
    while r < ecuaciones:
        constante = matriz[r][r]
        while t <= variables3:
            matriz[r][t] = round(matriz[r][t]/constante, 10)
            t = t + 1
        t = 0
        r = r + 1
    return matriz


# Función que elimina las filas de "puros ceros" en la matriz aumentada
def elimina_fila_cero(matrix, elementos):
    filas_eliminadas = 0
    fila_cero = []
    for cero in range(0, elementos):
        fila_cero.append(0)
    filas_cero = matrix.count(fila_cero)
    for eliminador in range(0, filas_cero):
        matrix.remove(fila_cero)
        filas_eliminadas = filas_eliminadas + 1
    return filas_eliminadas


# Función que imprime la infinidad de soluciones en términos de sus parámetros libres
def imprime_soluciones_infinitas(matrix, literales, num_param, param):
    comienzo = len(matrix[0]) - num_param
    p_l = 0
    bucles = 0
    for indice, ecuacion in enumerate(matrix):
        if matrix[indice][-1] == 0:
            print(f"{literales[indice]} = ", end="")
        else:
            print(f"{literales[indice]} = {matrix[indice][-1]}", end="")
        for p in range(comienzo, len(matrix[0])):
            if matrix[indice][p - 1] < 0:
                print("+", end="")
            print(f"{-matrix[indice][p - 1]}{param[p_l]}", end="")
            p_l = p_l + 1
        print("\n")
        p_l = 0

    p_l = 0
    print("O, con términos fraccionarios: ")
    for indice, ecuacion in enumerate(matrix):
        if matrix[indice][-1] == 0:
            print(f"{literales[indice]} ≈ ", end="")
        else:
            print(f"{literales[indice]} ≈ {Fraction(matrix[indice][-1]).limit_denominator(1000)}", end="")
        for p in range(comienzo, len(matrix[0])):
            if matrix[indice][p - 1] < 0:
                print("+", end="")
            print(f"{-Fraction(matrix[indice][p - 1]).limit_denominator(1000)}{param[p_l]}", end="")
            p_l = p_l + 1
        print("\n")
        bucles = bucles + 1
        p_l = 0

    for g in range(0, bucles):
        literales.pop(0)
#  --------------------------------------------------------------------------------------------------------------------
# PROGRAMA PRINCIPAL


matrix_aumentada = []
matrix_coeficientes = []
variables = []
filas_ceros = []
parametros = ["λ\u2081", "λ\u2082", "λ\u2083", "λ\u2084", "λ\u2085", "λ\u2086", "λ\u2087", "λ\u2088", "λ\u2089"]

print("                             ***SOLUCIÓN DE SISTEMAS DE ECUACIONES POR GAUSS-JORDAN***\n")
print("Instrucciones: Ingresa el sistema de ecuaciones con diferentes literales (...x,y,z), sin espacios"
      " y en un mismo orden.\n"
      "Por ejemplo: ax+by+cz=d\n"
      "             ex+fy+gz=h          Donde a,b,c,d,e,f,g,h,i,j,k,l ∈ ℝ\n"
      "             ix+jy+kz=l\n")
print("NOTA: Incluye todas las variables incluso si su coeficiente es 0 (cero).")
numero_ecs = int(input("¿Cuántas ecuaciones deseas ingresar?: "))
numero_incognitas = int(input("¿De cuántas variables?: "))

# Recibe datos
s = 0
while s < numero_ecs:
    ecuacion_str = input(f"Ec{s+1})     ")
    ecuacion_array = convierte_sistema_matriz(ecuacion_str)
    while len(ecuacion_array) < numero_incognitas + 1:
        print(f'La ecuación no tiene el numero correcto de variables, inténtalo nuevamente \U0001F61E.')
        ecuacion_str = input(f"Ec{s + 1})     ")
        ecuacion_array = convierte_sistema_matriz(ecuacion_str)
    matrix_aumentada.append(ecuacion_array)
    matrix_coeficientes.append(ecuacion_array)
    if s == 0:
        variables = almacena_variables(ecuacion_str)
    s = s+1

# Calcula el rango de la matriz aumentada y de coeficientes
matrix_coeficientes = pivote_distinto_cero(matrix_coeficientes, numero_ecs, 0, 0)
matrix_aumentada = pivote_distinto_cero(matrix_aumentada, numero_ecs, 0, 0)
diagonaliza_abajo(matrix_aumentada, numero_ecs, numero_incognitas)
diagonaliza_abajo(matrix_coeficientes, numero_ecs, numero_incognitas)

print(f"numero de incog {numero_incognitas}")
for ind in range(0, len(matrix_coeficientes)):
    matrix_coeficientes[ind] = matrix_coeficientes[ind][0:numero_incognitas]
rango_aumentada = calcula_range(matrix_aumentada)
rango_coeficientes = calcula_range(matrix_coeficientes)

# Clasifica al sistema
if rango_aumentada == rango_coeficientes and rango_aumentada == numero_incognitas:
    for cero in range(0, numero_incognitas + 1):
        filas_ceros.append(0)
    if filas_ceros in matrix_aumentada:
        numero_fceros = matrix_aumentada.count(filas_ceros)
        for n in range(0, numero_fceros):
            matrix_aumentada.remove(filas_ceros)
        numero_ecs = numero_ecs - numero_fceros
    diagonal_uno(matrix_aumentada, numero_ecs, numero_incognitas)
    diagonaliza_arriba(matrix_aumentada, numero_ecs, numero_incognitas)
    diagonal_uno(matrix_aumentada, numero_ecs, numero_incognitas)
    print('\nEl sistema tiene una única solución \U0001F642')
    print("Solución del sistema:")
    v = 0
    while v < len(matrix_aumentada):
        print(f"\t{variables[v]} = {matrix_aumentada[v][-1]} ≈ ", end="")
        print(f"{Fraction(matrix_aumentada[v][-1]).limit_denominator(1000)}")
        v = v + 1

elif rango_aumentada == rango_coeficientes and rango_aumentada < numero_incognitas:
    print('\nEl sistema tiene infinidad de soluciones \U0001F914')
    numero_parametros = numero_incognitas - rango_aumentada
    f_eliminadas = elimina_fila_cero(matrix_aumentada, numero_incognitas + 1)
    numero_ecs = numero_ecs - f_eliminadas
    diagonal_uno(matrix_aumentada, numero_ecs, numero_incognitas)
    diagonaliza_arriba(matrix_aumentada, numero_ecs, numero_incognitas)
    diagonal_uno(matrix_aumentada, numero_ecs, numero_incognitas)
    print(f"En términos de parámetros libres la solución es: ")
    imprime_soluciones_infinitas(matrix_aumentada, variables, numero_parametros, parametros)

    print("Donde: ")
    for ind, variable in enumerate(variables):
        print(f"{variable} = {parametros[ind]}")

elif rango_aumentada != rango_coeficientes:
    print('\nEl sistema no tiene solución, observa la matriz \U0001F910!!!')
    print(matrix_aumentada)