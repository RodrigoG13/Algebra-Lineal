def imprime_soluciones_infinitas(matrix, literales, num_param, param):

    comienzo = len(matrix[0]) - num_param
    p_l = 0
    for indice, ecuacion in enumerate(matrix):
        print(f"{literales[indice]} = {matrix[indice][-1]}", end="")
        for p in range(comienzo, len(matrix[0])):
            if matrix[indice][p - 1] < 0:
                print("+", end="")

            print(f"{-matrix[indice][p - 1]}{param[p_l]}", end="")
            p_l = p_l + 1
        print("\n")
        p_l = 0








variables = ["v", "w", "x", "y", "z"]
matriz = [[1, 0, 7, 3, 6, 26], [0, 1, 5, 1, 4, 12]]
parametros = ["λ\u2081", "λ\u2082", "λ\u2083", "λ\u2084", "λ\u2085", "λ\u2086", "λ\u2087", "λ\u2088", "λ\u2089"]
n_param = 3
imprime_soluciones_infinitas(matriz, variables, n_param, parametros)