from sympy import symbols
from fractions import Fraction

w = symbols("w", real=True)
x = symbols("x", real=True)
y = symbols("y", real=True)
z = symbols("z", real=True)
"""
lista = [x+y, x, y]
hola = (x+1)
lista1 = lista[:]
print(hola.evalf(1))
"""

"""
lista = [x+y, x, y]
matrix_res = []
p_l = 2
diccionarios = [{x:1, y:0}, {x:0, y:1}]
for i in range(0,2):
    aux = []
    for exp in lista:
        aux.append(exp.subs(diccionarios[i]))
    matrix_res.append(aux)
    aux = []
print(matrix_res)
"""
def genera_vectores(num_pl, pl,expresion):
    vect = []
    for j in range (0, num_pl):
        diccionario = {}
        for i in range(0, num_pl):
            if i == j:
                diccionario [pl[i]] = 1
            else:
                diccionario [pl[i]] = 0
        aux = []
        for exp in expresion:
            aux.append(Fraction(float(exp.subs(diccionario))).limit_denominator(1000))
        vect.append(aux)
        aux = []
    return vect

def imprimir_vectores(vect):
    for i in range(len(vect)):
        for j in range(len(vect[i])):
            if j == 0:
                print(f"({vect[i][j]}", end="")
            elif j == len(vect[i]) - 1:
                print(f"+{vect[i][j]})", end="")
            else:
                print(f"+{vect[i][j]}", end="")
        if i != len(vect) -1:
            print("+", end="")


param = [x,y]
lista = [x+y, x, y]
p_l = 2
"""
p_l = 1
param = [x]
lista = [-0.1*x, -0.3*x, x]
"""
vectores = genera_vectores(p_l,param, lista)
imprimir_vectores(vectores)








