#definir si un año es bisiesto 
año = int (input("ingrese el año que desea comprobas si es o no bisiesto "))

def bisiesto (año):
    if año %4 == 0 and año %100 != 0 or  año %400 == 0:
        print ("el ", año," es año bisiesto ")
    else:
        print ("el ", año," no es bisiesto")
bisiesto(año)
