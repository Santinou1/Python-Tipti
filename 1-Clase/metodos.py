# METODOS PYTHON

# LA SINTAXIS PARA UTILIZAR UN METODO ES EL NOMBRE DE LA LISTA + EL METODO.
# Por ejemplo lista.append(1)

# Metodo append()

# El metodo append lo que hace es añadir un elemento al final de la lista.
# Es similar al metodo PUSH en JS

lista = [1, 2, 3]
print(f"Esta es la Lista antes de utilizar el metodo Append = {lista}")
lista.append(4)
print(f"Esta es la lista despues de utilizar el metodo Append = {lista}")


# Metodo extend()
# El metodo extend lo que hace es añadir MULTIPLES elementos al final de una lista.
# ES IMPORTANTE AÑADIR QUE EL PARAMETRO DE EXTEND ES OTRA LISTA

lista = [4, 5, 6]
print(f"Esta es la Lista antes de utilizar el metodo extend = {lista}")
lista.extend([7, 8, 9])
print(f"Esta es la lista despues de utilizar el metodo extend = {lista}")


# Metodo insert()
# El metodo insert lo que hace es insertar un elemento en una posicion ESPECIFICA de la lista.
# Explicacion Extendida
# Este metodo toma 2 argumentos. El primer argumento es el indice que hace referencia a que lugar va a ocupar el elemento a introducir.
# Y el segundo argumento es el elemento.
# Un punto importante a destacar es que una vez insertado el emeneto desplaza el resto a la derecha.
# Como vamos a ver en este ejemplo

lista = [1, 2, 4, 5, 6, 7, 8]
print(f"Esta es la Lista antes de utilizar el metodo insert = {lista}")
lista.insert(2, 3)
print(f"Esta es la lista despues de utilizar el metodo insert = {lista}")


# Metodo remove()
# El metodo remove lo que hace es eliminar la PRIMERA aparicion del elemento de la lista.

lista = [1, 2, 4, 2, 3, 4]
print(f"Esta es la Lista antes de utilizar el metodo remove = {lista}")
lista.remove(4)
print(f"Esta es la lista despues de utilizar el metodo remove = {lista}")


# Metodo pop()
# Lo que hace el metodo pop es eliminar el ultimo elemento de la lista si no se le pasa ningun argumento, en caso de que se le pasa un argumento , ese argumento va a ser el indice a eliminar.
# DATO IMPORTANTE
# EL METODO POP PUEDE DEVOVLER EL ELEMENTO ELIMINADO Y LO PODEMOS ALMACENAR EN UNA VARIABLE SI ASI SE QUISIERA

# Ejemplo sin pasarle argumento 

lista= [1,2,3,4,5]
print(f"Esta es la Lista antes de utilizar el metodo pop = {lista}")
elementoEliminado= lista.pop()
print(f"Esta es la lista despues de utilizar el metodo pop sin ningun parametro = {lista}")
print(f"El elemento eliminado de la lista fue {elementoEliminado}")

# Ejemplo pasandole argumento

lista= [1,2,3,4,5]
print(f"Esta es la Lista antes de utilizar el metodo pop = {lista}")
elementoEliminado= lista.pop(2)
print(f"Esta es la lista despues de utilizar el metodo pop con el parametro 2 que hace referencia a eliminar el elemento que esta en el indice 2 = {lista}")
print(f"El elemento eliminado de la lista fue {elementoEliminado}")

# Metodo index()
# El metodo index va a obtener el indice de la primera aparicion del valor en la lista.

lista=[1,2,4,2,1,2]
print(f"Esta es la lista al cual analizar en que posicion esta el elemento 2 {lista}")
indice= lista.index(2) # output
print(f"El elemento 2 esta en el indice {indice} ")

# Metodo sort()
# El metodo sort lo que hace es ordenar los elementos de una lista en forma ascendente ( O DESCENDENTE en caso que se especifique)

lista=[3,6,1,9,4,5,3,2]
print(f"Esta es la lista antes de utiliar el metodo sort {lista}")
lista.sort()
print(f"Esta es la lista despues de utiliar el metodo sort por defecto {lista}")
lista.sort(reverse=True)
print(f"Esta es la lista despues de utiliar el metodo sort especificandole que sea de mayor a menor {lista}")


# Metodo reverse()
# El metodo reverse lo que hace es invertir el orden de la lista.

lista=[1,2,3,4,5,6]
print(f"Esta es la lista antes de utiliar el metodo reverse {lista}")
lista.reverse()
print(f"Esta es la lista despues de utiliar el metodo reverse {lista}")

# Metodo count()
# El metodo count lo que hace es contar cunatas veces aparece un valor especifico en la lista.

lista=[1,2,3,4,3,3,4,5]
print(f"Esta es la lista al cual analizar {lista}")
cantidad= lista.count(3)
print(f"Esta es la cantidad de veces que aparece el numero 3 = {cantidad}")

# Metodo clear()
# El metodo clear lo que hace es eliminar todos los elementos de una lista.

lista=[1,2,3,4,3,3,4,5]
print(f"Esta es la lista antes del metodo clear {lista}")
lista.clear()
print(f"Esta es la lista despues del metodo clear {lista}")

