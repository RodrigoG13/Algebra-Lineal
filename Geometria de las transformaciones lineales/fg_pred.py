'''
                        LIBRERÍA CON LOS DICCIONARIOS DE LAS FIGURAS PREESTABLECIDAS 
                                Y OPCIONES DE LAS TRANFORMACIONES LINEALES
@author: Rodrigo Gerardo Trejo Arriaga
'''

#  ------------------------------------------------------------------------------------------------
# Puntos para la figura del caballito
caballito =     [[2,-9], [2,-10], [3,-10], [4,-11], [4,-12], [5,-12], [5,-14],
                [-12,-14], [-12,-12], [-11,-12], [-11,-11], [-10,-10], [-9,-10],
                [-9,0], [-7,5], [-2.5,11.5], [-2,10], [-1,13], [0,9], [8,2], [7,0],
                [-0.5,2.5], [-1,-2], [2,-9]]

# Puntos para la figura del murciélago
murcielago =    [[3,3], [5,-1], [6,-2], [8,0], [10,4], [12,8], [13,12], [13,16],
                [15,15], [19,15], [22,15], [24,15], [26,16], [25,14], [23,10],
                [22,6], [19,5], [17,3], [16,1], [15,-3], [15,-7], [13,-8], [11,-10],
                [9,-12], [8,-14], [7,-18], [5,-16], [1,-14], [0,-14], [-4,-15], 
                [-6,-17], [-8,-15], [-10,-13], [-11,-12], [-12,-12], [-13,-12], 
                [-14,-13], [-17,-15], [-18,-15], [-22,-13], [-24,-12], [-25,-12],
                [-27,-13], [-25,-11], [-23,-8], [-21,-5], [-19,0], [-15,-2], [-12,-4],
                [-10,-5], [-7,-6], [-4,-6], [-1,-6], [-1,-3], [-2,1], [0,-1], [1,0],
                [2,0], [3,1], [3,3]]

# Puntos para la figura de superman
superman =      [[[12,0], [24,12], [20,16], [4,16], [0,12], [12,0]], [[2,12], [4,10], [4,12], [5,14],
                [7,15], [5,15], [2,12]], [[12,2], [15,5], [9,5], [12,2]], [[5,9], [8,8], [12,8], [16,7],
                [14,6], [12,6], [10,7], [7.5, 6], [5,9]], [[19,9], [22,12], [20,14], [20,12], [16,12], 
                [14,14], [12,15], [8,14], [7,13], [8,12], [12,11], [16,11], [19,9]], [[16,15], [17,15],
                [17,14], [16,15]]]

# Puntos para la figura de ironman
ironman =       [[[2,-3], [-2,-3], [-4,-1], [-5,1], [-6,5], [-6,15], [-5,17], [-3,18], [3,18],
                [5,17], [6,15], [6,5], [5,1], [4,-1], [2,-3]], 
                [[-4,-1], [-4,3], [-6,6], [-5,9], [-5,15], [-3,16], [-2,16], [-1,11], [1,11],
                [2,16], [3,16], [5,15], [5,9], [6,6], [4,3], [4,-1]],
                [[-4,1], [-3,0], [-2,1], [2,1], [3,0], [4,1]],
                [[-4,8], [-1,7], [1,7], [4,8], [5,7], [4,6], [2,6], [1,7], [-1,7], [-2,6],
                [-4,6], [-5,7], [-4,8]]]

# Puntos para la figura del futbolista
futbolista =    [[[-10,10], [-13,10], [-16,9], [-21,8], [-23,6], [-27,7], [-24,9],
                [-23,9], [-18,12], [-15,14],[-15,15], [-7,17], [-8,20], [-8,22], [-5,24], 
                [-3,24], [-1,23], [0,20], [0,18], [-1,18], [-2,16], [-3,16], [-1,12], [0,2],
                [-1,0], [7,-6], [6,-7], [7,-7], [9,-10], [14,-21], [17,-21], [18,-22],
                [18,-23], [12,-24], [11,-23], [11,-22], [8,-17], [8,-16], [6,-13], [6,-11],
                [5,-10], [1,-12], [-2,-9], [-3,-11], [-4,-11], [-6,-14], [-8,-14], [-20,-9],
                [-26,-12], [-27,-11], [-22,-5], [-21,-5], [-20,-7], [-15,-8], [-11,-8],
                [-9,-10], [-8,-9], [-9,-9], [-8,-4], [-8,1], [-7,3], [-10,10]],
                [[20,-16], [20,-13], [22,-11], [25,-11], [27,-13], [27,-16], [25,-18], 
                [22,-18], [20,-16]]]

# Diccionario con los puntos y banderas de cada figura preestablecida
# "X":[lista_puntos, bandera_reordenamiento, bandera_unicoTrazo]

figuras_pred = {"A": [[caballito], 0, 1], 
                "B": [[murcielago], 0, 1],
                "C": [superman, 0, 0],
                "D": [ironman, 0, 0],
                "E": [futbolista, 0, 0]}

# Diccionario con las opciones de las tranformaciones lineales
opciones_transf = {     1: "Reflexión en el eje X",
                        2: "Reflexión en el eje Y",
                        3: "Expanxión en el eje X",
                        4: "Expanxión en el eje Y",
                        5: "Corte en el eje X",
                        6: "Corte en el eje Y",
                        7: "Rotación"}