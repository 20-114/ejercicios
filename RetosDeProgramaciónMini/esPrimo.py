'''
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
'''


primos = []
for num in range(1,101):
    lista = []
    for i in range(1,101):
        if num % i == 0: 
            lista.append(i)
    if len(lista) == 2: 
        primos.append(num)
print(primos)

# un numero primo solo puede ser divisible por 1 y por si mismo. significa que 
# solo tiene dos divisores en las que el % es 0, cualquier número con más 
# de 2 divisores no es primo
