"""
Escribir una funcion que se llame "longitudTotal" que lo que haga sea tomar un string y devolver su longitud.
"""

def longitudTotal(string):
    return len(string)

print("FUNCION EJECUTADA UTILIZANDO EL METODO LEN")
print(longitudTotal("Hola Mundo"))

### SIN METODO

def longitudTotalOg(string):
    contador=0
    for letra in string:
        contador+=1
    return contador


# Ejemplo de uso

print("FUNCION EJECUTADA UTILIZANDO EL METODO PROPIO")
string = input("Ingrese un string ")
print(longitudTotalOg(string))