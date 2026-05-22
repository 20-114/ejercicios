'''
Contexto: Has sido contratado para programar el núcleo de 
un sistema de ciberseguridad perimetral. El software debe 
procesar una ráfaga secuencial de transmisiones de datos y 
clasificarlas para mitigar ataques antes de que la integridad 
del servidor caiga a cero.

Reglas de Funcionamiento:

Planificación del Turno: Al iniciar, el administrador debe 
ingresar cuántos paquetes de datos va a procesar el sistema 
en esta sesión de monitoreo (el rango permitido y seguro es 
estrictamente de 1 a 12 paquetes). Si ingresa un número fuera 
de este rango, el sistema se auto-configura automáticamente en 
5 paquetes por defecto.

Procesamiento por Lotes: El sistema procesará exactamente la 
cantidad de paquetes definidos, uno tras otro, llevando la cuenta 
del número de paquete actual.

Análisis Estructural del Paquete: Para cada paquete, se solicita 
una cadena de texto que representa la cabecera de red. El sistema 
debe evaluar los primeros caracteres de esa cadena para clasificar 
el paquete en uno de los siguientes 4 protocolos de seguridad:

Clasificación "SYS" (Paquetes de Sistema):

Se evalúa la longitud de la cadena. Si la longitud es un múltiplo 
exacto de 2, el paquete se considera "Estable". Si es impar, se 
considera "Inestable" e incrementa un contador de anomalías del sistema.

Clasificación "DAT" (Paquetes de Datos):

El sistema solicita el ingreso del tamaño del bloque de datos entrante 
y el tamaño del bloque saliente.

Debe calcular la diferencia absoluta entre ambos tamaños. Si la 
diferencia absoluta es mayor a 50, se asume que hay una fuga de datos 
en curso y la integridad total del servidor disminuye en 10 puntos.

Clasificación "SEC" (Tokens de Seguridad):

Solicita un código numérico de autenticación.

El sistema genera un código de verificación aleatorio (entre 1 y 100). 
Si el código numérico provisto por el usuario guardado respecto al aleatorio 
tiene un residuo de división igual a cero al evaluarse mutuamente (es decir, 
uno es divisible por el otro), el token se acepta como válido y el servidor 
recupera 5 puntos de integridad (máximo de integridad permitido: 100).

Cualquier otra cabecera no identificada:

El paquete se clasifica automáticamente como "Ataque de Fuerza Bruta". La 
integridad del servidor se reduce inmediatamente en 15 puntos y se emite 
una alerta de bloqueo.

Factor de Fluctuación del Tráfico: Si el número de paquete actual que se está 
procesando es un número impar, el tráfico de la red está saturado. El sistema 
debe imprimir un aviso de "Latencia Alta" antes de procesar los datos de ese 
paquete.

Contención de Datos Corruptos: Las mediciones de tamaños de bloques y códigos 
de autenticación deben estar protegidas. Si un paquete contiene letras o 
símbolos en campos que requieren cálculos matemáticos, el sistema debe 
reportar un "Fallo de Segmentación", descartar ese paquete reduciendo 
la integridad del servidor en 2 puntos por el riesgo del fallo, y pasar 
inmediatamente al siguiente paquete de la secuencia.

Auditoría Final: Al terminar de procesar todos los paquetes asignados (o si la 
integridad del servidor llega a 0 antes de tiempo), el sistema se detiene y muestra 
un reporte detallado: Total de paquetes limpios, total de anomalías, total de 
ataques bloqueados y el porcentaje de integridad restante del servidor.
'''

import random

integridad_server = 100
anomalias = 0
paquetes_limpios = 0
ataques_bloqueados = 0
try:
    pqts_a_ingresar = int(input("Indique el número de paquetes que se ingresaran (entre 1 a 12) \n : "))
    if pqts_a_ingresar > 12 or pqts_a_ingresar < 1:
        print("Fuera de rango")
        print("Solo podra ingresar 5 paquetes")
        pqts_a_ingresar = 5
except ValueError:
    print("Solo puede ingreasar números enteros")
    print("Solo podra ingresar 5 paquetes")
    pqts_a_ingresar = 5

for paquete_actual in range(1, pqts_a_ingresar+1):
    if paquete_actual % 2 != 0:
        print("Latencia Alta")
    # print(paquete)
    cabecera_red = input(f"Ingrese la cabecera de red del {paquete_actual}° paquete \n : ").upper()
    evaluacion_cabecera = cabecera_red[0:3]
    # print(evaluacion_cabecera)
    match evaluacion_cabecera:
#1. Clasificación SYS (paquetes del sistema) 
        case "SYS":
            if len(cabecera_red) % 2 == 0:                
                paquetes_limpios += 1
                print(f"Paquete {paquete_actual} estable")
            else: 
                print(f"Paquete {paquete_actual} inestable")
                anomalias += 1
#2. Clasificación "DAT" (Paquete de datos)
        case "DAT":
            tamano_paquete = input("Ingrese su solicitud\n : ").upper()
            if "DOWNLOAD" in tamano_paquete or "EXPORT" in tamano_paquete or "BACKUP" in tamano_paquete:
                print("Transferencia masiva de datos...")
                paquete_tratado = len(tamano_paquete) * random.randint(10, 15)
            else:
                print("Trafico normal de red...")
                paquete_tratado = len(tamano_paquete) * random.randint(1, 3)
            #evaluación de  fuga
            eva_fuga = abs(paquete_tratado - len(tamano_paquete))
            if eva_fuga > 50:
                print("Fuga de información detectada")
                integridad_server -= 10
            else:
                paquetes_limpios += 1
#3. Clasificación "SEC" (Tokens de Seguridad)
        case "SEC":
            try:
                while True:
                    codigo_autenticacion = int(input("Ingresa el código numerico de verificaión \n : "))
                    if codigo_autenticacion != 0:
                        print("Escribir solo 0 es invalido")
                        break
            except ValueError:
                print("Fallo de segmentación")
                integridad_server -= 2
            verificacion_sistema = random.randint(1, 100)
            evalua_codigo_ver_1 = codigo_autenticacion % verificacion_sistema
            evalua_codigo_ver_2 = verificacion_sistema % codigo_autenticacion
            if evalua_codigo_ver_1 == 0 or evalua_codigo_ver_2 == 0:
                print("Token valido")
                integridad_server += 5
                paquetes_limpios += 1
            else: 
                print("Token invalido")
            if integridad_server > 100:
                integridad_server = 100
# Cualquier otra cabecera no identificada
        case _:
            ataques_bloqueados += 1 
            print("Se ha identificado un ataque de fuerza bruta")
            print("Integridad del sistema disminuyendo...")
            integridad_server -= 15
            print("¡¡¡ALERTA DE BLOQUEO!!!")
    if integridad_server <= 0:
        print("Integridad del sistema perdida.")
        break

print("Reporte final:")
print(f'''
Integridad del sistema: {integridad_server}
Paquetes procesados seguros: {paquetes_limpios}
Anomalias detectadas: {anomalias}
Ataques bloqueados: {ataques_bloqueados}
''')



























