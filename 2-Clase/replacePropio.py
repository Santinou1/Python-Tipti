def replacePropio(lista,viejo,nuevo):
    for i in range(len(lista)):
        if lista[i] == viejo:
            lista[i] = nuevo
    return lista

# Ejemplo

lista=[1,2,3,4,5]
newLista= replacePropio(lista,2,5)
print(newLista)