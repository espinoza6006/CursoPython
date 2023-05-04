nombre =5 # Declaración de variable. En este caso no es necesario colocar el tipo de varibale en pyrhon el mismo compilador asigna que este tipo de variable es de tipo entera.  

print(type(nombre)) # Función type() --> nos devolvera el tipo de dato o el tipo de varible. en este caso devolvera <class 'int'> que hace referencia a que forma parte de la clase integer. 
nombre="Williams"
print(type(nombre)) # devolverá que el tipo de variable es de tipo str = String
nombre =5.2
print(type(nombre)) # devolverá que el tipo de variable es de tipo float. 

# Uso de las  Tripe comillas en los textos. va hacer util cuando queramos incluir saltos de lineas en los texto

mensaje="""Esto es un mensaje
con tres saltos
de linea"""
print(mensaje) # Se mostrará por consola un el contenido de la variable mensaje con sus saltos de linea

#Si quiero saber los metodos que puedo utilizar con la clase string. Puedo colocar el nombre de la variable mensaje.metodoAUtilizar. 

mensaje.isupper



# Condicionales If --> permite evaluadr dos o mas condiciones. 

print("********************************** Introducción Condicionales **************************")
#Sintaxis Condicionales ---> 
# if condicion1 Operadorlogico Condicion2:
#   Linea Codigo 1
#   Linea codigo 2
# else:
#   Linea codigo 3


numero1=5
numero2=7

if numero1 > numero2:
    print("El numero 1 es mayor")
else:
    print("el número 2 es mayor")


