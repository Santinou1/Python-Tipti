"""
### 1. `append()`   
**Ejercicio:** Tienes una lista de nombres de empleados y necesitas añadir nuevos empleados a la lista. Añade los nombres "Ana" y "Pedro" a la lista.


print(empleados)  # Salida esperada: ["Juan", "María", "Luis", "Ana", "Pedro"]
"""

empleados= ["Juan", "María", "Luis"]

def agregarNombres(lista,nombres):
    lista.append(nombres)
    return lista

agregarNombres(empleados,"Ana")
agregarNombres(empleados,"Pedro")
print(empleados)