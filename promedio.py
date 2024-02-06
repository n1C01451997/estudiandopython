cont = 0 
numero1 = 0
print("ingrese cualquier numero hasta completar 10 numeros para calcular su promedio")
while cont < 10 :
    numero = int(input("ingrese numero"))
    numero1=numero1+numero
    cont +=1
promedio = numero1/10
print("la suma de los numero es ", numero1)
print("el promedio de los numeros es ", promedio)