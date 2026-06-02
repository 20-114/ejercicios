'''
El Desafío: Diseñar un sistema que recopile y agrupe 
métricas de rendimiento de múltiples servidores, calculando 
promedios dinámicos y detectando anomalías sin permitir que 
datos corruptos dañen el historial.

Comportamiento esperado:

El programa inicia con una estructura de datos que ya contiene 
tres servidores pre-registrados ("Server-A", "Server-B" y 
"Server-C"). Cada uno tiene asociado un historial vacío para 
almacenar sus tiempos de respuesta (latencias).

El sistema debe solicitar repetidamente al operador el nombre 
de un servidor y la latencia detectada (un número entero). 
Este ciclo solo termina si el usuario escribe FIN.

Al recibir los datos, el programa debe validar estrictamente lo siguiente:

Si el nombre del servidor ingresado no existe en los registros actuales, 
el sistema rechaza la operación informando que el host no está autorizado.

Si la latencia introducida no es un número entero positivo, o si el 
usuario escribe texto en su lugar, el sistema reporta un fallo de 
telemetría y anula el ingreso para ese servidor.

Si los datos son válidos, la latencia se guarda en el historial 
específico de ese servidor. De inmediato, el sistema muestra en 
pantalla el historial completo de ese servidor y la diferencia 
absoluta entre la latencia que se acaba de ingresar y la primera 
latencia que se registró en ese servidor en todo el día.
'''

# serv_A = []
# serv_B = []
# serv_C = []

# def add_servA():
#     serv_A.append(latencia)
#     print(serv_A)
#     if len(serv_A) > 1: 
#         print(f"Latencia absoluta entre la primera y la ultima registrada en el servidor A es {abs(serv_A[0] - serv_A[-1])}")
# def add_servB():
#     serv_B.append(latencia)
#     print(serv_B)
#     if len(serv_B) > 1: 
#         print(f"Latencia absoluta entre la primera y la ultima registrada en el servidor B es {abs(serv_B[0] - serv_B[-1])}")
# def add_servC():
#     serv_C.append(latencia)
#     print(serv_C)
#     if len(serv_C) > 1: 
#         print(f"Latencia absoluta entre la primera y la ultima registrada en el servidor B es {abs(serv_C[0] - serv_C[-1])}")
    
# print('''
# Servidores Disponibles:
#     - serv_A
#     - serv_B
#     - serv_C
# ''')
# while True:
#     server = input("Ingrese el nombre del servidor a solicitar: ")
#     match server:
#         case "serv_A":
#             try:
#                 latencia = int(input("Ingrese latencia detectada: "))
#                 if latencia < 0:
#                     print("Fallo de telemetría")
#                     print("Ingreso anulado")
#                     continue
#             except ValueError:
#                 print("Fallo de telemetría")
#                 print("Ingreso anulado")
#                 continue
#             add_servA()
#         case "serv_B":
#             try:
#                 latencia = int(input("Ingrese latencia detectada: "))
#                 if latencia < 0:
#                     print("Fallo de telemetría")
#                     print("Ingreso anulado")
#                     continue
#             except ValueError:
#                 print("Fallo de telemetría")
#                 print("Ingreso anulado")
#                 continue
           
#             add_servB()
#         case "serv_C":
#             try:
#                 latencia = int(input("Ingrese latencia detectada: "))
#                 if latencia < 0:
#                     print("Fallo de telemetría")
#                     print("Ingreso anulado")
#                     continue
#             except ValueError:
#                 print("Fallo de telemetría")
#                 print("Ingreso anulado")
#                 continue
#             add_servC()        
#         case "FIN":
#             break
#         case _:
#             print("Operación rechazada. El host no esta autorizado")

'''Refactorización del original'''
# datos = {
# 'serv_A' : [],
# 'serv_B' : [],
# 'serv_C' : []
# }
# def add_serv(servidor, latencia):
#     historial = datos[servidor]
#     historial.append(latencia)
#     print(f"Historial de {servidor}: {historial}")
#     if len(historial) > 1:
#         diferencia = abs(historial[0] - historial[-1])
#         print(f"Diferencia absoluta entre la primera y ultima lectura: {diferencia}ms")

# print('''
# Servidores Disponibles:
#     - serv_A
#     - serv_B
#     - serv_C
# ''')
# while True:
#     server = input("Ingrese el nombre del servidor a solicitar: ")
#     match server:
#         case "serv_A":
#             try:
#                 latencia = int(input("Ingrese latencia detectada: "))
#                 if latencia < 0:
#                     print("Fallo de telemetría")
#                     print("Ingreso anulado")
#                     continue
#             except ValueError:
#                 print("Fallo de telemetría")
#                 print("Ingreso anulado")
#                 continue
#             add_serv(server, latencia)
#         case "serv_B":
#             try:
#                 latencia = int(input("Ingrese latencia detectada: "))
#                 if latencia < 0:
#                     print("Fallo de telemetría")
#                     print("Ingreso anulado")
#                     continue
#             except ValueError:
#                 print("Fallo de telemetría")
#                 print("Ingreso anulado")
#                 continue
#             add_serv(server, latencia)
#         case "serv_C":
#             try:
#                 latencia = int(input("Ingrese latencia detectada: "))
#                 if latencia < 0:
#                     print("Fallo de telemetría")
#                     print("Ingreso anulado")
#                     continue
#             except ValueError:
#                 print("Fallo de telemetría")
#                 print("Ingreso anulado")
#                 continue
#             add_serv(server, latencia)        
#         case "FIN":
#             break
#         case _:
#             print("Operación rechazada. El host no esta autorizado")

'''Refactorización IA del refactorizado'''

datos = {
'serv_A' : [],
'serv_B' : [],
'serv_C' : []
}
def add_serv(servidor, latencia):
    historial = datos[servidor]
    historial.append(latencia)
    print(f"Historial de {servidor}: {historial}")
    if len(historial) > 1:
        diferencia = abs(historial[0] - historial[-1])
        print(f"Diferencia absoluta entre la primera y ultima lectura: {diferencia}ms")

print('''
Servidores Disponibles:
    - serv_A
    - serv_B
    - serv_C
''')
while True:
    server = input("Ingrese el nombre del servidor a solicitar: ")
    
    if server == "FIN":
        break
        
    # El diccionario nos permite validar TODOS los servidores con una sola línea
    if server in datos:
        try:
            latencia = int(input("Ingrese latencia detectada: "))
            if latencia < 0:
                print("Fallo de telemetría\nIngreso anulado")
                continue
        except ValueError:
            print("Fallo de telemetría\nIngreso anulado")
            continue
            
        # Llamada única para cualquier servidor válido
        add_serv(server, latencia)
    else:
        print("Operación rechazada. El host no está autorizado")


