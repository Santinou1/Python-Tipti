"""
**Ejercicio:** Tienes una lista de productos en el inventario y necesitas eliminar un producto que se ha vendido. Elimina el producto "Producto B" de la lista.


print(inventario)  # Salida esperada: ["Producto A", "Producto C", "Producto D"]
"""

inventario= ["Producto A", "Producto B","Producto C", "Producto D"]

def eliminarElemento(lista,elemento):
    lista.remove(elemento)
    return lista

print(eliminarElemento(inventario,"Producto B"))