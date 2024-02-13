#Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales que realza cada conductor.
#Al finalizar se muestra la lista con los nombres de conductor y kilometros realizados 

nombre=[]
dia=0
dias=['lunes ','martes ','miercoles ','jueves ','viernes ','sabado ','domingo ']
kms=[]
totalkms=[]
kmscond=[]

nomcond=int(input("ingrese cuantos conductores tiene "))
for x in range(nomcond):
    nom = input(f"ingrese el nombre del conductor {x+1}: ")
    nombre.append(nom)
    
    for dia in dias:
        km = int(input(f"ingrese los kilometros transcurridos : {dia}"))
        
    kmscond.append(km)
    kms.append(kmscond)
    totalkms.append(sum(kmscond))

for nombre,totalkms in zip(nombre,totalkms):
    print(f"{nombre}: {totalkms} kilometros")


        