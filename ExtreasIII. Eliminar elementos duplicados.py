# Ejercicio 3: Eliminar duplicados Escribe un programa que tome una lista de números y elimine los elementos duplicados, dejando solo una ocurrencia de cada número. Luego, imprime la lista resultante.

miLista=[1,2,3,4,5,6,6,7,7,3,3,8,10,10,5,"ernesto"]
listaSinRepetidos=[]
contadorRepetidos=0
print("Mi Lista:\n",miLista)

for i in miLista:
    if i not in listaSinRepetidos:
        listaSinRepetidos.append(i)
        
print("Lista sin valores repetidos: ", listaSinRepetidos, end=" // ")



