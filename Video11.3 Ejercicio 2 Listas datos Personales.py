#Ejercicio 2. Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. 
#Esos tres datos deberán ser almacenados en una lista y mostrar en consola el mensaje: 
#Los datos personales son: nombre apellido teléfono” (Se mostrarán los datos introducidos por teclado).

# Declaración de variables. 

nombreUsuario= input(" Introduzca su Nombre: ")
direccionUsuario= input(" Introduzca su Dirección: ")
telefonoUsuario= input(" Introduzca su Telefono: ")

datosPersonales=[nombreUsuario,direccionUsuario,telefonoUsuario]
print("***********************************************************************************************************")
print("Los datos Personales son: ")
print("***********************************************************************************************************")
print("Nombre: ", datosPersonales[0], "// Direccion: ", datosPersonales[1], "// TLF: ", datosPersonales[2]) # Utilizo comas para hacer concatenaciojn
print("Nombre: "+ datosPersonales[0]+ "// Direccion: "+ datosPersonales[1]+ "// TLF: "+ datosPersonales[2]) # tambien puedo utiizar el signo + para concatenar como en java
print("***********************************************************************************************************")
print("Datos Personales: ")
print("***********************************************************************************************************")
print(datosPersonales)