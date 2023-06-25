# Hacer un programa para calcular la raiz cuadrada de un número. Las raices cuadradas tienen que ser positiva. 

import math # debemos importar la clase math que utilizamos para sacar la raiz cuadrada. 


print("promagrama calculo Raiz cuadrada. ")
numeroUsiuario= int(input("Introduce un número: "))
contadorIntentos=0
NUMERO_VALIDO_USUARIO=0

while numeroUsiuario<NUMERO_VALIDO_USUARIO:
    
    print("No se puede hallar la raíz cuadrada de un número negativo en los números reales. ")
    if contadorIntentos==2:
        print("Has superado el número de Intetos. El programa ha finalizado")
        break; # Lo que hace la instrucción break lo que hace es salir del bucle. Si el flujo del programa llega a leer break saldra del gucle y continuará con la flujo del programa fuera del bucle. 

    numeroUsiuario= int(input("Introduce un número: "))
    if numeroUsiuario<NUMERO_VALIDO_USUARIO:
       contadorIntentos=contadorIntentos+1

if contadorIntentos<2:
    solucion=math.sqrt(numeroUsiuario)
    print("la Razis cuadrad de ", numeroUsiuario, " es ", solucion)

                        






