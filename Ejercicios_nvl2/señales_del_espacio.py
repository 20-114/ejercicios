'''
Contexto: Has recibido una cadena de texto que contiene una transmisión de 
una civilización lejana. Tu trabajo es extraer los datos numéricos ocultos en el ruido.

Reglas de Funcionamiento:

Recepción de Señal: Solicita al usuario una cadena de texto. 
Si la longitud de la cadena es inferior a 12 caracteres, el sistema 
debe rechazarla por ser "ruido insuficiente" y pedir una nueva hasta que cumpla el requisito.

Procesamiento Secuencial: El sistema debe analizar cada elemento 
de la cadena, uno por uno, de principio a fin.

Extracción Selectiva: * El comportamiento del análisis cambia según 
la posición del carácter:
* En posiciones pares, el sistema debe intentar tratar ese carácter como 
un número. Si lo logra, debe sumarlo a un acumulador de "Energía de Señal".
* En posiciones impares, el sistema debe simplemente identificar si el 
carácter es una vocal o no.

Gestión de Errores Internos: Dado que la cadena contiene texto y números 
mezclados, el sistema debe ser capaz de intentar la conversión numérica sin detenerse 
ni mostrar errores técnicos si encuentra una letra donde esperaba un número. Simplemente 
debe saltar ese elemento y continuar.

Resultado del Análisis: Al finalizar el recorrido, debe mostrar la suma total 
obtenida y el promedio de valor por cada carácter de la cadena original.
'''
import random

while True:
    try:
        codigo_señal = input("Ingresa la señal: ")
        print("-"*25)
        if len(codigo_señal) < 12:
            print("Ruido insuficiente")
        else:
            break
    except ValueError:
        print("Ingreso Invalido")

# print(codigo_señal[2])
energia_de_señal = 0
for i in codigo_señal:
    if codigo_señal.index(i) % 2 == 0 and i == str(range(0,10)):
        print(i)
        energia_de_señal += int(i)
        print(energia_de_señal)
    elif i == "a"or i == "e"or i == "i"or i == "o"or i == "u":
        print(f"{i} es vocal")
    else:
        print(f"{i} NO es vocal")


print(energia_de_señal)


