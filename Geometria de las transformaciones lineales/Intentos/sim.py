import itertools
from string import ascii_uppercase
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker



def labels_gen():
    size = 1
    while True:
        for s in itertools.product(ascii_uppercase, repeat=size):
            yield "".join(s)
        size +=1


datos_frame = [[-3,0], [3,3], [3,0], [-3,-3]]
data = pd.DataFrame(datos_frame, columns=["x","y"])

#plt.title("jambiosa")
print("Data")
print(data)
print(type(data))
print("---------------------------")

# Cálculo del centroide
print("Centroide")
centroide = np.mean(data, axis=0)
print(centroide)
print("---------------------------")

# Cáculo del ángulo polar
aux = data - centroide
polar_angles = np.arctan2(aux.y, aux.x)

# Obtenemos un nuevo DataFrame con los vértices ordenados
print("Polar angles")
print(polar_angles)
print("---------------------------")
print("Type polar angles")
print(type(polar_angles))
data = data.reindex(polar_angles.argsort())
print("---------------------------")
print("polar_angles.argsort()")
print(polar_angles.argsort())
print("---------------------------")
print("Data reordenao")
print(data)


ax = plt.subplot(111)

# Creamos el polígono
plygon = plt.Polygon(data, fill=True, facecolor="#b3faff", edgecolor='#000e6b', alpha=1, zorder=1)
ax.add_patch(plygon)

# Creamos los vértices
ax.scatter(data.x, data.y, c='b', zorder=2)

# Etiquetas para cada vértice y arista
etiquetas = labels_gen()
print("---------------")
print(etiquetas)
print("---------------")
for i, vertice in enumerate(data.values):
    lb = next(etiquetas)
    print(lb)
    print(vertice)
    print(type(lb))
    ax.annotate(text=lb+f"({vertice[0]},{vertice[1]})", xy=vertice + 0.1)
    #punto_medio = (vertice +  data.values[(i + 1) % (data.shape[0])]) / 2
    #ax.annotate(s=lb.lower(), xy=punto_medio)

# Mostramos los ejes centrados en el origen
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')


# Configuramos la rejilla
ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)

# Escalamos la gráfica
ax.autoscale_view()
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

# Mostramos la gráfica
plt.savefig(f"jambiosa.jpg")
#plt.show()
#plt.savefig(f"jambiosa.jpg")