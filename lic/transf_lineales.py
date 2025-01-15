'''
                    LIBRERÍA DE GEOMETRÍA DE LAS TRANSFORMACIONES LINEALES
@author: Rodrigo Gerardo Trejo Arriaga
'''
#  -------------------------------------------------------------------------------------------------
# MÓDULOS Y LIBRERÍAS IMPORTADAS
import math

#  -------------------------------------------------------------------------------------------------
# FUNCIONES


# Función que convierte un punto a su forma matricial-columna
punto_matrix = lambda punto: [[i] for i in punto]


# Función que convierte un punto en su formato columna a su forma [x,y]
matriz_puntos = lambda matriz: [i[0] for i in matriz]


def multiplicar_matrix(m1, m2_aux):
    """
    Multiplica dos matrices compatibles entre sí
    :param m1: (list) Matriz m1 que se multiplicará por m2
    :param m2: (list) Matriz m2 que será multiplicada por m1
    :return m_pultiplicada: (list) Multiplicación de m1 x m2
    """
    m_pultiplicada = []
    m2 = punto_matrix(m2_aux)

    for i in range(len(m1)):
        m_pultiplicada.append([])
        for j in range(len(m2[0])):
            m_pultiplicada[i].append(0)
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m1[0])):
                m_pultiplicada[i][j] += m1[i][k] * m2[k][j]
    return m_pultiplicada


def reflejar(puntos, eje_x):
    """
    Realiza la transformación-reflexion a los puntos de una figura
    :param puntos: (list) Matriz que contiene a los puntos de una figura
    :param eje_x: (bool) True -> Reflexion en el eje "x"
                        False -> Reflexion en el eje "y"
    :return p_reflexion: (list) Lista de puntos en reflexión
    """
    if eje_x:
        matrix = [[-1,0], [0,1]]
    else:
        matrix = [[1,0], [0,-1]]
    nuevos = [multiplicar_matrix(matrix, p) for p in puntos]
    p_reflexion = [matriz_puntos(i) for i in nuevos]
    return p_reflexion


def expandir(puntos, cte_exp, eje_x):
    """
    Realiza la transformación-expansion a los puntos de una figura
    :param puntos: (list) Matriz que contiene a los puntos de una figura
    :param cte_exp: (float) Constante de expansión que se aplicará a una figura
    :param eje_x: (bool) True -> Expansión en el eje "x"
                        False -> Expansión en el eje "y"
    :return p_reflexion: (list) Lista de puntos en expansión
    """
    if eje_x:
        matrix = [[cte_exp, 0], [0, 1]]
    else:
        matrix = [[1,0], [0, cte_exp]]
    nuevos = [multiplicar_matrix(matrix, p) for p in puntos]
    p_expancion = [matriz_puntos(i) for i in nuevos]
    return p_expancion


def cortar(puntos, cte_corte, eje_x):
    """
    Realiza la transformación-corte a los puntos de una figura
    :param puntos: (list) Matriz que contiene a los puntos de una figura
    :param cte_exp: (float) Constante de corte que se aplicará a una figura
    :param eje_x: (bool) True -> Corte en el eje "x"
                        False -> Corte en el eje "y"
    :return p_corte: (list) Lista de puntos con el corte
    """
    if eje_x:
        matrix = [[1,cte_corte], [0,1]]
    else:
        matrix = [[1,0], [cte_corte, 1]]
    nuevos = [multiplicar_matrix(matrix, p) for p in puntos]
    p_corte = [matriz_puntos(i) for i in nuevos]
    return p_corte


def rotar(puntos, angulo):
    """
    Realiza la transformación-rotación a los puntos de una figura
    :param puntos: (list) Matriz que contiene a los puntos de una figura
    :param angulo: (float) Ángulo en que se rotará una figura
    :return p_corte: (list) Lista de puntos con la rotación
    """
    rad = (angulo*math.pi)/180
    matrix = [[math.cos(rad), math.sin(rad)], [-math.sin(rad), math.cos(rad)]]
    nuevos = [multiplicar_matrix(matrix, p) for p in puntos]
    p_corte = [matriz_puntos(i) for i in nuevos]
    return p_corte