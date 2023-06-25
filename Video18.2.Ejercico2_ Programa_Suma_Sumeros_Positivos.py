# Crea un programa que pida números positivos indefinidamente. El programa termina cuando se introduce un número negativo. Finalmente el programa muestras la suma de todos los números introducidos

contadorNumerosPositivos=0
sumatoriaNumerospositivos=0

while True:
    numeroUsuario=float(input(" Introduzca un Número: "))

    if numeroUsuario>0:
        sumatoriaNumerospositivos=sumatoriaNumerospositivos+numeroUsuario
    else: 
        break;



print("La sumarotia de los numeros positivos es: ", sumatoriaNumerospositivos)

'''
while numeroUsuario>0:
    numeroUsuario=float(input(" Introduzca un Número: "))

    sumatoriaNumerospositivos=sumatoriaNumerospositivos+numeroUsuario
   
print("La sumarotia de los numeros positiov ses: ", sumatoriaNumerospositivos)


'''