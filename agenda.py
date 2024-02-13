def registrar():
    #definimos diccionario
    agenda={}
    respuesta="s"

    while respuesta=="s":
        fecha=input("ingrese la fecha con formato dd/mm/aa : ")
        #puede tener varias respuestas
        lista=[]
        while respuesta =="s":
            hora=input("ingresar la hora de la actividad : h/m : ")
            actividad=input("ingresar el nombre de la actividad ")
            lista.append((hora,actividad))
            respuesta=input("¿quiere ingresar otra actividad para la misma fecha? s/n ")
        agenda[fecha]=lista #se utiliza para asignar un valor a una clave específica en un diccionario llamado agenda.
        respuesta=input("desea ingresar otra fecha s/n : ")
    return agenda 
def mostrar(agenda):
    print("listado de la agenda ")
    for fecha in agenda:
        print("para la fecha ")
        for hora,actividad in agenda[fecha]:
            print(hora,actividad)
def consultaxfecha(fecha):
    fecha=input("ingrese la fecha de la que quiere consultar sus actividades en formato dd/mm/aa ")
    if fecha in agenda:
        for hora,activiad in agenda[fecha]:
            print(hora,activiad)
    else:
        print("no existen acitividades para la fecha ingresada ")
agenda=registrar()
mostrar(agenda)
consultaxfecha(agenda)

