# Continuamos con las funciones en este capitulo veremos mas en profundidad el tema de funciones con y sin parámetros. 
# En Python se pasan los valores por referencia en las funciones. 

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

#Declaración de funciones que devulven un valor return --> Nomalmente se utiliza para almecenar el valor de la función en una variable
print()
print("este el valor de la suma de dos valores utilizando funciones con parametros y que retorne un valor")
def sumarParametrosReturn(numero1,numero2):
    resultado = numero1+numero2  #Declaro una variable dentro de la función que tendra como misión almacenar el valor de la suma de los dos numeros. 
    return resultado

almacenaResultado= sumarParametrosReturn(1,5) # Creo una variable nueva y alamceno el valor de 
print(almacenaResultado)
#comentario final
