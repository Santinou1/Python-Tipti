"""
### 2. `extend()`
**Ejercicio:** Tienes dos listas de proyectos realizados por diferentes equipos. Necesitas combinar estas listas en una sola lista de todos los proyectos realizados.

print(proyectos_equipo1)  # Salida esperada: ["Proyecto A", "Proyecto B", "Proyecto C", "Proyecto D"]

"""


proyecto1=["Proyecto A","Proyecto B"]
proyecto2=["Proyecto C","Proyecto D"]


def concatenarArrays(list1,list2):
    list1.extend(list2)
    return list1


proyectosTotales= concatenarArrays(proyecto1,proyecto2)
print(proyectosTotales)
