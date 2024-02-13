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
        clase=input(f"ingrese el nombre de la {x+1} clase : ")
        #puede tener variuas respuestas
        lista=[]
        while answer =="si":
            nombre=input(f"ingrese el(los) nombre del {x+1} estudiente ")
            apellido=input(f"ingrese el(los) apellido del {x+1} estudiente ")







        





nombre=[]
nomcond=int(input("ingrese cuantos alumnos quiere ingrear "))
for x in range(nomcond):
    nom = input(f"ingrese el nombre del alumno {x+1}: ")
    nombre.append(nom)
    totalnotas=0