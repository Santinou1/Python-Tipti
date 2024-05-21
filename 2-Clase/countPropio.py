# Metodo count()
# El metodo count lo que hace es contar cunatas veces aparece un valor especifico en la lista.

def countPropio(lista,elemento):
    contador = 0
    for item in lista:
        if item == elemento:
            contador += 1
    return contador

# Ejemplos

lista=[1,2,3,2,4,5]
total= countPropio(lista,2)
print(total)