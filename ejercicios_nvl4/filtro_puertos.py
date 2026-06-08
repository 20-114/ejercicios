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
import random

# ips = {}
# for ronda in range(3):

# ips = [] # Inicializamos como lista como solicitaste

# for ronda in range(1, 6): # Exactamente 5 rondas según el desafío
#     puerto = random.randint(1, 100)
#     print(f"\n--- Ronda {ronda} (Puerto generado: {puerto}) ---")
#     dirIP = input("Ingrese la dirección IP: ").strip()
#     ingreso_ip = {'IP' : dirIP , 'puertos' : puerto}
#     for indx, elemento in ips:
#         if dirIP == elemento['IP']:
#             elemento['puertos'].append(puerto)   
#         else:
#             ips.append(ingreso_ip)




ips = [] # Inicializamos como lista como solicitaste

for ronda in range(1, 6): # Exactamente 5 rondas según el desafío
    puerto = random.randint(1, 100)
    print(f"\n--- Ronda {ronda} (Puerto generado: {puerto}) ---")
    dirIP = input("Ingrese la dirección IP: ").strip()

    # Control de seguridad: IP vacía
    if not dirIP:
        print("Anomalía de origen: IP vacía. Ignorando ronda.")
        continue

    encontrado = False
    # Buscamos si la IP ya existe en nuestra lista de diccionarios
    for registro in ips:
        if registro['IP'] == dirIP:
            registro['puertos'].append(puerto)
            encontrado = True
            break # Ya la encontramos, no hace falta seguir buscando

    # Si después de recorrer toda la lista no existe, la creamos
    if not encontrado:
        # El puerto se guarda en una lista [puerto] para poder usar .append después
        ips.append({'IP': dirIP, 'puertos': [puerto]})

print("\n" + "="*40)
print("REPORTE FINAL DE CONEXIONES")
print("="*40)

# Inspección final de registros
for registro in ips:
    total_puertos = len(registro['puertos'])
    # Lógica de par (Escaneo) o impar (Análisis)
    alerta = "Sospecha de escaneo de red" if total_puertos % 2 == 0 else "Tráfico bajo análisis"
    
    print(f"IP: {registro['IP']} | Puertos: {registro['puertos']} | Resultado: {alerta}")
