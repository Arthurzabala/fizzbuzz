dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon'],
    'estudiantes': ['Vicente', 'Eduardo', 'Maca', 'Nicolás','Flavio'],
    'cursos': ['Python Feb 23', 'MERN Enero 23', 'Data Science Dic 22', 'Mern Marzo 23']
    }
def printInfo (obj):
    
    for key in obj.keys():
        name = key.upper()
        # el arreglo asociado a cada llave
        array = obj[key]
        largo_array = len(array)
        print(f'\n{largo_array} {name}')

        for item in array:
            print(f'- {item}')

printInfo(dojo)