# Practica donde se abordará estructuras de control de flujo. Condicionales. 
# Crrear un programa que se pida la nota de un alumno y en funcion a esa nota el programa imprimira por pantalla si el alumno ha aprobado o reprobrado. 

notaMinima=5
notaMaxima=10
notaCero=0

#Función input() --> permitirará introducir valores por teclado-. Es muy parecida a la clase Scanner en Java. Sintaxis: nombreVariable=input() --> Pero en python cualquier cosa que introduzcamos por teclado usando la función input() es cosiderado como texto- 

print("Programaa Para saber si un alumno aprobo o reprobo.")
#print("Introduzca Nota: ")
notaAlumno=input("Introduce la Nota: ") # La función input() todo lo considera como texto. si queremos convertir ese valor a numerot tenemos que utilizar las funciones int(), float()..// La función input permite parametros.. Pero el curso lo coloca al lado.  
#notaAlumno=float(input("introduce nota: ")) --> Puedo hacer un casting directamente en esta parte de la declaración. 
def evaluacion(nota):

    if nota>=notaMinima and nota<=notaMaxima:
        print("Tu nota es: ", nota, " has Aprobado.")
    if nota<notaMinima and nota>=notaCero:
        print("Tu nota es: ", nota, " has reprobrado. ")
    if nota<notaCero or nota>notaMaxima:
        print("Nota Incorrecta: La nota debe estar entre los valores:", notaCero, " & ", notaMaxima)


#evaluacion(4.5) #podemos evaluar el parametro de la función directamente con números. 

evaluacion(float(notaAlumno)) # Como la función input nos devuelve texto para convertir ese texto en un valor numérico utilizamos la función int()


