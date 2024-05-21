# La funcion "range()" en python funciona para generar una secuencia de numeros.
# Esta funcion cuenta con 3 paramentros.
# Start
# Stop
# Step
# Algunos de estos parametros tienen valores predeterminados.

# Parametros de range()

# Start= 0 (Opcional) El valor inicial de la secuencia. El valor inicial es 0 si no se especifica.
# Stop= (Obligatorio) El valor final de la secuencia.
# Step= +1 (Opcional) La diferencia entre cada par de numeros consecutivos. El valor predeterminado e 1 si no se especifica.



# Sintaxis

# range(stop)
# range(start,stop)
# range(start,stop,step)


# Ejemplo

# Utilizando solamente Stop:
for i in range(5):
    print(i)

# Output : 0,1,2,3,4
# En este ejemplo START es 0 ( VALOR PREDETERMINADO ) , STOP es 5 (valor brindado) , y STEP es 1 ( VALOR PREDETERMIANDO )

# Utilizamos Start y Stop

for i in range(2,6):
    print(i)

# Output: 2,3,4,5
# Star es 2, stops es 6 y step es 1 (VALOR PREDETERMINADO )

# Utilizamos Star,Stop,Step

for i in range(10,0,-2):
    print(i)

# Output: 10,8,6,4,2

# Star es 10, Stop es 0, y Step es -2. La secuencia se va a generar en orden descendente
