import pdb

print('Hola Curso!')

def elevar3(num):
    result = num ** 3
    return result

def elevarArr(arr):
    arr[1] = arr[1] ** 3
    return arr[1]
pdb.set_trace
def saludar (func , nombre = 'Anonimo'):
    saludo = f'hola {nombre} mucho gusto'
    func(saludo)

def write(text):
    arch = open('saludo.txt', 'w')
    arch.write(text)
    arch.close()




