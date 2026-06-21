'''
Contexto: Una fábrica gestiona los turnos de sus empleados. 
El sistema central es un diccionario donde la llave es el 
código del empleado, y el valor es otro diccionario con sus 
datos y una lista de turnos asignados.

🎯 Instrucciones de Funcionamiento
Implementa un menú que gestione a los trabajadores bajo estas 
directrices:

Crear (Contratar): Solicita un código de empleado y su nombre.

    Condición: El código debe empezar estrictamente con el texto "EMP-" 
    seguido de números. Si no cumple este formato, rechaza el registro.

    Validación: Si el código ya existe, impide que se sobrescriba al 
    empleado antiguo. El nuevo empleado debe iniciar con una lista de 
    turnos vacía.

Leer (Buscar Perfil): Solicita el código de un empleado y muestra 
toda su información (Nombre y turnos que tiene asignados). Si no 
existe, muestra un mensaje de error.

Actualizar (Asignar Turno): Solicita el código del empleado y el 
nombre del turno a asignar.

    Control de errores: Los únicos turnos válidos que el sistema acepta 
    son "mañana", "tarde" o "noche". Cualquier otra palabra debe ser rechazada.

    Condiciones Críticas: Un empleado no puede tener más de 2 turnos 
    asignados. Si intentas agregar un tercer turno, el sistema debe 
    bloquearlo por "Exceso de horas laborales". Además, no puedes asignarle 
    el mismo turno dos veces al mismo empleado.

Borrar (Despedir): Solicita el código de un empleado para eliminar todo 
su registro.

    Control de errores: Como es una acción destructiva, si el código existe, 
    el sistema debe pedirle al usuario que escriba la palabra "CONFIRMAR" en 
    mayúsculas. Si escribe cualquier otra cosa, la eliminación se cancela y 
    el empleado se mantiene en el sistema.
'''

empleados = {
    "EMP-01": {"nombre": "Ana", "turnos": ["mañana", "tarde"]},
    "EMP-02": {"nombre": "Luis", "turnos": ["noche"]}
}

def contratar():
    while True:
        try:
            print("Presiona Ctrl + C para volver")
            print("-"*50)
            new_empleado = input("Ingresa el codigo del nuevo empleado \n--|").upper()
            if not new_empleado.startswith("EMP-"):
                print("Registro rechazado")
                print("El codigo debe comenzar por 'EMP-'")
                continue
            split_numbre = new_empleado.split("EMP-", 1)
            if not split_numbre[1].isdigit():
                print("Registro rechazado")
                print("El codigo despues de 'EMP-' debe continuar con números")
                continue
            # print("todo bien ")
            if new_empleado in empleados:
                print("Este codgio ya se encuentra en los registros")
                continue        
            new_nombre = input("Ingresa el nombre del nuevo empleado \n--|")
            empleados[new_empleado] = {"nombre" :  new_nombre, "turnos" : []}
            break
        except KeyboardInterrupt:
            break

def buscarPerfil():
    while True:
        try:
            print("Presiona Ctrl + C para volver")
            print("-"*50)
            codigo = input("Indica el codigo del empleado \n--|").upper()
            if codigo in empleados:
                print(f"Nombre: {empleados[codigo]["nombre"]}")
                print("Turnos:")
                for turno in empleados[codigo]["turnos"]:
                    print(f"    {turno}")
                else:
                    break
            else:
                print("ERROR: el codigo no existe")
                continue
        except KeyboardInterrupt:
            break

def asignarTurno():
    while True:
        try:
            print("Presiona Ctrl + C para volver")
            codigo = input("Indica el codigo del empleado \n--|").upper()
            if codigo not in empleados:
                print("El codigo no esta registrado")
                continue
            elif len(empleados[codigo]["turnos"]) == 2:
                print("Exceso de horas")
                print("Este empleado ya tiene dos turnos")
                continue
            break
        except KeyboardInterrupt:
            break
    while True:
        try:
            turno = input(f"Indica que turno sera asignado a {empleados[codigo]["nombre"]} | mañana, tarde, noche \n--|").lower()
            turnos = ["mañana", "tarde", "noche"]
            if turno not in turnos:
                print("El turno ingresao no es válido")
                continue
            elif turno in empleados[codigo]["turnos"]:
                print("El empleado ya tiene este turno asignado")
                continue
            empleados[codigo]["turnos"].append(turno)
            break
        except KeyboardInterrupt:
            break

def despedir():
    while True:
        print("-"*50)
        try:
            print("Presiona Ctrl + C para volver")
            codigo = input("Indica el codigo del empleado \n--|").upper()
            if codigo not in empleados:
                print("El código no existe en los registros")
                continue
            print("Por seguridad escriba la palabra 'CONFIRMAR' en mayusculas para efectuar la eliminación")
            eliminar = input("--|")
            if "CONFIRMAR" == eliminar:
                del empleados[codigo]
                print(f"Eliminación de {codigo} realizada con exito")
                break
            else:
                print("Eliminación cancelada")
                continue
        except KeyboardInterrupt:
            break
        
def menuGestor():
    while True:
        print("-"*50)
        try:
            print('''    ----GESTOR DE PERSONAL----       
        1. Contratar
        2. Buscar perfil
        3. Asignar turno
        4. Despedir
        5. Salir''')
            op = input("Indica que operación quieres realiazr \n --|")
            match op:
                case "1":
                    contratar()
                case "2":
                    buscarPerfil()
                case "3":
                    asignarTurno()
                case "4":
                    despedir()
                case "5":
                    print("Cerrando del gestor")
                    break
                case _:
                    print("Opción Inválida")
        except KeyboardInterrupt:
            print("Bloqueo del sistema")
            break


menuGestor()