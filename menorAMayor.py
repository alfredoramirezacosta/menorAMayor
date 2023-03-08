#Pedir los numeros al usuario
numeros = input("Introduce los numeros separados por comas: ")

#Convertir la entrada en una lista de numeros
numeros = [int(n) for n in numeros.split(',')]

#Ordenar la lista utilizando el metodo de ordenamiento de burbuja
for i in range(len(numeros)):
    for j in range(len(numeros) - 1):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

#imprimir la lista ordenada
print("Lista ordenada de menor a mayor:", numeros)
