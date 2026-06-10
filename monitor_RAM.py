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
        div = 0
        for porcentaje in telemetria_ram[servidor][-3:]:
            div += 1
            print(porcentaje)
            suma_porcentajes += porcentaje
        prom = (suma_porcentajes / (div))
        print(f"promedio {prom}")
        return int(prom)
    else:
        return 0
def mostrar_servidores():
    'imprime los servidores y sus valores en orden vertical'
    for servidor, ram in telemetria_ram.items():
        print(f"Servidor: {servidor} | %ram: {ram}")
def finalizar(ingreso):
    'apagara el sistema cuando se escriba la palabra FINALIZAR'
    ingreso = ingreso.upper()
    if ingreso == "FINALIZAR":
        mostrar_servidores()
        return False
    else:
        return True

activo = True
while activo:
    try:
        print("-"*50)
        serv = input("Ingresa el nombre del servidor: ")
        activo = finalizar(serv)
        if activo == False:
            break
        while True:
            print("-"*50)
            ram_actual = input("Ingresa el porcentaje de consumo de RAM del servidor seleccionado: ")
            if ram_actual.lstrip("-").isdigit():
                ram_actual = int(ram_actual)
                if ram_actual > 100:
                    print("Solo puedes ignresar números entre 0 y 100")
                    continue
                elif ram_actual < 0:
                    print("Solo puede ingresar números enteros positivos")
                    continue
            if type(ram_actual) is str:
                activo = finalizar(ram_actual)
                if activo == False:
                    break
                else:
                    print("Ingreso Inválido")
                    continue
            break
        if activo == False:
            break
        analizar_consumo(serv, ram_actual)
        promedio = promedio_datos(serv)
        if promedio >= 85:
            print(f"[🚨 ALERTA] Servidor {serv} con sobrecarga sostenida de RAM") 
        mostrar_servidores()
    except KeyboardInterrupt:
        print("Sistema Bloqueado")
        mostrar_servidores()
        break
