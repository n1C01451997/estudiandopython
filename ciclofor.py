
cont = 0
cont1= 0
gasto = 0
n = int(input("ingrese # de empleados "))
for ini in range (n):
    sueldo = float(input("ingrese el valor del {ini} empleado "))
    gasto = gasto+sueldo
    if sueldo >=1300000 and sueldo <= 3000000:
        cont +=1
    elif sueldo > 3000000:
        cont1 +=1
print ("el gasto total de la empresa es ", gasto)
print ("los empleados que ganan entre 1300000 y 3000000 son ", cont)
print ("los empleados que ganan mas de 3000000 son ", cont1)