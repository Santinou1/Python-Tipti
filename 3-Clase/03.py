"""
**Ejercicio:** Tienes una lista de tareas pendientes y necesitas agregar una tarea urgente al principio de la lista.

print(tareas)  # Salida esperada: ["Tarea Urgente", "Tarea 1", "Tarea 2", "Tarea 3"]
"""

tareas= ["Tarea 1","Tarea 2","Tarea 3"]

def priorizacionDeTarea(lista,posicion,tarea):
     lista.insert(posicion,tarea)
     return lista

print(priorizacionDeTarea(tareas,0,"Tarea Urgente"))