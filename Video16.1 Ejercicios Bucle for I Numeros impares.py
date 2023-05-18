#Crea un programa que muestre los números impares del 1 al 100. Los números deberán
#aparecer una al lado del otro sin salto de línea.

# Los numeros impares son todos aquellos numeros que no son divisibles por 2
# numero%2!=0

print("Mostar los numeros Impares del 1 al 100: ")

for i in range(1,100):
    if i%2!=0:
        print(i, end=" // ")