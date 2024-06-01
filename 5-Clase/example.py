"""
example.py

Script de ejemplo que demustre como utilizar todas las funcionas del paquete "vehiculos"

● Crear clientes y vehiculos.
● Crear reservas y marcar vehiculos como alquilados.
● Guardar las reservas en un archivo excel.
● Devolver los vehiculos y mostrar su estado.


"""


# Importaciones

from vehiculos.clientes import crear_cliente,mostrar_cliente
from vehiculos.vehiculos import crear_vehiculo, mostrar_vehiculo, alquilar_vehiculo, devolver_vehiculo
from vehiculos.reservas import crear_reservas, mostrar_reserva, guardar_reserva_en_excel
from datetime import datetime

# Crear Clientes

cliente1 = crear_cliente("Sofia","Teram", "F12464280")

# Crear Vehiculos

vehiculo1= crear_vehiculo("ABC132", "Honda XR", 6)

# Crear reservas

fecha_inicio= datetime(2024,7,6)
fecha_final= datetime(2024,7,7)

reserva1= crear_reservas(cliente1,vehiculo1,fecha_inicio,fecha_final)

# Alquilar Vehiculos

alquilar_vehiculo(vehiculo1)


# Mostrar reservas

print(mostrar_reserva(reserva1))

# Mostrar Vehiculos en estado de No Disponible

print(mostrar_vehiculo(vehiculo1))



# Guardar reservas en excel

reservas = [reserva1]
guardar_reserva_en_excel(reservas,"reservas.xlsx")


# Devolver Vehiculos

devolver_vehiculo(vehiculo1)

# Mostrar vehiculos en estado Disponible

print(mostrar_vehiculo(vehiculo1))
