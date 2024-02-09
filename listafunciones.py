def ingresar():
    enteros = []
    for x in range (5):
        numero = int(input("ingresar el numero "))
        enteros.append(numero)
    imprimir(enteros)
    sumar(enteros)
def imprimir (enteros):
    print("los datos de la lsita son ")
    for x in enteros:
        print(x)
def sumar (enteros):
    acum=0 
    for x  in enteros:
        acum=acum+x
    print("la suma de los numeros es ",acum)
ingresar()
