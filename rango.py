# rango entre años ,,,, cuantos años hay bisiestos .... y cuantos años ahi ,,,,,, 
año1=int(input("ingrese el año desde al cual quiere realizar el calculo "))
año2=int(input("ingrese el ultimo año hasta el cual quiere realizar el calculo "))

def  bisiesto (año1,año2):
    cont = 0
    cont1 = 0
    
    for año in range(año1,año2+1):
        if año %4 == 0 and año %100 != 0 or  año %400 == 0:
            print ("el ", año," es año bisiesto ")
            cont +=1
        else:
            print ("el ", año," no es bisiesto")
            cont1 +=1
    print("Total de años bisiestos:", cont)
    print("Total de años no bisiestos:", cont1)
    suma=cont+cont1
    print("el total de años verificado son ", suma)

bisiesto (año1, año2)



    