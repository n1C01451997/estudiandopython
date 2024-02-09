def inicio():
    
    print("menu principal")
    print("seleccione la opcion correcta")
    print("1. operacion sumar")
    print("2. operacion resta")
    print("3. operacion multiplicar")
    print("4. operacion dividir")
    print("5. salir")

def main():
    while True:
        inicio()
        opcion = int(input("selecione la opcion"))
        if opcion == 1:
            print("ha seleccionado la ")
            num1 = int(input("ingresar el 1 numero "))
            num2 = int(input("ingresar el 2 numero "))
            sumar = num1+num2
            print("el resultado de la suma es: ", sumar)
        elif opcion == 2:
            print("ha selecionado operacion resat ")
            num1 = int(input("ingresar el 1 numero "))
            num2 = int(input("ingresar el 2 numero "))
            resta = num1-num2
            print("el resultado de la resta es: ", resta)
        elif opcion  ==3:
            print("ha selecionado multiplicar")
        elif opcion == 4:
            print ("ha selecionado dividir")
        elif opcion == 5:
            print("hasta luego")
            break
        else:
            print("opcion no valida")
main()