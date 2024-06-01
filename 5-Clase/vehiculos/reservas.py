"""
vehiculos/reservas.py:

Contiene las funciones para gestionar las reservas y guardarlas en el excel.

● `crear_reservas(cliente,vehiculo,fecha_inicio,fecha_final)` : Creamos un diccionario con la informacion de la reserva.

● `mostrar_reserva(reserva)` : Devolver en un string la reserva.

● `guardar_reserva_en_excel(reservas,archivo)` : Guardar la lista de reservas en el excel.


"""

from datetime import datetime
import pandas as pd
import os

def crear_reservas(cliente,vehiculo,fecha_inicio,fecha_final):
    return {
        "cliente":cliente,
        "vehiculo": vehiculo,
        "fecha_inicio": fecha_inicio,
        "fecha_final": fecha_final,
        "fecha_reserva": datetime.now()
    }

def mostrar_reserva(reserva):
    cliente= f"{reserva["cliente"]["nombre"]} {reserva["cliente"]["apellido"]}"
    vehiculo= f"{reserva["vehiculo"]["matricula"]} {reserva["vehiculo"]["modelo"]}"
    return f"Reserva de {cliente} para el vehiculo {vehiculo} del {reserva["fecha_inicio"]} al {reserva["fecha_final"]}"

def guardar_reserva_en_excel(reservas,archivo):
    data= [{
        "Cliente": f"{reserva["cliente"]["nombre"]} {reserva["cliente"]["apellido"]}",
        "Vehiculo": f"{reserva["vehiculo"]["matricula"]} {reserva["vehiculo"]["modelo"]}",
        "Fecha inicio": reserva["fecha_inicio"],
        "Fecha fin": reserva["fecha_final"],
        "Fecha reserva": reserva["fecha_reserva"]
    } for reserva in reservas]

    df_nuevas = pd.DataFrame(data)

    if os.path.exists(archivo):
        df_existente= pd.read_excel(archivo)

        df_total= pd.concat([df_nuevas,df_existente], ignore_index=True)
    else:
        df_total= df_nuevas

    df_total.to_excel(archivo,index=False)


    #df= pd.DataFrame(data)
    #df.to_excel(archivo, index=False)