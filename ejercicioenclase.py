cont=0
cont1 = 0
cont2 = 0
suma=0
suma1=0
suma2=0

for mañana in range (6):
    edad = int(input("ingrese la edad del  estudiante turno mañana"))
    suma = suma+edad
    promedio = suma/6
    
    

for tarde in range (7):
    edad1 = int(input("ingrese la edad del  estudiante turno tarde "))
    suma1 = suma1+edad1
    promedio1 = suma1/7
    
    

for noche in range (12):
    edad2 = int(input("ingrese la edad del  estudiante turno noche "))
    suma2 = suma2+edad2
    promedio2 = suma2/12
    

print("el promedio d e las edades de los estudiantes de la mañana es ", promedio)
print("el promedio d e las edades de los estudiantes de la tarde es ", promedio1)
print("el promedio d e las edades de los estudiantes de la noche es ", promedio2)
if promedio > promedio1 and promedio>promedio2 :
    print ("el mayor promedio de los tres es ", promedio, " de la mañana ")
elif promedio < promedio1 and promedio1>promedio2:
    print ("el mayor promedio de los tres es ", promedio1, " de la tarde ")
else:
    print ("el mayor promedio de los tres es ", promedio2 ," de la noche ")
