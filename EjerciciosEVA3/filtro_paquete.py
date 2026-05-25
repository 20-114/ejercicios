'''
El Desafío: Simular un conmutador de red que cruce un 
tamaño de datos variable con un criterio matemático 
provisto por el operador, evitando un colapso del sistema.

Comportamiento esperado:

El juego dura exactamente 3 rondas. En cada una, la 
máquina genera en secreto un tamaño de paquete impredecible entre 1 y 100.

El sistema le solicita al usuario un "Factor de división 
numérico".

El programa debe blindarse contra dos tipos de entradas 
del operador:

    Si el operador ingresa letras o símbolos, el sistema debe 
    notificar el error y saltar a la siguiente ronda.

    Si el operador ingresa el número 0, el programa debe 
    interceptarlo con un mensaje de advertencia específico antes 
    de realizar cualquier cálculo para evitar que el software se 
    rompa catastróficamente en la consola.

Si la entrada es un número válido, el sistema evalúa si el 
tamaño de paquete de esa ronda se puede dividir de forma exacta 
(sin dejar residuos) entre el factor del usuario. De ser así, el 
paquete se transmite; de lo contrario, se retiene en el buffer.
'''


import random

for ronda in range(3):
    size_paquete = random.randint(1,100)
    print(size_paquete)
    try:
        factor_division = int(input("Ingrese el factor de división: "))
        if factor_division == 0:
            print("No puede dividir por cero")
            continue
        if size_paquete % factor_division == 0:
            print("Transmitiendo el paquete")
            continue
        else:
            print("Paquete enviado al búfer por detalles imprevistos en su contenido")
    except ValueError:
        print("Ingreso no númerico inválio")
        continue
