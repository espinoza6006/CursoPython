# Se explicarán los conceptos básicos de los diccionarios. Sintaxis metodos, etc. 
#Sintaxis: nombreDiccionario={clave:valor}
miDiccionario={"Alemania":"Berlin", "Venezuela":"Caracas", "España":"Madrid", "Reino Unido":"Londres"}

# Aceder a un diccionario entero: 
print("Mi Diccionario: ")
print(miDiccionario)

# Acceder a los valores dentro de un diccionario. Lo que debemos hacer es preguntarle por la clave y accediendo a la clave podermos saber el valor. 

print("La capital de Alemania es: ",miDiccionario["Alemania"])
print("La capital de Venezuela es: ",miDiccionario["Venezuela"])

# Agregar más elementos a un diccionario ya construido --> debenmos escribir el nombre del dicccionario ya creado miDiccionario[clave]=valor --> Recordar que si estamos hablando de texto deben ir en comillas dobles. 

miDiccionario["Italia"]="Lisboa"
print("Mi Diccionario: ")
print(miDiccionario)

# Modicar el valor nuevo a una clave. 

miDiccionario["Italia"]="Roma"
print("Mi Diccionario: ")
print(miDiccionario)


# Como elimanos elementos utilizamos el metodo del --> del nombreDiccionario["Clave a eliminar"]

del miDiccionario["Alemania"]
print("Mi Diccionario: ")
print(miDiccionario)

# Diccionario en el cual hay mezclas de tipo string, int

diccionario2={"Williams":"Devops Engineer","TIE":123456789,185:"Estatura"}

print("Nuevo diccionario",diccionario2)

# Utilizar una Tupla como valores de clave y luego crear un diccionario con las clave de la tupla y asignarle un valor

miTupla=("España", "Francia", "Reino Unido", "Alemania")
diccionario3={miTupla[0]:"Madrid", miTupla[1]:"Paris", miTupla[2]:"Londres",miTupla[3]:"Berlin"}
print(diccionario3)         

print(diccionario3["Francia"])         
print(diccionario3["Reino Unido"])

# Guardar un valor en una lista

dicionario4={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":[1991,1992,1993,1996,1997,1998]}
print("Diccionario Jordan: ",dicionario4)
print(dicionario4["Anillos"])

# Guardar un diccinario desntro de otro diccionario

dicionario5={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":{"Temporadas":[1991,1992,1993,1996,1997,1998]}}
print(dicionario5)
print(dicionario5["Anillos"])


# Si quiero saber cuales son los valores de las claves de un diccionario puedo utilizar el metodo keys() --> Sintaxis: nombreDiccionario.kesys()

print(dicionario5.keys())
print(miDiccionario.keys())
print(diccionario3.keys())

# Si quiero sabes cuales son los valores de las claves. utilizo el método values() --> Sintaxis: nombreDiccionario.values()

print(miDiccionario.values())
print(dicionario5.values())

# Longitud del diccionario --> utilizo el método len() --> Sintaxis len(nombreDiccionario)

print("longitud del diccionario5: ",len(dicionario5))
