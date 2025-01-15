
def elimina_fila_cero(matrix, elementos):
    filas_eliminadas = 0
    fila_cero = []
    for cero in range(0, elementos):
        fila_cero.append(0)
    print(fila_cero)
    filas_cero = matrix.count(fila_cero)
    for eliminador in range(0, filas_cero):
        matrix.remove(fila_cero)
        filas_eliminadas = filas_eliminadas + 1
        print(matrix)
    return filas_eliminadas


matriz = [[1, 2, 3, 4],[0, 0, 0, 0], [7, 6, 5, 4], [0, 0, 0, 0], [3, 4, 5, 6], [0, 0, 0, 0]]
num_ecs = 6
num_var = 3
print(elimina_fila_cero(matriz, num_var + 1))
print(matriz)



