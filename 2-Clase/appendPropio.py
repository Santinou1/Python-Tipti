# Metodo append()

# El metodo append lo que hace es añadir un elemento al final de la lista.
# Es similar al metodo PUSH en JS

def appendPropio(lista,elemento):
    lista[len(lista):]=[elemento]

# Ejemplo

lista=[1,2,3]
elemento=[4]
lista[len(lista):]=elemento
print(lista)

# Paso 1 : len(lista)
# Calculaos la longitud todal. En este caso es 3

# Paso 2 : lista[3:]
# Selecciamos una parte de la lista desde el indice 3 hasta el final. Dado que el indice 3 siempre va a estar despues del ultimo elemento.

# Paso 3 : lista[3:]=[4]
# Asignamos el valor 4 a esta lista. Esto lo que hace es agregar el 4 al final de la lista.
# Porque la longitud total siempre va a ser uno menos que la cantidad total de elementos