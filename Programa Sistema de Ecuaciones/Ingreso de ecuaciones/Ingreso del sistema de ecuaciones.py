"""
Ingreso y lectura del sistema de ecuaciones mxn
"""


def llena_matrix(r, s):
    if s+1 < columnas:
        n = int(input(f"Ingresa el coeficiente de A{r+1}{s+1}: "))
    else:
        n = int(input(f"Ingresa el coeficiente de B{r+1}: "))
    return n


def imprime_sistema(sistema):
    for indice, ecuacion in enumerate(sistema):
        for indice2, numero in enumerate(sistema[indice]):
            if numero > 0 and indice2+1 < len(sistema[indice]):
                print(f"+{numero}X{indice2+1}", end="   ")
            elif numero < 0 and indice2+1 < len(sistema[indice]):
                print(f"{numero}X{indice2+1}", end="    ")
            else:
                print(f"=  {numero}")


i = 0
print("Este programa guarda un sistema de ecs de mxn del tipo:\n "
      "    A11X1 + A12X2 + ... + A1nXn = B1\n"
      "     A21X1 + A22X2 + ... + A2nXn = B2\n"
      "                     ...\n"
      "     Am1X1 + Am2X2 + ... + AmnXn = Bm\n")
filas = int(input("Ingresa el numero de ecuaciones: "))
columnas = int(input("Ingresa el numero de variables: ")) + 1
sistema_ecs = [[llena_matrix(i, j) for j in range(columnas)]for i in range(filas)]
print("\nTu sistema de ecuaciones es: ")
imprime_sistema(sistema_ecs)
print(sistema_ecs)
