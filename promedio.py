
def mayor_promedio(arr):
    sum = 0
    for num in array:
        sum = sum + num

    prom = sum / len(arr)
    
    mayores = []
    for num in array:
        if num > prom:
            mayores.append(num)
    return mayores

mayor_promedio = [12,18,8,6]
print (sum)
"""
n = int(input("ingrese la cantidad de nota a promediar:"))
suma=0
i = 1

while (i <= n):
    print("ingrese la nota numero:" , i)
    nota = float(input())
    suma=suma+nota
    i+=1
prom = suma / n 
print("prommedio de la notas es:" , prom)
"""

