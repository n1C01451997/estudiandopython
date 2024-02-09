frase= input("ingrese una frase ")
letra= input("ingrese la letra que quiere buscar ")
Cletra = 0
for i in frase:
    if i == letra :
        Cletra+=1
print("la letra '%s' aparece %2i  en la frase '%s'. "%(letra,Cletra,frase))