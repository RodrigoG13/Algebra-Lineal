'''
                        LIBRERÍA CON LOS DICCIONARIOS DE LAS FIGURAS PREESTABLECIDAS 
                                Y OPCIONES DE LAS TRANFORMACIONES LINEALES
@author: Rodrigo Gerardo Trejo Arriaga
'''

#  ------------------------------------------------------------------------------------------------
# Puntos para la figura de fig1
fig1 =     []

# Puntos para la figura de fig2
fig2 =    []

# Puntos para la figura de fig3
fig3 =      []

# Puntos para la figura de fig4
fig4 =       []

# Puntos para la figura de fig5
fig5 =    []

# Diccionario con los puntos y banderas de cada figura preestablecida
# "X":[lista_puntos, bandera_reordenamiento, bandera_unicoTrazo]

figuras_pred = {"A": [[fig1], 0, 1], 
                "B": [[fig2], 0, 1],
                "C": [fig3, 0, 0],
                "D": [fig4, 0, 0],
                "E": [fig5, 0, 0]}

# Diccionario con las opciones de las tranformaciones lineales
opciones_transf = {     1: "Reflexión en el eje X",
                        2: "Reflexión en el eje Y",
                        3: "Expanxión en el eje X",
                        4: "Expanxión en el eje Y",
                        5: "Corte en el eje X",
                        6: "Corte en el eje Y",
                        7: "Rotación"}