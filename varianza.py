import pdb
def var(arr):
    suma = 0
    for num in arr:
        suma += num
    prom =suma / len(arr)
    # colocando una pausa en el código
    #pdb.set_trace
    sigma = 0
    for num in arr:
        sigma += abs(num - prom)
    return sigma / prom

varianza = var([5,7,2,4,9,10])
print (varianza)