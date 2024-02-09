ancho = int(input("ingrese el ancho del rectangulo "))
altura = int(input("ingrese la altura del rectaangulo "))
caracter =input("ingrese el caracter que quiere utilizar para dinbujar el rectangulo ") 

def dibujar (ancho,altura,letra):
    for i in  range (ancho):
        for j in  range (altura):
            print(letra,end=" ")
        print()
dibujar(ancho,altura,caracter)