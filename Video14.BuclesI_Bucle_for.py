'''
Bucle Determinado for --> Cuando conocemos la cantidad de veces que se ejecutara el codigo dentro del bucle. 

Sintaxis: 

for variable in elemento a recorrer: 
	Cuerpo del bucle
	Cuerpo del bucle
	Cuerpo del bucle

Donde: 
For hace mención a que estamos utilizando un bucle for. 
Variable por convención se suele utilizar como nombre de variable i
Elemento a recorrer = --> Puede ser una lista, una tupla, cadena de texto, rango, etc. 

'''

for i in [4,2,3]:  # en este caso la canitdad de veces que se va a repetir el bucle son 3 veces porque?? --> porque la lista tiene 3 elementos. 
    print("Hola Bucles for, cuando el valor de i= ", i)

print("Mostar los valores de de la lista: ")
for i in [4,2,3]:
    print(i)

print("Mostar los valores de de la lista: ")   
for i in ["Primavera","Verano","Otoño", "Invierno"]:  #Inicialmente el valor de i="Primavera" y luego entra en el bucle e imprime el valor de i, en la sigueinte vuelata ahora i="Verano"  y en el interior del bucle se imprimira el valor de verano y asi susesivamente
    print(i)

print("Mostar mensaje en el interior del bucle: ")
for i in ["Primavera","Verano","Otoño", "Invierno"]:
    print("Hola Mundo. Este es un bucle for") # En este caso se imprimira por pantalla 4 veces el mensaje que print() que esta en el cuerpo del bucle. 