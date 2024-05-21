"""

VERSION 1

def removePropio(lista,elemento):
    # Crear una nueva lista el cual vamos a almacenar todos los elementos menos el que vamos a borrar
    nuevoArr=[]

    # Recorremos la lista original
    for item in lista:
        # Añadimos SOLAMENTE a la nueva lista los elementos que NO SON IGUALES al elemento pasado por parametro , que seria el elemento a eliminar
        if item != elemento:
            nuevoArr.append(item)
        else:
            # Una vez encontramso el primer elemento, salimos del bucle.
            break

    # Añadimos todos los elementos restantes a la lista original despeus de eliminar el primer elemento igual al elemento brindado por parametro
    nuevoArr.extend(lista[len(nuevoArr)+1:])

    # Reemplazamos la lista brindada por el usuario por la lista modificada.
    lista.clear()
    lista.extend(nuevoArr)


lista=[1,2,3,4,5,6]
removePropio(lista,8)
print(lista)
    

"""

# Version 2

def removePropio(lista,elemento):
    for i in range(len(lista)):
        if lista[i]== elemento:
            del lista[i]
            break

lista = ["hola","como","estas"]
removePropio(lista,"como")
print(lista)