# Números primos Escribe un programa que verifique si un número dado es primo. El usuario debe ingresar un número y el programa debe imprimir "Es primo" si el número es primo, o "No es primo" si no lo es.


numeroUsuario=int(input("Escribe un Número Entero: "))

def obtenerNumeroPrimo(_numeroUsuario):
        if _numeroUsuario<2:
                print("No es Primo")
        elif _numeroUsuario>=2 and _numeroUsuario%2==0:
                print(" No Es Primo")
        else: 
                print("Es primo")                 
                    
              
obtenerNumeroPrimo(numeroUsuario)