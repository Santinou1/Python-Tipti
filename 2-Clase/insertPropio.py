# Metodo insert()
# El metodo insert lo que hace es insertar un elemento en una posicion ESPECIFICA de la lista.
# Explicacion Extendida
# Este metodo toma 2 argumentos. El primer argumento es el indice que hace referencia a que lugar va a ocupar el elemento a introducir.
# Y el segundo argumento es el elemento.
# Un punto importante a destacar es que una vez insertado el emeneto desplaza el resto a la derecha.
# Como vamos a ver en este ejemplo

def insertPropio(lista,indice,elemento):
    lista[len(lista):]=[None] #Añadimos un espacio extra al final
    for i in range(len(lista)-1,indice,-1):
        lista[i]=lista[i-1]
    lista[indice]=elemento
    


# Ejemplo

lista=[1,2,4]
insertPropio(lista,2,3)
print(lista)