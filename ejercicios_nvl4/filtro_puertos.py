'''
El Desafío: Simular un sistema de detección de intrusos (IDS) 
que registre qué puertos de red intenta tocar cada dirección 
IP y dispare alertas si el comportamiento se vuelve hostil.

Comportamiento esperado:

El programa debe ejecutar un ciclo de exactamente 5 rondas. 
En cada ronda, la máquina simula un intento de conexión generando 
de forma imprevista y aleatoria un número de puerto entre 1 y 100.

En cada ronda, el sistema le pide al operador que ingrese la 
dirección IP (un texto) que originó esa conexión.

El sistema debe almacenar cada IP como un identificador único, 
y asociarle una lista con todos los puertos que ha intentado 
tocar durante el simulacro.

Control de seguridad: * Si el operador deja el campo de la IP 
vacío o presiona espacio, el sistema debe reportar una anomalía 
de origen, ignorar el puerto generado y saltar a la siguiente ronda.

    Si la IP es válida, se registra el puerto en su historial.

Al finalizar las 5 rondas, el programa inspecciona los registros: 
si alguna IP atacó un número total de puertos que sea un número par, 
el sistema imprime una alerta de "Sospecha de escaneo de red". Si el 
total de puertos atacados por esa IP es impar, muestra "Tráfico bajo 
análisis". Al final, muestra el reporte completo de qué puertos tocó 
cada IP.
'''
# import random
# ips = {}
# for ronda in range(3):
#     puerto = random.randint(1, 100)
#     dirIP = input("Ingrese la dirección IP: ").strip()
#     ingreso_ip = {'IP' : dirIP , 'puertos' : puerto}
#     for indx, elemento in ips:
#         if dirIP == elemento['IP']:
#             elemento['puertos'].append(puerto)   
#         else:
#             ips.append(ingreso_ip)

# print(ips)


import random

# Usamos un diccionario para que la búsqueda de IP sea instantánea y evitar modificar listas en loops
historial_ips = {} 

for ronda in range(1, 6): # Exactamente 5 rondas
    print(f"\n--- Ronda {ronda} ---")
    puerto = random.randint(1, 100)
    dirIP = input("Ingrese la dirección IP: ").strip()

    # Control de seguridad: Validar IP vacía
    if not dirIP:
        print("Anomalía de origen detectada: IP vacía. Ignorando puerto.")
        continue

    # Si la IP es válida, registramos el puerto
    if dirIP not in historial_ips:
        historial_ips[dirIP] = []
    historial_ips[dirIP].append(puerto)
    print(f"Conexión registrada en puerto {puerto}")

print("\n" + "="*30)
print("REPORTE DE AUDITORÍA")
print("="*30)

for ip, puertos in historial_ips.items():
    total_ataques = len(puertos)
    tipo_trafico = "Sospecha de escaneo de red" if total_ataques % 2 == 0 else "Tráfico bajo análisis"
    
    print(f"IP: {ip} | Puertos: {puertos} | Resultado: {tipo_trafico}")
    print(historial_ips)
