from itertools import combinations
def combinatoria(vect, cant_vect):
    for i in combinations(vect, cant_vect):
        #print(i)
        j = list(i)
        print(j)

cantidad = 2
vectores = [[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15]]
combinatoria(vectores, cantidad)