# Metodo clear()
# El metodo clear lo que hace es eliminar todos los elementos de una lista.

def clearPropio(lista):
    del lista[:]

# Ejemplo

lista=[1,2,3,4,5]
clearPropio(lista)
print(lista)