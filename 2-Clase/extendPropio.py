# Metodo extend()
# El metodo extend lo que hace es añadir MULTIPLES elementos al final de una lista.
# ES IMPORTANTE AÑADIR QUE EL PARAMETRO DE EXTEND ES OTRA LISTA

def extendPropio(lista,elementos):
    for elemento in elementos:
        lista[len(lista):] = [elemento]

# Ejemplo

lista=[1,2,3,4,5]
extendPropio(lista,[4,5,6])
print(lista)