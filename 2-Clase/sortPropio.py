# Metodo sort()
# El metodo sort lo que hace es ordenar los elementos de una lista en forma ascendente ( O DESCENDENTE en caso que se especifique)

def sortPropio(lista):
    # El bucle del for i in range (len(lista)) lo que realiza es iterar desde el 0 hasta el length total de la lista.
    for i in range(len(lista)):
        # Este bucle itera sobre los indiices de la lista, esto lo hacemos para poder comparar el indice actual con el indice que le sigue.
        for j in range(len(lista)-1):
            # En el if comparamos si el elemento actual lista[j] con el siguiente elemento lista[+1]. Si el elemento actual es mayor que el siguiente, se va a ejecutar el bloque de codigo que esta dentro del if.
            if lista[j] > lista[j+1]:
                # Si se cumple la condicion dle if es dcir que el elemento sea mayor al siguiente, se van a intercambiar los elementos. lista[j] y lista[j+1].
                # Esto se le llama ordenamiento en burbuja, se utiliza para mover el elemento mas grande al final de la lista.
                lista[j],lista[j+1]= lista[j+1],lista[j]



#Ejemplo 

lista=[3,1,4,2]
sortPropio(lista)
print(lista)