'''
Contexto: 
Eres el sistema operativo de un refugio subterráneo. 
Tu misión es gestionar los recursos de energía y oxígeno 
mientras el usuario toma decisiones críticas.

Reglas de Funcionamiento:

Estado Inicial: El búnker comienza con 100 unidades de energía y 100% de oxígeno.

Persistencia: El sistema debe mantenerse activo de forma ininterrumpida hasta que 
cualquiera de los dos recursos se agote por completo o el usuario decida apagar 
el sistema manualmente.

Interfaz de Comandos: En cada ciclo, el sistema debe presentar opciones 
para: 1. Filtrar Aire, 2. Activar Generador o 3. Salir.

Lógica de Consumo: * Cada acción realizada debe reducir los recursos de forma aleatoria.

El cálculo de la reducción debe garantizar que el valor restado sea siempre un número positivo, 
sin importar el orden de los factores en la resta de reserva. -------------------------------------------

Blindaje de Datos: Si el usuario ingresa texto, símbolos o deja vacía la elección del menú, 
el programa no debe cerrarse; en su lugar, debe informar que el comando es irreconocible 
y solicitar una nueva entrada.

Alertas del Sistema: Si el nivel actual de energía es un múltiplo exacto de 10, 
el sistema debe imprimir una advertencia visual de "Inestabilidad de Voltaje".

Informe de Cierre: Al terminar el programa, se debe mostrar el 
total de ciclos que el búnker logró mantenerse operativo.
'''

# import random

# def filtrar_aire(aire):
#     perdida_oxigeno = 0
#     perdida_oxigeno += aire
#     return perdida_oxigeno
# def activacion_generador(energia):
#     perdida_energia = 0
#     perdida_energia += energia
#     return perdida_energia


# oxigeno = 100
# unidaes_energia = 100
# ciclos_operacion = 0
# encendido = 0
# reduccion_aire = random.randint(4, 17)
# reduccion_energia = random.randint(4, 17)

# while unidaes_energia > 0 and oxigeno > 0 and encendido == 0:
#     try:
#         print("-"*25)
#         print(f"Energia del bunker  : {"_"*unidaes_energia}")
#         print(f"Oxígeno en el bunker: {"_"*oxigeno}\n")
#         op = int(input("Ingrese el proceso que desea efectuar: \n1)Filtrar aire \n2)Activar Generador \n3)Salir \n: "))
#         if op < 0:
#             print("-"*25)
#             print("Solo puede ingresar números positivos")
#             op = int(input("Ingrese el proceso que desea efectuar: \n1)Filtrar aire \nActivar Generador \n Salir \n: "))
#         match op:
#             case 1:
#                 oxigeno -= filtrar_aire(reduccion_aire)
#                 if oxigeno < 0:
#                     oxigeno = 0
#             case 2:
#                 unidaes_energia -= activacion_generador(reduccion_energia)
#                 if unidaes_energia < 0:
#                     unidaes_energia = 0
#             case 3:
#                 encendido = 1
#             case _:
#                 print("Ingreso invalido")
#         if unidaes_energia % 10 == 0 and unidaes_energia < 100:
#             print(f"Inestabilidad de voltaje. Celdas de enérgia al {unidaes_energia}%")        
#         if op == 1 or op == 2:
#             ciclos_operacion += 1
#     except:
#         print("El comano es irreconocible. Ingrese nuevamente la operación")
     
# print(f"ciclos operativos del bunker: {ciclos_operacion}")

#-----------------------------------------------------------------------------------------------------------------------
# CORRECCIONES
# 1. reduccion_aire y reduccion_energia integrarlos dentro del whil para que sus valores sean variables y no estaticos.
# 2. Integrar el valor absoluto en los descuentos para mejorar la fiabilidad del sistema de perdida de recursos.
# 3. Eliminar el if de op, ya que es redundante teniendo la opción "_" en match.
# 4. Agregar el error especifico en except

import random

def filtrar_aire(aire):
    perdida_oxigeno = 0
    perdida_oxigeno += aire
    return perdida_oxigeno
def activacion_generador(energia):
    perdida_energia = 0
    perdida_energia += energia
    return perdida_energia


oxigeno = 100
unidaes_energia = 100
ciclos_operacion = 0
encendido = 0

while unidaes_energia > 0 and oxigeno > 0 and encendido == 0:
    reduccion_aire = random.randint(4, 17)
    reduccion_energia = random.randint(4, 17)
    try:
        print("-"*25)
        print(f"Energia del bunker  : {"_"*unidaes_energia}")
        print(f"Oxígeno en el bunker: {"_"*oxigeno}\n")
        op = int(input("Ingrese el proceso que desea efectuar: \n1)Filtrar aire \n2)Activar Generador \n3)Salir \n: "))
        match op:
            case 1:
                oxigeno -= abs(filtrar_aire(reduccion_aire))
                if oxigeno < 0:
                    oxigeno = 0
            case 2:
                unidaes_energia -= abs(activacion_generador(reduccion_energia))
                if unidaes_energia < 0:
                    unidaes_energia = 0
            case 3:
                encendido = 1
            case _:
                print("Ingreso invalido")
        if unidaes_energia % 10 == 0 and unidaes_energia < 100:
            print(f"Inestabilidad de voltaje. Celdas de enérgia al {unidaes_energia}%")        
        if op == 1 or op == 2:
            ciclos_operacion += 1
    except ValueError:
        print("El comano es irreconocible. Ingrese nuevamente la operación")
     
print(f"ciclos operativos del bunker: {ciclos_operacion}")


