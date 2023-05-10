# Crear un programa que solicite al usuario introducir las notas por pantalla y dependiendo de la nota el programa  mostrara un mensaje por consola en que dira si la nota es: Insuficiente (<5), Suficiente (5-6), Bien (), Notable (>7)
notaLimiteInferior=0
notaMinima=5
notaBien=6
notaNotable=7
notaMaxima=9

print("***************************************************************************************")
print("Programa para calcular Rendimiento de un alumno en cuanto a su calificación")
print("***************************************************************************************")

notaUsuario=float(input("Introduzca su Nota: "))

def rendimientoAlumno(notaUsuario):
    if notaUsuario<0 or notaUsuario>10:
        print("Nota Incorrecta. La nota debe estar en el siguiente rango de valores: ", "(", notaLimiteInferior, " - ", notaMaxima,")")
    elif notaUsuario<notaMinima:
        print("tu nota es Insuficiente")
    elif notaUsuario<notaBien:
        print("tu nota es Suficiente")
    elif notaUsuario<notaNotable:
        print("Tu nota Bien")
    elif notaUsuario<notaMaxima:
        print("Tu nota es Notable")
    else: 
        print("tu nota es Sobresaliente")




#Llamada del método

rendimientoAlumno(notaUsuario)

print("***************************************************************************************")
print("Solucion Pildoras Informaticas")
print("***************************************************************************************")

if notaUsuario<5:
    print("Nota Insuficiente")
elif notaUsuario<6:
    print("Nota Suficiente")
elif notaUsuario<7:
    print("Nota es Bien")
elif notaUsuario<9:
    print("Nota Notable")
else:
    print("Nota Sobresaliente")
