def imprime_matrix(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]}\t\t", end="")
        print("\n")


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


def transpone_matrix(matriz):
    transpuesta = []
    for i in range(len(matriz[0])):
        transpuesta.append([])
        for j in range(len(matriz)):
            transpuesta[i].append(matriz[j][i])
    return transpuesta


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
A_cuadrada = multiplica_matrix(matrix, matrix)
print("Original")
imprime_matrix(matrix)
print("\n")
print("Cuadrada")
imprime_matrix(A_cuadrada)
print("\n")
print("Transpuesta")
matrix_transpuesta = transpone_matrix(matrix)
imprime_matrix(matrix_transpuesta)