"""
vehiculos/vehiculos.py:

Contiene las siguientes funciones para almacenar vehiculos

● `crear_vehiculo(matricula,modelo,precio_por_dia)` Crear un diccionario con la informacion del vehiculo

● `mostrar_vehiculo(vehiculo)` Devuelve una representacion en cadena del vehiculo.

● `alquilar_vehiculo(vehiculo)` Marca el vehiculo como "FALSE"

● `devolver_vehiculo(vehiculo)` Marca el vehiculo como "TRUE".
 
"""

def crear_vehiculo(matricula,modelo,precio_por_dia):

    """
    Creamos un diccionario que representa un vehiculo.

    Args:
    matricula (str) = La matricula del vehiculo
    modelo (str) = El modelo del vehiculo.
    precio_por_dia(float) = El precio de alquiler por dia del vehiculo

    Returns:

    Nosotros retornamos un diccionario el cual contiene la informacion del vechiulo, incluyendo su estado de disponibilidad.

    """

    return {
        "matricula":matricula,
        "modelo":modelo,
        "precio_por_dia":precio_por_dia,
        "disponible": True
    }


def mostrar_vehiculo(vehiculo):

    """ 
    Genereamos una representacion en string del vehiculo.

    Args:
    vehiculo (dict) = Un diccionario que representa un vehiculo.

    returns:
    str : Una cadena de texto que describe al vehiculo, incluyendo su estado y precio por dia.
    """

    #  Determinamos el estado del vehiculo basado su disponibilidad
    # En caso de que la key sea True, se va a catalogar como disponible y en caso de que sea false se va a catalogar como No Disponible.

    estado = "disponible" if vehiculo["disponible"] else "no disponible"
    return f"Vehiculo : {vehiculo["matricula"]} ({vehiculo["modelo"]}) - {estado}, Precio: {vehiculo["precio_por_dia"]} por día"



def alquilar_vehiculo(vehiculo):

    """
    Marcar el vehiculo como no disponible

    Args:
    vehiculo (dict) = Un diccionario que representa un vehiculo.

    Return:
    
    Le cambio el valor a la key "disponible" por False.


    """

    vehiculo["disponible"] = False

def devolver_vehiculo(vehiculo):

    """
    Marcar el vehiculo como disponible

    Args:
    vehiculo (dict) = Un diccionario que representa un vehiculo.

    Return:
    
    Le cambio el valor a la key "Disponible" por True.


    """
    vehiculo["disponible"] = True

