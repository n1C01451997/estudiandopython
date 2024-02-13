# definir las listas
nombre= []
notas= []
mb=0
mb1=[]
bu=0
ins=0
for x in range(1,):
    nom = input("ingrese el nombre del alumno ")
    nombre.append(nom)
    no = int(input(f"ingrese las notas del alumno :{x}"))
    notas.append(no)

for y in range(len(nombre)):
    print(nombre[y])
    print(notas[y])
    if notas[y]>=8:
        print("alumno muy bueno ")
        mb+=1
        mb1.append(nombre[y])
    elif notas[y]>=4  or notas[y]<=7:
        print("alumno bueno ")
        bu+=1
    else:
        print("alumno no aprobado ")
        ins+=1
for z in range(len(notas)):
    if notas[z]>=4 and notas [z]<=7:
        notas.pop(z)
        nombre.pop(z)

notas_filtradas = [nota for nota in notas if nota < 4 or nota > 7]
nombre_filtrado = [nombre[i] for i, nota in enumerate(notas) if nota < 4 or nota > 7]

print("La cantidad de alumnos muy buenos son:", mb)
print("Los nombres de los mejores alumnos por nota son:", mb1)
print("La lista de alumnos con notas entre 4 y 7 son:", nombre_filtrado)