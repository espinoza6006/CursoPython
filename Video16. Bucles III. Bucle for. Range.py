# Bucle for. utilizando tio range() como manejar este tipo a la hora de escribir tipo for. 
# Notaciones especiales con la función print() utilizamos desntro de bucles. 

for i in range(5):
    print("valor ", i)
    
for i in range(5):
    print(f"El valor de la variable {i}") # Anteiormente se utilizaba esta expresión para concatenar texto con valores numericos. al poner una f le indicamos a python que vamos a utilizar una notación especial

# las funciones de tipo f permiten jugar con formatos de tipo diferente, al poner el valor de la variable dentro de las llaves {i} lo que va hacer es concatenar el texto con el valor de la variable por cada vuelta del bucle. 
print()
print("Sintaxis tipo Range")
for i in range(5,10): # range(valor1,valor2) --> lo que le decimos a python es que empiece desde el valor numero 5 hasta el 9
    print("valor ", i)

print()
print("Sintaxis tipo Range 2:")
for i in range(5,30,3): # range(valor1,valor2,parametro3) --> lo que le decimos a python es que empiece desde el valor numero 5 hasta el 29, el parametro 3 me permite hacer q se vayan contando los numero de por ejemplo 3 en 3
    print("valor ", i)

# Funcion len("string") --> Devolcerá un numero entero con la cantidad de caracteres que hay en una cadena

#Ejercico Email: 

isEmailCorrecto=False

emailUsuario=input("Introduce tu Emails: ")

for i in range(len(emailUsuario)):
    if emailUsuario[i]=="@":
        isEmailCorrecto=True

if isEmailCorrecto==True:
    print("El emails es correcto")
else:
    print("Em emails es incorrecto")
