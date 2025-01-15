'''
                    LIBRERÍA DE SOLUCIÓN DE SISTEMAS DE ECUACIONES POR GAUSS JORDAN
@author: Rodrigo Gerardo Trejo Arriaga
'''
#  -------------------------------------------------------------------------------------------------
# MÓDULOS Y LIBRERÍAS IMPORTADAS

import itertools
from string import ascii_uppercase
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
#  -------------------------------------------------------------------------------------------------
# FUNCIONES


def labels_gen():
    """
    Genera las etiquetas que corresponden a cada punto del poligono
    :yield s: (str) Etiqueta que corrsponde a cada punto
    """
    size = 1
    while True:
        for s in itertools.product(ascii_uppercase, repeat=size):
            yield "".join(s)
        size +=1

# Crea un DataFrame con los puntos dados
crear_dataframe = lambda puntos: pd.DataFrame(puntos, columns=["x","y"])


def reordena_puntos(df):
    """
    Reordena los puntos de un polígono para poder graficarlo
    :param df: (DataFrame) DataFrame con los puntos introducidos por el usuario
    :return df: (DataFrame) DataFrame con los puntos ordenados para graficar
    """
    # Cálculo del centroide
    centroide = np.mean(df, axis=0)

    # Cáculo del ángulo polar
    aux = df - centroide
    polar_angles = np.arctan2(aux.y, aux.x)

    # Obtenemos un nuevo DataFrame con los vértices ordenados
    df = df.reindex(polar_angles.argsort())
    return df


def crear_guardar_grafico(df, titulo, min_x, max_x, min_y, max_y, un_solo_trazo):
    """
    Crea el gráfico persé y guarda la imagen en formato jpg
    :param df: (DataFrame) DataFrame con los puntos introducidos por el usuario
    :return None: El proceso de creación y guardado se realiza de manera interna
    """
    plt.title(titulo, fontsize=12)
    ax = plt.subplot(111)

    # Creamos el polígono
    plygon = plt.Polygon(df, fill=True, facecolor="#b3faff", edgecolor='#000e6b', alpha=1, zorder=1)
    ax.add_patch(plygon)

    # Creamos los vértices
    ax.scatter(df.x, df.y, c='b', zorder=2, s=12)

    # Mostramos los ejes centrados en el origen
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # Configuramos la rejilla
    ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.2)

    maxs = [max_x, max_y]
    mins = [min_x, min_y]

    min_min = min(mins)
    max_max = max(maxs)
    if min_min < 0:
        min_min = - min_min
    if max_max > min_min:
        rango = max_max
    else:
        rango = min_min

    saltos = 2*rango/10
    if saltos <= 2:
        saltos = 2*rango/5
    if saltos <= 2:
        saltos = 2*rango/2

    # Escalamos la gráfica
    #ax.autoscale_view()
    #plt.xticks(range(int(-rango)-int(saltos-1), int(rango)+int(saltos+1), int(saltos)))
    #plt.yticks(range(int(-rango)-int(saltos-1), int(rango)+int(saltos+1), int(saltos)))
    
    #ax.set_aspect('equal', ajustable = 'datalim')
    ax.set_aspect('equal')
    #ax.grid(color='none', linestyle='none', linewidth=0, alpha=0)
    # x.tick_params(axis='x', colors='none')
    #ax.tick_params(axis='y', colors='none')
    #plt.xticks(range(-20-5, 20+5))
    #plt.yticks(range(20-5, 20+5))
    #ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    #ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

    # Guardamos la gráfica
    #plt.savefig(f"{titulo}.jpg")

    if un_solo_trazo:
        plt.show()
        plt.close()


def graficar_poligono(puntos_usuario, num_trans, name_trans, reordenar, un_solo_trazo):
    """
    Funciión que gestina el gráfico del poligono
    :param puntos_usuario: (list) Lista de los puntos introducidos por el usuario
    :return None: El proceso de gestión se realiza de manera interna
    """

    puntos_x = [n[0] for n in puntos_usuario]
    puntos_y = [n[1] for n in puntos_usuario]

    min_x = min(puntos_x)
    max_x = max(puntos_x)
    min_y = min(puntos_x)
    max_y = max(puntos_x)

    #print(puntos_x)
    #print(puntos_y)

    data_frame = crear_dataframe(puntos_usuario)
    if reordenar:
        data_frame = reordena_puntos(data_frame)
    titulo = f"T{num_trans} - {name_trans}"
    crear_guardar_grafico(data_frame, titulo, min_x, max_x, min_y, max_y, un_solo_trazo)
    #if reordenar:
    return data_frame.to_numpy().tolist()