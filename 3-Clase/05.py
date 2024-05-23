""" 5. `pop()`
**Ejercicio:** Tienes una lista de clientes esperando en la fila para ser atendidos. Atiende (elimina y retorna) al último cliente de la fila.


print(ultimo_cliente)  # Salida esperada: "Cliente 3"
print(clientes)  # Salida esperada: ["Cliente 1", "Cliente 2"]
"""

clientes= ["Cliente 1","Cliente 2","Cliente 3"]

eliminado = clientes.pop(1)

print(clientes)
print(eliminado)
