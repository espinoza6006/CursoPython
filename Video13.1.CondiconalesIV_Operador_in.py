#Imaginar un alumno que tiene que cursar una carrera por ejemplo Informatica y tiene que escoger una asignatura opcional y se le va a dar entre todas esas asignaturas opcionales un listado en la cual 
# podrá escoger la asignatura de su preferencia. si el alumno selecciona una de las que esta en el listado el programa funciona adecuadamente. pero si el alumno
# escribe una asignatura que no esta en el listado el programa no funionara. mostrara un error


   
print("Asignaturas opcionales Ingenieria Informatica:")

listaAsignaturas=["informatica grafica", "prubea de software", "usabilidad y accesibilidad"]

print("Las Asignaturas Optativas son: ", listaAsignaturas[:])

asigaturaUsuario=input("Escriba la asignatura optativa que desee cursar: ").lower() # Función lower() convierto cadenas de texto en miniscula
print("Has seleccionado", asigaturaUsuario)

# En python tenmos la funcions upper() --> Para convertir todo un string en MAYUSCULAS
# lower() --> converitr String en minisculas. 

def comprobarAsignatura(_asignaturaUsuario, _listaAsignatura):
    if _asignaturaUsuario in _listaAsignatura:
        print("Se incluirá la asignatura, ", _asignaturaUsuario, " a tu Semestre")
    else: 
        print("La Asignatura ", _asignaturaUsuario, " no esta en la lista de opciones")

comprobarAsignatura(asigaturaUsuario,listaAsignaturas)


