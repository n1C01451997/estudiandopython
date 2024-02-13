persona={
    "nombre":"leidy johana",
    "apellido":"cifuentes martinez",
    "estatura":1.59,
    "edad":50,
    "email":"cifuentes0903@gmail.com",
    "ciudadnac":"ibage",
    "genero": ["femenino","masculino","otro"]
}
print(persona)
#mostrar elemento del dicionario 
print("el nombre de la persona es :",{persona["nombre"]})
#agregar elemento del dicionario 
persona["telefono"]=3158519335
print(persona)
#modificar elemento del dicionario 
#modificar la clave dentro del dicionario
persona["celular"]=persona.pop("telefono")
print(persona)
#eliminar elemento del diccionario
del persona["celular"]
print(persona)
#iterar los item de las claves y los valores
for clave,valor in persona.items():
    print(clave,": ",valor)