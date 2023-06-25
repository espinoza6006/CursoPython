# Crea un programa que pida números infinitamente. Los números introducidos deben ser cada vez mayores El programa finalizará cuando se introduce un número menor que el anterior.

numerosAlmacenados=[]
contadorNumeros=0
while True:
    numeroUsuario= float(input("Introduce un Número: "))
    numerosAlmacenados.append(numeroUsuario)
    
    if numerosAlmacenados[contadorNumeros]<numerosAlmacenados[contadorNumeros-1]:
        break;
    contadorNumeros=contadorNumeros+1

print("\nEl Número ", numerosAlmacenados[contadorNumeros], " es menor al número ", numerosAlmacenados[contadorNumeros-1], ".Programa Finalizado.")
    




