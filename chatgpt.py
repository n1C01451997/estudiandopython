nombre = []
notas = []
mb = []
mb1 = 0
bu = 0
bu1 = []
ins = 0
ins1 = []

# Llenar lista
for x in range(4):
    nom = input(f"Ingrese el nombre del alumno {x}: ")
    nombre.append(nom)
    no = int(input(f"Ingrese las notas del alumno {x}: "))
    notas.append(no)

# Recorrer lista
for y in range(len(nombre)):
    print(nombre[y])
    print(notas[y])
    if notas[y] >= 8:
        print("Alumno muy bueno")
        mb.append(nombre[y])
        mb1 += 1
    elif notas[y] >= 4:
        print("Alumno bueno")
        bu += 1
        bu1.append(nombre[y])
    else:
        print("Alumno no aprobado")
        ins += 1
        ins1.append(nombre[y])

# Eliminar elementos basados en la condición
eliminar = []
for z in range(len(notas)):
    if notas[z] >= 4 and notas[z] <= 7:
        eliminar.append(z)

for index in sorted(eliminar, reverse=True):
    notas.pop(index)
    nombre.pop(index)

print("La cantidad de alumnos muy buenos son:", mb1)
print("Los nombres de los mejores alumnos son:", mb)
print("La cantidad de alumnos buenos son:", bu)
print("Los nombres de los alumnos buenos son:", bu1)
print("La cantidad de alumnos no aprobados son:", ins)
print("Los nombres de los alumnos no aprobados son:", ins1)
