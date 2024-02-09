texto = "definiendo un parametro en una funcion "
#funcion sin parametros
def mensaje ():
    n1=int(input("ingrese el 1er numero "))
    n2=int(input("ingrese el 2do numero "))
    calcularmayor(n1,n2)
    positivo(n1,n2)
#funcion con parametros
def calcularmayor(num,num1):
    if num>num1:
        print("el 1er numero es mayor ")
    elif num<num1:
        print("el 2do numero es mayor ")
    else:
        print("ambos numeros son iguales ")
def positivo(p,p1):
    if p>0 and p1<0:
        print("numero positivo ")
    else:
        print("numero negativo ")
def positivo(p,p1):
    if p>0 and p1>0:
        print("numero positivo ")
    elif p<0 and p1<0:
        print("ambos numeros son negativos ")
    else:
        print("almenos uno de los numeros es negativo ")



mensaje()