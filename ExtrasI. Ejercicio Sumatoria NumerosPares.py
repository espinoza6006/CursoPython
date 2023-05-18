# Escribe un programa que calcule la suma de todos los números pares del 1 al 100 e imprima el resultado.




def sumarNumerosPares():
    sumarotiaNumerosPares=0
    for i in range(1,101):
        if i%2==0:
            sumarotiaNumerosPares=sumarotiaNumerosPares+i
    return sumarotiaNumerosPares

sumatoriaPares=sumarNumerosPares()

print(" La sumatoria de los numeros pares del 1 al 100 es: ", sumatoriaPares)
        



