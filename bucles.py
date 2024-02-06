import random

secreto = random.randint(1,10)

numero =int(input("adivine el numero entre 1 y 10 "))

while numero != secreto:
    if numero < secreto :
        print ("el numero es mayor ")
    else:
        print("el numero es menor ")
    numero = int(input("intenta de nuevo "))
print("felicidades adivinaste ") 
