'''
Bucle for. 
    • Recorriendo Strings
	• Tipo range ---> se ha convertido en un tipo de dato en python. Nos permite es utilizar el bucle for en python con conteo numérico. 
	• Notaciones espaciales con print --> ver algunas notaciones especiales que permite la función print dentro de sus parámetros. 
'''
print("Imprimiendo el cuerpo del bucle con salto de línea")
for i in ["Williams","Python", 1]:
    print("Imprimir valores: ", i) # Se imprimira 3 veces el mensaje que que hay en el cuerpo del bucle pero lo hace con salto de línea

print()
print("Imprimiendo el cuerpo del bucle sin salto de línea")
for i in ["Williams","Python", 1]:
    print("Imprimir valores: ", i, end=" // ") # Argumento end="" lo que va a fdeterminar es como queremos que temine la impresion por consola. Es decir, elimina el salto de línea y lo coloca todo en la misma linea. podemos colocar calgún caracter especial. 

print()
print()
print("Recorrer un string: ")
for i in "Williams":
    print("Hola Williams") # Se imprimira por pantalla el mensaja "Hola Williams" 8 veces porque es la cantidad de caracteres que tiene Williams


# Crear un programa en python que verifique si un Correo electronico es correcto. tomando en cuenta el @ 

'''
print()
print("Programa para validad Correo Electronico")
print()
correoUsuario2= input("Escrible tu correo Electronico: ")
isCorreoCorrecto=False


for i in correoUsuario2:
    if (i=="@"):
        isCorreoCorrecto=True
    

if isCorreoCorrecto==True:  # Para simplificar mas el codigo podemos poner if isCorreoCorrecto: con esto python sobreneiende que ese valor es True
     print("Correo electroico es Correcto")
else:
     print("Correo electroico es Incorrecto")


'''



 # Evaluar tambien con @ y punto. 

print()
print("Programa para validad Correo Electronico")
print()
correoUsuario2= input("Escrible tu correo Electronico: ")
contadorArroba=0
contadorPunto=0
#contadorArroba=0


for i in correoUsuario2:
    if (i=="@"): #or (i=="."):
        contadorArroba=contadorArroba+1
        #contadorPunto=contadorPunto+1
        #contadorArroba=contadorArroba+1
    if i==".":
        contadorPunto=contadorPunto+1
    
if (contadorArroba==1  and contadorPunto>=1):
    print("El correo es correcto")
else:
    print("Correco Incorrecto")


print()
print("Bucle for con tipo de dato Range")
# El tipo de dato range() lo que hace internamente python es crear crear una especie de array o una lista de 5 elementos que comienzan desde el 0 hasta el 4 [0,1,2,3,4]

for i in range(5):
    print(i) # se imprimirá los valores de i [0,1,2,3,4]

