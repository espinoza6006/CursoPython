# Crear una función generadora que nos devuelva uuna serie de ciudades 

def devulveciudades(*ciudades): # En python cuando utilizamos * le estamos indicando que va recibir un numiro interminado de elementos. y ademas esos elementos los va a recibir en forma de tupla por defecto. 
    for elemento in ciudades:    # Primer bucle for para el primer elemento que se almacena en el objeto generador
        #for subelemento in elemento: # segundo bucle for para conocer los subelementos de ese primer elemento (que este caso son caracteres o letras)
         #   yield subelemento
        yield from elemento # La idea del yield from es simplificar y evitar el uso de bucles anidados. 


ciudades_devueltas = devulveciudades("Madrid", "Barcelona", "Caracas", "Paris")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))




