#Crea un programa que pida por teclado introducir una contraseña. La contraseña no
#podrá tener menos de 8 caracteres ni espacios en blanco. Si la contraseña es correcta,
#el programa imprime Contraseña OK . En caso contrario imprime Contraseña
#errónea

print("****************** Programa Acceso Usiuario ***************** ")

userPassword=input("Introduce tu contraseña: ")
longitudContrasenna=len(userPassword)
longitudMaximaContrasenna=8
isPasswordValid=True

for i in range(len(userPassword)):
    if userPassword[i]==" " or longitudContrasenna<longitudMaximaContrasenna:
        isPasswordValid=False

if isPasswordValid==True:
    print("Contraseña Validad!!!")
else:
    print(" Contraseña Incorrecta!! Su contraseña no debe tener Espacios en blanco y al menos debe tener 8 caracteres!!!")

