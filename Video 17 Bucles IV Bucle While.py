# Bucle While
# Sintaxis: 
# While condicon:
#   cuerpo del bucle. 

i=0

# En este caso si no colocamoe el contador de i dentro del cuerpo el bucle la condicon del bucle nunca sería false. por lo que el bucle sería infinito
while i<10:
    i=i+1
    print(i)

# Crear un programa que pedirá por teclado la edad de un persona si la edad introducida en negativa el bucle volvera a preguntar la edad hata que el usuario introduzca una edad valida. 
print("********Programa de edad **************")

edadUsuario= int(input("Introduce tu edad: "))
limiteEdadvalida=0
limiteMaximoEdad=110
while edadUsuario<limiteEdadvalida or edadUsuario>limiteMaximoEdad:
    print("Edad Invalida: La edad tiene que ser positiva y edad debe ser menor a ", limiteMaximoEdad, " años")
    edadUsuario= int(input("Introduce tu edad: "))

print("Edad Correcta. Tu edad es: ", edadUsuario, " años")
#print(" Edad Correcta. Tu edad es: " + str(edadUsuario)) otra forma de concatenar con print

