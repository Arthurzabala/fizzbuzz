import pdb

x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
estudiantes[0]["last_name"] = 'Bryant'
directorio_deportes['fútbol'][0] = 'André' 
z[0]['y'] = 30

#pdb.set_trace()

#ejercicio 2

dojo = {
'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon'],
'estudiantes': ['Vicente', 'Eduardo', 'Maca', 'Nicolás','Flavio'],
'cursos': ['Python Feb 23', 'MERN Enero 23', 'Data Science Dic 22', 'Mern Marzo 23']
}

def informa(obj):
    cantidad = len(obj['ubicaciones'])
    print(f'UBICACIONES{cantidad}')
    for ubicacion in obj['ubicaciones']:
        print(ubicacion)

    cantidad = len(obj['instructores'])
    print(f'\n instructores{cantidad}')
    for instruccion in obj['instructores']:
        print(instruccion)    



informa(dojo)