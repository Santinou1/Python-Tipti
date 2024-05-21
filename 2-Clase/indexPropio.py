# Metodo Index()
# El metodo index va a obtener el indice de la primera aparicion del valor en la lista.

def indexPropio(lista,elemento):
    for i in range(len(lista)):
        if lista[i]== elemento:
            return i
    raise ValueError("El elemento no esta en la lista")
        
lista=[1,2,3,4,5]
data= indexPropio(lista,1)
print(data)