# Operadores Logicos "and" y "or" // función "in" // Concatenación de operadores de comparación.  

edad=120

if 0<edad<100: # Concatenación de operadores logicos. Lo que hace es establecer rangos de de valores. Se lee como en inecuaciones matemáticas edades <100 y edades mayores a cero.. 
    #El flujo se lee de izquierda a derecha primero lee 0<edad si la condicion pasa a evaluar la siguiente condición edad<100 si la condicion es cierta se ejecuta el codigo que hay dentro del if. 
    # si la condicion es falsa continua el flujo del programa hacia abajo. 
    print("Edad Correcta. ")
else:
    print("edad Incorrecta. ")
print()
print("PROGRAMA SALARIO TRABAJADORES")
# Crear un programa que evalue el salario de ciertas personas que trabajan en la misma empresa. 
# Se valuará el salrio del Presidente de la empresa, Salario del director, salario de un jefe de area, salario de un administrativo.
# Estos salario no son iguales porque los cargos son diferentes se asume que el el salario mayor corresponde al Presidente, seguido por Director, luego jefe de area y por último el administrativo. 
# salarioAdministrativo<salarioJefeArea<salarioDirector<salarioPresidente
# Despues de introducir estos salarios por teclado, lo que debe hacer ell el programa es evaluar si se esta cumpliendo con esta regla.

# Creación de variables: 
salarioAdministrativo=float(input("Introduzca salario Administrativo: "))
# Concatenación en el print(). Si queremos concatenar cadenas de caracteres dentro de la función print() no es posible hacerlo directamente con el simbolo + cpoomo en los demás
#lenguajes de programación para hacer esto debemos convertir todo la expresiones en string. Para hacer esto podemos utilizar la función str(parametrosAconvertir) para convertir los valores en string. 

print("Salario del administrativo: "+ str(salarioAdministrativo)) # foma 1: concatenar conviertiendo todo a string
print("Salario del administrativo: ", salarioAdministrativo) # comcatenar diferentes tipos de datos. utilizando coma (,)
salarioJefeArea=float(input("Introduzca salario Jefe de Area: "))
print("El salario del jefe de area es: " + str(salarioJefeArea))
salarioDirector=float(input("Introduzca salario del Director: "))
print("Salario del Director es: ", salarioDirector) # comcatenar diferentes tipos de datos. utilizando coma (,)
salarioPresidente=float(input("Introduzca salario del Presidente: "))    
print("El salario del Presidente es: " + str(salarioPresidente))

def evaluarSaliario(salarioAdministrativo,salasalarioJefeArea,salarioDirector,salarioPresidente):
    if salarioAdministrativo<salarioJefeArea<salarioDirector<salarioPresidente:
        print("Todos los salarios estan correctos dependindo a la posicion que se desempeña dentro de la empresa. ")
    else:
        print("Los salarios no cumplen con las condicones de la empresa")

evaluarSaliario(salarioAdministrativo,salarioJefeArea,salarioDirector,salarioPresidente)