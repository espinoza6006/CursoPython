# Ejercicio 3: Crea un programa que pida tres números por teclado. El programa imprime en consola la media aritmética de los números introducidos.

# Declaración de variables donde se alacenarás los tres numeros. 

numero1=float(input("Introduzca Número 1: ")) # hago casting a float para darle la opcion al usuraio de introducir números con decimales
numero2=float(input("Introduzca Número 2: "))
numero3=float(input("Introduzca Número 3: "))
sumatoriaNumeros=0
mediaNumeros=0
totalnumeros=3

def sumar(Numero1, Numero2, Numero3):
    sumatoria= Numero1+Numero2+Numero3
    return sumatoria

def mediaAritmetica(sumatoria,cantidadNumeros):
    media=sumatoria/cantidadNumeros
    return media


sumatoriaNumeros=sumar(numero1,numero2,numero3)
mediaNumeros=mediaAritmetica(sumatoriaNumeros,totalnumeros)

print("La media es", mediaNumeros)


