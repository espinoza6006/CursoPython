# Continuamos con las funciones en este capitulo veremos mas en profundidad el tema de funciones con y sin parámetros. 

def sumar():
    numero1=2.5
    numero2=3
    print(numero1+numero2)
  
sumar()

# Declaración de Funciones con parametros
def sumarParametros(numero1,numero2):
    print(numero1+numero2)

#LLamadas de la funciones con los parámetros. 
sumarParametros(1,5)
sumarParametros(100,200)
sumarParametros(5.5,2)

#Declaración de funciones que devulven un valor return
print()
print("este el valor de la suma de dos valores utilizando funciones con parametros y que retorne un valor")
def sumarParametrosReturn(numero1,numero2):
    resultado = numero1+numero2
    return resultado

resultado= sumarParametrosReturn(1,5)
print(resultado)