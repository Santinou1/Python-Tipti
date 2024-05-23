"""

set() es una funcion nativa de Python la cual se encarga de crear un conjunto, el cual es una coleccion desordenada de ELEMENTOS UNICOS

Los conjuntos (SETS) en Python no van a permitir nunca elementos duplicados, por lo que si vas a intentar crear un conjunto con elementos repetidos, lo que va a pasar es qeu se eliminaran automaticamente los duplicados.

Podemos realizar cualquier tipo de funcion iterable , y vas a obtener un conjunto que contienee los elementos unicos de ese iterable

"""

lista=[2,3,4,2,3,4,5,10,2,6,7,8,9,True,True,True,True,True,False]
lista2=[1,2,3,4,2,3,4,5,10,2,6,7,8,9,True,0,False]


conjunto = set(lista)
conjunto2=set(lista2)
print(conjunto)
print(conjunto2)


"""
Join()

join es unmetodo de string que se usa para concatenar elementos con un separador especifico.


"""

lista=["1","3","2","7","8","6","4","8","5"]
separador= " | "
resultado= separador.join(lista)

print(resultado)