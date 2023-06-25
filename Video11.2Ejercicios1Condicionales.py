''' Crea un programa que pida dos números por teclado. El programa tendrá una función llamada “DevuelveMax” encargada de devolver el número más alto de los dos introducidos.'''

numero1=float(input("Introduzca El Número 1: "))
numero2=float(input("Introduzca El Número 2: "))



#print("Identificar el número más alto")


def devulveMax(numero1,numero2):
    if numero1>numero2:
        print("En numero ", numero1, "Es el numero Mayor")
    elif numero2>numero1:
       print("el número  ", numero2, " es el número mayor. ")          
    else:
        print("Los números son iguales.")

devulveMax(numero1, numero2)