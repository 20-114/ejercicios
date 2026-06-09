'''
Contexto: Necesitas monitorear el consumo de memoria 
RAM de varios servidores en tiempo real para disparar 
alertas cuando un servidor esté en peligro crítico.

Requisitos del programa:

Crea un diccionario vacío llamado telemetria_ram.

Desarrolla una función llamada analizar_consumo(servidor, 
porcentaje) que reciba el nombre del servidor (string) y 
el consumo actual de RAM (entero de 0 a 100).

Si el servidor no existe en el diccionario, la función 
debe crear la llave y asignarle una lista con ese porcentaje.

Si ya existe, debe añadir el nuevo porcentaje a su historial (lista).

La Alerta: Justo después de añadir el dato, la función debe 
calcular el promedio de los últimos 3 consumos registrados 
de ese servidor. Si el promedio de esos 3 últimos datos es 
mayor o igual a 85, debe imprimir una alerta crítica: "[🚨 ALERTA] 
Servidor {nombre} con sobrecarga sostenida de RAM".

Implementa el bucle de captura de datos controlando que los 
porcentajes ingresados sean numéricos y estén en el rango real 
de 0 a 100. El sistema se apaga si se ingresa la palabra FINALIZAR.
'''

telemetria_ram = {}

def analizar_consumo(servidor, porcentaje):
    'evalua la existencia del servidor ingresado y define si crearlo caundo no exista o solo agregar el % de uso cuando ya existe'
    if servidor in telemetria_ram:
        telemetria_ram[servidor].append(porcentaje)
    else:
        telemetria_ram[servidor] = [porcentaje]
def promedio_datos(servidor):
    'calcula el promedio hasta los ultomos 3 consumos anteriores'
    if servidor in telemetria_ram:
        suma_porcentajes = 0
        cont = 1
        for porcentaje in telemetria_ram[servidor]:
            if cont > 3:
                break
            suma_porcentajes += porcentaje
            cont += 1
        prom = (suma_porcentajes / (cont-1))
        print(f"promedio {prom}")
        return int(prom)
    else:
        return 0
def finalizar(ingreso):
    'apagara el sistema cuando se escriba la palabra FINALIZAR'
    ingreso = str(ingreso.upper())
    if ingreso == "FINALIZAR":
        return False
activo = True
while activo:
    serv = input("Ingresa el nombre del servidor: ")
    activo = finalizar(serv)
    if activo == False:
        break
    while True:
        try:
            ram_actual = int(input("Ingresa el porcentaje de consumo de RAM del servidor seleccionado: "))
        except ValueError:
            print("Solo puedes ingresar números enteros")
        activo = finalizar(ram_actual)
        if activo == False:
            break
        if ram_actual > 100:
            print("Solo puedes ignresar números entre 0 y 100")
            continue
        elif ram_actual < 0:
            print("Solo puede ingresar números entreos positivos")
            continue
        break
    if activo == False:
        break
    promedio = promedio_datos(serv)
    if promedio >= 85:
        print(f"[🚨 ALERTA] Servidor {serv} con sobrecarga sostenida de RAM") 

    analizar_consumo(serv, ram_actual)
    print(telemetria_ram)
