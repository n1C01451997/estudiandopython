cont = 0 
numero1 = 0
acum = 0
acum1 = 0
acum2 = 0 
empleados = float(input("cuantos empledos quiere verificar "))
while cont < empleados :
    sueldo = float(input("ingrese su sueldo "))
    numero1=numero1+sueldo
    cont +=1
    print("el empleado numero ", cont, "recibe un sueldo de ", sueldo)
    if sueldo >= 1300000 and sueldo <= 3000000:
        acum +=1
    elif sueldo >= 3000000:
        acum1 +=1
    else:
        acum2 +=1
print("la cantidad de empleados que cobran entre $ 1.300.000 y $ 3.000.000 es ", acum)
print("la cantidad de empleados que cobran $ 3.000.000 o mas es ", acum1)
print("el importe que gasta la empresa e personal es ", numero1)
print("los empleados que ganan menos de $ 1.300.000 es ", acum2)
 