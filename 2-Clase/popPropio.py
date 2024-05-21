# Metodo pop()
# Lo que hace el metodo pop es eliminar el ultimo elemento de la lista si no se le pasa ningun argumento, en caso de que se le pasa un argumento , ese argumento va a ser el indice a eliminar.
# DATO IMPORTANTE
# EL METODO POP PUEDE DEVOVLER EL ELEMENTO ELIMINADO Y LO PODEMOS ALMACENAR EN UNA VARIABLE SI ASI SE QUISIERA


def popPropio(lista,indice=-1):
    elemento = lista[indice]
    del lista[indice]
    return elemento

# Ejemplo
lista=[1,2,3,4]
elementoBorrado= popPropio(lista)
print(elementoBorrado)
print(lista)

# Ejepmlo 2

lista2=[1,2,3,4]
elementoBorrado= popPropio(lista2,2)
print(elementoBorrado)
print(lista2)
