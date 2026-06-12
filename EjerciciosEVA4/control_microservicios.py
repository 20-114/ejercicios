'''
Contexto: Trabajas en el equipo de plataforma de una empresa tecnológica. 
Tu misión es construir un prototipo en consola para administrar los 
microservicios desplegados en un clúster. Cada microservicio tiene datos 
específicos que deben poder crearse, consultarse, modificarse y destruirse 
en caliente.

🏗️ Estructura de Datos Base
Crea un diccionario principal llamado cluster_servicios. Las llaves serán 
los nombres de los microservicios y los valores serán diccionarios anidados 
con sus propiedades. Inicialízalo con al menos un servicio:

Python
cluster_servicios = {
    'auth-api': {'version': 'v2.1.0', 'replicas': 3, 'status': 'Active'}
}
🛠️ Requisitos de las Funciones (El CRUD)
CREATE (Agregar Servicio): * Crea una función que solicite el nombre de un 
nuevo microservicio.

Defensa: Valida que el servicio no exista en el clúster antes de crearlo. 
Si ya existe, avisa al operador.

Si es nuevo, solicita su versión (ej. v1.0.0) y el número de réplicas 
(instancias corriendo, debe ser un número entero). Por defecto, el estado 
(status) al crearse siempre será 'Active'.

READ (Ver Estado):

Diseña una función que pueda listar todos los servicios con sus detalles 
en un formato limpio y ordenado.

Además, si el usuario ingresa el nombre de un servicio específico, debe 
mostrar únicamente la ficha técnica de ese servicio. Si no existe, debe indicarlo amablemente.

UPDATE (Actualizar Infraestructura):

Diseña una función que permita modificar un servicio existente. 
El operador debe poder elegir si quiere actualizar la versión o cambiar 
el número de réplicas (escalar el servicio).

Defensa: Valida que el servicio realmente exista antes de 
intentar modificarlo.

DELETE (Remover Servicio):

Diseña una función que elimine por completo un microservicio del 
diccionario del clúster.

Defensa: Como borrar infraestructura es peligroso, la función debe 
pedir una confirmación explícita (¿Está seguro? S/N) antes de aplicar 
el método correspondiente para eliminar la llave.

🔄 El Sistema de Control (Flujo Principal)
Construye un menú interactivo con match-case que ofrezca las opciones: 
1. Desplegar Servicio, 2. Monitorear Clúster, 3. Escalar/Actualizar, 
4. Dar de Baja y 5. Apagar Consola.

Aplica tu función mensajera de salida segura en cada entrada de datos. 
Si el usuario escribe la palabra EXIT en cualquier solicitud de texto, 
el programa debe abortar la operación actual de inmediato y cerrarse sin 
corromper el diccionario.

Protege el menú contra ingresos inválidos y capturas vacías.
'''


cluster_servicios = {
    'auth-api': {'version ': 'v2.1.0', 'replicas': 3, 'status  ': 'Active'}
}

def agregar_servicio():
    activo_agregar = True
    while activo_agregar:
        print("-"*50)
        new_service = input("Ingresa el nombre del nuevo servicio \n : ")
        activo_agregar = cancelar_proceso(new_service)
        if activo_agregar == False:
            break
        if new_service not in cluster_servicios:
            version = input("Indique la versión del servicio (Ejem. v1.0.0)\n : ")
            activo_agregar = cancelar_proceso(version)
            if activo_agregar == False:
                break
            while True:
                try:
                    replicas_cierre = input("Indique el numero de instancias replicadas del servicio \n : ")
                    replicas = int(replicas_cierre)
                    if replicas < 0:
                        print("Solo puede ingresar números enteros positivos")
                        continue
                    break
                except ValueError:
                    activo_agregar = cancelar_proceso(replicas_cierre)
                    if activo_agregar == False:
                        break
                    print("Solo puede ingresar números enteros positivos")
            if activo_agregar == False:
                break
            cluster_servicios[new_service] = {'versión ' : version}
            cluster_servicios[new_service]['replicas'] = replicas
            cluster_servicios[new_service]['status  '] = 'Active'
        else:
            print(f"Ya existe un servicio llamado {new_service}")
            continue
        break
    

def ver_estado():
    activo_estado = True
    while activo_estado:
        print("-"*50)
        print("Seleccione una opción:")
        print("1.Listar todos los servicio \n2.Listar un servicio especifico")
        op = input(" : ").upper()
        match op:
            case "1":
                print("-"*50)
                for servicio, propiedades in cluster_servicios.items():
                    print(F"Propiedades del servicio {servicio}:")
                    for propiedad, parametro in propiedades.items():
                        print("*"*6 , f"{propiedad} : {parametro}")
            case "2":
                while True:
                    servicio =  input("Ingresa el servicio que deseas listar: ")
                    activo_estado = cancelar_proceso(servicio)
                    if activo_estado == False:
                        break
                    if servicio not in cluster_servicios:
                        print("El servicio solicitado no se encuentra listado")
                        continue
                    print(F"Propiedades del servicio {servicio}:")
                    for propiedad, parametro in cluster_servicios[servicio].items():
                        print("*"*6 , f"{propiedad} : {parametro}")
                    break
            case "EXIT":
                break
            case _:
                print("Opción Inválida")
                continue
        
# def act_infraestructura():

# def remover_servicio():


def cancelar_proceso(ingreso):
    if ingreso.upper() == "EXIT":
        return False
    else:
        return True
# if activo == False:
#     break
def flujo_principal():
    activo = True
    while activo:
        print("ADMINISTRACIÓN DE CLUSTER DE INSTANCIAS")
        print("1. Desplegar Servicio \n2. Monitorear Clúster \n3. Escalar/Actualizar \n4. Dar de Baja \n5. Apagar Consola")
        try:
            op = input("").upper()
            match op:
                case '1':
                    agregar_servicio()
                case '2':
                    ver_estado()
                case '3':
                    act_infraestructura()
                case '4':
                    remover_servicio()
                case '5':
                    print("Apagando la Consola...")
                    break
                case "EXIT":
                    break
                case _:
                    print("Opción Inexistente")
                    continue
        except KeyboardInterrupt:
            print("Bloqueo de Emergencia")
            break
    print("Sistema cerrado de forma segura")
    
flujo_principal()


