#Hacer un programa que controle el acceso a los menores de edad. es decir, el programa pedirá la edad del ususario y dependiendo si el usuario es mayor o menor de edad este dira acceso aprobado o acceso denegado para el caso de los meores de edad. 
edadMayor=18
edadCero=0
edadViejo=120
print("Control de acceso: ")

edadUsuario=int(input("Introduzca su edad: "))
print()
print("*******************************************************************")
print("Solución utilizando solo bloque if -else: ")
print("*******************************************************************")
print()
''' Puedo Hacer comentarios en varias lienas '''
#Utilizando sentenciaif -else. Para este caso tenemos limitacoines si queremos evaluar mas edad como por ejemplo si el usuario introduce numeros negativos o numeros mayores a 120 años.. 
def controlAcceso(edadUsuario):
    if edadUsuario>=edadMayor:
       print("Eres mayor de edad. Acceso aprobado")
    else:
        print("Eres menor de edad: Acceso denegado") # Este else esta asociado al if mas cercano en este caso seria el anterior. Si queremos evaluar varias condiciones en n bloque condicional se utiliza elif condicion: 


controlAcceso(edadUsuario)
print()
print("*******************************************************************")
print("Solución evaluando varias condiciones a la vez. elif: ")
print("*******************************************************************")
print()
def comprobarEdad(edadUsuario):
    if edadUsuario>=edadViejo:
        print("Edad Invalidad. Nadie puede vivir más de ", edadUsuario, " años")
    elif edadUsuario>=edadMayor:
        print("Eres Mayor de edad. Acceso Accedido. ")
    elif edadUsuario<edadMayor and edadUsuario>edadCero:
        print("Eres Menor de edad. No pueden entrar.")
    else:
        print("Edad invalidad: ", edadUsuario, " No representa una edad real.")

comprobarEdad(edadUsuario)