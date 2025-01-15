'''
                            LIBRERÍA DE GRAFICADOR DE FIGURAS EN R2
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
    :return df: (DataFrame) DataFrame con los puntos ordenados y listos para graficar
    """
    # Cálculo del centroide
    centroide = np.mean(df, axis=0)

    # Cáculo del ángulo polar
    aux = df - centroide
    polar_angles = np.arctan2(aux.y, aux.x)

    # Obtenemos un nuevo DataFrame con los vértices ordenados
    df = df.reindex(polar_angles.argsort())
    return df


def crear_guardar_grafico(df, titulo, un_solo_trazo):
    """
    Crea el gráfico persé y guarda la imagen en formato jpg
    :param df: (DataFrame) DataFrame con los puntos introducidos por el usuario
    :param titulo: (str) Título que se colocará al gráfico
    :param un_solo_trazo: (int) 1 -> La gráfica es de un único trazo
                                0 -> La gráfica no es de un único trazo
    :return None: (None) El proceso de creación y guardado del gráfico se realiza de manera interna
    """
    plt.title(titulo, fontsize=12)
    ax = plt.subplot(111)

    # Creamos el polígono
    plygon = plt.Polygon(df, fill=True, facecolor="#f59e9e", edgecolor='#c70000', alpha=1, zorder=1)
    ax.add_patch(plygon)

    # Creamos los vértices
    ax.scatter(df.x, df.y, c='r', zorder=2, s=12)

    # Mostramos los ejes centrados en el origen
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # Configuramos la rejilla
    ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.2)
    ax.set_aspect('equal')

    # Guardamos la gráfica
    plt.savefig(f"{titulo}.jpg")

    # Si la gráfica es de un solo trazo, cierra la imagen
    if un_solo_trazo:
        plt.show()
        plt.close()


def graficar_poligono(puntos_usuario, num_trans, name_trans, reordenar, un_solo_trazo):
    """
    Funciión que gestina el gráfico del poligono
    :param puntos_usuario: (list) Lista de los puntos introducidos por el usuario
    :param num_trans: (int) Número de transformacion del gráfico
    :param name_trans: (str) Nombre de la transformación seleccionada
    :param reordenar: (int)     1 -> Reordenar los puntos para poder graficar
                                0 -> No reordenar los puntos
    :param un_solo_trazo: (int) 1 -> La gráfica es de un único trazo
                                0 -> La gráfica no es de un único trazo
    :return None: El proceso de gestión se realiza de manera interna
    """
    data_frame = crear_dataframe(puntos_usuario)
    if reordenar:
        data_frame = reordena_puntos(data_frame)
    titulo = f"T{num_trans} - {name_trans}"
    crear_guardar_grafico(data_frame, titulo, un_solo_trazo)
    return data_frame.to_numpy().tolist()