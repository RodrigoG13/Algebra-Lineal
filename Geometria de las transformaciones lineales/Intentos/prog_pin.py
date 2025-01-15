from grafico import *
from transf_lineales import *
import os

def convierte_string_array(string_num):
    """
    Convierte el string-vector ingresado por el usuario en una lista con los números del vector
    :param string_num: (string) String ingresado por el usuario
    :return array_num: (list) Vector ingresado por el usuario en una lista
    """
    array_num = []
    array_str = string_num.split(",")
    for numero in array_str:
        array_num.append(float(numero))
    return array_num

opciones = {    1: "Reflexión en el eje X",
                2: "Reflexión en el eje Y",
                3: "Expanxión en el eje X",
                4: "Expanxión en el eje Y",
                5: "Corte en el eje X",
                6: "Corte en el eje Y",
                7: "Rotación"}
os.system("cls")
print("\t\t\t***GEOMETRÍA DE LAS TRANSFORMACIONES LINEALES***\n")
print(f"""Instrucciones: Ingresa el numero de transformaciones que deseas hacer, a continuación, introduce los números del menu 
que correspondan a la transformación deseada.""")

print(  "\t 1. Reflexión en el eje X\n"
        "\t 2. Reflexión en el eje Y\n"
        "\t 3. Expanxión en el eje X\n"
        "\t 4. Expanxión en el eje Y\n"
        "\t 5. Corte en el eje X\n"
        "\t 6. Corte en el eje Y\n"
        "\t 7. Rotación\n")
num_transformaciones = int(input("¿Cuántas transformaciones deseas realizar?: "))


bandera_reorden = True
bandera_unicotrazo = True
transformaciones = []
for i in range(0, num_transformaciones):
    t = int(input(f"T{i+1})\t"))
    transformaciones.append(t)


puntos = []
num_puntos = int(input("¿De cuántos puntos será el polígono?: "))
for i in range(0, num_puntos):
    punto_string = input(f"P{i+1})\t")
    puntos.append(convierte_string_array(punto_string))
puntos = graficar_poligono(puntos,1, "Figura Original", True, True)

for j, i in enumerate(transformaciones):
    print("entra a for")
    puntos = [punto_matrix(r) for r in puntos]
    if i == 1:
        puntos = reflejar(puntos, True)
    elif i == 2:
        puntos = reflejar(puntos, False)
    elif i == 3:
        cte = float(input("Introduzca la constante de expansion: "))
        puntos = expandir(puntos, cte, True)
    elif i == 4:
        cte = float(input("Introduzca la constante de expansion: "))
        puntos = expandir(puntos, cte, False)
    elif i == 5:
        cte = float(input("Introduzca la constante de corte: "))
        puntos = cortar(puntos, cte, True)
    elif i == 6:
        cte = float(input("Introduzca la constante de corte: "))
        puntos = cortar(puntos, cte, False)
    elif i == 7:
        angulo = float(input("Introduzca el angulo de rotacion: "))
        puntos = rotar(puntos, angulo)
    
    
    elif i == 8:
        puntos = [[2,-9], [2,-10], [3,-10], [4,-11], [4,-12], [5,-12], [5,-14],
                [-12,-14], [-12,-12], [-11,-12], [-11,-11], [-10,-10], [-9,-10],
                [-9,0], [-7,5], [-2.5,11.5], [-2,10], [-1,13], [0,9], [8,2], [7,0],
                [-0.5,2.5], [-1,-2], [2,-9]]
        bandera_reorden = False
        puntos = graficar_poligono(puntos,j,"Jambas", True and bandera_reorden, True and bandera_unicotrazo)
    
    elif i == 9:
        bandera_reorden = False
        puntos = [[3,3], [5,-1], [6,-2], [8,0], [10,4], [12,8], [13,12], [13,16],
                [15,15], [19,15], [22,15], [24,15], [26,16], [25,14], [23,10],
                [22,6], [19,5], [17,3], [16,1], [15,-3], [15,-7], [13,-8], [11,-10],
                [9,-12], [8,-14], [7,-18], [5,-16], [1,-14], [0,-14], [-4,-15], 
                [-6,-17], [-8,-15], [-10,-13], [-11,-12], [-12,-12], [-13,-12], 
                [-14,-13], [-17,-15], [-18,-15], [-22,-13], [-24,-12], [-25,-12],
                [-27,-13], [-25,-11], [-23,-8], [-21,-5], [-19,0], [-15,-2], [-12,-4],
                [-10,-5], [-7,-6], [-4,-6], [-1,-6], [-1,-3], [-2,1], [0,-1], [1,0],
                [2,0], [3,1], [3,3]]
        puntos = graficar_poligono(puntos,j,"Jambas", True and bandera_reorden, True and bandera_unicotrazo)
    
    elif i == 10:
        bandera_unicotrazo = False
        bandera_reorden = False
        puntos = [[[12,0], [24,12], [20,16], [4,16], [0,12], [12,0]], [[2,12], [4,10], [4,12], [5,14],
        [7,15], [5,15], [2,12]], [[12,2], [15,5], [9,5], [12,2]], [[5,9], [8,8], [12,8], [16,7],
        [14,6], [12,6], [10,7], [7.5, 6], [5,9]], [[19,9], [22,12], [20,14], [20,12], [16,12], 
        [14,14], [12,15], [8,14], [7,13], [8,12], [12,11], [16,11], [19,9]], [[16,15], [17,15],
        [17,14], [16,15]]]
        for p in puntos:
            print(f"Puntos super = {p}")
            puntos = graficar_poligono(p,j,"Jambas", True and bandera_reorden, True and bandera_unicotrazo)    
    
    #puntos = graficar_poligono(puntos,j,"Jambas", True and bandera_reorden, True and bandera_unicotrazo)

    elif i == 11:
        bandera_unicotrazo = False
        bandera_reorden = False
        puntos = [[[2,-3], [-2,-3], [-4,-1], [-5,1], [-6,5], [-6,15], [-5,17], [-3,18], [3,18],
        [5,17], [6,15], [6,5], [5,1], [4,-1], [2,-3]], 
        [[-4,-1], [-4,3], [-6,6], [-5,9], [-5,15], [-3,16], [-2,16], [-1,11], [1,11],
        [2,16], [3,16], [5,15], [5,9], [6,6], [4,3], [4,-1]],
        [[-4,1], [-3,0], [-2,1], [2,1], [3,0], [4,1]],
        [[-4,8], [-1,7], [1,7], [4,8], [5,7], [4,6], [2,6], [1,7], [-1,7], [-2,6],
        [-4,6], [-5,7], [-4,8]]]
    
        for p in puntos:
            print(f"Puntos super = {p}")
            puntos = graficar_poligono(p,j,"Jambas", True and bandera_reorden, True and bandera_unicotrazo)    
    
    elif i == 12:
        bandera_unicotrazo = False
        bandera_reorden = False
        puntos = [[[-10,10], [-13,10], [-16,9], [-21,8], [-23,6], [-27,7], [-24,9],
        [-23,9], [-18,12], [-15,14],[-15,15], [-7,17], [-8,20], [-8,22], [-5,24], 
        [-3,24], [-1,23], [0,20], [0,18], [-1,18], [-2,16], [-3,16], [-1,12], [0,2],
        [-1,0], [7,-6], [6,-7], [7,-7], [9,-10], [14,-21], [17,-21], [18,-22],
        [18,-23], [12,-24], [11,-23], [11,-22], [8,-17], [8,-16], [6,-13], [6,-11],
        [5,-10], [1,-12], [-2,-9], [-3,-11], [-4,-11], [-6,-14], [-8,-14], [-20,-9],
        [-26,-12], [-27,-11], [-22,-5], [-21,-5], [-20,-7], [-15,-8], [-11,-8],
        [-9,-10], [-8,-9], [-9,-9], [-8,-4], [-8,1], [-7,3], [-10,10]],
        [[20,-16], [20,-13], [22,-11], [25,-11], [27,-13], [27,-16], [25,-18], 
        [22,-18], [20,-16]]]
        for p in puntos:
            print(f"Puntos super = {p}")
            puntos = graficar_poligono(p,j,"Jambas", True and bandera_reorden, True and bandera_unicotrazo)    
    