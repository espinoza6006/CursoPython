#En esta prácitca vamos a estudiar los operadores lógicos "and" & "or" y el operador "in"
#Operador lógico "and" se puede traducir como "y si ademas" --> si hacemos está traducción nos ayudará a entender la lógica del código. 
#Operador lógico "or", se puede traducir por "o si no".

#Crear un Programa que evalue si un alumno que va entrar en un colegio tiene derecho a beca o no tiene derecho a beca. Lo que va evaluar este programa son tres puntos: 
# va a evaluar la distancia a la que vive el alumno del colegio de tal forma si vive a una distancia superior a 40km. Inplica que puede aplicar una beca porque tiene que gastar dinero en transporte. 
# Evaluar si este alumno tiene más hermanos. Numeros de hermanos. se le da´ra beca a todos aquellos alumnos que tengas mas de dos hermanos. 
# evaluar el salario familiar. salarioFamiliar<=20000 euros
# Se le dará beca a todos aquellos alumnos que cumplas con estos 3 requisitos. 

#Requisitos para otorgar becas: Importante: Se deben de cumplir los tres requisitos: 
#1. La distancia de casa al centro >40 km
#2. Familia numeros. Numero de hermanos >2.
#3. Salario Familiar<=20000


#Declaración de variables

print("************************************************")
print("Programa para obtner una Beca de Estudio: ")
print("************************************************")
print("Debes completar el siguiente formulario: ")
print()

distanciaAlCentro=float(input(" A que distancia vives del centro (km): "))
numeroHermanos=int(input("Cuantos hermanos son: "))
salarioFamiliar=float(input("Cual es el salario familiar por año (Euros): "))

def otorgarBeca(_distanciaAlCentro,_numeroHermanos,_salarioFamiliar):
    if _distanciaAlCentro<0:
        print("*****************************************************************")
        print("Error en la distancia La distancia debe ser un valor Positivo.")
        print("*****************************************************************")

    elif _numeroHermanos<0:
        print("*****************************************************************")
        print("Error. La cantidad de hermanos debe ser un valor positivo. ")
        print("*****************************************************************")
    elif _salarioFamiliar<0:
        print("*****************************************************************")
        print("Error. El Salario familiar debe ser un valor Positivo. ")
        print("*****************************************************************")
    elif _distanciaAlCentro>40 and _numeroHermanos>2 and _salarioFamiliar<=20000:
        print("*****************************************************************")
        print("Felicidades Tu beca ha sido otorgada. ")
        print("*****************************************************************")
    else: 
        print("*****************************************************************")
        print("Beca NO Otorgada: No  cumples con todos los requisitos. ")
        print("*****************************************************************")

otorgarBeca(distanciaAlCentro, numeroHermanos, salarioFamiliar)









