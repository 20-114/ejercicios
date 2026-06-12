'''
Contexto: Los equipos de operaciones de TI reciben cientos 
de reportes de fallas al día. No todos los problemas son 
igual de urgentes, por lo que se deben atender primero los críticos.

Requisitos del programa:

Define un único diccionario llamado bandejas_soporte que 
contenga dos llaves principales: 'ALTA_PRIORIDAD' y 'BAJA_PRIORIDAD'. 
Ambas llaves deben apuntar inicialmente a listas vacías.

Crea una función para recibir nuevos incidentes. Esta función debe 
solicitar el nombre de la falla (un string) y su nivel de urgencia. 
Si es urgente, lo añade al final de la lista de alta prioridad; de 
lo contrario, al final de la de baja prioridad.

Crea una función llamada atender_ticket(). Su lógica debe ser la 
siguiente:

Si hay tickets en la lista de 'ALTA_PRIORIDAD', debe extraer, 
mostrar en pantalla y eliminar el ticket más antiguo de esa lista 
(el primero que llegó).

Si la lista de alta prioridad está completamente vacía, recién 
ahí puede proceder a extraer y eliminar el ticket más antiguo 
de la lista de 'BAJA_PRIORIDAD'.

Si ambas listas están vacías, debe avisar que el sistema está 
al día.

Construye el flujo principal continuo que permita al operador 
INGRESAR un ticket, ATENDER el siguiente ticket en fila o ver 
el ESTADO de las bandejas. Se apaga con la palabra SALIR.
'''

bandejas_soporte = {
    'ALTA_PRIORIDAD' : [],
    'BAJA_PRIORIDAD' : []
}

def nuevo_incidente():
    print("-"*50)
    list_ALTA = bandejas_soporte['ALTA_PRIORIDAD']
    list_BAJA = bandejas_soporte['BAJA_PRIORIDAD']
    nombre_falla = input("Indique el nombre de la falla: ")
    while True:
        nvl_urgencia = input("Indique el nivel de urgencia \n1.ALTA \n2.BAJA \n : ")
        match nvl_urgencia:
            case '1':
                list_ALTA.append(nombre_falla)
                print(f"El problema '{nombre_falla}' fue agregado a la lista de ALTA prioridad")
                break  
            case '2':
                list_BAJA.append(nombre_falla)
                print(f"El problema '{nombre_falla}' fue agregado a la lista de BAJA prioridad")
                break
            case _:
                print("Opción inexistente")
                continue

def mostrar_listaALTA():
    print("-$"*25)
    list_ALTA = bandejas_soporte['ALTA_PRIORIDAD']
    print("ALTA URGENCIA:")
    for problema in list_ALTA:
        print(problema)

def mostrar_listaBAJA():

    print("-$"*25)
    list_BAJA = bandejas_soporte['BAJA_PRIORIDAD']
    print("BAJA URGENCIA:")
    for problema in list_BAJA:
        print(problema)

def estado_bandeja():
    mostrar_listaALTA()
    mostrar_listaBAJA()

def atender_ticket():

    list_ALTA = bandejas_soporte['ALTA_PRIORIDAD']
    list_BAJA = bandejas_soporte['BAJA_PRIORIDAD']
    if len(list_ALTA) > 0:
        problema_actual = list_ALTA[0]
        del list_ALTA[0]
        print(f"El problema '{problema_actual}' de ALTA urgencia fue atendido")
    elif len(list_BAJA) > 0:
        problema_actual = list_BAJA[0]
        del list_BAJA[0]
        print(f"El problema '{problema_actual}' de BAJA urgencia fue atendido")
    else:
        print("El sistema esta al día")

def flujo_principal():
    while True:
        print("-"*50)
        print("Selecciona una opción \n1.INGRESAR Ticket \n2.ATENDER Ticket \n3.Ver estado de bandejas")
        print("In gresa SALIR para apagar el sistema")
        try:
            op = input(" : ").upper()
            match op:
                case "1":
                    nuevo_incidente()
                case "2":
                    atender_ticket()
                case "3":
                    estado_bandeja()
                case "SALIR":
                    print("Saliendo del Sistema")
                    break
                case _:
                    print("Opción Inválida")
        except KeyboardInterrupt:
            print("Apagado de emergencia")

flujo_principal()


