"""
vehiculos/clientes.py:
● Contiene la clase Cliente que almacena la información de los clientes.
● Métodos:
○ crear_cliente( nombre, apellido, licencia_conducir):
Inicializa un cliente con su nombre, apellido y licencia de conducir.
○ mostrar_cliente(): Devuelve una representación en cadena del cliente.

"""

def crear_cliente(nombre,apellido,licencia_conducir):

    """
    Creamos un diccionario que representa un Cliente.

    Args:
    nombre (str) = El nombre del cliente
    apellido (str) = El apellido del cliente.
    licencia_conducir(str) = La licencia de conducir del cliente
    Returns:

    Nosotros retornamos un diccionario el cual contiene la informacion del cliente.

    """
        
    return{
        "nombre":nombre,
        "apellido":apellido,
        "licencia_conducir": licencia_conducir
    }

def mostrar_cliente(cliente):

    """ 
    Genereamos una representacion en string del cliente.

    Args:
    cliente (dict) = Un diccionario que representa un cliente.

    returns:
    str : Una cadena de texto que describe al cliente.
    """

    return f"{cliente["nombre"]} {cliente["apellido"]}, Licencia: {cliente["licencia_conducir"]}"
