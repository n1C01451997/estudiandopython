cont = 0 
numero1 = 0
alturas = float(input("cuantas alturas quiere verificar "))
print("ingrese cualquier altura para calcular su promedio")
while cont < alturas :
    numero = float(input("ingrese su altura "))
    numero1=numero1+numero
    cont +=1
promedio = numero1/alturas
print("la suma de las alturas es ", numero1)
print("el promedio de las alturas es ", promedio)

