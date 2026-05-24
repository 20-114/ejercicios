'''
El Desafío: Diseñar un sistema de autenticación blindado que 
evalúe la estructura de una contraseña secreta y maneje un 
límite de intentos.

Comportamiento esperado:

El sistema debe definir de forma imprevista un PIN numérico 
secreto de 4 dígitos (entre 1000 y 9999) al iniciar.

El usuario tiene un límite estricto de 3 intentos para lograr 
el acceso.

Cada intento consume una oportunidad si no cumple con las 
siguientes reglas de negocio:

Si la entrada no es un número entero, se gasta un intento y 
avisa que solo se permiten dígitos.

Si la entrada es un número, pero no tiene exactamente 4 
dígitos de longitud, se gasta un intento y avisa del error de tamaño.

Si el número cumple con el tamaño, pero es un número impar, 
el sistema lo rechaza por políticas de seguridad interna y 
se gasta un intento.

Si el jugador agota sus intentos sin cumplir las reglas o sin 
adivinar, el sistema se bloquea por completo. Si tiene éxito, 
concede el acceso.
'''

import random

while True:
    pin_secreto = random.randint(1000, 9999)
    if pin_secreto % 2 == 0: #evalua que el pin segreto sea par para que sea compatible con las póliticas de seguridad
        break
# print(pin_secreto)
cont = 1
while cont <=3:
    try:
        pin_ingreso = int(input("Ingresa el PIN de acceso: "))
        if pin_ingreso == pin_secreto:
            print("Acceso concedido")
            break
        elif len(str(pin_ingreso)) != 4:
            cont += 1
            print("El PIN debe contener 4 dígitos")
            print(f"Intentos restantes: {4 - cont}")
            continue
        elif pin_ingreso % 2 != 0:
            cont += 1
            print("Alerta de PIN. Rechazado por políticas de seguridad interna.")
            print(f"Intentos restantes: {4 - cont}")
            continue
        else:
            cont += 1
            print("PIN incorrecto")
            print(f"Intentos restantes: {4 - cont}")
            continue
    except ValueError:
        cont += 1
        print("Solo se permiten dígitos")
        print(f"Intentos restantes: {4 - cont}")
if cont > 3:
    print("Sistema Bloqueado por ingreso de PIN fallido.")






