# Empezamos con las Listas en Python. Tienen la particularidad de ser Arrays o arreglos en otros lenguajes de programación. 
#Sintaxis
# nombreListas=[elemento1, elemento2, elemento3,..., elementoN]

#Declaración de una lista. 
# una lista de tipo String que almacenara nombres, recuerda que para datos de tipo Strinh los valores deben estar entre comillas. 
# La lista miLista conta de 4 elementos en la cual el elemento en la posicion [0] = Williams // [1]= lennin // [2]= Javier // [3]= Justina
miLista=["Williams", "Lennin", "Javier", "Justina"]  

print(miLista[:]) #Esta es la sintaxis para imprimir todos los elemetos de una lista nombreLista[:]


#Para acceder a n elemento en concreto. habra que escribir el nombre de la lisa con el indice: miLista[0]

print(miLista[0])
print(miLista[1])
print(miLista[2])
print(miLista[3])
#print(miLista[5]) --> ocurre una exeption porque el elemento en la posicion 5 no existe. 

#Pero que pasa si colocamos elementos con indices negativos. Python muestra los valores desde la posicion final hacia la posicion inicial y empieza a contar desde -1
print(miLista[-1])
print(miLista[-2])
print(miLista[-3])
print(miLista[-4])

# Cuando tenemos lista muy largas. Es recomendable acceder a ellos a través de porciones de lista. 
# porcion de lista: se accede a un trozo de todo los elementos de la lista. 

print(miLista[0:3]) # lo que hacemos aqui es accedera los tres primero elementos de la lista. [0:3] el [0] representa el indice desde donde se quiere acceder a la lista y el [3] hasta donde llegara el recorrido este es exclusive.  
print(miLista[:3]) # si no se coloca nada en el principi de los dos punto : python por defecto selecciona 0
print(miLista[1:4]) # 1 incusive 4 exclusive. output: lennin, javier, justina
print(miLista[2:3])

print(miLista[1:]) # en este caso estariamos accediendo desde el elemento 1 hasta el final. 

#AGREGAR ELEMENTOS A UNA LISTA --> se utiliza la función append (añadir) --> nombreLista. --> se muestran todas las funciones que contiene la clase Lista. 
#funcion append --> añadira un elemento al final de la lista. 
miLista.append("Ray")
print(miLista[:])

#Agregar un elemento en una posición intermedia __> Se utiliza la Función Insert(parametro1,Parametro2) --> donde parametro1= a la posicion donde se quiere insertar el elenmento y parametro2= el valor del elemento

miLista.insert(0,"Pedro") #En este caso esto agregando el Pedro en la posicion 0. y todos los elemento se corren hacia la derecha. 
print(miLista[:])
miLista.insert(5,5)
miLista.count("Pedro") #Función count devolvera un valor de tipo entero el cual representa la cantidad de valores que se repiten en una lista
print(miLista[:])
print(miLista.count("Pedro"))

#Agregar varios elementos en una lista --> Se utiliza la función extend([elemento1, elemento2...]) se añaderan o se concatenaran a las anterio

miLista.extend(["Rocio","Ricardo",True])
print(miLista[:])

# devolver el indice de un elemento en concreto en una lista. --> Se utiliza la función Index("elemento")
indicePedro= miLista.index("Pedro") # haciendo pruebas puedo verificar que puedo asignar variable a los metodos. En caso de haber elementos repetidos devolvera el indice del primer elemento que se repite
print(indicePedro)
print(miLista.index("Rocio"))

# Verificar si un elemento se encuentra en la lista --> Se utiliza la función in --> devolvera true si se encuentra el elemento y false si no se encuentra. 
isRocio= "Rocio" in miLista

if isRocio==True:
    print("Rocio esta en la lista")
else:
    print("Rocio no esta en la lista")

#Eliminar elementos --> Se utiliza Funcion Remove(elemento)

miLista.remove("Rocio") # Con esto estoy removiendo o eliminando a Rocio de la lista
print(miLista[:])


# Eliminar el último elemento de una lista --> Se utiliza la función pop

miLista.pop()
print(miLista[:])


# Concatenar o unir dos lista. Se utiliza el operador + 

miLista1=["Williams", 37,1985,"Masculino"]
miLista2=["Devops Ingineer", "Allianz",2022]
miLista3=miLista1+miLista2
print(miLista3)

# Operador Multiplicador * --> cuando se utilizan en lista se concatenara la lista cuandtas veces se requiera. 

miLista4=miLista3*2
print(miLista4)