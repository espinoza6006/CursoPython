'''
Definición: 
	• Son estructuras que extraen valores de una función y se almacenan en objetos iterables (que se pueden recorrer). Estos valores que se extraen de la función se van a almacenar en objetos iterables, eso quiere decir que esos objetos donde se almacenan los valores se pueden recorrer con un bucle. (form etc) e incluso con otras estructuras como iteradores o el método next. 
	• Esos valores además hay que tener en cuenta que se almacenan de uno en uno dentro del generador.
	• Cada vez que un generador almacena un valor, este pertenece en un estado de pausa hasta que se solicita el siguiente. Esta característica es conocida como "Suspensión de estado"
	
Funcionamiento: 


Función "tradicional"

Def generaNumero():
    Lineas de codigo

	Return numeros
	
generaNumeros()



Generador

Def generaNumeros():
	
    Lineas de codigo
    Yield numeros # instrucción. Lo que se consigue es que cuando en el código hay una llamada, el control de ejecución llama a la función y la instrucción yield construye un objeto con el primer valor de esa lista de números. 
	

generaNumero() # con un generado se construye un objeto generador iterable el cual va almacenando los valores de uno en uno. El generador entra en un estado de stand by o suspensión. Habrá que ir llamando la función generadora tantas veces como sea necesario. 


Ventajas: 

	• Son más eficientes que las funciones tradicionales. 
	• Muy útiles con lista con valores infinitos.
Bajo determinados escenarios, será muy útil que un generador devuelva valores de uno en uno. 
'''

# Ejemplo práctico generar un programa que genere números pares lo haremos utilizando un función tradicional y con generadores. 

'''
almacenarPares=[]

def numerosPares(limite):
    num=1
    almacenarPares=[]
    while num<limite:
        almacenarPares.append(num*2)
        num=num+1
    return almacenarPares

almacenarPares= numerosPares(10)

print("los Numeros pares son: ", almacenarPares)

# haciendolo con generadores. 

'''


print("Generadores")

#almacenarPares=[]

def numerosPares(limite):
    num=1
    
    while num<limite:
        num=num+1       
        pares=num*2
        yield pares
    

almacenarParesGenerador= numerosPares(10) # Declaro un objeto iterable que es donde se van almacenar los valores. Como me esta devolviendo un objeto tengo que recorrerlo con un bucle. 

'''
for i in almacenarParesGenerador:
    print(i)


'''

# Devolver valor a valor

elemento1=next(almacenarParesGenerador)
print("Aqui podria ir mas codigo")
elemento2=next(almacenarParesGenerador)
print("Aqui podria ir mas codigo")
elemento3=next(almacenarParesGenerador)
print(elemento1)
print("Aqui podria ir mas codigo")
print(elemento2)
print("Aqui podria ir mas codigo")
print(elemento3)






