# definir las listas
nombre= []
notas= []
mb=[]
mb1=0
bu=0
bu1=[]
ins=0
ins1=[]

#llenar lista

for x in range(4):
    nom = input(f"ingrese el nombre del alumno {x}")
    nombre.append(nom)
    no = int(input(f"ingrese las notas del alumno : {x}"))
    notas.append(no)

#recorrer lista
    
for y in range(len(nombre)):
    print(nombre[y])
    print(notas[y])
    if notas[y]>=8:
        print("alumno muy bueno ")
        mb.append(nombre[y])
        mb1+=1
    else:
        if notas[y]>=4:
            print("alumno bueno ")
            bu+=1
            bu1.append(nombre[y])
        else:
            print("alumno no aprobado ")
            ins+=1
            ins1.append(nombre[y])

print("la lista inicial de  alumnos es : ", nombre)

eliminar = []
for z in len(notas):
    if notas[z]>=4 and notas [z]<=7:
        eliminar.append(z)
        
for d in sorted (eliminar,reverse=True):
    notas.pop[d]
    nombre.pop[d]

print("cantidad de alumnos muy buenos son ", mb1)
print(f"los alumnos muy buenos son {mb}" )
print("listado de alumnos ", nombre)

