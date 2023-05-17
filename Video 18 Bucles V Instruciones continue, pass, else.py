'''
	• Instrucción Continue: esta instrucción lo que hace es salta a la siguiente interacción de bucle. 
	• Instrucción pass: Devolver null  en cuanto se lee en el interior del bucle, es decir, es como si no ejecutará el bucle. Esta instrucción se utiliza en contadas ocasiones en caso muy críticos. Se utiliza cuando estemos viendo POO, cuando por ejemplo se quiere definir una clase que sea nula. O también se suele utilizar como cuando desarrollador vas a dejar para después el desarrollo de un bucle y de momento pones un "pass" para que el programa se siga ejecutándose pesar de que ese bucle no tiene nada en su interior
    • Instrucción else: funciona de forma similar a como lo hace con un condicional, pues el sentido del "else" dentro de un bucle for o while tiene el mismo que dentro de un  condicional "if"

'''

for letra in "Python":
    if letra=="h": # que va  hacer el codigo, a cada vuelta de bucle va a evaluar esta condicion. cuando se encuentra con la letra "h" ignora el print donde esta la h.. y en consecuencia no imprimira la h en el print
        continue
    print("viendo la letra:", letra)


# Ejemplo utilidad. Imaginemos que queremos saber la longitud de una cadena de caracteres y desreamos conocer la cantidad de caracteres que tiene ese "string" pero sin contar los espacios en blanco.

cadenaString="Pildoras informaticas"
#contadorEspacio=0
contadorCadena=0
for i in cadenaString:
    if i==" ":
        continue
        #contadorEspacio=contadorEspacio+1
        
    contadorCadena+=1 # operador incremento es equivalente a : contadorCadena=contadorCadena+1
  

print(contadorCadena)


# intruccion pass.  Se utiliza en casos muy conretos, la verdad no es muy utilizada. porque  lo que hace es devolver un valor null, es como sie l bcle no se ejecutase. 
'''
while True: # Bucle infinito.. Para salir de un bucle infinito se utiliza la combiancion de teclas ctrl+c
    pass
'''


'''
class miClase:
    pass #para implementar más tarde. 
'''


# Intrucción else: 

email=input("Introduca su email por favor: ")

for i in email:
    if email=="@":
        arroba=True
        break
else:

    arroba=False

print(arroba)
        

