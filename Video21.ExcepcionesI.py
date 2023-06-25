'''
Definición:  Es un error en tiempo de ejecución. 
	• Las excepciones son errores que ocurren durante la ejecución del programa. La sintaxis del código es correcta pero durante la ejecución ha ocurrido algo inesperado. 
    Lo que hacen las excepciones es evitar que el programa se detenga donde ocurre ese error inesperado.

    Captura o control de excepcion: consiste basicamente en decirle a uestro codigo que intente realizar una instrrucción determnada (en el caso de divisiones /0) y en el caso de que no puedes el resto del programa se ejecute. 
'''

def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2
# Esta instrucción es la que esta arrojando una un error. Ya que si el usuraio introduce un cero en el denominador no es posible hacer esta división. #Por lo tanto, la instrucción que es propensa a cometer el error se debe meter detro de un bloque que se llama try-except
 
def divide(num1,num2): 
   try:
    return num1/num2
   except ZeroDivisionError:
    print("Error no se pouede Dividir entre Cero")
    return "Error"
   
    


	    


try:
    op1=(int(input("Introduce el primer número: ")))
except ValueError:
	print("Debes Introducir un valor numérico")
	
try:
    op2=(int(input("Introduce el segundo número: ")))
except ValueError:
	print("Debes Introducir un valor numérico")
	
operacion=input("Introduce la operaciún a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejeciciín del programa ")