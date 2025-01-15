#from numpy import real
import sympy
from sympy.solvers import solve
from sympy import Symbol
import time
#import numpy as np


inicio = time.time()

x = Symbol('alpha')
"""
print(solve(x**2 -1, x))
print(solve(x**3 + x**2 + x + 1, x))
print(solve(x**3 - 0*x**2 + 4*x -5, x))
print(solve(x**3 + 4*x -5, x))
print(solve((x-2)**2, x))
print(type(solve((x-2)**2, x)))
"""
print("--------------------------------")
sols = solve(x**3 + x**2 + x + 1, x)

for i in sols:
    try:
        print(f"Real {float(i)}")
    except:
        print(f"Complejo {i}")
print("--------------------------------")

matrix = sympy.Matrix([[x,0,0], [0, x**2, 0], [0,0,x**2+3]])
print(matrix.det())

# NO ES POSIBLE HACER EL DETERMINANTE CON SIMBOLICO
#array = np.array([[3,25,15], [30, 2, 2], [11,2,77]])
#det = np.linalg.det(array)
#print(f"Determinante = {det}")

final = time.time()
print(f"Tiempo ejecucion = {final - inicio}")