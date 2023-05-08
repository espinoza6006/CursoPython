#En este proyecto vamos a vestudiar las tuplas, su sitaxis y sus funciones principales. 

#Declaración de una tupla. 
miTupla=("Williams", 13,8,1985, "Venezuela")

print("la tupla miTupla es:")
print(miTupla) # Se imprimira por el output la lista y esta será entre Parentesis. 

# Acceder a los emelentos de una Tupla. Es parecido a como se acceden en las lista se utilizan los corchetes nombreTupla[IndiceElemento]
print("El elemento en la posicion 2 de la tupla es: ")
print(miTupla[2])

# Existen dos mmétodos que nos permiten convertir Listas en Tuplas y Tuplas en Listas. 

# Para convertir una tupla en Lista Utilizamos el método List. Para hacer eso debemos declarar una Lista por ejemplo: miLista=List(nombreTupla)
print("Convertir una tupla en una Lista.")
miLista=list(miTupla) #  Delcaro una Lista y luego utilizo el metodo List()
print(miLista) # Se imprimirá por output la lista y sabremos que es una lista poeque los elemtnso estan entre corchetes []

# Converitr una Lista en Tupla. Se utiliza el metodo Tuple. --> Declaro la tupla. nombreTupla=tuple(nombreLista)

listaNumero2=["España","Barcelona", 2023]
print("ListaNumero2")
print(listaNumero2)
tuplaNumero2=tuple(listaNumero2) # convierto la listaNumero2 en tupla. 
print("La tuplaNumero2:")
print(tuplaNumero2)

# Comprobar si hay elentos dentro de una tupla. Utilizamos el metodo in devolvera True o false. 

print("Williams" in miTupla)

isWilliams= "Williams" in miTupla

if isWilliams== True:
    print("Williams esta en la Tupla")
else:
    print("Williams no esta en la Tupla")


# Meétodo count () --> Devolcerá la cantidad de elementos que se repiten dentro de una tupla. 

miTupla.count("Williams")
print("Williams se repite ")
print(miTupla.count("Williams"),"veces")

# Método len me permite averiguar la longitud de la tupla. leng(nombreTupla)

print("Longitud de la tupla miTupla es:",len(miTupla))

# Tupla unitaria --> Tupla con un único elemento sintaxis: nombre tupla=(elemento1,)

tuplaUnitaria=("España",)
print("tuplaUnitaria:",tuplaUnitaria)

print("Longitud tuplaunitaria es: ",len(tuplaUnitaria))

# Declaración de tuplas sin parentesis: Se conoce como empaquetado de tupla. 

tuplaEmpaquetada="williams", "Maracay", "Venezuela", 13, 8, 1985
print("Tupla empaquetada: ")
print(tuplaEmpaquetada)

# Desempaquetado de tupla: Permite asignar todos los elementos de la tupla a variables distintas. 

#Declaro variables: 
nombre, diaNacimiento, mesNacimiento, annoNacimiento, paisNacimiento=miTupla # el objetivo es asiganar a cada una de estas variable los valores que estan presentes en la tuplaa miTupla. 

print("nombre:", nombre,"//Dia nacimiento: ", diaNacimiento, "//Mes nacimiento:", mesNacimiento, "//Año Nacimiento:", annoNacimiento, "//Pais nacimiento: ",paisNacimiento)



