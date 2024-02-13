#Codifica un programa en python que nos permita guardar los nombres de los 
#alumnos de una clase y las notas que han obtenido. 
#Cada alumno puede tener distinta cantidad de notas. 
#Guarda la información en un diccionario cuya claves serán los nombres 
#de los alumnos y los valores serán listas con las notas de cada alumno.

#El programa pedirá el número de alumnos que vamos a introducir, 
#pedirá su nombre e irá pidiendo sus notas hasta que introduzcamos 
#un número negativo.
def profesor():
    #definimos el dicionario con el nombre clase
    maestro={}
    answer="si"
    

    
    while answer=="si":
        alumnos=int(input("ingrese cuantos alumnos quiere agregar "))
        #puede tener variuas respuestas
        lista=[]
        for x in  range(alumnos):
            nombre=input(f"ingrese el(los) nombre del {x+1} estudiente ")
            apellido=input(f"ingrese el(los) apellido del {x+1} estudiente ")
            documento=int(input("ingrese el documento del estudiante"))
            lista.append((nombre,apellido,documento))
            notas=[]
            while answer =="si":
                cant=int(input("ingrese cuantas notas quiere agregar para este alumno "))
                for i in range(cant):
                    nota=input(f"ingrese la nota {i+1} del estudiente ")
                    notas.append((nota))
                answer=input("¿quiere ingresar otra nota  o nota extra para este estudiante? si/no ")
        maestro[alumnos]=lista
        answer=input("¿quiere ingresar otro alumno? si/no ")
    return maestro
def show(maestro):
    print("listado de los alumnos ")
    for alumnos in maestro:
        print("para los alumnos ")
        for nombre,apellido,documento in maestro[alumnos]:
            print(nombre,apellido,documento)
def consulxalumno(documento):
    documento=input("ingrese el nombre y apellido del alumno que quiere consultar ")
    if documento in lista:
        
