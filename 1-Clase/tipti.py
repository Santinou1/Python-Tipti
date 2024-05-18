"""
Ejercicio 1 = Tipti
Escribir una funcion llamada "tipti" que recorra un bucle de 0 hasta el numero ingresado por el usuario y haga lo siguiente=

Si el numero es multiplo de 3, imprimira = TIP
Si el numero es multiplo de 5, imprimira = TI
Si el numero es multiplo de 3 y de 5 imprimira= TIPTI
Si el numero no es multiplo de ninguno, no imprime nada.
"""


def tipti(n):
    for n in range(
        1, n + 1
    ):  # Recorre desde 1 hasta el numero ingresado el usuario
        if n % 3 == 0 and n % 5 == 0:
            print(f"{n} : tipti")
        elif n % 3 == 0:
            print(f"{n} : tip")
        elif n % 5 == 0:
            print(f"{n} : ti")
        else: 
            print(n)


# Ejemplo

numero = int(input("Ingrese un numero "))
tipti(numero)
